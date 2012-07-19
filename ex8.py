formatter = "{!r} {!r} {!r} {!r}"

print formatter.format(1,2,3,4)
print formatter.format("one","two","three","four")
print formatter.format(True,False,False,True)
print formatter.format(formatter,formatter,formatter,formatter)
print formatter.format(
       "I had this thing.",
       "That you could type up right.",
       "But it didn't sing.",
       "So I said goodnight." )

"""
Extra Credit 1:
Do your checks of your work, write down your mistakes, try not to make them on the next exercise.
Extra Credit 2:
Notice that the last line of output uses both single and double quotes for individual pieces. Why do you think that is?
    Double quotes are used where a string has a single quote included otherwise single quotes are used
"""
