# write a function that takes as input a string and an integer
# return the string in which each character has been shifted the integer-specified amount in the alphabet

# 'a',1 --> 'b'
# 'abc',1 --> 'bcd'
# 'hello',5 --> 'mjqqt'
# 'a',27 --> 'b'
# 'abc',2 --> 'cde'
# '', 1 --> ''
# 'Abc'1 --> 'Bcd'


def shift(s, n):

    if str(n) == n or int(n) != n:
        return 'Invalid Input'

    if len(s) == 0:
        return ''

    
    d = { 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k':10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    new_str = ''
    
    for i in range(0, len(s)):
        # convert to lower case
        c = s[i].lower()
        
        if c in d:
            # get the shifted position
            position = (d[c] + n) % 26
            
            # check if original is upper case
            if s[i].isupper():
                # if true: make the shifted char upper
                new_str += alpha[position].upper()
            else:
                # else: keep it the same
                new_str += alpha[position]
        else:
            new_str += c
        
    return new_str

print(shift('aaa',0))
print(shift('Abc',1.6))
print(shift(' cvb', "123"))
print(shift('AbC', 5))
print(shift('a', 1))
print(shift('abc', 1))
print(shift('abc', -11))
print(shift('hello', 5))
print(shift('hel#lo#', "a"))
print(shift('(hello)', 8))
print(shift('a', 27))
print(shift('abc', 2))
print(shift('', 1))
print(shift('', '1'))
print(shift('Abc',1))