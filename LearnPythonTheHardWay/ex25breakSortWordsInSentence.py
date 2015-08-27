import ex25def
# http://learnpythonthehardway.org/book/ex25.html

theSentence = "All good things come to those who wait."
words = ex25def.break_words(theSentence)
print "words: %s" % words
  
sorted_words = ex25def.sort_words(words)
print "sorted words: %s\n" % sorted_words

print "First and Last words: "
ex25def.print_first_word(words)
ex25def.print_last_word(words)
print "\nwords after popping: %s\n" % words
print "First and Last sorted words: "
ex25def.print_first_word(sorted_words)
ex25def.print_last_word(sorted_words)
print "sorted words after popping: %s\n" % sorted_words
print "\n"
ex25def.print_first_and_last(theSentence)
ex25def.print_first_and_last_sorted(theSentence)

