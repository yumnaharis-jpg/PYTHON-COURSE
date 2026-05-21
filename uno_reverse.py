class Reversal:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]          

word = input("Enter a word to reverse: ")
reversal = Reversal(word)
print(reversal.reverse())







