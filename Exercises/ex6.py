#here all %d and %s can be replace by numbers and strings respectfully
x = "There are %d types of people." % 2
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y


print "I said: %r." % x
print "I also said: '%s'." % y

# here %r is replaced by the other variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

a = "Home just got better! %r"
b = "you know right"

print a %  b