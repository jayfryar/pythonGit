##  http://learnpythonthehardway.org/book/ex39.html

# create a mapping of children to initials
children = { 
   'James Taylor Fryar': 'JTF',
   'Elmer Lee Fryar': 'ELF',
   'David Lawrence Fryar': 'DLF',
   'Judith Diane Fryar Keel': 'JDFK',
   'William Ralph Fryar': 'WRF',
   'Donie Lynn Fryar Upchurch': 'DLFU'
}

# create a basic set of children and some of their own children
grandkids = {
   'JTF': 'Caroline Morgan Fryar',
   'DLF': 'Laura Michelle Fryar',
   'WRF': 'Dustin Fryar'
}

# add some more grandkids
grandkids['DLFU'] = 'Tamara Upchurch'
grandkids['JDFK'] = 'Brian Keel'
grandkids['ELF'] = "NoOneThatWeKnowOf"


# print out some grandkids
print '-' * 10
print "JTF has: ", grandkids['JTF']
print "WRF has: ", grandkids['WRF']

# print some children
print '-' * 10
print "Judy's initials are: ", children['Judith Diane Fryar Keel']
print "Donie's initials are: ", children['Donie Lynn Fryar Upchurch']

# do it by using the children then grandkids dict
print '-' * 10
print "David has: ", grandkids[children['David Lawrence Fryar']]
print "James has: ", grandkids[children['James Taylor Fryar']]

#print every child's initials
print '-' * 10
for child, initials in children.items():
   print "%s has initials %s" % (child, initials)

#print every grandchild for children 
print '-' * 10
for child, gchild in grandkids.items():
   print "%s has the gchild %s" % (child, gchild)

# now do both at the same time
print '-' * 10
for child, initials in children.items():
   print "%s child has initials %s and has grandchild %s" % (
      child, initials, grandkids[initials])

print '-' * 10
# safely get a initials by child that might not be there
child = children.get('Junk', None)

if not child:
   print "Sorry, no Junk."

# get a city with a default value
child = children.get('Junk', 'Does Not Exist')
print "The grandchild for the child 'Junk' is: %s" % child













