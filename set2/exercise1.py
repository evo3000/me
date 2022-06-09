"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#This defines the some_words as a list with 6 items
some_words = ["what", "does", "this", "line", "do", "?"] #its defined some_words for the following script

#this prints a word (word, word, word..) in some_words list in succession 
for word in some_words:
    print(word) #words were printed in order 

#this prints a word denoted in number x (0, 1, 2, 3, 4, 5, 6) down the list in some_words list in succession 
for x in some_words:
    print(x)

#this prints the some_words list 
print(some_words)

#length of some_words is 6 so it is larger than 3 so "some_words contains more than 3 words" is printed
if len(some_words) > 3:
    print("some_words contains more than 3 words")

#the following prints info about my machine. Did I get hacked??
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
