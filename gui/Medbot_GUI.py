import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Enhanced Medbot")
root.geometry("800x480")
root.resizable(False, False)

bg_image1 = tk.PhotoImage(file="C://Users//elma//Downloads//Frame 4.png")

canvas = tk.Canvas(root, width=800, height=480)
canvas.pack()

bg_label = canvas.create_image(0, 0, anchor="nw", image=bg_image1)

second_image = Image.open("C://Users//elma//Downloads//reminder.png")
second_image = second_image.resize((900, 950), Image.ANTIALIAS)
second_image_tk = ImageTk.PhotoImage(second_image)
second_image_label = canvas.create_image(620, 300, image=second_image_tk) 

third_image = Image.open("C://Users//elma//Downloads//medbot.png")
third_image = third_image.resize((300, 300), Image.ANTIALIAS)
third_image_tk = ImageTk.PhotoImage(third_image)
third_image_label = canvas.create_image(140, 340, image=third_image_tk) 

logo = Image.open("C://Users//elma//Downloads//gui_logo.png")
logo = logo.resize((50,50), Image.ANTIALIAS)
logo_tk = ImageTk.PhotoImage(logo)
logo_label = canvas.create_image(760, 40, image=logo_tk) 

highlight_color = "black" 
text = "WELCOME TO"
text_label_highlight = canvas.create_text(225 + 2, 70 + 2, text=text, font=("Comic Sans MS", 40, "bold"), fill=highlight_color)
text_label = canvas.create_text(225, 70, text=text, font=("Comic Sans MS", 40, "bold"), fill="white")

text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(225 + 2, 135 + 2, text=text, font=("ROBOTO", 27, "bold"), fill=highlight_color)
text_label = canvas.create_text(225, 135, text=text, font=("ROBOTO", 27, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(225, 180, text=text, font=("ROBOTO", 12, "italic"), fill="white")

text = "Want to check your vital sign?"
text_label = canvas.create_text(370, 425, text=text, font=("ROBOTO", 12, "bold italic"), fill="white")

# bg_image2 = Image.open("C://Users//elma//Downloads//button.png")
# bg_image2 = bg_image2.resize((500, 500), Image.ANTIALIAS)
# bg_image2_tk = ImageTk.PhotoImage(bg_image2)
# bg_image2_label = canvas.create_image(550, 455, image=bg_image2_tk) 

text = "If you don't have an account\nyet, feel free to register on\nour website or simply scan\nthe QR Code we've got right\nhere for you."
text_label = canvas.create_text(615, 300, text=text, font=("Helvetica", 16), fill="black")

def on_qr_code_click(event):
    # Implement the action you want to perform when the QR code is clicked
    # For example, open a website or show a QR code scanner dialog
    pass

# Create clickable text "Scan QR Code Here"
qr_code_text = "Scan QR Code Here"
qr_code_text_label = canvas.create_text(570, 425, text=qr_code_text, font=("Helvetica", 12, "underline"), fill="white")
canvas.tag_bind(qr_code_text_label, "<Button-1>", on_qr_code_click)  # Bind a click event to the text

root.mainloop()
