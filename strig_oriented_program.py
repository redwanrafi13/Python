class stringoperator:
    def __init__(self,text):
        self.text=text
        
    def to_upper(self):
        return self.text.upper()
    
    def to_lower(self):
        return self.text.lower()
    
    def reverse(self):
        return self.text [::-1]
    
    def is_palindrome(self):
        return self.text == self.text [::-1]
    
    def count_vowels(self):
        return sum(1 for char in self.text.lower() if char in 'aeiou')
    def replace_word(self,old,new):
        return self.text.replace(old,new)
    
    def find_word(self,word):
        return self.text.find(word)
    
    def word_count(self):
        return len(self.text.split())
    
    def remove_whitespace(self):
        return self.text.strip()
    
    def capitalize_word(self):
        return self.text.title()
    
if __name__ == "__main__":
    sentence=input("enter a sentence:")
    operator=stringoperator(sentence)
    
    print("\n string operations:")
    print("1. uppercase:",operator.to_upper())
    print("2. lowercase:",operator.to_lower())
    print("3. reversed: ",operator.reverse())
    print("4. Is palindrome: ",operator.is_palindrome())
    print("5. vowel count: ",operator.count_vowels())
    print("6. find 'the':",operator.find_word('the'))
    print("7. word count: ",operator.word_count())
    print("8. trimmed: ",operator.remove_whitespace())
    print("9. capitalize word: ",operator.capitalize_word())
    