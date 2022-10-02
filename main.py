import tkinter as tk
from clipMaker import make_clip

bgImage = "starBG.jpg"


def btn_click():
    global bgImage
    text = textInput.get()
    if len(text) > 0:
        make_clip(text, bgImage)


def btn_sceleton_switch():
    global bgImage
    bgImage = "sceletonBG.jpg"
    button_choose_star.config(bg='grey')
    button_choose_fire.config(bg='grey')
    button_choose_sceleton.config(bg='cyan')


def btn_star_switch():
    global bgImage
    bgImage = "starBG.jpg"
    button_choose_star.config(bg='cyan')
    button_choose_fire.config(bg='grey')
    button_choose_sceleton.config(bg='grey')


def btn_fire_switch():
    global bgImage
    bgImage = "fireBG.jpg"
    button_choose_star.config(bg='grey')
    button_choose_fire.config(bg='cyan')
    button_choose_sceleton.config(bg='grey')


root = tk.Tk()

width = 800
height = 600
btn_font = 20

root['bg'] = '#cccccc'
root.title = "Clip Maker"
root.geometry(f"{width}x{height}")

root.resizable(width=False, height=False)

canvas = tk.Canvas(root, height=height, width=width)

frame = tk.Frame(root, bg='#cccccc')
frame.place(relwidth=1, relheight=1, relx=0.4, rely=0.5)

textInput = tk.Entry(frame, bg="grey")
textInput.grid(row=1, column=1)

button_make = tk.Button(frame, text="Сделать клип", bg='green', font=btn_font, command=btn_click)
button_make.grid(row=2, column=1, pady=15)

buttons_frame = tk.Frame(frame, bg='#cccccc')
buttons_frame.grid(row=3, column=1, pady=15)

button_choose_sceleton = tk.Button(buttons_frame, text="💀", bg='grey', font=btn_font, command=btn_sceleton_switch)
button_choose_sceleton.grid(row=1, column=1, padx=15)

button_choose_fire = tk.Button(buttons_frame, text="🔥", bg='grey', font=btn_font, command=btn_fire_switch)
button_choose_fire.grid(row=1, column=2, padx=15)

button_choose_star = tk.Button(buttons_frame, text="⭐", bg='cyan', font=btn_font, command=btn_star_switch)
button_choose_star.grid(row=1, column=3, padx=15)


root.mainloop()
