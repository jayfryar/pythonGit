
# http://learnpythonthehardway.org/book/ex11.html'

# 110814  Ran fine with python!!

# 110714  I ran it using jython with raw_input and it hung up after the first question and after I hit return...
# 110714  I then ran it using jython with input and it hung up after the first question and after I hit return...


#  Found this:
#  http://python.6.x6.nabble.com/input-not-working-on-Windows-td4987455.html




#  $ jython temp.py
(2, 5, 3, 'final', 0)
#  import sys
#  print sys.version_info

# even this did not work.
# http://stackoverflow.com/questions/17211118/issue-with-accepting-user-inputs-in-jython-script
#import sys
#if sys.hexversion < 0x3000000:
#   input = raw_input



# and hell no, this did not work either with jython but did with python.

def input(prompt):
   return eval( raw_input(prompt))

#
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
#print "How much do you weight?",
#weight = raw_input()
weight = input("How much do you weight?")
#
print "So, you're %r old, %r tall and %r heavy." % (
   age, height, weight      )




# even this does not work.
# http://www.jython.org/jythonbook/en/1.0/InputOutput.html
#import sys
#fav_team = sys.stdin.readline()
#sys.stdout.write(" fav team: %s" % fav_team)





