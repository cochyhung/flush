from sys import stdout
import sys, os, time
from colorama import Fore
d1 = ["cóc hy hùng là trick cơ đz s1tg"]
os.system('cls')
for dong1 in d1:
    for a in dong1:
        print(f"{Fore.GREEN} {a}", flush= True, end='')
        time.sleep(0.05)