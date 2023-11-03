import tkinter as tk
from PIL import Image, ImageTk

def toggle_language():
    global current_language
    if current_language == "English":
        current_language = "Filipino"
        eng_button.config(state=tk.NORMAL)
        fil_button.config(state=tk.DISABLED)
    else:
        current_language = "English"
        fil_button.config(state=tk.NORMAL)
        eng_button.config(state=tk.DISABLED)
    update_language()

def update_language():
    if current_language == "English":
        label.config(text="Click the Button to switch language")
    else:
        label.config(text="Pindutin ang Button para magpalit ng Wika")

# Initialize the GUI
current_language = "English"


root = tk.Tk()
root.title("Enhanced Medbot")
root.geometry("1030x540")
root.resizable(False, False)


# Create a label
label = tk.Label(root, text="Click the Toggle Button to switch language")
label.pack(side='bottom', pady=5)


bg_image1 = tk.PhotoImage(file=fr"images/Frame 4 (1).png")

canvas = tk.Canvas(root, width=1030, height=540)

canvas.pack()

bg_label = canvas.create_image(0, 0, anchor="nw", image=bg_image1)

logo = Image.open(fr"images/gui_logo.png")
logo = logo.resize((70, 70), Image.ANTIALIAS)
logo_tk = ImageTk.PhotoImage(logo)
logo_label = canvas.create_image(990, 40, image=logo_tk)

third_image = Image.open(fr"images/medbot.png")
third_image = third_image.resize((500, 500), Image.ANTIALIAS)
third_image_tk = ImageTk.PhotoImage(third_image)
third_image_label = canvas.create_image(180, 440, image=third_image_tk) 

box = Image.open(fr"images/white.png")
box = box.resize((450,450), Image.ANTIALIAS)
box_tk = ImageTk.PhotoImage(box)
box_label = canvas.create_image(425,280, image=box_tk)


# Create buttons for switching language
eng_button = tk.Button(root, text="ENG", command=toggle_language)
eng_button.place(x=700, y=400)
if current_language == "English":
    eng_button.config(state=tk.DISABLED)

fil_button = tk.Button(root, text="FIL", command=toggle_language)
fil_button.place(x=760, y=400)
if current_language == "Filipino":
    fil_button.config(state=tk.DISABLED)

highlight_color = "black" 
text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(515 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
text_label = canvas.create_text(515, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(515, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

text = "Place your hands near the \nright arm of the Enhanced \nMed-Bot, and we'll get this \nsanitation started."
text_label = canvas.create_text(425, 245, text=text, font=("Helvetica", 18), fill="black")


root.mainloop()
