# assignment of x variable
x = "There are {} types of people.".format(10)
# assignment of binary variable
binary = "binary"
# assignment of do_not variable
do_not = "don't"
# assignment of y variable (includes previous two variables in string)
y = "Those who know {} and those who {}.".format(binary, do_not)
# two print statements
print x
print y
# two more print statements
print "I said: {}.".format(x)
print "I also said: {}.".format(y)
# variable hilarious (has boolean value)
hilarious = False
# another way to return two strings??
joke_evaluation = "Isn't that joke so funny?! %r"
# in reference to the above assignment...
print joke_evaluation % hilarious
# two variables
w = "This is the left side of..."
e = "a string with a right side."
# and finally printed
print w + e