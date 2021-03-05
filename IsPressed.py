#import all needed modules
import time
import tkinter as tk
import win32api as w32

#declareing all variables

#tkinter gui window,size,icon,titile
root = tk.Tk()
root.title("IsPressed")
root.iconbitmap('ispressedicon.ico')
root.geometry("200x35")
#make the gui window remain on the top
root.wm_attributes("-topmost", 1)

string = ""
current_time = 0.0
pressed = ""
temp = " "

#creating a dictionary to keep all virtual key codes
#adding a boolean to seperately detect condition of every keys
dict = {'Mouse-Left':[0x01,False],
           'Mouse-Right':[0x02,False],
           'Mouse-Middle':[0x04,False],
           'backspace':[0x08,False],
           'tab':[0x09,False],
           'clear':[0x0C,False],
           'enter':[0x0D,False],
           'shift':[0x10,False],
           'ctrl':[0x11,False],
           'alt':[0x12,False],
           'pause':[0x13,False],
           'caps_lock':[0x14,False],
           'esc':[0x1B,False],
           'spacebar':[0x20,False],
           'page_up':[0x21,False],
           'page_down':[0x22,False],
           'end':[0x23,False],
           'home':[0x24,False],
           'left_arrow':[0x25,False],
           'up_arrow':[0x26,False],
           'right_arrow':[0x27,False],
           'down_arrow':[0x28,False],
           'select':[0x29,False],
           'print':[0x2A,False],
           'execute':[0x2B,False],
           'print_screen':[0x2C,False],
           'ins':[0x2D,False],
           'del':[0x2E,False],
           'help':[0x2F,False],
           '0':[0x30,False],
           '1':[0x31,False],
           '2':[0x32,False],
           '3':[0x33,False],
           '4':[0x34,False],
           '5':[0x35,False],
           '6':[0x36,False],
           '7':[0x37,False],
           '8':[0x38,False],
           '9':[0x39,False],
           'a':[0x41,False],
           'b':[0x42,False],
           'c':[0x43,False],
           'd':[0x44,False],
           'e':[0x45,False],
           'f':[0x46,False],
           'g':[0x47,False],
           'h':[0x48,False],
           'i':[0x49,False],
           'j':[0x4A,False],
           'k':[0x4B,False],
           'l':[0x4C,False],
           'm':[0x4D,False],
           'n':[0x4E,False],
           'o':[0x4F,False],
           'p':[0x50,False],
           'q':[0x51,False],
           'r':[0x52,False],
           's':[0x53,False],
           't':[0x54,False],
           'u':[0x55,False],
           'v':[0x56,False],
           'w':[0x57,False],
           'x':[0x58,False],
           'y':[0x59,False],
           'z':[0x5A,False],
           'numpad_0':[0x60,False],
           'numpad_1':[0x61,False],
           'numpad_2':[0x62,False],
           'numpad_3':[0x63,False],
           'numpad_4':[0x64,False],
           'numpad_5':[0x65,False],
           'numpad_6':[0x66,False],
           'numpad_7':[0x67,False],
           'numpad_8':[0x68,False],
           'numpad_9':[0x69,False],
           'multiply_key':[0x6A,False],
           'add_key':[0x6B,False],
           'separator_key':[0x6C,False],
           'subtract_key':[0x6D,False],
           'decimal_key':[0x6E,False],
           'divide_key':[0x6F,False],
           'F1':[0x70,False],
           'F2':[0x71,False],
           'F3':[0x72,False],
           'F4':[0x73,False],
           'F5':[0x74,False],
           'F6':[0x75,False],
           'F7':[0x76,False],
           'F8':[0x77,False],
           'F9':[0x78,False],
           'F10':[0x79,False],
           'F11':[0x7A,False],
           'F12':[0x7B,False],
           'F13':[0x7C,False],
           'F14':[0x7D,False],
           'F15':[0x7E,False],
           'F16':[0x7F,False],
           'F17':[0x80,False],
           'F18':[0x81,False],
           'F19':[0x82,False],
           'F20':[0x83,False],
           'F21':[0x84,False],
           'F22':[0x85,False],
           'F23':[0x86,False],
           'F24':[0x87,False],
           'num_lock':[0x90,False],
           'scroll_lock':[0x91,False],
           'browser_back':[0xA6,False],
           'browser_forward':[0xA7,False],
           'browser_refresh':[0xA8,False],
           'browser_stop':[0xA9,False],
           'browser_search':[0xAA,False],
           'browser_favorites':[0xAB,False],
           'browser_start_and_home':[0xAC,False],
           'volume_mute':[0xAD,False],
           'volume_Down':[0xAE,False],
           'volume_up':[0xAF,False],
           'next_track':[0xB0,False],
           'previous_track':[0xB1,False],
           'stop_media':[0xB2,False],
           'play/pause_media':[0xB3,False],
           'start_mail':[0xB4,False],
           'select_media':[0xB5,False],
           'start_application_1':[0xB6,False],
           'start_application_2':[0xB7,False],
           'attn_key':[0xF6,False],
           'crsel_key':[0xF7,False],
           'exsel_key':[0xF8,False],
           'play_key':[0xFA,False],
           'zoom_key':[0xFB,False],
           'clear_key':[0xFE,False],
           '+':[0xBB,False],
           ',':[0xBC,False],
           '-':[0xBD,False],
           '.':[0xBE,False],
           '/':[0xBF,False],
           '`':[0xC0,False],
           ';':[0xBA,False],
           '[':[0xDB,False],
           '\\':[0xDC,False],
           ']':[0xDD,False],
           "'":[0xDE,False],
           '`':[0xC0,False]}

#make the text lebel in the gui
w = tk.Label(root, text=string,font=20)
w.pack()

#main loop
while True:
    #update tkinter window everytime the loop runs
    root.update()
    #check key-strokes comparing with the created dictionary
    for key,value in dict.items():
        if w32.GetKeyState(value[0])<0 and value[1] == False:
            if pressed == "" :
                string = ""
            pressed = key
            string += " " +key
            #detecting double clicks in a certain amount of time
            if temp == string and time.time()-current_time < 0.5:
                string += " x2"
            value[1] = True
            current_time = time.time()
        #toggle the value of boolean to define key condition
        if w32.GetKeyState(value[0])>=0:
            value[1]=False
            if key == pressed:
                pressed = ""
        #make key text disappear after 2.5 seconds of interval
        if time.time()-current_time > 2.5 :
            string=""
    #update the text
    w.config(text=string)
    #keep current keystrokes in a variable to detect double click next time
    temp = string
    #Important
    #restrict the loop to every 0.05 second
    #You dont need to run the loop at full power it can give
    #otherwise computer cpu,power and other resources will be misused and may cause the computer slow down
    time.sleep(0.05)

#prevent the python script from stop running instantly after starting
input()


