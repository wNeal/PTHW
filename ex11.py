#!/usr/bin/python2
age = raw_input("How old are you?")
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're {!r} old, {!r} tall and {!r} heavy.".format(age,height,weight)

# EC3
gender = raw_input("What is your gender?")
name = raw_input("What is your name?")

print "Hello, {0:s}. You are a {1:s}.".format(name,gender)

"""
Extra Credit 1:
Go online and find out what Python's raw_input does.
    raw_input reads input from the user. It strips trailing trailing newline characters

Extra Credit 2:
Can you find other ways to use it? Try some of the samples you find.
    a promt can be passed as an argument see first occurance for and example

Extra Credit 3:
Write another "form" like this to ask some other questions.

Extra Credit 4:
Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence. See how the single-quote needs to be escaped because otherwise it would end the string?
    Because both versions of the quotes are used and we are using repr() to dump out out strings, the function must handle the use of quotes to avoid escaping the string
"""
