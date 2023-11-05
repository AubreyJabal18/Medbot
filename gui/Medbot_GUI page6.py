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

image2 = Image.open(fr"images/button (18).png")
image2 = image2.resize((900, 700), Image.ANTIALIAS)
image2_tk = ImageTk.PhotoImage(image2)
image2_label = canvas.create_image(515, 320, image=image2_tk) 

logo = Image.open(fr"images/gui_logo.png")
logo = logo.resize((70, 70), Image.ANTIALIAS)
logo_tk = ImageTk.PhotoImage(logo)
logo_label = canvas.create_image(990, 40, image=logo_tk)

highlight_color = "black" 
text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
text_label = canvas.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

text = "Tapos na ang pagkumpleto nang iyong vital \nsign check up! Kasi ay nagpapasalamat sa \niyong pagpili nang aming Med-Bot at pagpa-\npahintulot sa amin na tulungan ka sa \npagsubaybay sa iyong kagalingan."
text_label = canvas.create_text(515, 320, text=text, font=("ROBOTO", 20, "bold italic"), fill="black")



root.mainloop()
