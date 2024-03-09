import os
from os import listdir
from os.path import isfile, join
import time
import subprocess

path_to_files = "frames/"

clear = lambda: os.system('cls')
frames = [f for f in listdir(path_to_files) if isfile(join(path_to_files, f))]
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

def party(i, path_to_files=path_to_files):
    """Takes number of parrot iterations as integer 
    and path to the frames which has to be named 0.txt, 1.txt etc with a max of 9.txt"""
    if path_to_files == "":
        raise Exception("Missing path to files (path_to_files, takes string)")

    for _ in range(i):
        for frame in frames:
            color = colors[int(frame.replace(".txt", ""))]
            print(color)
            with open(str(path_to_files+frame)) as f: # The with keyword automatically closes the file when you are done
                clear()
                print(f"{color}{f.read()}")

            elapsed_time = time.perf_counter() - start_time
            
            # Adjust delay to achieve the desired interval
            desired_interval = 0.1  # 1 second interval
            delay = max(0, desired_interval - elapsed_time % desired_interval)
            
            time.sleep(delay)
    print("\033[0;37;40m")
    clear()

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2 or sys.argv[1] != "party":
        command = f"start cmd /k python parrot.py party"
        subprocess.Popen(command, shell=True)
        sys.exit(1)

    party(5)
