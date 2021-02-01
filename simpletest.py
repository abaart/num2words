from num2words import *
from random import randint


for i in range(2,10):
    for y in range(0,2):
        maxnum = int(str(9)*i)
        number = randint(0,maxnum)
        res = num2words(number,lang='bm')

        print(f"{number} = {res}")