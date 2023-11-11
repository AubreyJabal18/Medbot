from .__bp3gy12n import Microlife_BTLE#
from .__max30102 import MAX30102
from serial import Serial
from datetime import datetime
from pyzbar.pyzbar import decode
from escpos.connections import getUSBPrinter

import cv2
import numpy
import pyttsx3
import mysql.connector
import bcrypt
import time

########################################################
#                      Main Class                      #
########################################################

# This class requires a Database object to be initialized
# Commented lines is due to this code is being tested on a Windows Machine
# Would later remove if ported on Raspberry Pi
class Medbot:

    def __init__(self):
        self.database = mysql.connector.connect(
            host='127.0.0.1',
            user='medbot',
            password='medbot',
            database='medbot'
        )
        self.user = None
        self.cursor = self.database.cursor()
        self.availabe_commands = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        try:
            self.arduino = Serial('/dev/ttyACM0', 9600, timeout = 1)
        except:
            self.arduino = Serial('/dev/ttyACM1', 9600, timeout = 1)

        self.reset_arduino()
        self.oximeter = MAX30102()
        self.qrcode_scanner = cv2.VideoCapture(0)
        self.printer = getUSBPrinter()(idVendor=0x28e9,
                          idProduct=0x0289,
                          inputEndPoint=0x81,
                          outputEndPoint=0x03)
        self.speaker = pyttsx3.init()
        voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('rate', 150)

    #########################################
    #                                       #
    #            ARDUINO INTERFACE          #
    #                                       #
    #########################################

    def get_arduino_response(self, timeout: float = 0):
        '''
            Get the Arduino response if available \n
        '''
        try:
            response = self.arduino.readline().decode('utf-8').rstrip()
        except UnicodeDecodeError:
            response = self.arduino.readline().decode('utf-8').rstrip()
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
        
    def wait_until_operation_completed(self):
        response = self.get_arduino_response()
        while response != '90':
            response = self.get_arduino_response()

    def start_hand_santizer(self, wait_until_completed: bool = False):
        '''
        Turn on the ultrasonic sensor.If your hand is detected, the relay will automatically turn on,and the alcohol dispenser will spray onto your hand.
        ''' 
        self.send_command(8)
        if wait_until_completed:
            self.wait_until_operation_completed()
        else:
            self.get_arduino_response()
    
    def detect_hand(self):
        '''
        detect your your hand using ultrasonic sensor
        '''
        self.send_command(6)
        response = self.get_arduino_response()
        return response
    

    def detect_finger(self):
        '''
        detect your finger tip using touch sensor
        '''
        self.send_command(5)
        response = self.get_arduino_response()
        if response == "91":
            return True
        else:
            return False   

    def start_motor_forward(self):
        '''
        DC motor clockwise
        '''
        self.send_command(0)
        
    def start_motor_backward(self):
        '''
        DC motor counter clockwise
        '''
        self.send_command(1)
        
    def stop_motor(self):
        '''
        Stop DC motor
        '''
        self.send_command(2)    

    def lock_oximeter(self):
        '''
        close oximeter
        '''
        self.send_command(3)

    def unlock_oximeter(self):
        '''
        open oximeter
        '''
        self.send_command(4)

    def lock_arm(self):
        '''
        Lock arm cuff
        '''
        self.send_command(12)
        response = self.get_arduino_response()

        if response <= '200':
           response = self.get_arduino_response()
        else:
            response = self.get_arduino_response()
            self.send_command(2)
        return response
        




        # self.send_command(12)
        # if wait_until_completed:
        #     self.wait_until_operation_completed()
            
        # else:
        #     self.get_arduino_response()


        # self.send_command(13)
        # fsr_value = self.get_arduino_response()
        # while fsr_value <= 600:
        #     fsr_value = self.get_arduino_response()
        # self.send_command(2)
    
    def unlock_arm(self):
        '''
        Unlock arm cuff
        '''
        self.send_command(1)
        time.sleep(2)
        self.send_command(2)
        self.send_command

    def detect_arm(self):
        '''
        detect your using FSR sensor
        '''
        self.send_command(13)
        response = self.get_arduino_response()
        if response == "91":
            return True
        else:
            return False    

    def detect_arm_bpm(self):
        '''
        detect your using FSR sensor
        '''
        self.send_command(14)
        response = self.get_arduino_response()
        if response == "91":
            return True
        else:
            return False 
        
    def start_solenoid(self, wait_until_completed: bool = False):
        self.send_command(7)
        '''
        start blood pressure sensor
        '''
        if wait_until_completed:
            self.wait_until_operation_completed()
        else:
            self.get_arduino_response

    def reset_arduino(self):
        '''
        Reset Arduino
        '''
        self.send_command(9)
    #########################################
    #                                       #
    #           VITAL SIGN SENSORS          #
    #                                       #
    #########################################

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
        # start solenoid
        # detect air_pressure until 0
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
    
    def start_oximeter(self):
        while True:
            red, ir = self.oximeter.read_sequential()
            result = self.oximeter.calc_hr_and_spo2(ir, red)
            if result[1] and result[3]:
                spO2 = int (result[2])
                return spO2

    def get_temperature(self):
        self.send_command(11)   

        response = self.get_arduino_response() 
        while not response:
            response = self.get_arduino_response()

        temperature = float (response) 
        return temperature      
    
    #########################################
    #                                       #
    #              LOGIN RELATED            #
    #                                       #
    #########################################

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
    
    def login(self, id, password):
        self.cursor.execute("SELECT * FROM users where id="+id)
        result = self.cursor.fetchone()
        if result:
            saved_password = result[14]
            if bcrypt.hashpw(password.encode(), saved_password.encode()) == saved_password.encode():
                self.user = result
                return True
            else:
                return False
        else:
            return False
        
    def logout(self):
        self.user = None

    #########################################
    #                                       #
    #                OTHERS                 #
    #                                       #
    #########################################

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

    def determine_bp(self, systolic, diastolic):
        if systolic >= 90 and systolic <= 120 and diastolic >= 60 and diastolic <= 80:
            result = 'normal'
        elif systolic < 90 and diastolic < 60:
            result = 'low'
        else:
            result = 'high'
        return result
    
    def determine_os(self, oxy_sat):
        if oxy_sat >= 95 and oxy_sat <= 100:
            result = 'normal'
        elif oxy_sat > 100:
            result = 'high'
        else:
            result = 'low'
        return result

    def determine_pr(self, pulse):
        if pulse >= 60 and pulse <= 100:
            result = 'normal'
        elif pulse >100:
            result = 'high'
        else:
            result = 'low'
        return result

    def determine_temp(self, temp):
        if temp >= 33 and temp <= 37:
            result = 'normal'
        elif temp > 37:
            result = 'high'
        else:
            result = 'low' 
        return result

    def save_reading(self, user_id, systolic, diastolic, oxy_sat, pulse, temp):
        query = f'INSERT INTO readings(user_id, blood_pressure_systolic, blood_pressure_diastolic, blood_pressure_rating, blood_saturation, blood_saturation_rating,temperature, temperature_rating, pulse_rate, pulse_rate_rating,created_at,updated_at) VALUES({user_id}, {systolic}, {diastolic}, "{self.determine_bp(systolic, diastolic)}", {oxy_sat}, "{self.determine_os(oxy_sat)}" ,{pulse}, "{self.determine_pr(pulse)}",{temp},"{self.determine_temp(temp)}", "{datetime.now()}",  "{datetime.now()}")'
        self.cursor.execute(query)