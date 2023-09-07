import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Enhanced Medbot")
root.geometry("1030x540")
root.resizable(False, False)

image = Image.open(fr"images/Frame 5.png")
image = image.resize((1030, 540), Image.ANTIALIAS)

bg_image1 = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=1030, height=540)
canvas.pack()

bg_label = canvas.create_image(0, 0, anchor="nw", image=bg_image1)

image2 = Image.open(fr"images/vitals/1.png")
image2_tk = ImageTk.PhotoImage(image2)
image2_label = canvas.create_image(245, 250, image=image2_tk) 

image3 = Image.open(fr"images/vitals/2.png")
image3_tk = ImageTk.PhotoImage(image3)
image3_label = canvas.create_image(245, 250, image=image3_tk) 

image4 = Image.open(fr"images/vitals/3.png")
image4_tk = ImageTk.PhotoImage(image4)
image4_label = canvas.create_image(635, 250, image=image4_tk) 

image5 = Image.open(fr"images/vitals/4.png")
image5_tk = ImageTk.PhotoImage(image5)
image5_label = canvas.create_image(635, 250, image=image5_tk) 

box1 = Image.open(fr"images/button (9).png")
box1_tk = ImageTk.PhotoImage(box1)
box1_label = canvas.create_image(245, 248, image=box1_tk) 

box2 = Image.open(fr"images/button (9).png")
box2_tk = ImageTk.PhotoImage(box2)
box2_label = canvas.create_image(440, 248, image=box2_tk) 

box3 = Image.open(fr"images/button (9).png")
box3_tk = ImageTk.PhotoImage(box3)
box3_label = canvas.create_image(635, 248, image=box3_tk) 

box4 = Image.open(fr"images/button (9).png")
box4_tk = ImageTk.PhotoImage(box4)
box4_label = canvas.create_image(828, 248, image=box4_tk) 

highlight_color = "black" 
text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(400 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
text_label = canvas.create_text(400, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(400, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

text = "TEMPERATURE"
text_label = canvas.create_text(128, 205, text=text, font=("ROBOTO", 12, "bold"), fill="black")

text = "PULSE RATE"
text_label = canvas.create_text(325, 205, text=text, font=("ROBOTO", 12, "bold"), fill="black")

text = "OXYGEN \nSATURATION"
text_label = canvas.create_text(520, 205, text=text, font=("ROBOTO", 12, "bold"), fill="black", justify=tk.CENTER)

text = "BLOOD \nPRESSURE"
text_label = canvas.create_text(710, 205, text=text, font=("ROBOTO", 12, "bold"), fill="black", justify=tk.CENTER)

root.mainloop()
