import random 
import string

def pass_gen():
    pass_word = ''.join(random.choices(string.ascii_letters+ string.digits +'+_-*&%$#@',k = random.randint(5,8)))
    return pass_word
pass_words= [pass_gen() for i in range(10)]

for i,pass_word in enumerate(pass_words,1):
    print(f'{i}:{pass_word}')

