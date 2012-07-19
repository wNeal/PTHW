# Decided to use and practice the new way to format text

# Define the variables
x = "There are {0:d} types of people".format(10)
binary = "binary"
do_not = "don't"
# EC2 First Occurance
y = "Those who know {0:s} and those who {1:s}".format(binary, do_not)

# Print x and y
print x
print y

# Show of the difference between repr() and str()
# EC2 2nd Occurance
print "I said: {!r}.".format(x)
# EC2 3rd Occurance
print "I also said: '{0:s}'.".format(y)

# Define some new variables
hilarious = False
# EC2 4rd Occurance
joke_evaluation = "Isn't that joke so funny?! {!r}"

# Join the variables to format and output
print joke_evaluation.format(hilarious)

# Define even more variables
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate the strings and print
print w + e

"""
Extra Credit 1: Go through this program and write a comment above each line explaining it.
Extra Credit 2: Find all the places where a string is put inside a string. There are four places.
Extra Credit 3: Are you sure there's only four places? How do you know? Maybe I like lying.
    If you count the first occurance as 2 then there are 5
Extra Credit 4: Explain why adding the two strings w and e with + makes a longer string.
    concatenation
"""
