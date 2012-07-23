name = 'Zed A. Shaw'
age = 35
height = 75 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# EC 4
height_cm = height * 2.54
weight_kilos = weight * 0.453592


print "Let's talk about %s." % name
print "He's %d inches tall." % height
print 'That\'s {0:.1f} in centimeters'.format(height_cm)
# using the new way to format strings
print "He's %d pounds heavy." % weight
# using the new way to format strings
print 'That\'s {0:.2f} in kilograms'.format(weight_kilos)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# EC2
print "%d, %i: %%d and %%i are signed integer decimals" % (1.0, 1)
print "%o: %%o is an octal number" % 0177
print "%u: %%u is an unsigned decimal" % -20
print "%x: %%x is an unsigned hexadecimal (lowercase)" % 0x12
print "%X: %%X is an unsigned hexadecimal (uppercase)" % 0X12
"""
Extra Credit 1: Change all the variables so there isn't the my_ in front. Make sure you change the name everywhere, not just where you used = to set them.

Extra Credit 2: Try more format characters. %r is a very useful one. It's like saying "print this no matter what".

Extra Credit 3: Search online for all of the Python format characters.

d	Signed integer decimal.
i	Signed integer decimal.
o	Unsigned octal.
u	Unsigned decimal. # Obsolete
x	Unsigned hexadecimal (lowercase).
X	Unsigned hexadecimal (uppercase).
e	Floating point exponential format (lowercase).
E	Floating point exponential format (uppercase).
f	Floating point decimal format.
F	Floating point decimal format.
g	Floating point format. Uses exponential format if exponent is greater than -4 or less than precision, decimal format otherwise.
G	Floating point format. Uses exponential format if exponent is greater than -4 or less than precision, decimal format otherwise.
c	Single character (accepts integer or single character string).
r	String (converts any python object using repr()).
s	String (converts any python object using str()).
%	No argument is converted, results in a "%" character in the result.

Extra Credit 4: Try to write some variables that convert the inches and pounds to centimeters and kilos. Do not just type in the measurements. Work out the math in Python.
"""
