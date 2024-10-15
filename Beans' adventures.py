#========= importing dependancies

import random as rand  #allows dice rolls


#========= defining subroutines & classes

def roll(die=20):  #rolls a die of author-declared faces, or 20 by default
    return(rand.randint(1,die))

class Entity:  #class for an entity/thing; player, monster, etc

    
    #creates an entity with (by default) average statistics -- skillcheck modifiers will be 0 by default
    def __init__(self, name, strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10):
        # a name and the 6 core stats used in most dnd-esque systems -- this will hopefully change in future, allowing authors to declare their own stats
        self.name = name
        self.str = strength
        self.dex = dexterity
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma

    # Takes an entity's statistic and a "difficulty class", allowing for a declared modifier, rolls a die (20-sided by default, but changeable) and allows for advantage/disadvantage
    def skillcheck(self,stat,dc,modifier=0,die=20,adv=0):
        modifier += (stat-10) // 2  #Converts an entity's stat into a modifier, and adds it to the declared modifier
        dieroll = roll(die) #rolls the first die

        if (adv>0): #if entity makes the check with advantage,
            for i in adv: #per level of advantage,
                dieroll2 = roll(die) #roll another die,
                if (dieroll2>dieroll):  #compare the two rolls, and take whichever die is higher
                    dieroll = dieroll2
        elif (adv<0): # if entity makes check with disadvantage,
            for i in (adv*-1): #per level of disadvantage,
                dieroll2 = roll(die) #roll another die
            if (dieroll2<dieroll): # compare the two rolls, and take whichever is higher
                    dieroll = dieroll2

        else: #if no advantage or disadvantage,
            pass #continue without rolling any additional dice

        score = (dieroll+modifier) #adds modifier to the used die roll into a score

        #if score meets or exceeds the difficulty, return "success" to indicate the entity passes the skill check. Otherwise, indicates the entity fails the check by returning "Failure"
        if (score >= dc): 
            return("Success")
        else:
            return("Failure")


#========== Placeholder or WIP testing

next = "Start" #placeholder variable
path = f"Story/{next}.txt"


while True:
    file = open(path)
    print(file.read())
    foundchoices=False
    while (foundchoices==False):
        choicesline=1
        if (file.readline(-choicesline) == "*ENDSTORY*"):
            foundchoices=True
        else:
            choicesline+=1

    nextchoice = int(input(print("make your selection:")))
    for i in choicesline:
        choice = file.readline(-i)
        for g in length(choice):
            if (file.readline(-i)[g] == nextchoice):
                next = (f"{file.readline(-i)[g]}"-f"{-i}: ")
