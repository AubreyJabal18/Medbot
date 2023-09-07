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

image2 = Image.open(fr"images/vitals/7.png")
image2_tk = ImageTk.PhotoImage(image2)
image2_label = canvas.create_image(400, 280, image=image2_tk) 

image3 = Image.open(fr"images/vitals/8.png")
image3_tk = ImageTk.PhotoImage(image3)
image3_label = canvas.create_image(400, 280, image=image3_tk) 

image4 = Image.open(fr"images/vitals/9.png")
image4_tk = ImageTk.PhotoImage(image4)
image4_label = canvas.create_image(400, 280, image=image4_tk) 

image5 = Image.open(fr"images/vitals/10.png")
image5_tk = ImageTk.PhotoImage(image5)
image5_label = canvas.create_image(400, 280, image=image5_tk) 

image6 = Image.open(fr"images/button (13).png")
image6_tk = ImageTk.PhotoImage(image6)
image6_label = canvas.create_image(400, 420, image=image6_tk) 

red_button = canvas.create_rectangle(450, 410, 480, 430, fill="red")
red_button_label = canvas.create_text(465, 420, text="No", font=("ROBOTO", 12, "bold"), fill="white")

green_button = canvas.create_rectangle(410, 410, 440, 430, fill="green")
green_button_label = canvas.create_text(425, 420, text="Yes", font=("ROBOTO", 12, "bold"), fill="white")


highlight_color = "black" 
text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(400 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
text_label = canvas.create_text(400, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(400, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

text = "TEMPERATURE"
text_label = canvas.create_text(295, 175, text=text, font=("ROBOTO", 12, "bold"), fill="black")

text = "PULSE RATE"
text_label = canvas.create_text(540, 175, text=text, font=("ROBOTO", 12, "bold"), fill="black")

text = "OXYGEN \nSATURATION"
text_label = canvas.create_text(295, 310, text=text, font=("ROBOTO", 12, "bold"), fill="black", justify=tk.CENTER)

text = "BLOOD \nPRESSURE"
text_label = canvas.create_text(540, 310, text=text, font=("ROBOTO", 12, "bold"), fill="black", justify=tk.CENTER)

temperature_reading = "37 °C" 
temperature_label = canvas.create_text(295, 205, text=temperature_reading, font=("ROBOTO", 12, "bold"), fill="black")

pulse_rate_reading = "98 BPM"
pulse_rate_label = canvas.create_text(540, 205, text=pulse_rate_reading, font=("ROBOTO", 12, "bold"), fill="black")

oxygen_saturation_reading = "95%" 
oxygen_saturation_label = canvas.create_text(290, 345, text=oxygen_saturation_reading, font=("ROBOTO", 12, "bold"), fill="black")

blood_pressure_reading = "120/80 mmHg" 
blood_pressure_label = canvas.create_text(540, 345, text=blood_pressure_reading, font=("ROBOTO", 12, "bold"), fill="black")

text = "PRINT RESULT?"
text_label = canvas.create_text(350, 420, text=text, font=("ROBOTO", 10, "bold"), fill="white")

root.mainloop()
