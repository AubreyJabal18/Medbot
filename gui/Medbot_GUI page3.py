import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Enhanced Medbot")
root.geometry("1030x540")
root.resizable(False, False)

bg_image1 = tk.PhotoImage(file=fr"images/Frame 4 (1).png")

canvas = tk.Canvas(root, width=1030, height=540)


canvas.pack()

bg_label = canvas.create_image(0, 0, anchor="nw", image=bg_image1)

second_image = Image.open(fr"images/box.png")
second_image = second_image.resize((400, 600), Image.ANTIALIAS)
second_image_tk = ImageTk.PhotoImage(second_image)
second_image_label = canvas.create_image(800, 325, image=second_image_tk) 


third_image = Image.open(fr"images/medbot.png")
third_image = third_image.resize((500, 500), Image.ANTIALIAS)
third_image_tk = ImageTk.PhotoImage(third_image)
third_image_label = canvas.create_image(180, 440, image=third_image_tk) 

box = Image.open(fr"images/white.png")
box = box.resize((450,450), Image.ANTIALIAS)
box_tk = ImageTk.PhotoImage(box)
box_label = canvas.create_image(425,280, image=box_tk)

check= Image.open(fr"images/sanitation/2.png")
check = check.resize((150, 200), Image.ANTIALIAS)
check_tk = ImageTk.PhotoImage(check)
check_label = canvas.create_image(740, 440, image=check_tk) 

wrong= Image.open(fr"images/sanitation/1.png")
wrong = wrong.resize((150, 200), Image.ANTIALIAS)
wrong_tk = ImageTk.PhotoImage(wrong)
wrong_label = canvas.create_image(870, 440, image=wrong_tk) 

sanitation= Image.open(fr"images/sanitation/5.png")
sanitation = sanitation.resize((300, 400), Image.ANTIALIAS)
sanitation_tk = ImageTk.PhotoImage(sanitation)
sanitation_label = canvas.create_image(800, 320, image=sanitation_tk) 

text = "HAND SANITATION"
text_label = canvas.create_text(800, 210, text=text, font=("Helvetica", 16, "bold"), fill="black")

highlight_color = "black" 
text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
text_label = canvas.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

text = "Place your hands near the \nright arm of the Enhanced \nMed-Bot, and we'll get this \nsanitation started."
text_label = canvas.create_text(425, 245, text=text, font=("Helvetica", 18), fill="black")


root.mainloop()
