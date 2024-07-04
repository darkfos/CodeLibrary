"""
    Write a class that, when given a string, will return an uppercase
    string with each letter shifted forward in the alphabet by however
    many spots the cipher was initialized to.
    
    If something in the string is not in the alphabet (e.g. punctuation, spaces),
    simply leave it as is.
    The shift will always be in range of [1, 26].
"""


class CaesarCipher(object):
    #5 kyu

    def __init__(self, shift):
        self.shift: int = shift
        self.alfa_string: list[str] = [chr(i) for i in range(97, 123)]

    def encode(self, st):

        new_st: str = ""

        for ch in st.lower():
            
            if ch not in self.alfa_string:
                new_st += ch
            else:
                indx: int = self.alfa_string.index(ch)
                new_indx: int = (indx + self.shift) % len(self.alfa_string)
                new_st += self.alfa_string[new_indx]
        return new_st.upper()
        
    def decode(self, st):
        
        new_st: str = ""

        for ch in st.lower():
            
            if ch not in self.alfa_string:
                new_st += ch
            else:
                indx = self.alfa_string.index(ch)
                new_indx: int = (indx - self.shift) % len(self.alfa_string)
                new_st += self.alfa_string[new_indx]
        return new_st.upper()