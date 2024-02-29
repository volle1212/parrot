import os
from os import listdir
from os.path import isfile, join
import time
import rainbowtext

clear = lambda: os.system('cls')
frames = [f for f in listdir("C:/Users/vilmer.folcke/Documents/python/projects/celebration/frames") if isfile(join("C:/Users/vilmer.folcke/Documents/python/projects/celebration/frames", f))]
start_time = time.perf_counter()

all_colors = {
    "red": "\033[1;31;40m",
    "green": "\033[1;32;40m",
    "yellow": "\033[1;33;40m",
    "blue": "\033[1;34;40m",
    "magenta": "\033[1;35;40m",
    "cyan": "\033[1;36;40m",
    "white": "\033[1;37;40m",
              }

colors = [all_colors.get('red'), all_colors.get('red'), all_colors.get('yellow'), all_colors.get('green'), all_colors.get('green'), all_colors.get('red'), all_colors.get('cyan'), all_colors.get('blue'), all_colors.get('blue'),  all_colors.get('magenta'), all_colors.get('white')]

def party_if_accepted(i):
    """Takes number of parrot iterations as integer"""
    accept = False
    while not accept:
        print("")
        if input('Do you want to celebrate? (y/n)\n(console logs will get lost)').lower() == "y":
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
    print("\033[0;37;40m")
    clear()

party_if_accepted(5)