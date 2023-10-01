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

logo = Image.open(fr"images/gui_logo.png")
logo = logo.resize((70, 70), Image.ANTIALIAS)
logo_tk = ImageTk.PhotoImage(logo)
logo_label = canvas.create_image(990, 40, image=logo_tk)

#TEMP
image2 = Image.open(fr"images/vitals/1.png")
image2 = image2.resize((700, 700), Image.ANTIALIAS)
image2_tk = ImageTk.PhotoImage(image2)
image2_label = canvas.create_image(820, 250, image=image2_tk) 

image3 = Image.open(fr"images/vitals/2.png")
image3 = image3.resize((700, 700), Image.ANTIALIAS)
image3_tk = ImageTk.PhotoImage(image3)
image3_label = canvas.create_image(320, 250, image=image3_tk) 

image4 = Image.open(fr"images/vitals/3.png")
image4 = image4.resize((700, 700), Image.ANTIALIAS)
image4_tk = ImageTk.PhotoImage(image4)
image4_label = canvas.create_image(1070, 250, image=image4_tk) 

image5 = Image.open(fr"images/vitals/4.png")
image5 = image5.resize((700, 700), Image.ANTIALIAS)
image5_tk = ImageTk.PhotoImage(image5)
image5_label = canvas.create_image(60, 250, image=image5_tk) 

box1 = Image.open(fr"images/button (9).png")
box1 = box1.resize((700, 700), Image.ANTIALIAS)
box1_tk = ImageTk.PhotoImage(box1)
box1_label = canvas.create_image(310, 248, image=box1_tk) 

box2 = Image.open(fr"images/button (9).png")
box2 = box2.resize((700, 700), Image.ANTIALIAS)
box2_tk = ImageTk.PhotoImage(box2)
box2_label = canvas.create_image(570, 248, image=box2_tk) 

box3 = Image.open(fr"images/button (9).png")
box3 = box3.resize((700, 700), Image.ANTIALIAS)
box3_tk = ImageTk.PhotoImage(box3)
box3_label = canvas.create_image(820, 248, image=box3_tk) 

box4 = Image.open(fr"images/button (9).png")
box4 = box4.resize((700, 700), Image.ANTIALIAS)
box4_tk = ImageTk.PhotoImage(box4)
box4_label = canvas.create_image(1070, 248, image=box4_tk)

highlight_color = "black" 
text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
text_label = canvas.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

text = "BLOOD \nPRESSURE"
text_label = canvas.create_text(160, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black")

text = "OXYGEN \nSATURATION"
text_label = canvas.create_text(425, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black")

text = "TEMPERATURE"
text_label = canvas.create_text(670, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black", justify=tk.CENTER)

text = "PULSE RATE"
text_label = canvas.create_text(920, 190, text=text, font=("ROBOTO", 14, "bold"), fill="black", justify=tk.CENTER)

root.mainloop()
