import math
import unicodedata
class SP_TO_WR:
    def __init__(self,inp):
        self.raw_input = inp
        self.output = ""
        self.raw_output = []
        self.multiples = {"single":1,"double":2, "triple":3,"quadruple":4,"quintuple":5}
        self.numbers = {"zero": 0,
                        "one" : 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "ten": 10,
                        "twenty": 20,
                        "thirty": 30,
                        "forty": 40,
                        "fifty": 50,
                        "sixty": 60,
                        "seventy": 70,
                        "eighty": 80,
                        "ninety": 90,
                        "hundred": 100}
        self.abbr = {"dollars":"$","dollar":"$","rupees":u"\u20B9","rupee":u"\u20B9","euros":unicodedata.lookup("EURO SIGN"),"euro":unicodedata.lookup("EURO SIGN")}

    def convert(self):
        print("This is the given input: \n", self.raw_input)
        S = self.raw_input.split()
        N = len(S)
        i = 0
        print(S)
        while(i < N):
            if i+1 < N:
                if S[i].lower() in self.multiples.keys() and len(S[i+1]) == 1:
                    self.output += S[i+1]*self.multiples[S[i]]
                    i+=2
                elif S[i].lower() in self.numbers.keys() and S[i+1] in self.abbr.keys():
                    self.output += self.abbr[S[i+1]] + str(self.numbers[S[i]])
                    i += 2
                elif S[i].lower() in self.numbers.keys():
                    self.output += str(self.numbers[S[i]])
                    i += 1
                elif len(S[i]) == 1 and len(S[i+1]) == 1:
                    self.output += S[i] + S[i+1]
                    i += 2
                else:
                    self.output += S[i]
                    i+=1
            else:
                if i == N-1:
                    self.output += S[i]
                    break
            self.output += " "
        return self.output

    def printOP(self):
        print("This is the produced input: \n", self.output)





###Testing
# inp = "Hello I have three dollars to buy two mangoes of triple A type to offer to C M at eight P M"
# converter = SP_TO_WR(inp)
# op = converter.convert()
# converter.printOP()

