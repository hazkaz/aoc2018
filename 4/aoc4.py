# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:16:40 2019

@author: HARIKRISHNAN
"""

START=0
SLEEP=1
WAKE=2

import re
import datetime
import operator
from collections import Counter

def main():
    with open('input4.txt') as file:
    # with open('test4.txt') as file:
        times = file.read().strip().split("\n")
        timing = []
        for line in times:
            guard=None
            matches = re.match("^\\[([^\\]]+)\\](.*)",line)
            time = datetime.datetime.fromisoformat(matches.group(1))
            action = matches.group(2)
            action_marker = None
            b= re.search("#(\\d+)",action)
            if(b is not None):
                guard=int(b.group(1))
            if("wakes" in action):
                action_marker=2
            elif("begins" in action):
                action_marker=0
            elif("asleep" in action):
                action_marker=1
            timing.append((time,action_marker,guard))
        timing.sort(key=lambda a:a[0])
        sleep_counter = {}
        frequency_counter = {}
        sleep_start=None
        current_guard=None
        for time,action,guard in timing:
            if(action==0 and guard is not None):
                if(guard not in sleep_counter):
                    sleep_counter[guard]=0
                if(guard not in frequency_counter):
                    frequency_counter[guard]={}
                current_guard=guard
            if(action==1):
                sleep_start=time
            if(action==2):
                diff = ((time-sleep_start).seconds//60)
                sleep_counter[current_guard]+=diff
                for i in range(sleep_start.minute,time.minute):
                    if(i not in frequency_counter[current_guard]):
                        frequency_counter[current_guard][i]=1
                    else:
                        frequency_counter[current_guard][i]+=1

        max_sleeper = max(sleep_counter.items(),key=operator.itemgetter(1))[0]
        max_sleep_pattern = []
        for time,action,guard in timing:
            if(guard==max_sleeper or current_guard==max_sleeper):
                if(action==0):
                    current_guard=guard
                if(action==1):
                    sleep_start=time
                if(action==2):
                    max_sleep_pattern.extend(range(sleep_start.minute,time.minute))
        safest_time = Counter(max_sleep_pattern).most_common()[0][0]

        print(safest_time)
        print(max_sleeper)
        print(safest_time*max_sleeper)

        maximum=(0,0)
        # print(frequency_counter)
        sleepiest_guard = None
        for minute,frequencies in frequency_counter.items():
            # print(minute,frequencies)
            frequency = Counter(frequencies)
            if(len(frequency)>0 and maximum[1]<frequency.most_common()[0][1]):
                maximum=frequency.most_common()[0]
                sleepiest_guard = minute
        print(f"guard #{sleepiest_guard} spend {maximum[1]} minutes sleeping on minute {maximum[0]}...zzzz....answer to part 2 is {maximum[0]*sleepiest_guard}")
if __name__=="__main__":
    main()