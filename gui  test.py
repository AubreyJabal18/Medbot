import medbot

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

class Homepage(tk.Canvas):
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
        self.logo_label = self.create_image(990, 40, image=self.logo_tk)

        self.highlight_color = "black"
        text = "WELCOME TO"
        self.text_label_highlight = self.create_text(540 + 2, 70 + 2, text=text, font=("ROBOTO", 40, "bold"), fill=self.highlight_color)
        self.text_label = self.create_text(540, 70, text=text, font=("ROBOTO", 40, "bold"), fill="white")

        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(540 + 2, 135 + 2, text=text, font=("ROBOTO", 27, "bold"), fill=self.highlight_color)
        self.text_label = self.create_text(540, 135, text=text, font=("ROBOTO", 27, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(540, 180, text=text, font=("ROBOTO", 12, "italic"), fill="white")

        self.get_started_button = tk.Button(root, text="Get Started", font=("Helvetica", 16), command=self.on_get_started_click)
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
        self.logo_label = self.create_image(990, 40, image=self.logo_tk)

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

        self.qr_code_text = "Scan Your QR Code"
        self.qr_code_text_label = self.create_text(700, 490, text=self.qr_code_text, font=("Helvetica", 12, "underline italic"), fill="white")
        self.tag_bind(self.qr_code_text_label, "<Button-1>", self.on_qr_code_click) 

        self.qr_code_window = None
        self.qr_code_bg_image1 = ImageTk.PhotoImage(file=fr"images/Frame 4.png")

        self.after(500, self.welcome)
        
    def welcome(self):
        self.medbot.speak('Hi')
        self.medbot.speak('I am Enhanced Med-Bot')
        self.medbot.speak('Youre All in One Healthcare Budddy')
        self.medbot.speak('Please scan your qrcode')

    def on_qr_code_click(self, event):
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

        self.medbot.speak('Sanitizing complete. Please position your arm correctly')
        self.medbot.speak('Please rest your arm properly')

class VitalsMeasuringPage(tk.Canvas):
    def __init__(self, root: Root, bot: medbot.Medbot, **kwargs):
        super().__init__(master = root, width=1030, height=540, **kwargs)
        self.medbot = bot

        image = Image.open(fr"images/Frame 5.png")
        image = image.resize((1030, 540), Image.ANTIALIAS)
        bg_image1 = ImageTk.PhotoImage(image)
        self.bg_label = self.create_image(0, 0, anchor="nw", image=bg_image1)

        logo = Image.open(fr"images/gui_logo.png")
        logo = logo.resize((70, 70), Image.ANTIALIAS)
        logo_tk = ImageTk.PhotoImage(logo)
        self.logo_label = self.create_image(990, 40, image=logo_tk)

        image2 = Image.open(fr"images/vitals/1.png")
        image2 = image2.resize((700, 700), Image.ANTIALIAS)
        image2_tk = ImageTk.PhotoImage(image2)
        self.image2_label = self.create_image(310, 250, image=image2_tk) 

        image3 = Image.open(fr"images/vitals/2.png")
        image3 = image3.resize((700, 700), Image.ANTIALIAS)
        image3_tk = ImageTk.PhotoImage(image3)
        self.image3_label = self.create_image(320, 250, image=image3_tk) 

        image4 = Image.open(fr"images/vitals/3.png")
        image4 = image4.resize((700, 700), Image.ANTIALIAS)
        image4_tk = ImageTk.PhotoImage(image4)
        self.image4_label = self.create_image(820, 250, image=image4_tk) 

        image5 = Image.open(fr"images/vitals/4.png")
        image5 = image5.resize((700, 700), Image.ANTIALIAS)
        image5_tk = ImageTk.PhotoImage(image5)
        self.image5_label = self.create_image(820, 250, image=image5_tk) 

        box1 = Image.open(fr"images/button (9).png")
        box1 = box1.resize((700, 700), Image.ANTIALIAS)
        box1_tk = ImageTk.PhotoImage(box1)
        self.box1_label = self.create_image(310, 248, image=box1_tk) 

        box2 = Image.open(fr"images/button (9).png")
        box2 = box2.resize((700, 700), Image.ANTIALIAS)
        box2_tk = ImageTk.PhotoImage(box2)
        self.box2_label = self.create_image(570, 248, image=box2_tk) 

        box3 = Image.open(fr"images/button (9).png")
        box3 = box3.resize((700, 700), Image.ANTIALIAS)
        box3_tk = ImageTk.PhotoImage(box3)
        self.box3_label = self.create_image(820, 248, image=box3_tk) 

        box4 = Image.open(fr"images/button (9).png")
        box4 = box4.resize((700, 700), Image.ANTIALIAS)
        box4_tk = ImageTk.PhotoImage(box4)
        self.box4_label = self.create_image(1070, 248, image=box4_tk)

        highlight_color = "black" 
        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
        self.text_label = self.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

        text = "TEMPERATURE"
        self.text_label = self.create_text(160, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black")

        text = "PULSE RATE"
        self.text_label = self.create_text(425, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black")

        text = "OXYGEN \nSATURATION"
        self.text_label = self.create_text(670, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black", justify=tk.CENTER)

        text = "BLOOD \nPRESSURE"
        self.text_label = self.create_text(920, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black", justify=tk.CENTER)


if __name__ == "__main__":
    bot = medbot.Medbot()
    root = Root(bot)

