#!/usr/bin/python2
from sys import argv

script, filename = argv

# Open the filename that was provided as an argument
txt = open(filename)

print "Here's your file {!r}:".format(filename)
# Print out the file contents
print txt.read()
txt.close()

print "Type the filename again:"
# Ask for a new filename
file_again = raw_input("> ")

# Open the second file
txt_again = open(file_again)

# Print its contents
print txt_again.read()
txt_again.close()
