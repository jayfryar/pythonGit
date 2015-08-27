# http://learnpythonthehardway.org/book/ex6.html

x	 =  "There are %d types of people."  % 10
binary	 =  "binary"
do_not	 =  "don't"
y	 =  "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "\nI said rr:      '%r'"  % x
print "I said ss:      '%s'"  % x
print "\nI also said: '%s'"  % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e

print """
%s invokes str(), whereas %r invokes repr(). 
"""
