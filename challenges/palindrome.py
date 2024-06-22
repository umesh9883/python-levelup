def is_palindrome(sentence):
    charlist= [x for x in sentence]
    if charlist == charlist[::-1]:
        return True
    

is_palindrome("malayalam")