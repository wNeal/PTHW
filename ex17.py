#!/usr/bin/python2
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from {} to {}".format(from_file, to_file)

# We could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print "The input file is {} bytes long".format(len(indata))

print "Does the output file exist? {!r}".format(exists(to_file))
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()
