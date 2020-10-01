#!/usr/bin/python3
import altimeter as alt

# init altimeter with "altimeter_init()"
alt.altimeter_init()

# read values from the altimeter with "get_altitude()"
# use those values to look for apogee

max_alt_count = 5

running = True
count = 0
last_alt = None
curr_alt = None
while(running):
    last_alt = curr_alt
    curr_alt = alt.get_altitude()
    if curr_alt is not None:
        print(curr_alt)
        if last_alt is not None:
            if last_alt - curr_alt > 0:
                count = count + 1
    if count >= max_alt_count:
        print("Apogee!")
        running = False


# close the altimeter with "altimeter_close()"
alt.altimeter_close()
