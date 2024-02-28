import os
from os import listdir
from os.path import isfile, join
import time
import rainbowtext

clear = lambda: os.system('cls')
frames = [f for f in listdir("C:/Users/vilmer.folcke/Documents/python/projects/celebration/frames") if isfile(join("C:/Users/vilmer.folcke/Documents/python/projects/celebration/frames", f))]
start_time = time.perf_counter()

colors = ["\033[1;31;40m", "\033[1;31;40m", "\033[1;33;40m", "\033[1;32;40m", "\033[1;32;40m", "\033[1;31;40m", "\033[1;36;40m", "\033[1;34;40m", "\033[1;34;40m",  "\033[1;35;40m" "\033[1;37;40m"]

def party_if_accepted(i):
    """Takes number of parrot iterations as integer"""
    accept = False
    while not accept:
        if input(f"{rainbowtext.text('Do you want to party?')}\033[0;37;40m (\033[0;32;40my\033[0;37;40m/\033[0;31;40mn\033[0;37;40m)\n(Some console data might get lost)").lower() == "y":
            accept = True
    for _ in range(i):
        for frame in frames:
            color = colors[int(frame.replace(".txt", ""))]
            print(color)
            with open(str("C:/Users/vilmer.folcke/Documents/python/projects/celebration/frames/"+frame)) as f: # The with keyword automatically closes the file when you are done
                clear()
                print(f"{color}{f.read()}")

            elapsed_time = time.perf_counter() - start_time
            
            # Adjust delay to achieve the desired interval
            desired_interval = 0.1  # 1 second interval
            delay = max(0, desired_interval - elapsed_time % desired_interval)
            
            time.sleep(delay)
    clear()

party_if_accepted(5)