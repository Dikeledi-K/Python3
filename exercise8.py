# Printing, printing

formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Let me",
"not to",
"the marriage",
"of true minds"
))

"""
In this exercise I am using something called a function to turn the formatter variable into other strings.
When you see me write formatter.format(...) I am telling python to do the following:
1.Take the formatter string deﬁned on line 1.
2.Call its format function, which is similar to telling it to do a command line command named
format.
3.
Pass to format four arguments, which match up with the four {}s in the formatter variable.
This is like passing arguments to the command line command format.
4.
The result of calling format on formatter is a new string that has the {} replaced with the
four variables. This is what print is now printing out.
"""