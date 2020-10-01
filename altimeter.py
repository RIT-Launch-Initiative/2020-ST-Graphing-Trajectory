#!/usr/bin/python3
import time

# I hate Python globals
global file
global data
global count

delta_t = 0.8 #ms

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
        return data[count - 1]
    except IndexError:
        return -1

if __name__ == '__main__':
    altimeter_init()
    print(get_altitude())
    altimeter_close()
