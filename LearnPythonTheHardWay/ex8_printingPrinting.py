
# http://learnpythonthehardway.org/book/ex8.html

r_formatter = "%r %r %r %r"

print r_formatter % (1, 2, 3, 5)
print r_formatter % ('one', 'two', 'three', 'four')
print r_formatter % (True, False, False, True)
print r_formatter % ('True', 'False', 'False', 'True')

print r_formatter % (r_formatter, r_formatter, r_formatter, r_formatter)
print r_formatter % (
   "I had this thing.",
   "That you could type up right.",
   "But it didn't sing.",
   'So I said good night.'
)




