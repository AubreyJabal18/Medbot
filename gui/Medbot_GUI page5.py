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
image2 = image2.resize((700, 700), Image.ANTIALIAS)
image2_tk = ImageTk.PhotoImage(image2)
image2_label = canvas.create_image(500, 325, image=image2_tk) 

image3 = Image.open(fr"images/vitals/8.png")
image3 = image3.resize((700, 700), Image.ANTIALIAS)
image3_tk = ImageTk.PhotoImage(image3)
image3_label = canvas.create_image(550, 330, image=image3_tk) 

image4 = Image.open(fr"images/vitals/9.png")
image4 = image4.resize((700, 700), Image.ANTIALIAS)
image4_tk = ImageTk.PhotoImage(image4)
image4_label = canvas.create_image(500, 300, image=image4_tk) 

image5 = Image.open(fr"images/vitals/10.png")
image5 = image5.resize((700, 700), Image.ANTIALIAS)
image5_tk = ImageTk.PhotoImage(image5)
image5_label = canvas.create_image(550, 300, image=image5_tk) 

image6 = Image.open(fr"images/button (13).png")
image6 = image6.resize((800, 900), Image.ANTIALIAS)
image6_tk = ImageTk.PhotoImage(image6)
image6_label = canvas.create_image(515, 470, image=image6_tk) 

red_button = canvas.create_rectangle(600, 455, 640, 485, fill="red")
red_button_label = canvas.create_text(620, 470, text="No", font=("ROBOTO", 12, "bold"), fill="white")

green_button = canvas.create_rectangle(540, 455, 580, 485, fill="green")
green_button_label = canvas.create_text(560, 470, text="Yes", font=("ROBOTO", 12, "bold"), fill="white")


highlight_color = "black" 
text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
text_label = canvas.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

text = "TEMPERATURE"
text_label = canvas.create_text(370, 195, text=text, font=("ROBOTO", 12, "bold"), fill="black")

text = "PULSE RATE"
text_label = canvas.create_text(740, 195, text=text, font=("ROBOTO", 12, "bold"), fill="black")

text = "OXYGEN \nSATURATION"
text_label = canvas.create_text(370, 345, text=text, font=("ROBOTO", 12, "bold"), fill="black", justify=tk.CENTER)

text = "BLOOD \nPRESSURE"
text_label = canvas.create_text(740, 345, text=text, font=("ROBOTO", 12, "bold"), fill="black", justify=tk.CENTER)

temperature_reading = "37 °C" 
temperature_label = canvas.create_text(360, 230, text=temperature_reading, font=("ROBOTO", 14, "underline bold"), fill="black")

pulse_rate_reading = "98 BPM"
pulse_rate_label = canvas.create_text(740, 230, text=pulse_rate_reading, font=("ROBOTO", 14, "underline bold"), fill="black")

oxygen_saturation_reading = "95%" 
oxygen_saturation_label = canvas.create_text(360, 385, text=oxygen_saturation_reading, font=("ROBOTO", 14, "underline bold"), fill="black")

blood_pressure_reading = "120/80 mmHg" 
blood_pressure_label = canvas.create_text(740, 385, text=blood_pressure_reading, font=("ROBOTO", 14, "underline bold"), fill="black")

text = "PRINT RESULT?"
text_label = canvas.create_text(455, 470, text=text, font=("ROBOTO", 12, "bold"), fill="white")

root.mainloop()
