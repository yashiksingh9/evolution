import random
import string
import os
import time as ts
from datetime import datetime
age  = 0
time = 0
c    = -1
path = __file__


def born_time(c):
    global born_year,born_month,born_date,born_hour,born_minute,born_second
    born_year = []
    now         = datetime.now()
    time        = now.strftime("%Y-%m-%d %H:%M:%S")
    time        = list(time)
    for i in time:
        c = c + 1
        if i == '-':
            break
    for i in range(c):
        born_year.append(time[i])
    born_year   = int("".join(born_year))
    born_month  = int(time[5] + time[6])
    born_date   = int(time[8] + time[9])
    born_hour   = int(time[11] + time[12])
    born_minute = int(time[14] + time[15])
    born_second = int(time[17] + time[18])

born_time(c)

def current_time(c):
    global current_year,current_month,current_date,current_hour,current_minute,current_second
    current_year = []
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    time = list(time)
    for i in time:
        c = c + 1
        if i == '-':
            break
    for i in range(c):
        current_year.append(time[i])
    current_year   = int("".join(current_year))
    current_month  = int(time[5] + time[6])
    current_date   = int(time[8] + time[9])
    current_hour   = int(time[11] + time[12])
    current_minute = int(time[14] + time[15])
    current_second = int(time[17] + time[18])

def growth_track():
    global age_day,age_hour,age_minute,age_second
    age_day,age_hour,age_minute,age_second =0,0,0,0

    while True:
        current_time(c)
        if age_hour    == 24 and age_second == 0 and age_minute == 0:
            age_day    = age_day + 1
        if age_minute  == 59 and age_second == 59:
            age_hour   = age_hour + 1
        if age_second  == 59:
            age_minute = age_minute + 1
        ts.sleep(1)
        age_second = age_second + 1
        if age_second == 60:
            age_second = 1
        if age_minute == 60:
            age_minute = 0
        if age_hour   == 24:
            age_hour   = 0
        print(age_day, age_hour, age_minute, age_second)
        print(path)
        reproduce_compatibility_checker()

def name_gen(name_size=3):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(name_size))

def kill():
    os.system("start /B start cmd.exe @cmd /k python "+n_1)
    os.system("start /B start cmd.exe @cmd /k python "+n_2)
    soul = os.path.abspath(path)
    os.remove(soul)
    exit()

def reproduce(path):
    global n_1,n_2
    name_1 = name_gen()
    name_2 = name_gen()
    n_1    = str("grass_"+name_1+".py")
    n_2    = str("grass_"+name_2+".py")
    print(n_1)
    print(n_2)
    with open(n_1, "w+") as newfile, open(path) as program:
        for line in program:
            newfile.write(line)
    with open(n_2, "w+") as newfile, open(path) as program:
        for line in program:
            newfile.write(line)

def reproduce_compatibility_checker():

    if age_minute == 1 or age_minute > 1:
        reproduce(path)
        kill()

growth_track()
