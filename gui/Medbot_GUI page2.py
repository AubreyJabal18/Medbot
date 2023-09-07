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

second_image = Image.open("C://Users//elma//Downloads//Rectangle 9.png")
second_image = second_image.resize((300, 300), Image.ANTIALIAS)
second_image_tk = ImageTk.PhotoImage(second_image)
second_image_label = canvas.create_image(630, 300, image=second_image_tk) 

image = Image.open("C://Users//elma//Downloads//image.png")
image = image.resize((260, 250), Image.ANTIALIAS)
image_tk = ImageTk.PhotoImage(image)
image_label = canvas.create_image(630, 300, image=image_tk) 

third_image = Image.open("C://Users//elma//Downloads//medbot.png")
third_image = third_image.resize((300, 300), Image.ANTIALIAS)
third_image_tk = ImageTk.PhotoImage(third_image)
third_image_label = canvas.create_image(140, 300, image=third_image_tk) 

logo = Image.open("C://Users//elma//Downloads//gui_logo.png")
logo = logo.resize((50,50), Image.ANTIALIAS)
logo_tk = ImageTk.PhotoImage(logo)
logo_label = canvas.create_image(760, 40, image=logo_tk) 

highlight_color = "black" 
text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(400 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
text_label = canvas.create_text(400, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(400, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

text = "Scan Your \n QR Code"
text_label = canvas.create_text(370, 280, text=text, font=("Helvetica", 30, "bold"), fill="black")



root.mainloop()
