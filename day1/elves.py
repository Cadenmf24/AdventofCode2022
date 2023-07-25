class Elf:
    def __init__(self, name, pouch):
        total = 0
        self.name = name
        self.pouch = pouch
        
        for i in pouch:
            total += i

        self.total = total


    def getName(self):
        return self.name
    
    def getPouch(self):
        return self.pouch
    
    def getTotal(self):
        return self.total
    
    def setPouch(self, list):
        self.pouch = list

        return True

    def setName(self, name):
        self.name = name

        return True 

    

    def compare(self, party):

        highestCalorie = 0
        highestElf = ''

        for elf in party:

            if elf.total > highestCalorie:
                highestCalorie = elf.total
                highestElf = elf.name

        return (highestElf, highestCalorie)


