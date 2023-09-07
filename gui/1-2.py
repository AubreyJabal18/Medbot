import tkinter as tk
from PIL import Image, ImageTk

class EnhancedMedBotApp:
    def __init__(self, root):
        self.root = root
        root.title("Enhanced Medbot")
        root.geometry("800x480")
        root.resizable(False, False)

        self.bg_image1 = ImageTk.PhotoImage(file="C://Users//elma//Downloads//Frame 4.png")

        self.canvas = tk.Canvas(root, width=800, height=480)
        self.canvas.pack()

        self.bg_label = self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image1)

        self.second_image = Image.open("C://Users//elma//Downloads//reminder.png")
        self.second_image = self.second_image.resize((900, 950), Image.ANTIALIAS)
        self.second_image_tk = ImageTk.PhotoImage(self.second_image)
        self.second_image_label = self.canvas.create_image(620, 300, image=self.second_image_tk)

        self.third_image = Image.open("C://Users//elma//Downloads//medbot.png")
        self.third_image = self.third_image.resize((300, 300), Image.ANTIALIAS)
        self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        self.third_image_label = self.canvas.create_image(140, 340, image=self.third_image_tk)

        self.logo = Image.open("C://Users//elma//Downloads//gui_logo.png")
        self.logo = self.logo.resize((50, 50), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.logo_label = self.canvas.create_image(760, 40, image=self.logo_tk)

        self.highlight_color = "black"
        text = "WELCOME TO"
        self.text_label_highlight = self.canvas.create_text(225 + 2, 70 + 2, text=text, font=("Comic Sans MS", 40, "bold"), fill=self.highlight_color)
        self.text_label = self.canvas.create_text(225, 70, text=text, font=("Comic Sans MS", 40, "bold"), fill="white")

        text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.canvas.create_text(225 + 2, 135 + 2, text=text, font=("ROBOTO", 27, "bold"), fill=self.highlight_color)
        self.text_label = self.canvas.create_text(225, 135, text=text, font=("ROBOTO", 27, "bold"), fill="#26B4BE")

        text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.canvas.create_text(225, 180, text=text, font=("ROBOTO", 12, "italic"), fill="white")

        text = "If you don't have an account\nyet, feel free to register on\nour website or simply scan\nthe QR Code we've got right\nhere for you."
        self.text_label = self.canvas.create_text(615, 300, text=text, font=("Helvetica", 16), fill="black")
        
        text = "Want to check your vital sign?"
        self.text_label = self.canvas.create_text(370, 425, text=text, font=("ROBOTO", 12, "bold italic"), fill="white")

        self.qr_code_text = "Scan QR Code Here"
        self.qr_code_text_label = self.canvas.create_text(570, 425, text=self.qr_code_text, font=("Helvetica", 12, "underline"), fill="white")
        self.canvas.tag_bind(self.qr_code_text_label, "<Button-1>", self.on_qr_code_click)  # Bind a click event to the text

    def on_qr_code_click(self, event):
        self.qr_code_window = tk.Toplevel()
        self.qr_code_window.title("QR Code Scanner")
        self.qr_code_window.geometry("800x480")
        self.qr_code_window.resizable(False, False)

        # Background image
        self.qr_code_canvas = tk.Canvas(self.qr_code_window, width=800, height=480)
        self.qr_code_canvas.pack()
        self.qr_code_bg_label = self.qr_code_canvas.create_image(0, 0, anchor="nw", image=self.qr_code_bg_image1)

        # Other elements for QR Code Scanner
        self.second_image = Image.open("C://Users//elma//Downloads//Rectangle 9.png")
        self.second_image = self.second_image.resize((300, 300), Image.ANTIALIAS)
        self.second_image_tk = ImageTk.PhotoImage(self.second_image)
        self.qr_code_second_image_label = self.qr_code_canvas.create_image(630, 300, image=self.second_image_tk)

        self.image = Image.open("C://Users//elma//Downloads//image.png")
        self.image = self.image.resize((260, 250), Image.ANTIALIAS)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.qr_code_image_label = self.qr_code_canvas.create_image(630, 300, image=self.image_tk)

        self.third_image = Image.open("C://Users//elma//Downloads//medbot.png")
        self.third_image = self.third_image.resize((300, 300), Image.ANTIALIAS)
        self.third_image_tk = ImageTk.PhotoImage(self.third_image)
        self.qr_code_third_image_label = self.qr_code_canvas.create_image(140, 300, image=self.third_image_tk)

        self.logo = Image.open("C://Users//elma//Downloads//gui_logo.png")
        self.logo = self.logo.resize((50, 50), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.qr_code_logo_label = self.qr_code_canvas.create_image(760, 40, image=self.logo_tk)

        self.highlight_color = "black"
        self.text = "ENHANCED MED-BOT"
        self.text_label_highlight = self.qr_code_canvas.create_text(400 + 2, 60 + 2, text=self.text, font=("ROBOTO", 30, "bold"), fill=self.highlight_color)
        self.text_label = self.qr_code_canvas.create_text(400, 60, text=self.text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

        self.text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
        self.text_label = self.qr_code_canvas.create_text(400, 100, text=self.text, font=("ROBOTO", 14, "italic"), fill="white")

        self.text = "Scan Your \n QR Code"
        self.text_label = self.qr_code_canvas.create_text(370, 280, text=self.text, font=("Helvetica", 30, "bold"), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedMedBotApp(root)
    root.mainloop()
