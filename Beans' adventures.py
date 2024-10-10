import random as rand

class entity:
    def __init__(self, name, strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10):
        self.name = name
        self.str = strength
        self.dex = dexterity
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma

    def skillcheck(skill,dc,modifier=0,die=20,adv=0):
        modifier += (skill-10) // 2
        roll = rand.randint(0,die)

        if (adv>0):
            for i in adv:
                roll2 = rand.randint(0,die)
                if (roll2>roll):
                    roll = roll2
                i+1
        elif (adv<0):
            for i in (adv*-1):
                roll2 = rand.randint(0,die)
                
        if (roll2<roll):
                    roll = roll2
                i+1
        else:
            pass 
        if (roll < dc):
            return("Fail")
        else:
            return("Success")
                
