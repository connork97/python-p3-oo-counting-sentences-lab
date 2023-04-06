#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=""):
    self.value = value

  def get_string(self):
    return self._value
  
  def set_string(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_string, set_string)

  def is_sentence(self):
    if (self.value.endswith(".")):
      return True
    else:
      return False
    
  def is_question(self):
    if (self.value.endswith("?")):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if (self.value.endswith("!")):
      return True
    else:
      return False
    
  def count_sentences(self):
    
    sentences = self.value

    for punc in ["!", "?"]:
      sentences = sentences.replace(punc, ".")
    
    sentences_list = [letter for letter in sentences.split(". ") if letter]

    print(sentences_list)
    return len(sentences_list)

      
test = MyString("Test. Test again! Test a third time?")
print(test.count_sentences())