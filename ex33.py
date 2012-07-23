#!/usr/bin/python2

i = 0
numbers = []

while i < 6:
    print "At the top i is {}".format(i)
    numbers.append(i)

    i = i + 1
    print "Numbers now: {}".format(numbers)
    print "At the bottom i is {}".format(i)

print "The numbers: "

for num in numbers:
    print num
