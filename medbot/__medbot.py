from .__bp3gy12n import Microlife_BTLE#
from .__max30102 import MAX30102

########################################################
#                      Main Class                      #
########################################################

# This class requires a Database object to be initialized
# Commented lines is due to this code is being tested on a Windows Machine
# Would later remove if ported on Raspberry Pi
class Medbot:

    def __init__(self):
        self.oximeter = MAX30102()

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
    