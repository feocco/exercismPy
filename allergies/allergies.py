import math

class Allergies:
    def __init__(self, allScore):
        self.allScore = allScore
        self.possibleAllergies = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
        self.lst = self.getAllergies()


    def getAllergies(self):
        score = self.allScore
        returnList = []

        while score > 0:
            num = int(math.log(score, 2))
            returnList.append(self.possibleAllergies[num])
            score = score % (2 ** num)

        return returnList


    def is_allergic_to(self, item):
        returnList = []
        if item in self.lst:
            return True
        else:
            return False