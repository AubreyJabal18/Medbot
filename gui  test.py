import medbot
from datetime import datetime

import tkinter as tk
from PIL import Image, ImageTk

class Root(tk.Tk):
    def __init__(self, bot):
        super().__init__()
        self.medbot = bot
        self.title('Medbot')
        self.geometry("1030x540")
        self.resizable(False, False)

        self.show_homepage()

        self.mainloop()

    def show_homepage(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = Homepage(self, self.medbot)
        homepage.pack()

    def show_scan_page(self):
        for child in self.winfo_children():
            child.destroy()
        scan_page = ScanQRCodePage(self, self.medbot)
        scan_page.pack()

    def show_sanitation_page(self):
        for child in self.winfo_children():
            child.destroy()
        santitation_page = HandSanitiationPage(self, self.medbot)
        santitation_page.pack()
    
    def show_vitals_measuring_page(self):
        for child in self.winfo_children():
            child.destroy()
        vitals_measuring_page = VitalsMeasuringPage(self, self.medbot)
        vitals_measuring_page.pack()
    
    def show_vitals_reading_page(self, systolic, diastolic, pulse_rate, temperature, oxygen_saturation, bp_rating, pr_rating, temp_rating, os_rating):
        for child in self.winfo_children():
            child.destroy()
        vitals_reading_page = VitalsReadingPage(self, self.medbot, systolic, diastolic, pulse_rate, temperature, oxygen_saturation, bp_rating, pr_rating, temp_rating, os_rating)
        vitals_reading_page.pack()

    def show_thank_you_page(self):
        for child in self.winfo_children():
            child.destroy()
        thank_you_page = ThankYouPage(self, self.medbot)
        thank_you_page.pack()

class Homepage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(root, width=1030, height=540, **kwargs)
        self.medbot = bot

        self.bg_image1 = ImageTk.PhotoImage(file=fr"images/Frame 4 (1).png")

        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.third_image = Image.open(fr"images/medbot.png") 
        self.third_image = self.third_image.resize((500, 500), Image.ANTIALIAS)
        self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        self.third_image_label = self.create_image(220, 300, image=self.third_image_tk)

        self.logo = Image.open(fr"images/gui_logo.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.create_image(970, 60, image=self.logo_tk)

        self.highlight_color = "black"
        text = "WELCOME TO"
        self.text_label_highlight = self.create_text(540 + 2, 70 + 2, text=text, font=("ROBOTO", 40, "bold"), fill=self.highlight_color)
        self.text_label = self.create_text(540, 70, text=text, font=("ROBOTO", 40, "bold"), fill="white")

        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(540 + 2, 135 + 2, text=text, font=("ROBOTO", 27, "bold"), fill=self.highlight_color)
        self.text_label = self.create_text(540, 135, text=text, font=("ROBOTO", 27, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(540, 180, text=text, font=("ROBOTO", 12, "italic"), fill="white")

        self.get_started_button = tk.Button(root, text="Get Started", font=("Helvetica", 24), command=self.on_get_started_click)
        self.get_started_button_window = self.create_window(615, 300, anchor="nw", window=self.get_started_button)
    
    def on_get_started_click(self):
        self.master.show_scan_page()

class ScanQRCodePage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(root, width=1030, height=540, **kwargs)
        self.medbot = bot

        self.bg_image1 = ImageTk.PhotoImage(file=fr"images/Frame 4 (1).png")

        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.second_image = Image.open(fr"images/reminder.png")
        self.second_image = self.second_image.resize((1000, 1000), Image.ANTIALIAS)
        self.second_image_tk = ImageTk.PhotoImage(self.second_image)
        self.second_image_label = self.create_image(750, 350, image=self.second_image_tk)

        self.third_image = Image.open(fr"images/medbot.png") 
        self.third_image = self.third_image.resize((500, 500), Image.ANTIALIAS)
        self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        self.third_image_label = self.create_image(220, 300, image=self.third_image_tk)

        self.logo = Image.open(fr"images/gui_logo.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.create_image(970, 60, image=self.logo_tk)

        self.highlight_color = "black"
        text = "WELCOME TO"
        self.text_label_highlight = self.create_text(540 + 2, 70 + 2, text=text, font=("ROBOTO", 40, "bold"), fill=self.highlight_color)
        self.text_label = self.create_text(540, 70, text=text, font=("ROBOTO", 40, "bold"), fill="white")

        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(540 + 2, 135 + 2, text=text, font=("ROBOTO", 27, "bold"), fill=self.highlight_color)
        self.text_label = self.create_text(540, 135, text=text, font=("ROBOTO", 27, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(540, 180, text=text, font=("ROBOTO", 12, "italic"), fill="white")

        text = "If you don't have an account\nyet, feel free to register on\nour website or simply scan\nthe QR Code we've got right\nhere for you."
        self.text_label = self.create_text(750, 350, text=text, font=("Helvetica", 18), fill="black")
        
        text = "Want to check your vital sign?"
        self.text_label = self.create_text(470, 490, text=text, font=("ROBOTO", 12, "bold"), fill="white")

        self.qr_code_window = None
        self.qr_code_bg_image1 = ImageTk.PhotoImage(file=fr"images/Frame 4.png")

        self.after(500, self.welcome)
        
    def welcome(self):
        self.medbot.speak('Hi')
        self.medbot.speak('I am Enhanced Med-Bot')
        self.medbot.speak('Youre All in One Healthcare Budddy')
        self.medbot.speak('To proceed, please scan your qrcode')

        self.after(50, self.on_qr_code_click)

    def on_qr_code_click(self):
        qr_data = self.medbot.scan_qrcode()
        credentials = qr_data.split(' ')
        if credentials[0] != 'medbot':
            self.medbot.speak('Wrong QRCode')
            return
        user_id = credentials[1]
        password = credentials[2]
        if not bot.login(user_id, password):
            self.medbot.speak('Credentials do not match')
            return
        self.medbot.speak(f'Welcome {self.medbot.user[1]}')
        self.master.show_sanitation_page()

class HandSanitiationPage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(master = root, width=1030, height=540, **kwargs)
        self.medbot = bot

        self.bg_image1 = tk.PhotoImage(file=fr"images/Frame 4 (1).png")
        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.logo = Image.open(fr"images/gui_logo.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.create_image(990, 40, image=self.logo_tk)

        self.second_image = Image.open(fr"images/blue.png")
        self.second_image = self.second_image.resize((400, 600), Image.ANTIALIAS)
        self.second_image_tk = ImageTk.PhotoImage(self.second_image)
        self.second_image_label = self.create_image(800, 325, image=self.second_image_tk) 

        self.third_image = Image.open(fr"images/medbot.png")
        self.third_image = self.third_image.resize((500, 500), Image.ANTIALIAS)
        self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        self.third_image_label = self.create_image(180, 440, image=self.third_image_tk) 

        self.box = Image.open(fr"images/white.png")
        self.box = self.box.resize((450,450), Image.ANTIALIAS)
        self.box_tk = ImageTk.PhotoImage(self.box)
        self.box_label = self.create_image(425,280, image=self.box_tk)

        self.check= Image.open(fr"images/sanitation/2.png")
        self.check = self.check.resize((150, 200), Image.ANTIALIAS)
        self.check_tk = ImageTk.PhotoImage(self.check)
        self.check_label = self.create_image(740, 440, image=self.check_tk) 

        self.wrong= Image.open(fr"images/sanitation/1.png")
        self.wrong = self.wrong.resize((150, 200), Image.ANTIALIAS)
        self.wrong_tk = ImageTk.PhotoImage(self.wrong)
        self.wrong_label = self.create_image(870, 440, image=self.wrong_tk) 

        self.sanitation= Image.open(fr"images/sanitation/5.png")
        self.sanitation = self.sanitation.resize((300, 400), Image.ANTIALIAS)
        self.sanitation_tk = ImageTk.PhotoImage(self.sanitation)
        self.sanitation_label = self.create_image(800, 320, image=self.sanitation_tk) 

        text = "HAND SANITATION"
        self.text_label = self.create_text(800, 210, text=text, font=("Helvetica", 16, "bold"), fill="black")

        highlight_color = "black" 
        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
        self.text_label = self.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

        text = "Place your hands near the \nright arm of the Enhanced \nMed-Bot, and we'll get this \nsanitation started."
        self.text_label = self.create_text(425, 245, text=text, font=("Helvetica", 18), fill="black")

        self.after(500, self.welcome)
    
    def welcome(self):
        self.medbot.speak('Please put your hands in front of the sanitizer')
        
        self.after(500, self.hand_sanitation)

    def hand_sanitation(self):
        hand_position = self.medbot.detect_hand()
        while hand_position != '91':
            if hand_position == '95':
                self.medbot.speak('Hand is too close')
            elif hand_position == '96':
                self.medbot.speak('Hand is too far')
            hand_position = self.medbot.detect_hand()
        self.medbot.speak('Please keep your hands still. Now starting sanitizer')

        # Start sanitizer
        self.medbot.start_hand_santizer(wait_until_completed=True)

        self.medbot.speak('Sanitizing complete')
        
        self.master.show_vitals_measuring_page()

class VitalsMeasuringPage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(master = root, width=1030, height=540, **kwargs)
        self.medbot = bot

        self.image = Image.open(fr"images/Frame 5.png")
        self.image = self.image.resize((1030, 540), Image.ANTIALIAS)
        self.bg_image1 = ImageTk.PhotoImage(self.image)
        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.logo = Image.open(fr"images/gui_logo.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.create_image(990, 40, image=self.logo_tk)

        self.image2 = Image.open(fr"images/vitals/1.png")
        self.image2 = self.image2.resize((700, 700), Image.ANTIALIAS)
        self.image2_tk = ImageTk.PhotoImage(self.image2)
        self.image2_label = self.create_image(820, 250, image=self.image2_tk) 

        self.image3 = Image.open(fr"images/vitals/2.png")
        self.image3 = self.image3.resize((700, 700), Image.ANTIALIAS)
        self.image3_tk = ImageTk.PhotoImage(self.image3)
        self.image3_label = self.create_image(320, 250, image=self.image3_tk) 

        self.image4 = Image.open(fr"images/vitals/3.png")
        self.image4 = self.image4.resize((700, 700), Image.ANTIALIAS)
        self.image4_tk = ImageTk.PhotoImage(self.image4)
        self.image4_label = self.create_image(1070, 250, image=self.image4_tk) 

        self.image5 = Image.open(fr"images/vitals/4.png")
        self.image5 = self.image5.resize((700, 700), Image.ANTIALIAS)
        self.image5_tk = ImageTk.PhotoImage(self.image5)
        self.image5_label = self.create_image(60, 250, image=self.image5_tk)

        self.box1 = Image.open(fr"images/button (9).png")
        self.box1 = self.box1.resize((700, 700), Image.ANTIALIAS)
        self.box1_tk = ImageTk.PhotoImage(self.box1)
        self.box1_label = self.create_image(310, 248, image=self.box1_tk) 

        self.box2 = Image.open(fr"images/button (9).png")
        self.box2 = self.box2.resize((700, 700), Image.ANTIALIAS)
        self.box2_tk = ImageTk.PhotoImage(self.box2)
        self.box2_label = self.create_image(570, 248, image=self.box2_tk) 

        self.box3 = Image.open(fr"images/button (9).png")
        self.box3 = self.box3.resize((700, 700), Image.ANTIALIAS)
        self.box3_tk = ImageTk.PhotoImage(self.box3)
        self.box3_label = self.create_image(820, 248, image=self.box3_tk) 

        self.box4 = Image.open(fr"images/button (9).png")
        self.box4 = self.box4.resize((700, 700), Image.ANTIALIAS)
        self.box4_tk = ImageTk.PhotoImage(self.box4)
        self.box4_label = self.create_image(1070, 248, image=self.box4_tk)

        highlight_color = "black" 
        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
        self.text_label = self.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

        text = "BLOOD \nPRESSURE"
        self.text_label = self.create_text(160, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black")

        text = "OXYGEN \nSATURATION"
        self.text_label = self.create_text(425, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black")

        text = "TEMPERATURE"
        self.text_label = self.create_text(670, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black", justify=tk.CENTER)

        text = "PULSE RATE"
        self.text_label = self.create_text(920, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black", justify=tk.CENTER)

       
        self.after(500, self.welcome)
    
    def welcome(self):
        self.medbot.speak('Proceeding to vital signs measurement. Please position your arm correctly')
        self.medbot.speak('Please rest your arm properly')

        self.after(500)

        # # Detect arm position
        # arm_position = self.medbot.detect_arm()
        # while not arm_position:
        #     self.medbot.speak('Your arm is not detected')
        #     arm_position = bot.detect_arm()
        # self.medbot.speak('Your arm was detected')  

        self.after(500)

        self.medbot.speak('Please insert your finger on the oximeter')

        # Detect finger position until okay
        finger_position = self.medbot.detect_finger()
        while not finger_position:
            self.medbot.speak('Finger not detected')
            finger_position = self.medbot.detect_finger()

        #stepper clockwise
        self.medbot.lock_oximeter()
        self.medbot.speak('Locking oximeter, please do not remove your finger')

        self.medbot.speak('Please stay still. Now getting your Blood Pressure and Pulse Rate')

        # self.medbot.start_solenoid()

        # Get Blood Pressure
        systolic, diastolic, pulse_rate = self.medbot.start_blood_pressure_monitor()
        bp_rating = self.medbot.determine_bp(systolic, diastolic)
        print(systolic, diastolic)
        print(bp_rating)

        # Update the image of the box for Blood Pressure
        self.itemconfig(self.box1_label, image=(fr"images/button (9).png"))  # Replace 'new_image' with the image you want

        # Get Pulse Rate
        pr_rating = self.medbot.determine_pr(pulse_rate)
        print(pulse_rate)
        print(pr_rating)
        
        self.after(500)

        # Get Temperature
        self.medbot.speak('Now getting your Temperature Measurement')
        temperature = self.medbot.get_temperature()
        temp_rating = self.medbot.determine_temp(temperature)
        print(temperature)
        print(temp_rating)

        self.medbot.speak('Please stay still. Now getting your oxygen saturation')

        # Get Oxygen Saturation
        oxygen_saturation = self.medbot.start_oximeter()   
        os_rating = self.medbot.determine_os(oxygen_saturation)
        print(oxygen_saturation) 
        print(os_rating)

        # self.after(500)

        self.medbot.speak('Vital Signs Measurement has Completed')

        self.after(500)
        
        self.master.show_vitals_reading_page(systolic, diastolic, pulse_rate, temperature, oxygen_saturation, bp_rating, pr_rating, temp_rating, os_rating)


class VitalsReadingPage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, systolic, diastolic, pulse_rate, temperature, oxygen_saturation, bp_rating, pr_rating, temp_rating, os_rating, **kwargs):
        super().__init__(master = root, width=1030, height=540, **kwargs)
        self.medbot = bot
        self.systolic = systolic
        self.diastolic = diastolic
        self.pulse_rate = pulse_rate
        self.temperature = temperature
        self.oxygen_saturation = oxygen_saturation
        self.bp_rating = bp_rating
        self.pr_rating = pr_rating
        self.temp_rating = temp_rating
        self.os_rating = os_rating

        self.image = Image.open(fr"images/Frame 5.png")
        self.image = self.image.resize((1030, 540), Image.ANTIALIAS)

        self.bg_image1 = ImageTk.PhotoImage(self.image)

        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.logo = Image.open(fr"images/gui_logo.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.create_image(990, 40, image=self.logo_tk)

        self.image2 = Image.open(fr"images/vitals/7.png")
        self.image2 = self.image2.resize((700, 700), Image.ANTIALIAS)
        self.image2_tk = ImageTk.PhotoImage(self.image2)
        self.image2_label = self.create_image(500, 325, image=self.image2_tk) 

        self.image3 = Image.open(fr"images/vitals/8.png")
        self.image3 = self.image3.resize((700, 700), Image.ANTIALIAS)
        self.image3_tk = ImageTk.PhotoImage(self.image3)
        self.image3_label = self.create_image(550, 330, image=self.image3_tk) 

        self.image4 = Image.open(fr"images/vitals/9.png")
        self.image4 = self.image4.resize((700, 700), Image.ANTIALIAS)
        self.image4_tk = ImageTk.PhotoImage(self.image4)
        self.image4_label = self.create_image(500, 300, image=self.image4_tk) 

        self.image5 = Image.open(fr"images/vitals/10.png")
        self.image5 = self.image5.resize((700, 700), Image.ANTIALIAS)
        self.image5_tk = ImageTk.PhotoImage(self.image5)
        self.image5_label = self.create_image(550, 300, image=self.image5_tk) 

        self.image6 = Image.open(fr"images/button (13).png")
        self.image6 = self.image6.resize((800, 900), Image.ANTIALIAS)
        self.image6_tk = ImageTk.PhotoImage(self.image6)
        self.image6_label = self.create_image(515, 470, image=self.image6_tk)

        highlight_color = "black" 
        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
        self.text_label = self.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

        text = "BLOOD \nPRESSURE"
        self.text_label = self.create_text(370, 195, text=text, font=("ROBOTO", 12, "bold"), fill="black")

        text = "OXYGEN \nSATURATION"
        self.text_label = self.create_text(740, 195, text=text, font=("ROBOTO", 12, "bold"), fill="black")

        text = "TEMPERATURE"
        self.text_label = self.create_text(370, 345, text=text, font=("ROBOTO", 12, "bold"), fill="black", justify=tk.CENTER)

        text = "PULSE"
        self.text_label = self.create_text(740, 345, text=text, font=("ROBOTO", 12, "bold"), fill="black", justify=tk.CENTER)


        blood_pressure_reading = f"{systolic}/{diastolic}  mmHg" 
        self.blood_pressure_label = self.create_text(360, 230, text=blood_pressure_reading, font=("ROBOTO", 14, "underline bold"), fill="black")


        oxygen_saturation_reading = f"{oxygen_saturation}%" 
        self.oxygen_saturation_label = self.create_text(740, 230, text=oxygen_saturation_reading, font=("ROBOTO", 14, "underline bold"), fill="black")            

        temperature_reading = f"{temperature}°C" 
        self.temperature_label = self.create_text(360, 385, text=temperature_reading, font=("ROBOTO", 14, "underline bold"), fill="black")

        pulse_rate_reading = f"{pulse_rate} bpm"
        self.pulse_rate_label = self.create_text(740, 385, text=pulse_rate_reading, font=("ROBOTO", 14, "underline bold"), fill="black")

        text = "PRINT RESULT?"
        self.text_label = self.create_text(455, 470, text=text, font=("ROBOTO", 12, "bold"), fill="white")

        self.after(1000, self.after_init)
    
    def after_init(self):
        self.medbot.speak('Here are your vital measurement!')
        self.medbot.speak(f'Your blood pressure is {self.systolic} over {self.diastolic} MMHG and it is {self.bp_rating}') 
        self.medbot.speak(f'Your oxygen saturation is {self.oxygen_saturation} percent and it is {self.os_rating}')
        self.medbot.speak(f'Your temperature is {self.temperature} celcius and it is {self.temp_rating}')
        self.medbot.speak(f'Your pulse rate is {self.pulse_rate} BPM and it is {self.pr_rating}')

        self.medbot.speak('Do you want to print your vital sign measurement?')
        self.medbot.speak('Please click the button to print your results.')

         # Create the "Red" button
        self.red_button = tk.Button(root, text="NO", font=("Helvetica", 10), command=self.on_red_button_click, bg="red")
        self.red_button_window = self.create_window(300, 470, window=self.red_button)

        # Create the "Green" button
        self.green_button = tk.Button(root, text="YES", font=("Helvetica", 10), command=self.on_green_button_click, bg="green")
        self.green_button_window = self.create_window(600, 470, window=self.green_button)

    def on_red_button_click(self, event):
        self.master.show_thank_you_page()
    
    def on_green_button_click(self, event):

        message = f'''     
   
    MARINDUQUE STATE COLLEGE
     TANZA, BOAC, MARIDUQUE
_________________________________

        ENHANCED MED-BOT
    "YOU'RE ULTIMATE ALL-ONE 
        HEALTHCARE BUDDY"    

    Here are your vital sign 
      measurement results.

Name: {bot.user[1]}, {bot.user[2]}
Blood Pressure: {self.systolic}/{self.diastolic} mmHg ({self.bp_rating})
Oxygen Saturation:  {self.oxygen_saturation} % ({self.os_rating})
Temperature: {self.temperature} C ({self.temp_rating})
Pulse Rate: {self.pulse_rate} bpm ({self.pr_rating})

_________________________________
      THANK YOU FOR USING 
        ENHANCED MED-BOT

{datetime.now()}


    '''
        self.medbot.print(message) 
    
        self.master.show_thank_you_page()

class ThankYouPage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(master = root, width=1030, height=540, **kwargs)
        self.medbot = bot

        self.image = Image.open(fr"images/Frame 5.png")
        self.image =  self.image.resize((1030, 540), Image.ANTIALIAS)

        self.bg_image1 = ImageTk.PhotoImage(self.image)

        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.image2 = Image.open(fr"images/button (18).png")
        self.image2 = self.image2.resize((900, 700), Image.ANTIALIAS)
        self.image2_tk = ImageTk.PhotoImage(self.image2)
        self.image2_label = self.create_image(515, 320, image=self.image2_tk) 

        self.logo = Image.open(fr"images/gui_logo.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.create_image(990, 40, image=self.logo_tk)

        highlight_color = "black" 
        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
        self.text_label = self.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

        text = "Well done on completing your vital sign \ncheck up! We genuinely thank you for \nchoosing our Med-Bot and allowing us to \nassist you in monitoring your well-being."
        self.text_label = self.create_text(515, 320, text=text, font=("ROBOTO", 20, "bold italic"), fill="black")

        self.after(1000, self.thankyou)
    
    def thankyou(self):   
        self.medbot.speak('Well done on completing your vital sign check up! We genuinely thank you for choosing our Med-Bot and allowing us to assist you in monitoring your well-being.')

if __name__ == "__main__":
    bot = medbot.Medbot()
    root = Root(bot)

