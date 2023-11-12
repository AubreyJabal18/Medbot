import medbot
import datetime
import yaml
import tkinter as tk
from PIL import Image, ImageTk
import time

class Root(tk.Tk):
    # Initialize the GUI
    current_language = "English"

    def __init__(self, bot):
        super().__init__()
        self.medbot = bot
        self.title('Medbot')
        self.geometry("1030x540")
        self.resizable(False, False)

        self.load_config()
        self.language = self.config['active_language']

        self.show_homepage()

        self.mainloop()

    def update_language(self, language):
        self.config['active_language'] = language
        yaml.safe_dump(self.config)
        self.language = language

    def load_config(self):
        with open('config.yml', 'r') as file:
            self.config = yaml.safe_load(file) 

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
        vitals_reading_page = VitalsReadingPage(self, self.medbot, systolic, diastolic, pulse_rate, temperature, oxygen_saturation,bp_rating, pr_rating, temp_rating, os_rating)
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
        self.root = root
     
        self.bg_image1 = ImageTk.PhotoImage(file=fr"images/Frame 4 (1).png")

        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.third_image = Image.open(fr"images/side view 2.png") 
        self.third_image = self.third_image.resize((400, 500), Image.ANTIALIAS)
        self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        self.third_image_label = self.create_image(220, 280, image=self.third_image_tk)

        self.logo = Image.open(fr"images/gui_logo2.png")
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

        text1 = self.root.config['text_labels']['text1'][self.root.language]

        self.get_started_button = tk.Button(root, text=text1, font=("Helvetica", 24), command=self.on_get_started_click)
        self.get_started_button_window = self.create_window(615, 300, anchor="nw", window=self.get_started_button)

        # Create a label
        self.label = tk.Label(root, text="Click the Button to switch language")
        self.label.pack(side='bottom', pady=5)

        self.eng_button = tk.Button(root, text="ENG",command=self.toggle_language, width=5, height=2)
        self.eng_button.place(x=860, y=420)
        self.eng_button.config(font=("Helvetica", 12))

        if self.root.language == "eng":
            self.eng_button.config(state=tk.DISABLED)

        self.fil_button = tk.Button(root, text="FIL", command=self.toggle_language, width=5, height=2)
        self.fil_button.place(x=920, y=420)
        self.fil_button.config(font=("Helvetica", 12))

        if self.root.language == "fil":
            self.fil_button.config(state=tk.DISABLED)

    def toggle_language(self):
        if self.root.language == "eng":
            self.root.language = "fil"
            self.eng_button.config(state=tk.NORMAL)
            self.fil_button.config(state=tk.DISABLED)
            self.root.update_language('fil')

        else:
            self.root.language = "eng"
            self.fil_button.config(state=tk.NORMAL)
            self.eng_button.config(state=tk.DISABLED)
            self.update_language()
            self.root.update_language('eng')

    def update_language(self):
        if self.root.language == "eng":
            self.label.config(text="Click the Button to switch language")
        else:
            self.label.config(text="Pindutin ang Button para magpalit ng Wika")

    def on_get_started_click(self):
        self.master.show_scan_page()

class ScanQRCodePage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(root, width=1030, height=540, **kwargs)
        self.medbot = bot
        self.root = root

        self.bg_image1 = ImageTk.PhotoImage(file=fr"images/Frame 4 (1).png")

        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.second_image = Image.open(fr"images/reminder.png")
        self.second_image = self.second_image.resize((1000, 1000), Image.ANTIALIAS)
        self.second_image_tk = ImageTk.PhotoImage(self.second_image)
        self.second_image_label = self.create_image(750, 350, image=self.second_image_tk)

        self.third_image = Image.open(fr"images/side view 2.png") 
        self.third_image = self.third_image.resize((400, 500), Image.ANTIALIAS)
        self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        self.third_image_label = self.create_image(220, 280, image=self.third_image_tk)

        self.logo = Image.open(fr"images/gui_logo2.png")
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

        # text = "If you don't have an account\nyet, feel free to register on\nour website or simply scan\nthe QR Code we've got right\nhere for you."
        text2 = self.root.config['text_labels']['text2'][self.root.language]
        self.text2_label = self.create_text(750, 350, text=text2, font=("Helvetica", 18), fill="black")

        # text = "Want to check your vital sign?"
        # self.text_label = self.create_text(470, 490, text=text, font=("ROBOTO", 12, "bold"), fill="white")

        self.qr_code_window = None
        self.qr_code_bg_image1 = ImageTk.PhotoImage(file=fr"images/Frame 4.png")

        self.after(500, self.welcome)
        
    def welcome(self):
        self.medbot.speak(self.root.config['intro_prompt']['welcome'][self.root.language])
        self.medbot.speak(self.root.config['intro_prompt']['proceed'][self.root.language])

        self.after(50, self.on_qr_code_click)

    def on_qr_code_click(self):
        success = False
        ready = True
        last_scaned = datetime.datetime.now()
        while not success:
            if not ready:
                elapse_time = datetime.datetime.now() - last_scaned
                if elapse_time >= datetime.timedelta(seconds=7):
                    ready = True

            qr_data = self.medbot.scan_qrcode()
            credentials = qr_data.split(' ')
            
            if ready and credentials[0] != 'medbot':
    
                self.medbot.speak(self.root.config['scan_prompt']['fail_qrcode'][self.root.language])

                credentials[0] = None
                ready = False
                last_scaned = datetime.datetime.now()
                time.sleep(1)
                continue            
      
            if ready and credentials[0] == 'medbot':
                user_id = credentials[1]
                password = credentials[2]
                
                if not self.medbot.login(user_id, password):
                    
                    self.medbot.speak(self.root.config['scan_prompt']['fail_credentials'][self.root.language])

                    credentials[0] = None
                    ready = False
                    last_scaned = datetime.datetime.now()
                    time.sleep(1)
                    continue
                success = True

        self.medbot.speak(self.root.config['scan_prompt']['success'][self.root.language].format(self.medbot.user[1]))

        self.master.show_sanitation_page()

class HandSanitiationPage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(master = root, width=1030, height=540, **kwargs)
        self.medbot = bot
        self.root = root

        self.bg_image1 = tk.PhotoImage(file=fr"images/Frame 4 (1).png")
        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.logo = Image.open(fr"images/gui_logo2.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.create_image(990, 40, image=self.logo_tk)

        self.second_image = Image.open(fr"images/blue.png")
        self.second_image = self.second_image.resize((400, 600), Image.ANTIALIAS)
        self.second_image_tk = ImageTk.PhotoImage(self.second_image)
        self.second_image_label = self.create_image(800, 325, image=self.second_image_tk) 

        self.third_image = Image.open(fr"images/side view 2.png")
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

        # text = "Place your hands near the \nright arm of the Enhanced \nMed-Bot, and we'll get this \nsanitation started."
        
        text3 = self.root.config['text_labels']['text3'][self.root.language]
        self.text3_label = self.create_text(425, 245, text=text3, font=("Helvetica", 18), fill="black")

        self.after(500, self.welcome)
    
    def welcome(self):
        self.medbot.speak(self.root.config['sanitizing_prompt']['position'][self.root.language])

        self.after(500, self.hand_sanitation)

    def hand_sanitation(self):
        hand_position = self.medbot.detect_hand()
        while hand_position != '91':
            if hand_position == '95':
                self.medbot.speak(self.root.config['sanitizing_prompt']['too_close'][self.root.language])

            elif hand_position == '96':
                self.medbot.speak(self.root.config['sanitizing_prompt']['too_far'][self.root.language])

            hand_position = self.medbot.detect_hand()

        self.medbot.speak(self.root.config['sanitizing_prompt']['correct_position'][self.root.language])

        # Start sanitizer
        self.medbot.start_hand_santizer(wait_until_completed=True)

        self.medbot.speak(self.root.config['sanitizing_prompt']['success'][self.root.language])

        
        self.master.show_vitals_measuring_page()

class VitalsMeasuringPage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(master = root, width=1030, height=540, **kwargs)
        self.medbot = bot
        self.root = root

        self.image = Image.open(fr"images/Frame 5.png")
        self.image = self.image.resize((1030, 540), Image.ANTIALIAS)
        self.bg_image1 = ImageTk.PhotoImage(self.image)
        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.logo = Image.open(fr"images/gui_logo2.png")
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

        self.box1 = Image.open(fr"images/button (19).png")
        self.box1 = self.box1.resize((700, 700), Image.ANTIALIAS)
        self.box1_tk = ImageTk.PhotoImage(self.box1)
        self.box1_label = self.create_image(310, 248, image=self.box1_tk) 

        self.box2 = Image.open(fr"images/button (19).png")
        self.box2 = self.box2.resize((700, 700), Image.ANTIALIAS)
        self.box2_tk = ImageTk.PhotoImage(self.box2)
        self.box2_label = self.create_image(570, 248, image=self.box2_tk) 

        self.box3 = Image.open(fr"images/button (19).png")
        self.box3 = self.box3.resize((700, 700), Image.ANTIALIAS)
        self.box3_tk = ImageTk.PhotoImage(self.box3)
        self.box3_label = self.create_image(820, 248, image=self.box3_tk) 

        self.box4 = Image.open(fr"images/button (19).png")
        self.box4 = self.box4.resize((700, 700), Image.ANTIALIAS)
        self.box4_tk = ImageTk.PhotoImage(self.box4)
        self.box4_label = self.create_image(1070, 248, image=self.box4_tk)

        self.box5 = Image.open(fr"images/button (9).png")
        self.box5 = self.box5.resize((700, 700), Image.ANTIALIAS)
        self.box5_tk = ImageTk.PhotoImage(self.box5)
        
        highlight_color = "black"
        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
        self.text_label = self.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

        text = "BLOOD \nPRESSURE"
        self.text_label = self.create_text(160, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black")

        text = "OXYGEN \nSATURATION"
        self.text_label = self.create_text(920, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black")

        text = "TEMPERATURE"
        self.text_label = self.create_text(670, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black", justify=tk.CENTER)

        text = "PULSE RATE"
        self.text_label = self.create_text(425, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black", justify=tk.CENTER)

        self.after(500, self.welcome_os)
    
    def welcome_os(self):
        self.medbot.speak(self.root.config['finger_prompt']['position'][self.root.language])


        # Detect finger position until okay
        finger_position = self.medbot.detect_finger()
        while not finger_position:
            self.medbot.speak(self.root.config['finger_prompt']['fail'][self.root.language])

            finger_position = self.medbot.detect_finger()

        #stepper clockwise
        self.medbot.lock_oximeter()
        self.medbot.speak(self.root.config['finger_prompt']['success'][self.root.language])


        self.after(500, self.welcome_arm)
    
    def welcome_arm(self):
        self.medbot.speak(self.root.config['arm_prompt']['position'][self.root.language])
        self.medbot.speak(self.root.config['arm_prompt']['rest'][self.root.language])


        self.after(500)

        # Detect arm position
        # arm_position = self.medbot.detect_arm()
        # while not arm_position:
        #     self.medbot.speak(self.root.config['arm_prompt']['fail'][self.root.language])

        #     arm_position = bot.detect_arm()
        # self.medbot.speak(self.root.config['arm_prompt']['success'][self.root.language])


        # self.after(500)


        self.medbot.speak(self.root.config['vital_signs_measurement']['getting_bp'][self.root.language])


        self.medbot.start_solenoid()

        # Get temp
        self.after(500, self.get_bp_and_pr)

    def get_bp_and_pr(self):
        # Get Blood Pressure
        self.systolic, self.diastolic, self.pulse_rate = self.medbot.start_blood_pressure_monitor()
        self.bp_rating = self.medbot.determine_bp(self.systolic, self.diastolic)
        print(self.systolic, self.diastolic)
        print(self.bp_rating)  

        # Get Pulse Rate
        self.pr_rating = self.medbot.determine_pr(self.pulse_rate)
        print(self.pulse_rate)
        print(self.pr_rating)

        # Change the color of pr
        self.after(500, self.change_box_color1)

    # Function to change the box color of bp
    def change_box_color1(self):
        self.itemconfig(self.box1_label, image=self.box5_tk)
                                
        # Change the color of bp
        self.after(500, self.change_box_color2)

    # Function to change the box color of pr
    def change_box_color2(self):
        self.itemconfig(self.box2_label, image=self.box5_tk)

        # Get temp
        self.after(500, self.get_temperature)

    def get_temperature(self):
        # Get Temperature
        self.medbot.speak(self.root.config['vital_signs_measurement']['getting_temp'][self.root.language])

        self.temperature = self.medbot.get_temperature()
        self.temp_rating = self.medbot.determine_temp(self.temperature)
        print(self.temperature)
        print(self.temp_rating)

        # Change the color of temp after printing temperature rating
        self.after(500, self.change_box_color3)

    # Function to change the box color of temp
    def change_box_color3(self):
        self.itemconfig(self.box3_label, image=self.box5_tk)

        # Get Oxygen Saturation
        self.after(500, self.get_oxygen_saturation)

    def get_oxygen_saturation(self):
        self.medbot.speak(self.root.config['vital_signs_measurement']['getting_os'][self.root.language])

        self.oxygen_saturation = self.medbot.start_oximeter()  
        self.os_rating = self.medbot.determine_os(self.oxygen_saturation)
        print(self.oxygen_saturation)
        print(self.os_rating)

        # Change the color of spO2 after printing os rating
        self.after(500, self.change_box_color4)

    # Function to change the box color of spO2
    def change_box_color4(self):
        self.itemconfig(self.box4_label, image=self.box5_tk)

        # Perform final actions after printing os rating
        self.after(500, self.complete)

    # Perform final actions after both temp and os readings
    def complete(self):
        self.medbot.speak(self.root.config['vital_signs_measurement']['success'][self.root.language])    
        
        self.master.show_vitals_reading_page(self.systolic, self.diastolic, self.pulse_rate, self.temperature, self.oxygen_saturation, self.bp_rating, self.pr_rating, self.temp_rating, self.os_rating)


class VitalsReadingPage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, systolic, diastolic, pulse_rate, temperature, oxygen_saturation,  bp_rating, pr_rating, temp_rating, os_rating,**kwargs):
        super().__init__(master = root, width=1030, height=540, **kwargs)

        self.medbot = bot
        self.root = root
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

        self.logo = Image.open(fr"images/gui_logo2.png")
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

        # Create the "Red" button
        self.red_button = tk.Button(self, text="NO", font=("Helvetica", 10), command=self.on_red_button_click, bg="red")
        self.red_button_window = self.create_window(640, 470, window=self.red_button)

        # Create the "Green" button
        self.green_button = tk.Button(self, text="YES", font=("Helvetica", 10), command=self.on_green_button_click, bg="green")
        self.green_button_window = self.create_window(570, 470, window=self.green_button)

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


        self.medbot.save_reading(self.medbot.user[0], self.systolic, self.diastolic, self.oxygen_saturation, self.pulse_rate, self.temperature)
        
        self.after(1000, self.after_init)
    
    def after_init(self):
        self.medbot.speak(self.root.config['results_prompt']['prompt'][self.root.language])

        self.medbot.speak(self.root.config['results_prompt']['result_bp'][self.root.language].format(str(self.systolic), str(self.diastolic), str(self.bp_rating)))
       
        self.medbot.speak(self.root.config['results_prompt']['result_os'][self.root.language].format(str(self.oxygen_saturation), str(self.os_rating)))
     
        self.medbot.speak(self.root.config['results_prompt']['result_temp'][self.root.language].format(str(self.temperature), str(self.temp_rating)))
        
        self.medbot.speak(self.root.config['results_prompt']['result_pr'][self.root.language].format(str(self.pulse_rate), str(self.pr_rating)))

        self.medbot.speak(self.root.config['printing']['prompt'][self.root.language])
        

    def on_red_button_click(self):
        self.master.show_thank_you_page()
    
    def on_green_button_click(self):

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
Pulse Rate: {self.pulse_rate} bpm ({self.pr_rating})
Temperature: {self.temperature} C ({self.temp_rating})
Oxygen Saturation: {self.oxygen_saturation} % ({self.os_rating})


_________________________________
      THANK YOU FOR USING 
        ENHANCED MED-BOT

{datetime.datetime.now()}


    '''
        self.medbot.print(message)
    
        self.master.show_thank_you_page()

class ThankYouPage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(master = root, width=1030, height=540, **kwargs)
        self.medbot = bot
        self.root = root

        self.image = Image.open(fr"images/Frame 5.png")
        self.image =  self.image.resize((1030, 540), Image.ANTIALIAS)

        self.bg_image1 = ImageTk.PhotoImage(self.image)

        self.bg_label = self.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.image2 = Image.open(fr"images/button (18).png")
        self.image2 = self.image2.resize((900, 700), Image.ANTIALIAS)
        self.image2_tk = ImageTk.PhotoImage(self.image2)
        self.image2_label = self.create_image(515, 320, image=self.image2_tk) 

        self.logo = Image.open(fr"images/gui_logo2.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.create_image(990, 40, image=self.logo_tk)

        highlight_color = "black" 
        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
        self.text_label = self.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

        # text = "Well done on completing your vital sign \ncheck up! We genuinely thank you for \nchoosing our Med-Bot and allowing us to \nassist you in monitoring your well-being."
        text4 = self.root.config['text_labels']['text4'][self.root.language]
        self.text4_label = self.create_text(515, 320, text=text4, font=("ROBOTO", 20, "bold italic"), fill="black")

        self.after(1000, self.thankyou)
    
    def thankyou(self):   
        self.medbot.speak(self.root.config['printing']['thank_you_voice'][self.root.language])

if __name__ == "__main__":
    bot = medbot.Medbot()
    root = Root(bot)

