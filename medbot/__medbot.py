from .__bp3gy12n import Microlife_BTLE#
from .__max30102 import MAX30102
from serial import Serial
from datetime import datetime
from pyzbar.pyzbar import decode
from escpos.connections import getUSBPrinter

import cv2
import numpy
import pyttsx3

########################################################
#                      Main Class                      #
########################################################

# This class requires a Database object to be initialized
# Commented lines is due to this code is being tested on a Windows Machine
# Would later remove if ported on Raspberry Pi
class Medbot:

    def __init__(self):
        self.availabe_commands = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.oximeter = MAX30102()
        try:
            self.arduino = Serial('/dev/ttyACM0', 9600, timeout = 1)
        except:
            self.arduino = Serial('/dev/ttyACM1', 9600, timeout = 1)
        self.qrcode_scanner = cv2.VideoCapture(0)
        self.printer = getUSBPrinter()(idVendor=0x28e9,
                          idProduct=0x0289,
                          inputEndPoint=0x81,
                          outputEndPoint=0x03)
        self.speaker = pyttsx3.init()
        voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('rate', 150)

    def get_arduino_response(self, timeout: float = 0):
        '''
            Get the Arduino response if available \n
            Timeout could be set to listen for response
            within the timeout duration. If `timeout` is
            set to 0, function will execute one time.
            Setting `timeout` to 0 may return empty string
            and recommended to call in a loop \n
            Possible response:
            - `90` False
            - `91` True
        '''
        if(timeout <= 0):
            try:
                response = self.arduino.readline().decode('utf-8').rstrip()
            except UnicodeDecodeError:
                response = self.arduino.readline().decode('utf-8').rstrip()
        else:
            start_time = datetime.timestamp(datetime.now())
            now_time = datetime.timestamp(datetime.now())
            while((now_time - start_time) < timeout + 0.1):
                try:
                    response = self.arduino.readline().decode('utf-8').rstrip()
                except UnicodeDecodeError:
                    response = self.arduino.readline().decode('utf-8').rstrip()
                if(response != ''):
                    break
                now_time = datetime.timestamp(datetime.now())
            if((start_time - now_time) > timeout and response == ''):
                raise Exception('Timeout reached')
        return response
    
    def send_command(self, command: int):
        '''
            Send command to arduino.\n
            Can be used to explicitly invoke Arduino operation without calling specific functions 
        '''
        if(command in self.availabe_commands):
            while True:
                self.arduino.write(bytes(str(command)+'\n','utf-8'))
                response = self.get_arduino_response()
                if(response == 'ok'):
                    break
        else:
            raise Exception('Unknown command')

    def start_oximeter(self):
        while True:
            red, ir = self.oximeter.read_sequential()
            print(self.oximeter.calc_hr_and_spo2(ir, red))

    def start_blood_pressure_monitor(self, retry_on_fail: bool = False):
        '''
            Send command to the Arduino to press the start button on the blood pressure monitor
            and fetches the last measurement \n
            Returns and cache systolic and diastolic if `pulse_rate_from_bpm` is `False
            otherwise returns and cache systolic, diastolic and pulse rate\n
            If `retry_on_fail` is `True`, the medbot will restart getting data
            from the bpm unit until a measurement is secured \n
            `Note:` if the you wants to get the pulse rate from the bpm, you need to set the
            `pulse_rate_from_bpm` property to true by direct or by calling
            `set_pulse_rate_from_bpm(True)`.
        '''
        
        while True:
            try:
                blood_pressure_monitor = Microlife_BTLE()
                blood_pressure_monitor.bluetooth_communication(blood_pressure_monitor.patient_id_callback)                          
                latest_measurement = blood_pressure_monitor.get_measurements()[-1]
                break
            except:
                print('Retrying')
        systolic = latest_measurement[1] 
        diastolic = latest_measurement[2] 
        pulse_rate = latest_measurement[3] 
        return systolic, diastolic, pulse_rate 
    
    def start_hand_santizer(self):
        '''
        Turn on the ultrasonic sensor.If your hand is detected, the relay will automatically turn on,and the alcohol dispenser will spray onto your hand.
        ''' 
    
    def detect_finger(self, wait_until_detected: bool = False):
        if wait_until_detected:
            self.send_command(6)
            response = self.get_arduino_response()
            while(response != '90'):
                response = self.get_arduino_response()
            return True
        else:
            self.send_command(5)
            response = self.get_arduino_response()
            if response == '90':
                return True
            else:
                return False

    def lock_oximeter(self):
        self.send_command(3)

    def unlock_oximeter(self):
        self.send_command(4)

    def __decodeframe(self, image):
        '''
            Returns the decoded QR Code message
        '''
        trans_img = cv2.cvtColor(image,0)
        qrcode = decode(trans_img)
        for obj in qrcode:
            points = obj.polygon
            (x,y,w,h) = obj.rect
            pts = numpy.array(points, numpy.int32)
            pts = pts.reshape((-1, 1, 2))
            thickness = 2
            isClosed = True
            line_color = (0, 0, 255)
            cv2.polylines(image, [pts], isClosed, line_color, thickness)
            data = obj.data.decode("utf-8")
            return data
        
    def scan_qrcode(self):
        '''
            Opens an OpenCV window and scans QR Code   
        '''
        data = ''
        while True:
            ret, frame = self.qrcode_scanner.read()
            data = self.__decodeframe(frame)
            cv2.imshow('Image', frame)
            cv2.waitKey(1)
            if(data != None):
                break
        cv2.destroyAllWindows()
        return data

    def print(self, content: str):
        '''
            Print some text on the thermal printer
        '''
        success = False
        while(not success):
            try:
                self.printer.text(content)
                self.printer.lf()
                success = True
            except:
                break
        return success
    
    def speak(self, text: str):
        '''
            Converts text to speech \n
            Only available if `voice_prompt_enabled` property is `True`
        '''
        self.speaker.say(text)
        self.speaker.runAndWait()
