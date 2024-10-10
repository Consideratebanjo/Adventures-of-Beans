#importing dependancies

import random as rand  #allows dice rolls


#class for an entity/thing, player, monster, etc
class entity:
    
    #creates an entity with average statistics -- skillcheck modifiers will be 0 by default
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
    def skillcheck(stat,dc,modifier=0,die=20,adv=0):
        modifier += (stat-10) // 2  #Converts an entity's stat into a modifier, and adds it to the declared modifier
        roll = rand.randint(0,die) #rolls the first die

        if (adv>0): #if entity makes the check with x advantage,
            for i in adv: #per x,
                roll2 = rand.randint(0,die) #roll another die,
                if (roll2>roll):  #compare the two rolls, and take whichever die is higher
                    roll = roll2
                i+1
        elif (adv<0): # if entity makes check with disadvantage,
            for i in (adv*-1): #per disadvantage,
                roll2 = rand.randint(0,die) #roll another die
            if (roll2<roll): # compare the two rolls, and take whichever die is higher
                    roll = roll2
                i+1
        else: #if no advantage or disadvantage,
            pass #continue without rolling any additional dice

        score = (roll+modifier) #adds modifier to the used die roll into a score

        #if score meets or exceeds the difficulty, return "success" to indicate the entity passes the skill check. Otherwise, indicates the entity fails the check by returning "Failure"
        if (score >= dc): 
            return("Success")
        else:
            return("Failure")
                
