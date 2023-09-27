from pynput import keyboard
from threading import Thread
import time

flag = False
thread = None

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    global flag, thread
    if key == keyboard.up:
        flag = True
        thread = Thread(target = on_press)
        thread.start()
    elif key == keyboard.down:
        print("stopped")
        flag = False
        if thread.is_alive():
            thread.join()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
