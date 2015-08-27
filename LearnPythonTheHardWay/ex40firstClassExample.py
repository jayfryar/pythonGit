
# http://learnpythonthehardway.org/book/ex40.html

class Song(object):
   # Python looks to see if you made a "magic" __init__ function, and if 
   # you have it calls that function to initialize your newly created 
   # empty object.
   
   # In the function __init__ you then get this extra variable self, 
   # which is that empty object Python made, and you can set 
   # variables on it just like you would with a module, dictionary, or 
   # other object.

   def __init__(self, lyrics):
      self.lyrics = lyrics

   def sing_me_a_song(self):
      for line in self.lyrics:
	 print line


happy_bday = Song(["Happy birthday to you",
		   "I don't want to get sued",
		   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
			"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

