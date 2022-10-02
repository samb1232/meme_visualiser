import tkinter as tk
from clipMaker import make_clip


def btn_click():
    text = textInput.get()
    if len(text) > 0:
        make_clip(text)


root = tk.Tk()

width = 800
height = 600
btn_font = 20

root['bg'] = '#cccccc'
root.title = "Clip Maker"
root.geometry(f"{width}x{height}")

root.resizable(width=False, height=False)

canvas = tk.Canvas(root, height=height, width=width)

frame_right = tk.Frame(root, bg='#cccccc')
frame_right.place(relwidth=0.5, relheight=1, rely=0.4, relx=0.2)

textInput = tk.Entry(frame_right, bg="white")
textInput.grid(row=1, column=1)

button_make = tk.Button(frame_right, text="Сделать клип", bg='green', command=btn_click)
button_make.grid(row=2, column=1)

buttons_frame = tk.Frame(frame_right)
buttons_frame.grid(row=3, column=1)

button_choose_sceleton = tk.Button(buttons_frame, text="💀", bg='grey', font=btn_font)
button_choose_sceleton.grid(row=1, column=1)

button_choose_fire = tk.Button(buttons_frame, text="🔥", bg='grey', font=btn_font)
button_choose_fire.grid(row=1, column=2)

button_choose_star = tk.Button(buttons_frame, text="⭐", bg='cyan', font=btn_font)
button_choose_star.grid(row=1, column=3)

root.mainloop()
