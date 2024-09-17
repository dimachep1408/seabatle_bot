import customtkinter
import os
from PIL import Image

screen = customtkinter.CTk(fg_color= "dark blue")
screen.geometry("700x700")

color_now = "dark red"
hover_color_now = "grey"
bg_color_now = "dark blue"

matrix_strings = [
    [],
    [],
    [],
    [],
    [],
    [],  
    [],
    [],
    [],
    [],
]

matrix_columns = [
    [],
    [],
    [],
    [],
    [],
    [],  
    [],
    [],
    [],
    [],
]


matrix_cells = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

final_matrix = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],  
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]


def button1_1_cmd():
    if button1_1._fg_color == "white" or button1_1._fg_color == "dark green":
        button1_1.configure(fg_color=color_now)
    elif button1_1._fg_color == "dark red" or button1_1._fg_color == "dark orange":
        button1_1.configure(fg_color="white")

def button1_2_cmd():
    if button1_2._fg_color == "white" or button1_2._fg_color == "dark green":
        button1_2.configure(fg_color=color_now)
    elif button1_2._fg_color == "dark red" or button1_2._fg_color == "dark orange":
        button1_2.configure(fg_color="white")

def button1_3_cmd():
    if button1_3._fg_color == "white" or button1_3._fg_color == "dark green":
        button1_3.configure(fg_color=color_now)
    elif button1_3._fg_color == "dark red" or button1_3._fg_color == "dark orange":
        button1_3.configure(fg_color="white")

def button1_4_cmd():
    if button1_4._fg_color == "white" or button1_4._fg_color == "dark green":
        button1_4.configure(fg_color=color_now)
    elif button1_4._fg_color == "dark red" or button1_4._fg_color == "dark orange":
        button1_4.configure(fg_color="white")

def button1_5_cmd():
    if button1_5._fg_color == "white" or button1_5._fg_color == "dark green":
        button1_5.configure(fg_color=color_now)
    elif button1_5._fg_color == "dark red" or button1_5._fg_color == "dark orange":
        button1_5.configure(fg_color="white")

def button1_6_cmd():
    if button1_6._fg_color == "white" or button1_6._fg_color == "dark green":
        button1_6.configure(fg_color=color_now)
    elif button1_6._fg_color == "dark red" or button1_6._fg_color == "dark orange":
        button1_6.configure(fg_color="white")

def button1_7_cmd():
    if button1_7._fg_color == "white" or button1_7._fg_color == "dark green":
        button1_7.configure(fg_color=color_now)
    elif button1_7._fg_color == "dark red" or button1_7._fg_color == "dark orange":
        button1_7.configure(fg_color="white")

def button1_8_cmd():
    if button1_8._fg_color == "white" or button1_8._fg_color == "dark green":
        button1_8.configure(fg_color=color_now)
    elif button1_8._fg_color == "dark red" or button1_8._fg_color == "dark orange":
        button1_8.configure(fg_color="white")

def button1_9_cmd():
    if button1_9._fg_color == "white" or button1_9._fg_color == "dark green":
        button1_9.configure(fg_color=color_now)
    elif button1_9._fg_color == "dark red" or button1_9._fg_color == "dark orange":
        button1_9.configure(fg_color="white")

def button1_10_cmd():
    if button1_10._fg_color == "white" or button1_10._fg_color == "dark green":
        button1_10.configure(fg_color=color_now)
    elif button1_10._fg_color == "dark red" or button1_10._fg_color == "dark orange":
        button1_10.configure(fg_color="white")

def button2_1_cmd():
    if button2_1._fg_color == "white" or button2_1._fg_color == "dark green":
        button2_1.configure(fg_color=color_now)
    elif button2_1._fg_color == "dark red" or button2_1._fg_color == "dark orange":
        button2_1.configure(fg_color="white")

def button2_2_cmd():
    if button2_2._fg_color == "white" or button2_2._fg_color == "dark green":
        button2_2.configure(fg_color=color_now)
    elif button2_2._fg_color == "dark red" or button2_2._fg_color == "dark orange":
        button2_2.configure(fg_color="white")

def button2_3_cmd():
    if button2_3._fg_color == "white" or button2_3._fg_color == "dark green":
        button2_3.configure(fg_color=color_now)
    elif button2_3._fg_color == "dark red" or button2_3._fg_color == "dark orange":
        button2_3.configure(fg_color="white")

def button2_4_cmd():
    if button2_4._fg_color == "white" or button2_4._fg_color == "dark green":
        button2_4.configure(fg_color=color_now)
    elif button2_4._fg_color == "dark red" or button2_4._fg_color == "dark orange":
        button2_4.configure(fg_color="white")

def button2_5_cmd():
    if button2_5._fg_color == "white" or button2_5._fg_color == "dark green":
        button2_5.configure(fg_color=color_now)
    elif button2_5._fg_color == "dark red" or button2_5._fg_color == "dark orange":
        button2_5.configure(fg_color="white")

def button2_6_cmd():
    if button2_6._fg_color == "white" or button2_6._fg_color == "dark green":
        button2_6.configure(fg_color=color_now)
    elif button2_6._fg_color == "dark red" or button2_6._fg_color == "dark orange":
        button2_6.configure(fg_color="white")

def button2_7_cmd():
    if button2_7._fg_color == "white" or button2_7._fg_color == "dark green":
        button2_7.configure(fg_color=color_now)
    elif button2_7._fg_color == "dark red" or button2_7._fg_color == "dark orange":
        button2_7.configure(fg_color="white")

def button2_8_cmd():
    if button2_8._fg_color == "white" or button2_8._fg_color == "dark green":
        button2_8.configure(fg_color=color_now)
    elif button2_8._fg_color == "dark red" or button2_8._fg_color == "dark orange":
        button2_8.configure(fg_color="white")

def button2_9_cmd():
    if button2_9._fg_color == "white" or button2_9._fg_color == "dark green":
        button2_9.configure(fg_color=color_now)
    elif button2_9._fg_color == "dark red" or button2_9._fg_color == "dark orange":
        button2_9.configure(fg_color="white")

def button2_10_cmd():
    if button2_10._fg_color == "white" or button2_10._fg_color == "dark green":
        button2_10.configure(fg_color=color_now)
    elif button2_10._fg_color == "dark red" or button2_10._fg_color == "dark orange":
        button2_10.configure(fg_color="white")

def button3_1_cmd():
    if button3_1._fg_color == "white" or button3_1._fg_color == "dark green":
        button3_1.configure(fg_color=color_now)
    elif button3_1._fg_color == "dark red" or button3_1._fg_color == "dark orange":
        button3_1.configure(fg_color="white")

def button3_2_cmd():
    if button3_2._fg_color == "white" or button3_2._fg_color == "dark green":
        button3_2.configure(fg_color=color_now)
    elif button3_2._fg_color == "dark red" or button3_2._fg_color == "dark orange":
        button3_2.configure(fg_color="white")

def button3_3_cmd():
    if button3_3._fg_color == "white" or button3_3._fg_color == "dark green":
        button3_3.configure(fg_color=color_now)
    elif button3_3._fg_color == "dark red" or button3_3._fg_color == "dark orange":
        button3_3.configure(fg_color="white")

def button3_4_cmd():
    if button3_4._fg_color == "white" or button3_4._fg_color == "dark green":
        button3_4.configure(fg_color=color_now)
    elif button3_4._fg_color == "dark red" or button3_4._fg_color == "dark orange":
        button3_4.configure(fg_color="white")

def button3_5_cmd():
    if button3_5._fg_color == "white" or button3_5._fg_color == "dark green":
        button3_5.configure(fg_color=color_now)
    elif button3_5._fg_color == "dark red" or button3_5._fg_color == "dark orange":
        button3_5.configure(fg_color="white")

def button3_6_cmd():
    if button3_6._fg_color == "white" or button3_6._fg_color == "dark green":
        button3_6.configure(fg_color=color_now)
    elif button3_6._fg_color == "dark red" or button3_6._fg_color == "dark orange":
        button3_6.configure(fg_color="white")

def button3_7_cmd():
    if button3_7._fg_color == "white" or button3_7._fg_color == "dark green":
        button3_7.configure(fg_color=color_now)
    elif button3_7._fg_color == "dark red" or button3_7._fg_color == "dark orange":
        button3_7.configure(fg_color="white")

def button3_8_cmd():
    if button3_8._fg_color == "white" or button3_8._fg_color == "dark green":
        button3_8.configure(fg_color=color_now)
    elif button3_8._fg_color == "dark red" or button3_8._fg_color == "dark orange":
        button3_8.configure(fg_color="white")

def button3_9_cmd():
    if button3_9._fg_color == "white" or button3_9._fg_color == "dark green":
        button3_9.configure(fg_color=color_now)
    elif button3_9._fg_color == "dark red" or button3_9._fg_color == "dark orange":
        button3_9.configure(fg_color="white")

def button3_10_cmd():
    if button3_10._fg_color == "white" or button3_10._fg_color == "dark green":
        button3_10.configure(fg_color=color_now)
    elif button3_10._fg_color == "dark red" or button3_10._fg_color == "dark orange":
        button3_10.configure(fg_color="white")

def button4_1_cmd():
    if button4_1._fg_color == "white" or button4_1._fg_color == "dark green":
        button4_1.configure(fg_color=color_now)
    elif button4_1._fg_color == "dark red" or button4_1._fg_color == "dark orange":
        button4_1.configure(fg_color="white")

def button4_2_cmd():
    if button4_2._fg_color == "white" or button4_2._fg_color == "dark green":
        button4_2.configure(fg_color=color_now)
    elif button4_2._fg_color == "dark red" or button4_2._fg_color == "dark orange":
        button4_2.configure(fg_color="white")

def button4_3_cmd():
    if button4_3._fg_color == "white" or button4_3._fg_color == "dark green":
        button4_3.configure(fg_color=color_now)
    elif button4_3._fg_color == "dark red" or button4_3._fg_color == "dark orange":
        button4_3.configure(fg_color="white")

def button4_4_cmd():
    if button4_4._fg_color == "white" or button4_4._fg_color == "dark green":
        button4_4.configure(fg_color=color_now)
    elif button4_4._fg_color == "dark red" or button4_4._fg_color == "dark orange":
        button4_4.configure(fg_color="white")

def button4_5_cmd():
    if button4_5._fg_color == "white" or button4_5._fg_color == "dark green":
        button4_5.configure(fg_color=color_now)
    elif button4_5._fg_color == "dark red" or button4_5._fg_color == "dark orange":
        button4_5.configure(fg_color="white")

def button4_6_cmd():
    if button4_6._fg_color == "white" or button4_6._fg_color == "dark green":
        button4_6.configure(fg_color=color_now)
    elif button4_6._fg_color == "dark red" or button4_6._fg_color == "dark orange":
        button4_6.configure(fg_color="white")

def button4_7_cmd():
    if button4_7._fg_color == "white" or button4_7._fg_color == "dark green":
        button4_7.configure(fg_color=color_now)
    elif button4_7._fg_color == "dark red" or button4_7._fg_color == "dark orange":
        button4_7.configure(fg_color="white")

def button4_8_cmd():
    if button4_8._fg_color == "white" or button4_8._fg_color == "dark green":
        button4_8.configure(fg_color=color_now)
    elif button4_8._fg_color == "dark red" or button4_8._fg_color == "dark orange":
        button4_8.configure(fg_color="white")

def button4_9_cmd():
    if button4_9._fg_color == "white" or button4_9._fg_color == "dark green":
        button4_9.configure(fg_color=color_now)
    elif button4_9._fg_color == "dark red" or button4_9._fg_color == "dark orange":
        button4_9.configure(fg_color="white")

def button4_10_cmd():
    if button4_10._fg_color == "white" or button4_10._fg_color == "dark green":
        button4_10.configure(fg_color=color_now)
    elif button4_10._fg_color == "dark red" or button4_10._fg_color == "dark orange":
        button4_10.configure(fg_color="white")

def button5_1_cmd():
    if button5_1._fg_color == "white" or button5_1._fg_color == "dark green":
        button5_1.configure(fg_color=color_now)
    elif button5_1._fg_color == "dark red" or button5_1._fg_color == "dark orange":
        button5_1.configure(fg_color="white")

def button5_2_cmd():
    if button5_2._fg_color == "white" or button5_2._fg_color == "dark green":
        button5_2.configure(fg_color=color_now)
    elif button5_2._fg_color == "dark red" or button5_2._fg_color == "dark orange":
        button5_2.configure(fg_color="white")

def button5_3_cmd():
    if button5_3._fg_color == "white" or button5_3._fg_color == "dark green":
        button5_3.configure(fg_color=color_now)
    elif button5_3._fg_color == "dark red" or button5_3._fg_color == "dark orange":
        button5_3.configure(fg_color="white")

def button5_4_cmd():
    if button5_4._fg_color == "white" or button5_4._fg_color == "dark green":
        button5_4.configure(fg_color=color_now)
    elif button5_4._fg_color == "dark red" or button5_4._fg_color == "dark orange":
        button5_4.configure(fg_color="white")

def button5_5_cmd():
    if button5_5._fg_color == "white" or button5_5._fg_color == "dark green":
        button5_5.configure(fg_color=color_now)
    elif button5_5._fg_color == "dark red" or button5_5._fg_color == "dark orange":
        button5_5.configure(fg_color="white")

def button5_6_cmd():
    if button5_6._fg_color == "white" or button5_6._fg_color == "dark green":
        button5_6.configure(fg_color=color_now)
    elif button5_6._fg_color == "dark red" or button5_6._fg_color == "dark orange":
        button5_6

        
def button5_7_cmd():
    if button5_7._fg_color == "white" or button5_7._fg_color == "dark green":
        button5_7.configure(fg_color=color_now)
    elif button5_7._fg_color == "dark red" or button5_7._fg_color == "dark orange":
        button5_7.configure(fg_color="white")

def button5_8_cmd():
    if button5_8._fg_color == "white" or button5_8._fg_color == "dark green":
        button5_8.configure(fg_color=color_now)
    elif button5_8._fg_color == "dark red" or button5_8._fg_color == "dark orange":
        button5_8.configure(fg_color="white")

def button5_9_cmd():
    if button5_9._fg_color == "white" or button5_9._fg_color == "dark green":
        button5_9.configure(fg_color=color_now)
    elif button5_9._fg_color == "dark red" or button5_9._fg_color == "dark orange":
        button5_9.configure(fg_color="white")

def button5_10_cmd():
    if button5_10._fg_color == "white" or button5_10._fg_color == "dark green":
        button5_10.configure(fg_color=color_now)
    elif button5_10._fg_color == "dark red" or button5_10._fg_color == "dark orange":
        button5_10.configure(fg_color="white")

def button6_1_cmd():
    if button6_1._fg_color == "white" or button6_1._fg_color == "dark green":
        button6_1.configure(fg_color=color_now)
    elif button6_1._fg_color == "dark red" or button6_1._fg_color == "dark orange":
        button6_1.configure(fg_color="white")

def button6_2_cmd():
    if button6_2._fg_color == "white" or button6_2._fg_color == "dark green":
        button6_2.configure(fg_color=color_now)
    elif button6_2._fg_color == "dark red" or button6_2._fg_color == "dark orange":
        button6_2.configure(fg_color="white")

def button6_3_cmd():
    if button6_3._fg_color == "white" or button6_3._fg_color == "dark green":
        button6_3.configure(fg_color=color_now)
    elif button6_3._fg_color == "dark red" or button6_3._fg_color == "dark orange":
        button6_3.configure(fg_color="white")

def button6_4_cmd():
    if button6_4._fg_color == "white" or button6_4._fg_color == "dark green":
        button6_4.configure(fg_color=color_now)
    elif button6_4._fg_color == "dark red" or button6_4._fg_color == "dark orange":
        button6_4.configure(fg_color="white")

def button6_5_cmd():
    if button6_5._fg_color == "white" or button6_5._fg_color == "dark green":
        button6_5.configure(fg_color=color_now)
    elif button6_5._fg_color == "dark red" or button6_5._fg_color == "dark orange":
        button6_5.configure(fg_color="white")

def button6_6_cmd():
    if button6_6._fg_color == "white" or button6_6._fg_color == "dark green":
        button6_6.configure(fg_color=color_now)
    elif button6_6._fg_color == "dark red" or button6_6._fg_color == "dark orange":
        button6_6.configure(fg_color="white")

def button6_7_cmd():
    if button6_7._fg_color == "white" or button6_7._fg_color == "dark green":
        button6_7.configure(fg_color=color_now)
    elif button6_7._fg_color == "dark red" or button6_7._fg_color == "dark orange":
        button6_7.configure(fg_color="white")

def button6_8_cmd():
    if button6_8._fg_color == "white" or button6_8._fg_color == "dark green":
        button6_8.configure(fg_color=color_now)
    elif button6_8._fg_color == "dark red" or button6_8._fg_color == "dark orange":
        button6_8.configure(fg_color="white")

def button6_9_cmd():
    if button6_9._fg_color == "white" or button6_9._fg_color == "dark green":
        button6_9.configure(fg_color=color_now)
    elif button6_9._fg_color == "dark red" or button6_9._fg_color == "dark orange":
        button6_9.configure(fg_color="white")

def button6_10_cmd():
    if button6_10._fg_color == "white" or button6_10._fg_color == "dark green":
        button6_10.configure(fg_color=color_now)
    elif button6_10._fg_color == "dark red" or button6_10._fg_color == "dark orange":
        button6_10.configure(fg_color="white")

def button7_1_cmd():
    if button7_1._fg_color == "white" or button7_1._fg_color == "dark green":
        button7_1.configure(fg_color=color_now)
    elif button7_1._fg_color == "dark red" or button7_1._fg_color == "dark orange":
        button7_1.configure(fg_color="white")

def button7_2_cmd():
    if button7_2._fg_color == "white" or button7_2._fg_color == "dark green":
        button7_2.configure(fg_color=color_now)
    elif button7_2._fg_color == "dark red" or button7_2._fg_color == "dark orange":
        button7_2.configure(fg_color="white")

def button7_3_cmd():
    if button7_3._fg_color == "white" or button7_3._fg_color == "dark green":
        button7_3.configure(fg_color=color_now)
    elif button7_3._fg_color == "dark red" or button7_3._fg_color == "dark orange":
        button7_3.configure(fg_color="white")

def button7_4_cmd():
    if button7_4._fg_color == "white" or button7_4._fg_color == "dark green":
        button7_4.configure(fg_color=color_now)
    elif button7_4._fg_color == "dark red" or button7_4._fg_color == "dark orange":
        button7_4.configure(fg_color="white")

def button7_5_cmd():
    if button7_5._fg_color == "white" or button7_5._fg_color == "dark green":
        button7_5.configure(fg_color=color_now)
    elif button7_5._fg_color == "dark red" or button7_5._fg_color == "dark orange":
        button7_5.configure(fg_color="white")

def button7_6_cmd():
    if button7_6._fg_color == "white" or button7_6._fg_color == "dark green":
        button7_6.configure(fg_color=color_now)
    elif button7_6._fg_color == "dark red" or button7_6._fg_color == "dark orange":
        button7_6.configure(fg_color="white")

def button7_7_cmd():
    if button7_7._fg_color == "white" or button7_7._fg_color == "dark green":
        button7_7.configure(fg_color=color_now)
    elif button7_7._fg_color == "dark red" or button7_7._fg_color == "dark orange":
        button7_7.configure(fg_color="white")

def button7_8_cmd():
    if button7_8._fg_color == "white" or button7_8._fg_color == "dark green":
        button7_8.configure(fg_color=color_now)
    elif button7_8._fg_color == "dark red" or button7_8._fg_color == "dark orange":
        button7_8.configure(fg_color="white")

def button7_9_cmd():
    if button7_9._fg_color == "white" or button7_9._fg_color == "dark green":
        button7_9.configure(fg_color=color_now)
    elif button7_9._fg_color == "dark red" or button7_9._fg_color == "dark orange":
        button7_9.configure(fg_color="white")

def button7_10_cmd():
    if button7_10._fg_color == "white" or button7_10._fg_color == "dark green":
        button7_10.configure(fg_color=color_now)
    elif button7_10._fg_color == "dark red" or button7_10._fg_color == "dark orange":
        button7_10.configure(fg_color="white")

def button8_1_cmd():
    if button8_1._fg_color == "white" or button8_1._fg_color == "dark green":
        button8_1.configure(fg_color=color_now)
    elif button8_1._fg_color == "dark red" or button8_1._fg_color == "dark orange":
        button8_1.configure(fg_color="white")

def button8_2_cmd():
    if button8_2._fg_color == "white" or button8_2._fg_color == "dark green":
        button8_2.configure(fg_color=color_now)
    elif button8_2._fg_color == "dark red" or button8_2._fg_color == "dark orange":
        button8_2.configure(fg_color="white")

def button8_3_cmd():
    if button8_3._fg_color == "white" or button8_3._fg_color == "dark green":
        button8_3.configure(fg_color=color_now)
    elif button8_3._fg_color == "dark red" or button8_3._fg_color == "dark orange":
        button8_3.configure(fg_color="white")

def button8_4_cmd():
    if button8_4._fg_color == "white" or button8_4._fg_color == "dark green":
        button8_4.configure(fg_color=color_now)
    elif button8_4._fg_color == "dark red" or button8_4._fg_color == "dark orange":
        button8_4.configure(fg_color="white")

def button8_5_cmd():
    if button8_5._fg_color == "white" or button8_5._fg_color == "dark green":
        button8_5.configure(fg_color=color_now)
    elif button8_5._fg_color == "dark red" or button8_5._fg_color == "dark orange":
        button8_5.configure(fg_color="white")

def button8_6_cmd():
    if button8_6._fg_color == "white" or button8_6._fg_color == "dark green":
        button8_6.configure(fg_color=color_now)
    elif button8_6._fg_color == "dark red" or button8_6._fg_color == "dark orange":
        button8_6.configure(fg_color="white")

def button8_7_cmd():
    if button8_7._fg_color == "white" or button8_7._fg_color == "dark green":
        button8_7.configure(fg_color=color_now)
    elif button8_7._fg_color == "dark red" or button8_7._fg_color == "dark orange":
        button8_7.configure(fg_color="white")

def button8_8_cmd():
    if button8_8._fg_color == "white" or button8_8._fg_color == "dark green":
        button8_8.configure(fg_color=color_now)
    elif button8_8._fg_color == "dark red" or button8_8._fg_color == "dark orange":
        button8_8.configure(fg_color="white")

def button8_9_cmd():
    if button8_9._fg_color == "white" or button8_9._fg_color == "dark green":
        button8_9.configure(fg_color=color_now)
    elif button8_9._fg_color == "dark red" or button8_9._fg_color == "dark orange":
        button8_9.configure(fg_color="white")

def button8_10_cmd():
    if button8_10._fg_color == "white" or button8_10._fg_color == "dark green":
        button8_10.configure(fg_color=color_now)
    elif button8_10._fg_color == "dark red" or button8_10._fg_color == "dark orange":
        button8_10.configure(fg_color="white")

def button9_1_cmd():
    if button9_1._fg_color == "white" or button9_1._fg_color == "dark green":
        button9_1.configure(fg_color=color_now)
    elif button9_1._fg_color == "dark red" or button9_1._fg_color == "dark orange":
        button9_1.configure(fg_color="white")

def button9_2_cmd():
    if button9_2._fg_color == "white" or button9_2._fg_color == "dark green":
        button9_2.configure(fg_color=color_now)
    elif button9_2._fg_color == "dark red" or button9_2._fg_color == "dark orange":
        button9_2.configure(fg_color="white")

def button9_3_cmd():
    if button9_3._fg_color == "white" or button9_3._fg_color == "dark green":
        button9_3.configure(fg_color=color_now)
    elif button9_3._fg_color == "dark red" or button9_3._fg_color == "dark orange":
        button9_3.configure(fg_color="white")

def button9_4_cmd():
    if button9_4._fg_color == "white" or button9_4._fg_color == "dark green":
        button9_4.configure(fg_color=color_now)
    elif button9_4._fg_color == "dark red" or button9_4._fg_color == "dark orange":
        button9_4.configure(fg_color="white")

def button9_5_cmd():
    if button9_5._fg_color == "white" or button9_5._fg_color == "dark green":
        button9_5.configure(fg_color=color_now)
    elif button9_5._fg_color == "dark red" or button9_5._fg_color == "dark orange":
        button9_5.configure(fg_color="white")

def button9_6_cmd():
    if button9_6._fg_color == "white" or button9_6._fg_color == "dark green":
        button9_6.configure(fg_color=color_now)
    elif button9_6._fg_color == "dark red" or button9_6._fg_color == "dark orange":
        button9_6.configure(fg_color="white")

def button9_7_cmd():
    if button9_7._fg_color == "white" or button9_7._fg_color == "dark green":
        button9_7.configure(fg_color=color_now)
    elif button9_7._fg_color == "dark red" or button9_7._fg_color == "dark orange":
        button9_7.configure(fg_color="white")

def button9_8_cmd():
    if button9_8._fg_color == "white" or button9_8._fg_color == "dark green":
        button9_8.configure(fg_color=color_now)
    elif button9_8._fg_color == "dark red" or button9_8._fg_color == "dark orange":
        button9_8.configure(fg_color="white")

def button9_9_cmd():
    if button9_9._fg_color == "white" or button9_9._fg_color == "dark green":
        button9_9.configure(fg_color=color_now)
    elif button9_9._fg_color == "dark red" or button9_9._fg_color == "dark orange":
        button9_9.configure(fg_color="white")

def button9_10_cmd():
    if button9_10._fg_color == "white" or button9_10._fg_color == "dark green":
        button9_10.configure(fg_color=color_now)
    elif button9_10._fg_color == "dark red" or button9_10._fg_color == "dark orange":
        button9_10.configure(fg_color="white")

def button10_1_cmd():
    if button10_1._fg_color == "white" or button10_1._fg_color == "dark green":
        button10_1.configure(fg_color=color_now)
    elif button10_1._fg_color == "dark red" or button10_1._fg_color == "dark orange":
        button10_1.configure(fg_color="white")

def button10_2_cmd():
    if button10_2._fg_color == "white" or button10_2._fg_color == "dark green":
        button10_2.configure(fg_color=color_now)
    elif button10_2._fg_color == "dark red" or button10_2._fg_color == "dark orange":
        button10_2.configure(fg_color="white")

def button10_3_cmd():
    if button10_3._fg_color == "white" or button10_3._fg_color == "dark green":
        button10_3.configure(fg_color=color_now)
    elif button10_3._fg_color == "dark red" or button10_3._fg_color == "dark orange":
        button10_3.configure(fg_color="white")

def button10_4_cmd():
    if button10_4._fg_color == "white" or button10_4._fg_color == "dark green":
        button10_4.configure(fg_color=color_now)
    elif button10_4._fg_color == "dark red" or button10_4._fg_color == "dark orange":
        button10_4.configure(fg_color="white")

def button10_5_cmd():
    if button10_5._fg_color == "white" or button10_5._fg_color == "dark green":
        button10_5.configure(fg_color=color_now)
    elif button10_5._fg_color == "dark red" or button10_5._fg_color == "dark orange":
        button10_5.configure(fg_color="white")

def button10_6_cmd():
    if button10_6._fg_color == "white" or button10_6._fg_color == "dark green":
        button10_6.configure(fg_color=color_now)
    elif button10_6._fg_color == "dark red" or button10_6._fg_color == "dark orange":
        button10_6.configure(fg_color="white")

def button10_7_cmd():
    if button10_7._fg_color == "white" or button10_7._fg_color == "dark green":
        button10_7.configure(fg_color=color_now)
    elif button10_7._fg_color == "dark red" or button10_7._fg_color == "dark orange":
        button10_7.configure(fg_color="white")

def button10_8_cmd():
    if button10_8._fg_color == "white" or button10_8._fg_color == "dark green":
        button10_8.configure(fg_color=color_now)
    elif button10_8._fg_color == "dark red" or button10_8._fg_color == "dark orange":
        button10_8.configure(fg_color="white")

def button10_9_cmd():
    if button10_9._fg_color == "white" or button10_9._fg_color == "dark green":
        button10_9.configure(fg_color=color_now)
    elif button10_9._fg_color == "dark red" or button10_9._fg_color == "dark orange":
        button10_9.configure(fg_color="white")

def button10_10_cmd():
    if button10_10._fg_color == "white" or button10_10._fg_color == "dark green":
        button10_10.configure(fg_color=color_now)
    elif button10_10._fg_color == "dark red" or button10_10._fg_color == "dark orange":
        button10_10.configure(fg_color="white")




    
def clear_widgets():
    button1_1.configure(fg_color = "white")
    button1_2.configure(fg_color = "white")
    button1_3.configure(fg_color = "white")
    button1_4.configure(fg_color = "white")
    button1_5.configure(fg_color = "white")
    button1_6.configure(fg_color = "white")
    button1_7.configure(fg_color = "white")
    button1_8.configure(fg_color = "white")
    button1_9.configure(fg_color = "white")
    button1_10.configure(fg_color = "white")



    button2_1.configure(fg_color = "white")
    button2_2.configure(fg_color = "white")
    button2_3.configure(fg_color = "white")
    button2_4.configure(fg_color = "white")
    button2_5.configure(fg_color = "white")
    button2_6.configure(fg_color = "white")
    button2_7.configure(fg_color = "white")
    button2_8.configure(fg_color = "white")
    button2_9.configure(fg_color = "white")
    button2_10.configure(fg_color = "white")




    button3_1.configure(fg_color = "white")
    button3_2.configure(fg_color = "white")
    button3_3.configure(fg_color = "white")
    button3_4.configure(fg_color = "white")
    button3_5.configure(fg_color = "white")
    button3_6.configure(fg_color = "white")
    button3_7.configure(fg_color = "white")
    button3_8.configure(fg_color = "white")
    button3_9.configure(fg_color = "white")
    button3_10.configure(fg_color = "white")



    button3_1.configure(fg_color = "white")
    button3_2.configure(fg_color = "white")
    button3_3.configure(fg_color = "white")
    button3_4.configure(fg_color = "white")
    button3_5.configure(fg_color = "white")
    button3_6.configure(fg_color = "white")
    button3_7.configure(fg_color = "white")
    button3_8.configure(fg_color = "white")
    button3_9.configure(fg_color = "white")
    button3_10.configure(fg_color = "white")



    button4_1.configure(fg_color = "white")
    button4_2.configure(fg_color = "white")
    button4_3.configure(fg_color = "white")
    button4_4.configure(fg_color = "white")
    button4_5.configure(fg_color = "white")
    button4_6.configure(fg_color = "white")
    button4_7.configure(fg_color = "white")
    button4_8.configure(fg_color = "white")
    button4_9.configure(fg_color = "white")
    button4_10.configure(fg_color = "white")



    button5_1.configure(fg_color = "white")
    button5_2.configure(fg_color = "white")
    button5_3.configure(fg_color = "white")
    button5_4.configure(fg_color = "white")
    button5_5.configure(fg_color = "white")
    button5_6.configure(fg_color = "white")
    button5_7.configure(fg_color = "white")
    button5_8.configure(fg_color = "white")
    button5_9.configure(fg_color = "white")
    button5_10.configure(fg_color = "white")



    button6_1.configure(fg_color = "white")
    button6_2.configure(fg_color = "white")
    button6_3.configure(fg_color = "white")
    button6_4.configure(fg_color = "white")
    button6_5.configure(fg_color = "white")
    button6_6.configure(fg_color = "white")
    button6_7.configure(fg_color = "white")
    button6_8.configure(fg_color = "white")
    button6_9.configure(fg_color = "white")
    button6_10.configure(fg_color = "white")




    button7_1.configure(fg_color = "white")
    button7_2.configure(fg_color = "white")
    button7_3.configure(fg_color = "white")
    button7_4.configure(fg_color = "white")
    button7_5.configure(fg_color = "white")
    button7_6.configure(fg_color = "white")
    button7_7.configure(fg_color = "white")
    button7_8.configure(fg_color = "white")
    button7_9.configure(fg_color = "white")
    button7_10.configure(fg_color = "white")



    button8_1.configure(fg_color = "white")
    button8_2.configure(fg_color = "white")
    button8_3.configure(fg_color = "white")
    button8_4.configure(fg_color = "white")
    button8_5.configure(fg_color = "white")
    button8_6.configure(fg_color = "white")
    button8_7.configure(fg_color = "white")
    button8_8.configure(fg_color = "white")
    button8_9.configure(fg_color = "white")
    button8_10.configure(fg_color = "white")



    button9_1.configure(fg_color = "white")
    button9_2.configure(fg_color = "white")
    button9_3.configure(fg_color = "white")
    button9_4.configure(fg_color = "white")
    button9_5.configure(fg_color = "white")
    button9_6.configure(fg_color = "white")
    button9_7.configure(fg_color = "white")
    button9_8.configure(fg_color = "white")
    button9_9.configure(fg_color = "white")
    button9_10.configure(fg_color = "white")



    button10_1.configure(fg_color = "white")
    button10_2.configure(fg_color = "white")
    button10_3.configure(fg_color = "white")
    button10_4.configure(fg_color = "white")
    button10_5.configure(fg_color = "white")
    button10_6.configure(fg_color = "white")
    button10_7.configure(fg_color = "white")
    button10_8.configure(fg_color = "white")
    button10_9.configure(fg_color = "white")
    button10_10.configure(fg_color = "white")


    





def on_notes():
    global color_now
    if notes_button._fg_color == "dark orange":
        notes_button.configure(fg_color = "white")
        color_now = "dark red"
    else:
        notes_button.configure(fg_color = "dark orange")
        color_now = "dark orange"

    
    
def settings():
    if button1_1.winfo_ismapped():
        button1_1.place_forget()
        button1_2.place_forget()
        button1_3.place_forget()
        button1_4.place_forget()
        button1_5.place_forget()
        button1_6.place_forget()
        button1_7.place_forget()
        button1_8.place_forget()
        button1_9.place_forget()
        button1_10.place_forget()

        button2_1.place_forget()
        button2_2.place_forget()
        button2_3.place_forget()
        button2_4.place_forget()
        button2_5.place_forget()
        button2_6.place_forget()
        button2_7.place_forget()
        button2_8.place_forget()
        button2_9.place_forget()
        button2_10.place_forget()

        button3_1.place_forget()
        button3_2.place_forget()
        button3_3.place_forget()
        button3_4.place_forget()
        button3_5.place_forget()
        button3_6.place_forget()
        button3_7.place_forget()
        button3_8.place_forget()
        button3_9.place_forget()
        button3_10.place_forget()

        button4_1.place_forget()
        button4_2.place_forget()
        button4_3.place_forget()
        button4_4.place_forget()
        button4_5.place_forget()
        button4_6.place_forget()
        button4_7.place_forget()
        button4_8.place_forget()
        button4_9.place_forget()
        button4_10.place_forget()

        button5_1.place_forget()
        button5_2.place_forget()
        button5_3.place_forget()
        button5_4.place_forget()
        button5_5.place_forget()
        button5_6.place_forget()
        button5_7.place_forget()
        button5_8.place_forget()
        button5_9.place_forget()
        button5_10.place_forget()

        button6_1.place_forget()
        button6_2.place_forget()
        button6_3.place_forget()
        button6_4.place_forget()
        button6_5.place_forget()
        button6_6.place_forget()
        button6_7.place_forget()
        button6_8.place_forget()
        button6_9.place_forget()
        button6_10.place_forget()

        button7_1.place_forget()
        button7_2.place_forget()
        button7_3.place_forget()
        button7_4.place_forget()
        button7_5.place_forget()
        button7_6.place_forget()
        button7_7.place_forget()
        button7_8.place_forget()
        button7_9.place_forget()
        button7_10.place_forget()

        button8_1.place_forget()
        button8_2.place_forget()
        button8_3.place_forget()
        button8_4.place_forget()
        button8_5.place_forget()
        button8_6.place_forget()
        button8_7.place_forget()
        button8_8.place_forget()
        button8_9.place_forget()
        button8_10.place_forget()

        button9_1.place_forget()
        button9_2.place_forget()
        button9_3.place_forget()
        button9_4.place_forget()
        button9_5.place_forget()
        button9_6.place_forget()
        button9_7.place_forget()
        button9_8.place_forget()
        button9_9.place_forget()
        button9_10.place_forget()

        button10_1.place_forget()
        button10_2.place_forget()
        button10_3.place_forget()
        button10_4.place_forget()
        button10_5.place_forget()
        button10_6.place_forget()
        button10_7.place_forget()
        button10_8.place_forget()
        button10_9.place_forget()
        button10_10.place_forget()


        letters.place_forget()

        numbers.place_forget()
        numbers2.place_forget()
        numbers3.place_forget()
        numbers4.place_forget()


        clear_button.place_forget()

        notes_button.place_forget()

        button_submit.place_forget()


        
        bg_color_text.place(x = 270, y = 50)



    else:
        button1_1.place(x = 100, y = 100)
        button1_2.place(x = 149, y = 100)
        button1_3.place(x = 198, y = 100)
        button1_4.place(x = 247, y = 100)
        button1_5.place(x = 296, y = 100)
        button1_6.place(x = 345, y = 100)
        button1_7.place(x = 394, y = 100)
        button1_8.place(x = 444, y = 100)
        button1_9.place(x = 493, y = 100)
        button1_10.place(x = 542, y = 100)

        button2_1.place(x = 100, y = 149)
        button2_2.place(x = 149, y = 149)
        button2_3.place(x = 198, y = 149)
        button2_4.place(x = 247, y = 149)
        button2_5.place(x = 296, y = 149)
        button2_6.place(x = 345, y = 149)
        button2_7.place(x = 394, y = 149)
        button2_8.place(x = 444, y = 149)
        button2_9.place(x = 493, y = 149)
        button2_10.place(x = 542, y = 149)

        button3_1.place(x = 100, y = 198)
        button3_2.place(x = 149, y = 198)
        button3_3.place(x = 198, y = 198)
        button3_4.place(x = 247, y = 198)
        button3_5.place(x = 296, y = 198)
        button3_6.place(x = 345, y = 198)
        button3_7.place(x = 394, y = 198)
        button3_8.place(x = 444, y = 198)
        button3_9.place(x = 493, y = 198)
        button3_10.place(x = 542, y = 198)

        button4_1.place(x = 100, y = 247)
        button4_2.place(x = 149, y = 247)
        button4_3.place(x = 198, y = 247)
        button4_4.place(x = 247, y = 247)
        button4_5.place(x = 296, y = 247)
        button4_6.place(x = 345, y = 247)
        button4_7.place(x = 394, y = 247)
        button4_8.place(x = 444, y = 247)
        button4_9.place(x = 493, y = 247)
        button4_10.place(x = 542, y = 247)

        button5_1.place(x = 100, y = 296)
        button5_2.place(x = 149, y = 296)
        button5_3.place(x = 198, y = 296)
        button5_4.place(x = 247, y = 296)
        button5_5.place(x = 296, y = 296)
        button5_6.place(x = 345, y = 296)
        button5_7.place(x = 394, y = 296)
        button5_8.place(x = 444, y = 296)
        button5_9.place(x = 493, y = 296)
        button5_10.place(x = 542, y = 296)

        button6_1.place(x = 100, y = 345)
        button6_2.place(x = 149, y = 345)
        button6_3.place(x = 198, y = 345)
        button6_4.place(x = 247, y = 345)
        button6_5.place(x = 296, y = 345)
        button6_6.place(x = 345, y = 345)
        button6_7.place(x = 394, y = 345)
        button6_8.place(x = 444, y = 345)
        button6_9.place(x = 493, y = 345)
        button6_10.place(x = 542, y = 345)

        button7_1.place(x = 100, y = 394)
        button7_2.place(x = 149, y = 394)
        button7_3.place(x = 198, y = 394)
        button7_4.place(x = 247, y = 394)
        button7_5.place(x = 296, y = 394)
        button7_6.place(x = 345, y = 394)
        button7_7.place(x = 394, y = 394)
        button7_8.place(x = 444, y = 394)
        button7_9.place(x = 493, y = 394)
        button7_10.place(x = 542, y = 394)

        button8_1.place(x = 100, y = 444)
        button8_2.place(x = 149, y = 444)
        button8_3.place(x = 198, y = 444)
        button8_4.place(x = 247, y = 444)
        button8_5.place(x = 296, y = 444)
        button8_6.place(x = 345, y = 444)
        button8_7.place(x = 394, y = 444)
        button8_8.place(x = 444, y = 444)
        button8_9.place(x = 493, y = 444)
        button8_10.place(x = 542, y = 444)

        button9_1.place(x = 100, y = 493)
        button9_2.place(x = 149, y = 493)
        button9_3.place(x = 198, y = 493)
        button9_4.place(x = 247, y = 493)
        button9_5.place(x = 296, y = 493)
        button9_6.place(x = 345, y = 493)
        button9_7.place(x = 394, y = 493)
        button9_8.place(x = 444, y = 493)
        button9_9.place(x = 493, y = 493)
        button9_10.place(x = 542, y = 493)

        button10_1.place(x = 100, y = 542)
        button10_2.place(x = 149, y = 542)
        button10_3.place(x = 198, y = 542)
        button10_4.place(x = 247, y = 542)
        button10_5.place(x = 296, y = 542)
        button10_6.place(x = 345, y = 542)
        button10_7.place(x = 394, y = 542)
        button10_8.place(x = 444, y = 542)
        button10_9.place(x = 493, y = 542)
        button10_10.place(x = 542, y = 542)

        letters.place(x = 115, y = 70)

        numbers.place(x = 70, y = 100)
        numbers2.place(x = 70, y = 255)
        numbers3.place(x = 70, y = 405)
        numbers4.place(x = 65, y = 555)


        clear_button.place(x = 650, y = 0)

        notes_button.place(x = 650, y = 50)

        button_submit.place(x = 250, y = 600)

        settings_button.place(x = 0, y = 0)





        
        bg_color_text.place_forget()

    # for string in matrix_strings:
    #     for cell in string:
    #         for count in range(4):
    #             if string[count] == 1:
    #                 matrix_cells[0][count] + 1








button1_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_1_cmd)
button1_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_2_cmd)
button1_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_3_cmd)
button1_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_4_cmd)
button1_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_5_cmd)
button1_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_6_cmd)
button1_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_7_cmd)
button1_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_8_cmd)
button1_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_9_cmd)
button1_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button1_10_cmd)

button2_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_1_cmd)
button2_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_2_cmd)
button2_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_3_cmd)
button2_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_4_cmd)
button2_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_5_cmd)
button2_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_6_cmd)
button2_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_7_cmd)
button2_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_8_cmd)
button2_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_9_cmd)
button2_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button2_10_cmd)

button3_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_1_cmd)
button3_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_2_cmd)
button3_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_3_cmd)
button3_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_4_cmd)
button3_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_5_cmd)
button3_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_6_cmd)
button3_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_7_cmd)
button3_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_8_cmd)
button3_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_9_cmd)
button3_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button3_10_cmd)

button4_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_1_cmd)
button4_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_2_cmd)
button4_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_3_cmd)
button4_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_4_cmd)
button4_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_5_cmd)
button4_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_6_cmd)
button4_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_7_cmd)
button4_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_8_cmd)
button4_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_9_cmd)
button4_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button4_10_cmd)

button5_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_1_cmd)
button5_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_2_cmd)
button5_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_3_cmd)
button5_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_4_cmd)
button5_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_5_cmd)
button5_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_6_cmd)
button5_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_7_cmd)
button5_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_8_cmd)
button5_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_9_cmd)
button5_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button5_10_cmd)

button6_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_1_cmd)
button6_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_2_cmd)
button6_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_3_cmd)
button6_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_4_cmd)
button6_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_5_cmd)
button6_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_6_cmd)
button6_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_7_cmd)
button6_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_8_cmd)
button6_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_9_cmd)
button6_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button6_10_cmd)

button7_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_1_cmd)
button7_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_2_cmd)
button7_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_3_cmd)
button7_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_4_cmd)
button7_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_5_cmd)
button7_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_6_cmd)
button7_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_7_cmd)
button7_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_8_cmd)
button7_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_9_cmd)
button7_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button7_10_cmd)

button8_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_1_cmd)
button8_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_2_cmd)
button8_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_3_cmd)
button8_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_4_cmd)
button8_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_5_cmd)
button8_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_6_cmd)
button8_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_7_cmd)
button8_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_8_cmd)
button8_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_9_cmd)
button8_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button8_10_cmd)

button9_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_1_cmd)
button9_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_2_cmd)
button9_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_3_cmd)
button9_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_4_cmd)
button9_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_5_cmd)
button9_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_6_cmd)
button9_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_7_cmd)
button9_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_8_cmd)
button9_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_9_cmd)
button9_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button9_10_cmd)

button10_1 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_1_cmd)
button10_2 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_2_cmd)
button10_3 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_3_cmd)
button10_4 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_4_cmd)
button10_5 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_5_cmd)
button10_6 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_6_cmd)
button10_7 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_7_cmd)
button10_8 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_8_cmd)
button10_9 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_9_cmd)
button10_10 = customtkinter.CTkButton(screen, width= 50, height= 50, fg_color= "white", border_color= "black", border_width= 2, text= "", command= button10_10_cmd)

clear_image = customtkinter.CTkImage(light_image= Image.open(__file__ + "/../images/clear-icon.png"), size= (35, 35))
clear_button = customtkinter.CTkButton(screen, width= 50, height= 50, image= clear_image, fg_color= "white", border_color= "black", border_width= 2, text= "", command= clear_widgets)


notes_icon = customtkinter.CTkImage(light_image= Image.open(__file__ + "/../images/notes.png"), size= (35, 35))
notes_button = customtkinter.CTkButton(screen, width= 50, height= 50, image= notes_icon, fg_color= "white", border_color= "black", border_width= 2, text= "", command= on_notes)


settings_icon = customtkinter.CTkImage(light_image= Image.open(__file__ + "/../images/settings.png"), size= (35, 35))
settings_button = customtkinter.CTkButton(screen, width= 50, height= 50, image= settings_icon, fg_color= "white", border_color= "black", border_width= 2, text= "", command= settings)


bg_color_text = customtkinter.CTkLabel(screen, text = "Background Color:", width= 75, height= 20, text_color= "white", font= (25, 25))





def sumbit_cmd():


    global matrix_strings, matrix_columns, final_matrix




    matrix_strings = [
        [],
        [],
        [],
        [],
        [],
        [],  
        [],
        [],
        [],
        [],
    ]

    matrix_columns = [
        [],
        [],
        [],
        [],
        [],
        [],  
        [],
        [],
        [],
        [],
    ]

    if button1_1._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)

    if button1_2._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)



    if button1_3._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)


    if button1_4._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)

    if button1_5._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)


    if button1_6._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)  

    if button1_7._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)


    if button1_8._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)

    if button1_9._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)

    if button1_10._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)  












    if button2_1._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)

    if button2_2._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)



    if button2_3._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)




    if button2_4._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)

    if button2_5._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)


    if button2_6._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)  

    if button2_7._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)


    if button2_8._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)

    if button2_9._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)


    if button2_10._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)  

















    if button3_1._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)

    if button3_2._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)



    if button3_3._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)


    if button3_4._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)

    if button3_5._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)


    if button3_6._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)  

    if button3_7._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)


    if button3_8._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)

    if button3_9._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)


    if button3_10._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)  



    if button4_1._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)

    if button4_2._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)



    if button4_3._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)


    if button4_4._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)

    if button4_5._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)


    if button4_6._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)  

    if button4_7._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)


    if button4_8._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)

    if button4_9._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)


    if button4_10._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)  
    





    if button5_1._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)

    if button5_2._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)



    if button5_3._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)


    if button5_4._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)

    if button5_5._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)


    if button5_6._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)  

    if button5_7._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)


    if button5_8._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)

    if button5_9._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)


    if button5_10._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)  





    if button6_1._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)

    if button6_2._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)



    if button6_3._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)


    if button6_4._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)

    if button6_5._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)


    if button6_6._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)  

    if button6_7._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)


    if button6_8._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)

    if button6_9._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)


    if button6_10._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)  











    if button7_1._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)

    if button7_2._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)



    if button7_3._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)


    if button7_4._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)

    if button7_5._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)


    if button7_6._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)  

    if button7_7._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)


    if button7_8._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)

    if button7_9._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)


    if button7_10._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)  






    if button8_1._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)

    if button8_2._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)



    if button8_3._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)


    if button8_4._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)

    if button8_5._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)


    if button8_6._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)  

    if button8_7._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)


    if button8_8._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)

    if button8_9._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)


    if button8_10._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)  






    if button9_1._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)

    if button9_2._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)



    if button9_3._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)


    if button9_4._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)

    if button9_5._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)


    if button9_6._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)  

    if button9_7._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)


    if button9_8._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)

    if button9_9._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)


    if button9_10._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)  







    if button10_1._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)

    if button10_2._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)



    if button10_3._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)


    if button10_4._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)

    if button10_5._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)


    if button10_6._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)  

    if button10_7._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)


    if button10_8._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)

    if button10_9._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)


    if button10_10._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)  








    if button1_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)

    if button2_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)



    if button3_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)


    if button4_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)

    if button5_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)


    if button6_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)  

    if button7_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)


    if button8_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)

    if button9_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)

    if button10_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)  




    if button1_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)

    if button2_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)



    if button3_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)


    if button4_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)

    if button5_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)


    if button6_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)  

    if button7_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)


    if button8_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)

    if button9_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)

    if button10_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)  




    if button1_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)

    if button2_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)



    if button3_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)


    if button4_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)

    if button5_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)


    if button6_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)  

    if button7_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)


    if button8_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)

    if button9_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)

    if button10_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)  







    if button1_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)

    if button2_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)



    if button3_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)


    if button4_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)

    if button5_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)


    if button6_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)  

    if button7_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)


    if button8_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)

    if button9_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)

    if button10_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)  





    if button1_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)

    if button2_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)



    if button3_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)


    if button4_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)

    if button5_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)


    if button6_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)  

    if button7_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)


    if button8_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)

    if button9_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)

    if button10_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)  





    if button1_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)

    if button2_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)



    if button3_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)


    if button4_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)

    if button5_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)


    if button6_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)  

    if button7_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)


    if button8_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)

    if button9_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)

    if button10_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)  







    if button1_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)

    if button2_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)



    if button3_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)


    if button4_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)

    if button5_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)


    if button6_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)  

    if button7_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)


    if button8_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)

    if button9_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)

    if button10_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)  







    if button1_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)

    if button2_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)



    if button3_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)


    if button4_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)

    if button5_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)


    if button6_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)  

    if button7_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)


    if button8_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)

    if button9_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)

    if button10_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)  





    if button1_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)

    if button2_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)



    if button3_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)


    if button4_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)

    if button5_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)


    if button6_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)  

    if button7_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)


    if button8_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)

    if button9_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)

    if button10_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)  







    if button1_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)

    if button2_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)



    if button3_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)


    if button4_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)

    if button5_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)


    if button6_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)  

    if button7_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)


    if button8_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)

    if button9_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)

    if button10_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)  


    count1 = 0
    column_count1 = 0

    counter_cells1 = []

    counter_cells = []

    column_count = 0

    count = 0

    for string in matrix_strings:
        for cell in string:
            for index in range(5):
                try:
                    counter_cells1.append(string[count1 + index])
                except:
                    counter_cells1.append(1)

            if 1 in counter_cells1:
                pass
            elif 1 not in counter_cells1:
                for index in range(5):
                    try:
                        final_matrix[column_count1][count1 + index] += 1
                    except:
                        counter_cells1.append(1)
            count1 += 1
            counter_cells1 = []
        count1 = 0
        column_count1 += 1


                
    for column in matrix_columns:
        for cell in column:
            for index in range(5):
                try:
                    counter_cells.append(column[count + index])
                except:
                    counter_cells.append(1)

            if 1 in counter_cells:
                pass
            elif 1 not in counter_cells:
                for index in range(5):
                    try:
                        final_matrix[count + index][column_count] += 1
                    except:
                        counter_cells.append(1)
            count += 1
            counter_cells = []
        count = 0
        column_count += 1
        
        


    
    count1 = 0

    column_count1 = 0

    counter_cells1 = []

    counter_cells = []

    column_count = 0

    count = 0

    for string in matrix_strings:
        for cell in string:
            for index in range(4):
                try:
                    counter_cells1.append(string[count1 + index])
                except:
                    counter_cells1.append(1)

            if 1 in counter_cells1:
                pass
            elif 1 not in counter_cells1:
                for index in range(4):
                    try:
                        final_matrix[column_count1][count1 + index] += 1
                    except:
                        counter_cells1.append(1)
            count1 += 1
            counter_cells1 = []
        count1 = 0
        column_count1 += 1

        
                
    for column in matrix_columns:
        for cell in column:
            for index in range(4):
                try:
                    counter_cells.append(column[count + index])
                except:
                    counter_cells.append(1)

            if 1 in counter_cells:
                pass
            elif 1 not in counter_cells:
                for index in range(4):
                    try:
                        final_matrix[count + index][column_count] += 1
                    except:
                        counter_cells.append(1)
            count += 1
            counter_cells = []
        count = 0
        column_count += 1
                
        



    
    count1 = 0

    column_count1 = 0

    counter_cells1 = []

    counter_cells = []

    column_count = 0

    count = 0

    for string in matrix_strings:
        for cell in string:
            for index in range(3):
                try:
                    counter_cells1.append(string[count1 + index])
                except:
                    counter_cells1.append(1)

            if 1 in counter_cells1:
                pass
            elif 1 not in counter_cells1:
                for index in range(3):
                    try:
                        final_matrix[column_count1][count1 + index] += 1
                    except:
                        counter_cells1.append(1)
            count1 += 1
            counter_cells1 = []
        count1 = 0
        column_count1 += 1

        
                
    for column in matrix_columns:
        for cell in column:
            for index in range(3):
                try:
                    counter_cells.append(column[count + index])
                except:
                    counter_cells.append(1)

            if 1 in counter_cells:
                pass
            elif 1 not in counter_cells:
                for index in range(3):
                    try:
                        final_matrix[count + index][column_count] += 1
                    except:
                        counter_cells.append(1)
            count += 1
            counter_cells = []
        count = 0
        column_count += 1
        
    
    

                
        


    
    count1 = 0

    column_count1 = 0

    counter_cells1 = []

    counter_cells = []

    column_count = 0

    count = 0

    for string in matrix_strings:
        for cell in string:
            for index in range(2):
                try:
                    counter_cells1.append(string[count1 + index])
                except:
                    counter_cells1.append(1)

            if 1 in counter_cells1:
                pass
            elif 1 not in counter_cells1:
                for index in range(2):
                    try:
                        final_matrix[column_count1][count1 + index] += 2
                    except:
                        counter_cells1.append(1)
            count1 += 1
            counter_cells1 = []
        count1 = 0
        column_count1 += 1

            
                
    for column in matrix_columns:
        for cell in column:
            for index in range(2):
                try:
                    counter_cells.append(column[count + index])
                except:
                    counter_cells.append(1)

            if 1 in counter_cells:
                pass
            elif 1 not in counter_cells:
                for index in range(2):
                    try:
                        final_matrix[count + index][column_count] += 2
                    except:
                        counter_cells.append(1)
            count += 1
            counter_cells = []
        count = 0
        column_count += 1

            
    print("\n\nstrings:\n")
    for string in matrix_strings:
        print(string)


    print("\n\ncolumns:\n")
    for column in matrix_columns:
        print(column)

    print("\n\n", matrix_cells)
    for cell in matrix_cells:
        print(cell)


    for string in final_matrix:
        print(f"sosiska {string}")


    max_value = float('-inf')
    max_index = (-1, -1)


    for i in range(len(final_matrix)):
        for j in range(len(final_matrix[i])):
            if final_matrix[i][j] > max_value:
                max_value = final_matrix[i][j]
                max_index = (i, j)

    print("Наибольшее число в матрице:", max_value)
    print("Индекс наибольшего числа в матрице:", max_index)

                
    button_dict = {
    "button1_1": button1_1,
    "button1_2": button1_2,
    "button1_3": button1_3,
    "button1_4": button1_4,
    "button1_5": button1_5,
    "button1_6": button1_6,
    "button1_7": button1_7,
    "button1_8": button1_8,
    "button1_9": button1_9,
    "button1_10": button1_10,
    "button2_1": button2_1,
    "button2_2": button2_2,
    "button2_3": button2_3,
    "button2_4": button2_4,
    "button2_5": button2_5,
    "button2_6": button2_6,
    "button2_7": button2_7,
    "button2_8": button2_8,
    "button2_9": button2_9,
    "button2_10": button2_10,
    "button3_1": button3_1,
    "button3_2": button3_2,
    "button3_3": button3_3,
    "button3_4": button3_4,
    "button3_5": button3_5,
    "button3_6": button3_6,
    "button3_7": button3_7,
    "button3_8": button3_8,
    "button3_9": button3_9,
    "button3_10": button3_10,
    "button4_1": button4_1,
    "button4_2": button4_2,
    "button4_3": button4_3,
    "button4_4": button4_4,
    "button4_5": button4_5,
    "button4_6": button4_6,
    "button4_7": button4_7,
    "button4_8": button4_8,
    "button4_9": button4_9,
    "button4_10": button4_10,
    "button5_1": button5_1,
    "button5_2": button5_2,
    "button5_3": button5_3,
    "button5_4": button5_4,
    "button5_5": button5_5,
    "button5_6": button5_6,
    "button5_7": button5_7,
    "button5_8": button5_8,
    "button5_9": button5_9,
    "button5_10": button5_10,
    "button6_1": button6_1,
    "button6_2": button6_2,
    "button6_3": button6_3,
    "button6_4": button6_4,
    "button6_5": button6_5,
    "button6_6": button6_6,
    "button6_7": button6_7,
    "button6_8": button6_8,
    "button6_9": button6_9,
    "button6_10": button6_10,
    "button7_1": button7_1,
    "button7_2": button7_2,
    "button7_3": button7_3,
    "button7_4": button7_4,
    "button7_5": button7_5,
    "button7_6": button7_6,
    "button7_7": button7_7,
    "button7_8": button7_8,
    "button7_9": button7_9,
    "button7_10": button7_10,
    "button8_1": button8_1,
    "button8_2": button8_2,
    "button8_3": button8_3,
    "button8_4": button8_4,
    "button8_5": button8_5,
    "button8_6": button8_6,
    "button8_7": button8_7,
    "button8_8": button8_8,
    "button8_9": button8_9,
    "button8_10": button8_10,
    "button9_1": button9_1,
    "button9_2": button9_2,
    "button9_3": button9_3,
    "button9_4": button9_4,
    "button9_5": button9_5,
    "button9_6": button9_6,
    "button9_7": button9_7,
    "button9_8": button9_8,
    "button9_9": button9_9,
    "button9_10": button9_10,
    "button10_1": button10_1,
    "button10_2": button10_2,
    "button10_3": button10_3,
    "button10_4": button10_4,
    "button10_5": button10_5,
    "button10_6": button10_6,
    "button10_7": button10_7,
    "button10_8": button10_8,
    "button10_9": button10_9,
    "button10_10": button10_10
    }

    



    button_dict[f"button{max_index[0] + 1}_{max_index[1] + 1}"].configure(fg_color = "dark green")      





    final_matrix = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],  
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]




button_submit = customtkinter.CTkButton(screen, text="SUMBIT", font=(25,25), width= 200, height= 50, border_width= 2, border_color= "black", corner_radius= 10, fg_color= "grey", text_color="black", command= sumbit_cmd)


letters = customtkinter.CTkLabel(screen, font= (25,25), text_color= "light gray", text= "А    Б     В     Г     Д    Е    Ж    З     И     К")
numbers = customtkinter.CTkLabel(screen, font= (25,25), text_color= "light gray", text= "1\n\n2\n\n3")
numbers2 = customtkinter.CTkLabel(screen, font= (25,25), text_color= "light gray", text= "4\n\n5\n\n6")
numbers3 = customtkinter.CTkLabel(screen, font= (25,25), text_color= "light gray", text= "7\n\n8\n\n9")
numbers4 = customtkinter.CTkLabel(screen, font= (25,25), text_color= "light gray", text= "10")



letters.place(x = 115, y = 70)

numbers.place(x = 70, y = 100)
numbers2.place(x = 70, y = 255)
numbers3.place(x = 70, y = 405)
numbers4.place(x = 65, y = 555)



button1_1.place(x = 100, y = 100)
button1_2.place(x = 149, y = 100)
button1_3.place(x = 198, y = 100)
button1_4.place(x = 247, y = 100)
button1_5.place(x = 296, y = 100)
button1_6.place(x = 345, y = 100)
button1_7.place(x = 394, y = 100)
button1_8.place(x = 444, y = 100)
button1_9.place(x = 493, y = 100)
button1_10.place(x = 542, y = 100)

button2_1.place(x = 100, y = 149)
button2_2.place(x = 149, y = 149)
button2_3.place(x = 198, y = 149)
button2_4.place(x = 247, y = 149)
button2_5.place(x = 296, y = 149)
button2_6.place(x = 345, y = 149)
button2_7.place(x = 394, y = 149)
button2_8.place(x = 444, y = 149)
button2_9.place(x = 493, y = 149)
button2_10.place(x = 542, y = 149)

button3_1.place(x = 100, y = 198)
button3_2.place(x = 149, y = 198)
button3_3.place(x = 198, y = 198)
button3_4.place(x = 247, y = 198)
button3_5.place(x = 296, y = 198)
button3_6.place(x = 345, y = 198)
button3_7.place(x = 394, y = 198)
button3_8.place(x = 444, y = 198)
button3_9.place(x = 493, y = 198)
button3_10.place(x = 542, y = 198)

button4_1.place(x = 100, y = 247)
button4_2.place(x = 149, y = 247)
button4_3.place(x = 198, y = 247)
button4_4.place(x = 247, y = 247)
button4_5.place(x = 296, y = 247)
button4_6.place(x = 345, y = 247)
button4_7.place(x = 394, y = 247)
button4_8.place(x = 444, y = 247)
button4_9.place(x = 493, y = 247)
button4_10.place(x = 542, y = 247)

button5_1.place(x = 100, y = 296)
button5_2.place(x = 149, y = 296)
button5_3.place(x = 198, y = 296)
button5_4.place(x = 247, y = 296)
button5_5.place(x = 296, y = 296)
button5_6.place(x = 345, y = 296)
button5_7.place(x = 394, y = 296)
button5_8.place(x = 444, y = 296)
button5_9.place(x = 493, y = 296)
button5_10.place(x = 542, y = 296)

button6_1.place(x = 100, y = 345)
button6_2.place(x = 149, y = 345)
button6_3.place(x = 198, y = 345)
button6_4.place(x = 247, y = 345)
button6_5.place(x = 296, y = 345)
button6_6.place(x = 345, y = 345)
button6_7.place(x = 394, y = 345)
button6_8.place(x = 444, y = 345)
button6_9.place(x = 493, y = 345)
button6_10.place(x = 542, y = 345)

button7_1.place(x = 100, y = 394)
button7_2.place(x = 149, y = 394)
button7_3.place(x = 198, y = 394)
button7_4.place(x = 247, y = 394)
button7_5.place(x = 296, y = 394)
button7_6.place(x = 345, y = 394)
button7_7.place(x = 394, y = 394)
button7_8.place(x = 444, y = 394)
button7_9.place(x = 493, y = 394)
button7_10.place(x = 542, y = 394)

button8_1.place(x = 100, y = 444)
button8_2.place(x = 149, y = 444)
button8_3.place(x = 198, y = 444)
button8_4.place(x = 247, y = 444)
button8_5.place(x = 296, y = 444)
button8_6.place(x = 345, y = 444)
button8_7.place(x = 394, y = 444)
button8_8.place(x = 444, y = 444)
button8_9.place(x = 493, y = 444)
button8_10.place(x = 542, y = 444)

button9_1.place(x = 100, y = 493)
button9_2.place(x = 149, y = 493)
button9_3.place(x = 198, y = 493)
button9_4.place(x = 247, y = 493)
button9_5.place(x = 296, y = 493)
button9_6.place(x = 345, y = 493)
button9_7.place(x = 394, y = 493)
button9_8.place(x = 444, y = 493)
button9_9.place(x = 493, y = 493)
button9_10.place(x = 542, y = 493)

button10_1.place(x = 100, y = 542)
button10_2.place(x = 149, y = 542)
button10_3.place(x = 198, y = 542)
button10_4.place(x = 247, y = 542)
button10_5.place(x = 296, y = 542)
button10_6.place(x = 345, y = 542)
button10_7.place(x = 394, y = 542)
button10_8.place(x = 444, y = 542)
button10_9.place(x = 493, y = 542)
button10_10.place(x = 542, y = 542)

clear_button.place(x = 650, y = 0)

notes_button.place(x = 650, y = 50)

button_submit.place(x = 250, y = 600)

settings_button.place(x = 0, y = 0)


screen.mainloop()