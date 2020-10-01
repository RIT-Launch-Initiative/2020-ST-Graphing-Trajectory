#!/usr/bin/python3
import time

# I hate Python globals
global file
global data
global count

delta_t = 0.05 #sec (not ms, dumb Python)

def altimeter_init():
    global file, data, count
    file = open("alt_data")
    data = file.readlines()
    count = 0

def altimeter_close():
    global file
    file.close()

def get_altitude():
    global count, data
    try:
        time.sleep(delta_t)
        count = count + 1
        return float(data[count - 1])
    except IndexError:
        return None

if __name__ == '__main__':
    altimeter_init()
    running = True
    while running:
        alt = get_altitude()
        if alt is not None:
            print(alt)
        else:
            running = False

    altimeter_close()
