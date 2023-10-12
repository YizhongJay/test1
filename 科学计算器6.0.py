# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:36:41 2023

@author: 79245
"""

import tkinter as tk
from tkinter import ttk
import math
from fractions import Fraction
import pygame
import cv2
from PIL import Image, ImageTk

pygame.mixer.init() 
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:36:41 2023

@author: 79245
"""

import tkinter as tk
import math
from fractions import Fraction
import pygame
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
pygame.mixer.init() 
def play_button_click_sound(): #音效函数
    pygame.mixer.music.load("audio/岡本光市 - 8.mp3") 
    pygame.mixer.music.play()
    

def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

def calculate_factorial():
    try:
        num = int(entry.get())
        result = math.factorial(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_square_root():
    try:
        num = float(entry.get())
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_fraction_to_decimal():
    try:
        fraction_str = entry.get()
        fraction = Fraction(fraction_str)
        result = float(fraction)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_decimal_to_fraction():
    try:
        num = float(entry.get())
        fraction = Fraction(num).limit_denominator()
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(fraction))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def on_button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        play_button_click_sound()
        expression = entry.get()
        result = calculate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "sin":
        expression = "math.sin(" + entry.get() + ")"
        result = calculate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif text == "cos":
        expression = "math.cos(" + entry.get() + ")"
        result = calculate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif text == "tan":
        expression = "math.tan(" + entry.get() + ")"
        result = calculate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif text == "sqrt":
        calculate_square_root()
    elif text == "abs":
        expression = "abs(" + entry.get() + ")"
        result = calculate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif text == "!":
        calculate_factorial()
    elif text == "x^2":
        expression = "({})**2".format(entry.get())
        result = calculate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif text == "分数":
        calculate_decimal_to_fraction()
    elif text == "小数":
        calculate_fraction_to_decimal()
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("450x680")
root.title("科学计算器")

# 创建一个 Frame 用于放置视频区域和按钮区域
frame = ttk.Frame(root)
frame.pack()
video_label = ttk.Label(frame)
video_label.grid(row=0, column=0, pady=(0, 10), columnspan=2, rowspan=2)



# 创建 entry 窗口
entry = tk.Entry(frame, font="Arial 28 bold", justify='right', width=30) 
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# 创建按钮区域
button_frame = ttk.Frame(frame)
button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
def update_video():
    _, frame = cap.read()
    if frame is not None:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (470,200))
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        video_label.config(image=photo)
        video_label.photo = photo
    if cap.isOpened():
        root.after(20, update_video)  # 每隔10毫秒更新一次视频帧

def play_video():
    global cap
    cap = cv2.VideoCapture('movie/apex第三季.mp4')  # 替换成你的视频文件路径
    update_video()  # 开始更新视频

def stop_video():
    global cap
    if cap.isOpened():
        cap.release()  # 释放视频捕获对象

def loop_video():  # 添加一个新的函数用于循环播放视频
    play_video()
    root.after(147000, loop_video)  # 每隔一秒重新播放视频

loop_video()  # 开始循环播放视频

play_button = ttk.Button(button_frame, text="播放视频", command=play_video)
play_button.grid(row=1, column=0)

photo = tk.PhotoImage(file="images/7.png")#将图片值赋予photo

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", ".", "=", "/",
    "C", "sin", "cos", "tan",
    "(", ")", "sqrt", "abs",
    "!", "x^2",
    "分数", "小数"
]

row = 1
col = 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, width=6,height=2,font="Arial 18",bg='#666', fg='white')
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
