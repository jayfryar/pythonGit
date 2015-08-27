# http://learnpythonthehardway.org/book/ex39.html

import hashmap

# create a mapping of state to abbreviation
print "\n j  create a mapping of state to abbreviation"
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
print "\n j  create a basic set of states and some cities in them"
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

print '\nfinished setting cities and states $\n' * 2 
#  082315  I tried (google etc,) and could not find where I got printkeys
#	 It is not working so commenting it out
#	 Go to LittleTestForPrintingDictKeys
#  082315  It is all about LISTS!   so of course it has no keys!   
#hashmap.printkeys(states)

# print out some cities
print '-' * 10
print "j  print out some cities"
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "j  print some states"
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "j Do it by using the state then cities dict"
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
print "every state abbreviation"
hashmap.list(states)

# print every city in state
print '-' * 10
print "every city in state"
hashmap.list(cities)

print '-' * 10
# by default ruby says "nil" when something isn't in there
state = hashmap.get(states, 'Texas')

if not state:
  print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

