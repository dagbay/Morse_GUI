from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)

# Morse Code Procedures
def dot():
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.1)
    
def dash():
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.15)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.1)

# Takes each char and translates it into morse code.
def translate(i):
    if i == 'A':
        dot()
        dash()
        time.sleep(space)
    if i == 'B':
        dash()
        dot()
        dot()
        dot()
        time.sleep(space)
    if i == 'C':
        dash()
        dot()
        dash()
        dot()
        time.sleep(space)
    if i == 'D':
        dash()
        dot()
        dot()
        time.sleep(space)
    if i == 'E':
        dot()
        time.sleep(space)
    if i == 'F':
        dot()
        dot()
        dash()
        dot()
        time.sleep(space)
    if i == 'G':
        dash()
        dash()
        dot()
        time.sleep(space)
    if i == 'H':
        dot()
        dot()
        dot()
        dot()
        time.sleep(space)
    if i == 'I':
        dot()
        dot()
        time.sleep(space)
    if i == 'J':
        dot()
        dash()
        dash()
        dash()
        time.sleep(space)
    if i == 'K':
        dash()
        dot()
        dash()
        time.sleep(space)
    if i == 'L':
        dot()
        dash()
        dot()
        dot()
        time.sleep(space)
    if i == 'M':
        dash()
        dash()
        time.sleep(space)
    if i == 'N':
        dash()
        dot()
        time.sleep(space)
    if i == 'O':
        dash()
        dash()
        time.sleep(space)
    if i == 'P':
        dot()
        dash()
        dash()
        dot()
        time.sleep(space)
    if i == 'Q':
        dash()
        dash()
        dot()
        dash()
        time.sleep(space)
    if i == 'R':
        dot()
        dash()
        dot()
        time.sleep(space)
    if i == 'S':
        dot()
        dot()
        dot()
        time.sleep(space)
    if i == 'T':
        dash()
        time.sleep(space)
    if i == 'U':
        dot()
        dot()
        dash()
        time.sleep(space)
    if i == 'V':
        dot()
        dot()
        dot()
        dash()
        time.sleep(space)
    if i == 'W':
        dot()
        dash()
        dash()
        time.sleep(space)
    if i == 'X':
        dash()
        dot()
        dot()
        dash()
        time.sleep(space)
    if i == 'Y':
        dash()
        dot()
        dash()
        dash()
        time.sleep(space)
    if i == 'Z':
        dash()
        dash()
        dot()
        dot()
        time.sleep(space)

# Loop
# Procedure to close the app.
def close():
    GPIO.cleanup()
    win.destroy()

# Validation procedure
def callback(input):
    if len(input) < 13:
        return True
    else:
        return False

# GUI Definitions
win = Tk()
win.title("Morse Code Translator")
my_font = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")
e = Entry(win, width = 50)
e.pack()
reg = win.register(callback)
e.config(validate="key",validatecommand=(reg,'%P'))

# Number of seconds to pause the blink.
space = 0.15

# Procedure that performs when the button is clicked, translates the input to morse code.
def my_click():
    code = ''
    code_length = 0
    i = chr
    in_char = e.get().upper()
    for x in range(len(in_char)):
        code += in_char[x]
    print(code)
    do_string(code)

# Procedure that takes in the user input and translates it to morse code.
def do_string(code):
    for x in range(len(code)):
        i = code[x];
        translate(i)

# Button for the GUI with the command my_click.
my_button = Button(win, text="Translate", command=my_click)
my_button.pack()

# Closes the window if close button is clicked.
win.protocol("WM_DELETE_WINDOW", close)   
win.mainloop()
        
        
        
        
        
        
        
        
