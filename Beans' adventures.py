next = "Start" #placeholder variable
path = f"Story/{next}.txt"
file = open(path)
Choices = {}
next = "Start" #next page to open

while True: #until user closes/kills the program,
    path = f"Story/{next}.txt" #sets the next file to be opened to an easier-to-refer-to variable
    count = 0 #resets a counting variable to 0
    Choices.clear() #clears the log of choicecs pulled from the previous document, if applicable


    with open(path) as file: #open file -- this form automatically closes the document when indented code block is completed
        reading = True #variable used to remember when we are done with reading, and must present the user with a choice
        story = True #variable used to remember we are still reading story and outputting to the user
        choosing = False #variable used to remember when we are documenting choices to present to the user

        while (reading == True): #while the program knows it's still reading the document,

            for line in file:  #Each line in the file is iterated through,
                line = line.removesuffix("\n")  #the line is cleared of it's "enter key" stroke at the end, so output is not double-spaced on lines

                if (story == True): #while the program is still reading story to the user,
                    if (line == "*ENDSTORY*"): #if it hits the end of the story,
                        print("Do you:\n") #introduces choices,
                        story = False #stops outputting text and begins documenting choices
                        choosing = True 
                    else:   #if the line is not the endline,
                        print(line) #outputs it

                elif (choosing == True): #if we're choosing, continues reading line-by-line

                    if (line == "*ENDCHOICE*"): #if the line is the end of the choices seciton,
                        print(Choices) #presents the choises to the user
                        reading = False #signals that choices have been presented, and signals to close the page

                    else: #if the line is not *ENDCHOICES*, 
                        line = line.replace(" ", "").split(":") #removes any spaces, and splits it into two items, around (not including) the colon
                        if (len(line) == 2 ): #if there are indeed two items (ie. line was not blank),
                            Choices[line[0]] = line[1] #adds the line's two items to a dictionary
                        
                    
    nextchoice = str(input())  #takes an input and casts it as a string, so it can be compared to the dictionary of choices held
    for i in Choices: #for each entry in the choices dictionary,
        if (i == nextchoice): #if the entry corresponds to the user input,
            next = Choices[i] #sets the corresponding document name as the next page to be opened
    print("\n=============================\n") #once a choice has been made, prints an enter, a line of = symbols, and another enter -- to clear up the flow and make it more obviousn where the page turns
                
                    



