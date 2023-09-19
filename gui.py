import medbot

import tkinter as tk
from PIL import Image, ImageTk

class EnhancedMedBotApp:
    def __init__(self, root, bot):
        self.root = root
        self.medbot = bot
        root.title("Enhanced Medbot")
        root.geometry("1030x540")
        root.resizable(False, False)

        self.bg_image1 = ImageTk.PhotoImage(file=fr"images/Frame 4 (1).png")

        self.canvas = tk.Canvas(root, width=1030, height=540)
        self.canvas.pack()

        self.bg_label = self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.second_image = Image.open(fr"images/reminder.png")
        self.second_image = self.second_image.resize((1000, 1000), Image.ANTIALIAS)
        self.second_image_tk = ImageTk.PhotoImage(self.second_image)
        self.second_image_label = self.canvas.create_image(750, 350, image=self.second_image_tk)

        self.third_image = Image.open(fr"images/medbot.png") 
        self.third_image = self.third_image.resize((500, 500), Image.ANTIALIAS)
        self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        self.third_image_label = self.canvas.create_image(220, 300, image=self.third_image_tk)

        self.logo = Image.open(fr"images/gui_logo.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.canvas.create_image(990, 40, image=self.logo_tk)

        self.highlight_color = "black"
        text = "WELCOME TO"
        self.text_label_highlight = self.canvas.create_text(540 + 2, 70 + 2, text=text, font=("ROBOTO", 40, "bold"), fill=self.highlight_color)
        self.text_label = self.canvas.create_text(540, 70, text=text, font=("ROBOTO", 40, "bold"), fill="white")

        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.canvas.create_text(540 + 2, 135 + 2, text=text, font=("ROBOTO", 27, "bold"), fill=self.highlight_color)
        self.text_label = self.canvas.create_text(540, 135, text=text, font=("ROBOTO", 27, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.canvas.create_text(540, 180, text=text, font=("ROBOTO", 12, "italic"), fill="white")

        text = "If you don't have an account\nyet, feel free to register on\nour website or simply scan\nthe QR Code we've got right\nhere for you."
        self.text_label = self.canvas.create_text(750, 350, text=text, font=("Helvetica", 18), fill="black")
        
        text = "Want to check your vital sign?"
        self.text_label = self.canvas.create_text(470, 490, text=text, font=("ROBOTO", 12, "bold"), fill="white")

        self.qr_code_text = "Scan Your QR Code"
        self.qr_code_text_label = self.canvas.create_text(700, 490, text=self.qr_code_text, font=("Helvetica", 12, "underline italic"), fill="white")
        self.canvas.tag_bind(self.qr_code_text_label, "<Button-1>", self.on_qr_code_click) 

        self.qr_code_window = None
        self.qr_code_bg_image1 = ImageTk.PhotoImage(file=fr"images/Frame 4.png")

    def on_qr_code_click(self, event):
        self.root.withdraw()
        self.medbot.scan_qrcode()
        # self.qr_code_window = tk.Toplevel()
        # self.qr_code_window.title("QR Code Scanner")
        # self.qr_code_window.geometry("800x480")
        # self.qr_code_window.resizable(False, False)

        # self.qr_code_canvas = tk.Canvas(self.qr_code_window, width=800, height=480)
        # self.qr_code_canvas.pack()
        # self.qr_code_bg_label = self.qr_code_canvas.create_image(0, 0, anchor="nw", image=self.qr_code_bg_image1)

        # self.second_image = Image.open(fr"images/Rectangle 9.png")
        # self.second_image = self.second_image.resize((300, 300), Image.ANTIALIAS)
        # self.second_image_tk = ImageTk.PhotoImage(self.second_image)
        # self.qr_code_second_image_label = self.qr_code_canvas.create_image(630, 300, image=self.second_image_tk)

        # self.third_image = Image.open(fr"images/medbot.png")
        # self.third_image = self.third_image.resize((300, 300), Image.ANTIALIAS)
        # self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        # self.qr_code_third_image_label = self.qr_code_canvas.create_image(140, 300, image=self.third_image_tk)

        # self.logo = Image.open(fr"images/gui_logo.png")
        # self.logo = self.logo.resize((50, 50), Image.ANTIALIAS)
        # self.logo_tk = ImageTk.PhotoImage(self.logo)
        # self.qr_code_logo_label = self.qr_code_canvas.create_image(760, 40, image=self.logo_tk)

        # self.highlight_color = "black"
        # self.text = "ENHANCED MED-BOT"
        # self.text_label_highlight = self.qr_code_canvas.create_text(400 + 2, 60 + 2, text=self.text, font=("ROBOTO", 30, "bold"), fill=self.highlight_color)
        # self.text_label = self.qr_code_canvas.create_text(400, 60, text=self.text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        # self.text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        # self.text_label = self.qr_code_canvas.create_text(400, 100, text=self.text, font=("ROBOTO", 14, "italic"), fill="white")

        # self.text = "Scan Your \n QR Code"
        # self.text_label = self.qr_code_canvas.create_text(370, 280, text=self.text, font=("Helvetica", 30, "bold"), fill="black")

    def hand_sanitation(self):
        self.bg_image1 = tk.PhotoImage(file=fr"images/Frame 4 (1).png")

        self.canvas = tk.Canvas(root, width=1030, height=540)

        self.canvas.pack()

        self.bg_label = self.canvas.create_image(0, 0, anchor="nw", image=bg_image1)

        self.logo = Image.open(fr"images/gui_logo.png")
        self.logo = self.logo.resize((70, 70), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.canvas.create_image(990, 40, image=self.logo_tk)

        self.second_image = Image.open(fr"images/blue.png")
        self.second_image = self.second_image.resize((400, 600), Image.ANTIALIAS)
        self.second_image_tk = ImageTk.PhotoImage(self.second_image)
        self.second_image_label = self.canvas.create_image(800, 325, image=second_image_tk) 


        self.third_image = Image.open(fr"images/medbot.png")
        self.third_image = self.third_image.resize((500, 500), Image.ANTIALIAS)
        self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        self.third_image_label = self.canvas.create_image(180, 440, image=third_image_tk) 

        self.box = Image.open(fr"images/white.png")
        self.box = self.box.resize((450,450), Image.ANTIALIAS)
        self.box_tk = ImageTk.PhotoImage(self.box)
        self.box_label = self.canvas.create_image(425,280, image=self.box_tk)

        self.check= Image.open(fr"images/sanitation/2.png")
        self.check = self.check.resize((150, 200), Image.ANTIALIAS)
        self.check_tk = ImageTk.PhotoImage(self.check)
        self.check_label = self.canvas.create_image(740, 440, image=self.check_tk) 

        self.wrong= Image.open(fr"images/sanitation/1.png")
        self.wrong = self.wrong.resize((150, 200), Image.ANTIALIAS)
        self.wrong_tk = ImageTk.PhotoImage(self.wrong)
        self.wrong_label = self.canvas.create_image(870, 440, image=self.wrong_tk) 

        self.sanitation= Image.open(fr"images/sanitation/5.png")
        self.sanitation = self.sanitation.resize((300, 400), Image.ANTIALIAS)
        self.sanitation_tk = ImageTk.PhotoImage(self.sanitation)
        self.sanitation_label = self.canvas.create_image(800, 320, image=self.sanitation_tk) 

        text = "HAND SANITATION"
        self.text_label = self.canvas.create_text(800, 210, text=text, font=("Helvetica", 16, "bold"), fill="black")

        highlight_color = "black" 
        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.canvas.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
        self.text_label = self.canvas.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.canvas.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

        text = "Place your hands near the \nright arm of the Enhanced \nMed-Bot, and we'll get this \nsanitation started."
        self.text_label = self.canvas.create_text(425, 245, text=text, font=("Helvetica", 18), fill="black")


if __name__ == "__main__":
    root = tk.Tk()
    bot = medbot.Medbot()
    app = EnhancedMedBotApp(root, bot)
    root.after(1000, lambda: bot.speak('Welcome, I am Enhanced Med-bot'))
    root.after(1000, lambda:bot.speak('Youre ultimate all in one healthcare buddy'))
    root.after(1000, lambda:bot.speak('To start measuring, please click Scan your QR Code'))
    root.mainloop()
