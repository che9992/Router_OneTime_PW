import random, string

class CreatePasswd:
    rnd = random.SystemRandom()
    alphabet = string.ascii_lowercase
    vowels = 'aeiou'

    def make_word_pw(self, leng = 4):
        consonants = ''.join([x for x in CreatePasswd.alphabet if x not in CreatePasswd.vowels])
        pwd = ''.join([CreatePasswd.rnd.choice(consonants) + CreatePasswd.rnd.choice(CreatePasswd.vowels) for i in range(leng)]).title()
        return pwd

    def random_in_len(self,pwd):
        leng = len(pwd)
        number = str(CreatePasswd.rnd.choice(range(0,leng)))
        return number

    def random_special(self):
        special = ['!', '?', '@', '*', '#', '&', '$', '%', '+', '%', '^^']
        cho = CreatePasswd.rnd.choice(special)
        return cho

    def make_hard_pw(self):
        sour1= self.make_word_pw(2)
        sour2 = self.make_word_pw(3)
        sour1 = sour1.join([self.random_in_len(sour1),self.random_special()])
        sour2 = sour2.join([self.random_in_len(sour2), self.random_special()])
        pwd = sour1+sour2
        pwd = pwd[0:13]
        return pwd


    def __init__(self):
        self.new = self.make_word_pw()
        self.hard = self.make_hard_pw()
        if len(self.new) < 8:
            self.new = self.make_hard_pw()



c = CreatePasswd()
print(c.hard)