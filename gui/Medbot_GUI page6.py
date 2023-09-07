import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Enhanced Medbot")
root.geometry("800x480")
root.resizable(False, False)

image = Image.open("C:\\Users\\elma\\OneDrive\\Desktop\\Medbot\\gui\\images\\Frame 5.png")
image = image.resize((800, 480), Image.ANTIALIAS)

bg_image1 = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=800, height=480)
canvas.pack()

bg_label = canvas.create_image(0, 0, anchor="nw", image=bg_image1)

image2 = Image.open("C:\\Users\\elma\\OneDrive\\Desktop\\Medbot\\gui\\images\\button (18).png")
image2 = image2.resize((800, 700), Image.ANTIALIAS)
image2_tk = ImageTk.PhotoImage(image2)
image2_label = canvas.create_image(400, 300, image=image2_tk) 

highlight_color = "black" 
text = "ENHANCED MED-BOT"
text_label_highlight = canvas.create_text(400 + 2, 60 + 2, text=text, font=("ROBOTO", 30, "bold"), fill=highlight_color)
text_label = canvas.create_text(400, 60, text=text, font=("ROBOTO", 30, "bold"), fill="#26B4BE")

text = "“Your Ultimate ALL-in-ONE Healthcare Buddy”"
text_label = canvas.create_text(400, 100, text=text, font=("ROBOTO", 14, "italic"), fill="white")

text = "Well done on completing your vital sign \ncheck up! We genuinely thank you for \nchoosing our Med-Bot and allowing us to \nassist you in monitoring your well-being."
text_label = canvas.create_text(410, 300, text=text, font=("ROBOTO", 20, "bold italic"), fill="black")



root.mainloop()