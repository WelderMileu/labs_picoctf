#!/usr/bin/bash
from collections import defaultdict
import os

n = [0, 29, 4, 2, 23, 3, 17, 1, 7, 10, 5, 9, 11, 15, 8, 12, 20, 14, 6, 24, 18, 13,
     19, 21, 16, 27, 30, 25, 22, 28, 26, 31]

string = 'd9r5rc43b_43tclHc_m5r34TH52_307e'
resolve = ''

new = defaultdict(list)
for x in n: new[x].append(string[n.index(x)])

for x in range(0, 32): resolve += new[x][0]

flag = "picoCTF{" + resolve + "}"

if not os.path.exists('flag.txt'):
    flag_write = open('flag.txt', 'w')
    flag_write.write(flag)

print(flag) 
