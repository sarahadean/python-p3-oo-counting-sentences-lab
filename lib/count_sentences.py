#!/usr/bin/env python3
# print(dir(str))
# For this lab, you will be creating the MyString class and several methods on the class. 
#You will need to use the self keyword in the body of these methods to refer to the instance of MyString on which the method is being called.

# 1. Create the MyString class and give it a value property. 
#     The class should verify that the value is a string before assigning it. 
#     The default value of value should be the empty string, ''.

# 2. Define an instance method is_sentence()
# returns True if the value ends in a period and False if it does not.
# Hint: You might want to take a look at the list of built in string methods above to see if there's something there that can help you.
class MyString:
    def __init__(self, string='default'):
        self.string = string
    
    def get_string(self):
        return self._string
    
    def set_string(self, string):
        if (isinstance(string, str)):
            self._string = string
        else:
            print("The value must be a string.")

    string = property(get_string, set_string)

#endswith
    def is_sentence(self, string):
        if string.endswith('.'):
            return True
        else:
            return False
        
    def is_exclamation(self, string):
        if string.endswith('!'):
            return True
        else:
            return False
        
    def is_question(self, string):
        if string.endswith('?'):
            return True
        else:
            return False
    #return the number of sentences
    def count_sentences(self, string):
        #split by symbols, create list, len(list)
        # sentence_list = string.split('. ' and '? ' and '! ')
        ends_added = string.replace('?' or '!', '.')
        print(ends_added)
        sentence_list = ends_added.split('.')
        print(sentence_list)
        return len(sentence_list)


ta_da = MyString("ta da")
sentence = MyString("Sentence one. Count two. Peaches, peaches, peaches, peaches, peaches. ")

print(sentence.count_sentences("Sentence one. Count two? Peaches, peaches, peaches, peaches, peaches! "))
#The value must be a string.

# print(ta_da.is_sentence('sentence'))
# False

# print(ta_da.is_sentence("is a sentence."))
#True

