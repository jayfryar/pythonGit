# http://learnpythonthehardway.org/book/ex10.html

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'd do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print "*" * 20
print '*' * 21
print '*' * 22
print """\""""
print """\a"""
print "I am 6'2\" tall."   # escape double quote inside string
print 'I am 6\'2" tall.'   # escape single quote inside string

print '*' * 23 

n = 0
while True:
   if n < 1000000:
      for i in ["/", "-", "|", "\\", "|"]:
         print "%s %s\r" % (i,i),

         #print "%s %s\r" % (i,i)
	 # I can not figure out why the comma makes it behave differently
	 # in python 2.7 the comma is to show that the string will be printed on the same line 

   else:
       break
   n += 1
