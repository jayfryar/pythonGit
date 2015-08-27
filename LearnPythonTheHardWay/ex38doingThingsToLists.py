#  http://learnpythonthehardway.org/book/ex38.html

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list.   Let's fixt that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
   next_one = more_stuff.pop()
   print "Adding: ", next_one
   stuff.append(next_one)
   print "There are %d itens now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print "stuff[1]: %s\n" % stuff[1]

print "stuff[-1]: %s\n" % stuff[-1]

print "stuff.pop(): %s\n" % stuff.pop()

print "' '.join(stuff): %s\n" % ' '.join(stuff)

print "' HH '.join(stuff): %s\n" % ' HH '.join(stuff)

print "'#'.join(stuff)[3:5]: %s\n" % '#'.join(stuff[3:5])

print '#'.join(stuff[3:5])
