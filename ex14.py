#!/usr/bin/python2
from sys import argv

script, user_name = argv
prompt = '> '

print "Hi {0}, I'm the {1} script.".format(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me {}?".format(user_name)
likes = raw_input(prompt)

print "Where do you live {}?".format(user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said {!r} about liking me.
You live in {!r}. Not sure where that is.
And you have a {!r} computer. Nice.
""".format(likes, lives, computer)
