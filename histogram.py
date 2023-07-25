import os
import sys
import string

lines = sys.stdin.readline()
key_value_dict = {}
total_count = 0

while lines != "":
    key_value = lines.split()
    key = key_value[0]
    value = int(key_value[1])
    key_value_dict[key] = value
    total_count += value
    lines = sys.stdin.readline()

for key, value in key_value_dict.items():
    print(key.ljust(15), "\t [",sep="",end="")
    pre = int(value)*100//total_count
    for i in range(0,pre,5):
        print("*",sep="",end="")
    print("]",pre,"%",sep="")