import math
from copy import copy
from itertools import compress
from pysortlib import bubble_sort
import time
import numpy as np
import sympy
import pulp

with open('2025 input') as file:
    lines = [line.strip() for line in file]


def apply(lights, button):
    for i in button:
        if lights[i] == '.':
            lights[i] = '#'
        else:
            lights[i] = '.'

    return lights

c = 0
for i, line in enumerate(lines):
    line = line.split(" ")
    goal = line.pop(0)
    joltages = line.pop(-1)
    goal = list(goal.replace('[','').replace(']',''))

    for j, button in enumerate(line):
        button = button.replace('(','').replace(")", '')
        button = list(map(int, button.split(',')))
        line[j] = button


    buttons = line
    numperms = 2**len(buttons)
    minlength = math.inf
    for perm in range(numperms):
        comp = bin(perm)[2:]
        l = comp.count("1")
        while len(comp) < len(buttons):
            comp = '0' + comp
        activated_buttons = list(compress(buttons, list(map(int, list(comp)))))
        lights = ['.']*len(goal)
        for button in activated_buttons:
            lights = apply(lights, button)
        if lights == goal:
            minlength = min(minlength, l)

    c += minlength
    lines[i] = [goal, buttons, joltages]


print(f'Part 1: {c}')

c = 0

def minSteps(joltages, buttons):
    A = []
    for i, joltage in enumerate(joltages):
        row = []
        for j, button in enumerate(buttons):
            if i in button:
                row.append(1)
            else:
                row.append(0)

        A.append(copy(row))



for i, line in enumerate(lines):
    buttons = line[1]
    joltages = line[2]
    joltages = joltages.replace('{', "").replace("}","")
    joltages = list(map(int, joltages.split(",")))

    goal = [0]*len(joltages)
    buttons = list(map(tuple, buttons))
    mindict = dict()
    minSteps(joltages, buttons)

print(c)




