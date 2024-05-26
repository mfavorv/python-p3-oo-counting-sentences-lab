#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
        self._value = value
    
  def get_value(self):
        return self._value
    
  def set_value(self, stringVal):
        if isinstance(stringVal, str):
            self._value = stringVal
        else:
            print("The value must be a string.")

  value = property(get_value, set_value)

  def test_value_string(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self.value = new_value

       
  def is_sentence(self):
    if self.value.endswith("."):
       return True
    else:
        return False
  
  def is_question(self):
     if self.value.endswith("?"):
       return True
     else:
        return False
    
  def is_exclamation(self):
     if self.value.endswith("!"):
       return True
     else:
        return False
     
  def count_sentences(self):
    
    potential_sentences = self.value.replace("?", ".").replace("!", ".")

    sentences = potential_sentences.split(".")
    count = 0

    for sentence in sentences:     
        if sentence and sentence != ".":
            count += 1

    return count
  
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
string.count_sentences()
pass
