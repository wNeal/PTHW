tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
    test
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

"""
Extra Credit 1:
Search online to see what other escape sequences are available.
    Note that added slashes are to prevent errors
    \\newline	Ignored
    \\	Backslash (\)
    \\'	Single quote (')
    \\"	Double quote (")
    \\a	ASCII Bell (BEL)
    \\b	ASCII Backspace (BS)
    \\f	ASCII Formfeed (FF)
    \\n	ASCII Linefeed (LF)
    \\N{name}	Character named name in the Unicode database (Unicode only)
    \\r	ASCII Carriage Return (CR)
    \\t	ASCII Horizontal Tab (TAB)
    \\uxxxx	Character with 16-bit hex value xxxx (Unicode only)
    \\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
    \\v	ASCII Vertical Tab (VT)
    \\ooo	Character with octal value ooo
    \\xhh	Character with hex value hh
Extra Credit 2:
Use ''' (triple-single-quote) instead. Can you see why you might use that instead of \"\"\"?
    If you wanted to comment out a section that used the triple double-quotes
    then you might want to use three singles. Or if a string contained three
    consecutive double-quotes or preference
Extra Credit 3:
Combine escape sequences and format strings to create a more complex format.
Extra Credit 4:
Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
"""
