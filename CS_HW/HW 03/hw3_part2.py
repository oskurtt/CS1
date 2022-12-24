# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:57:19 2021

@author: Oscar
"""

def battle (poketurns, i, ls, direction, name, record):
    if (i % poketurns == 0 and i != 0):
        print ("Turn {0}, {1} at ({2}, {3})".format(i, name, min(max(ls[0], 0), 150), min(max(ls[1], 0), 150))) 
        poketype = input ("What type of pokemon do you meet (W)ater, (G)round? => ")
        print (poketype)
        if (poketype == 'w' or poketype == 'W'):
            record.append("Win")
            if (direction == 'n' or direction == 'N'):
                ls[0]-= 1
                ls[0] = min(max(ls[0], 0), 150)
                print ("{2} wins and moves to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name))
            elif (direction == 's' or direction == 'S'):
                ls[0]+= 1
                ls[0] = min(max(ls[0], 0), 150)
                print ("{2} wins and moves to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name))
            elif (direction == 'e' or direction == 'E'):
                ls[1]+= 1
                ls[1] = min(max(ls[1], 0), 150)
                print ("{2} wins and moves to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name))
            elif (direction == 'w' or direction == 'W'):
                ls[1]-= 1
                ls[1] = min(max(ls[1], 0), 150)
                print ("{2} wins and moves to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name))
            else:
                print (("{2} wins and moves to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name)))
        elif (poketype == 'g' or poketype == 'G'):
            record.append("Lose")
            if (direction == 'n' or direction == 'N'):
                ls[0]+= 10
                print ("{2} runs away to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name))
            elif (direction == 's' or direction == 'S'):
                ls[0]-= 10
                print ("{2} runs away to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name))
            elif (direction == 'e' or direction == 'E'):
                ls[1]-= 10
                print ("{2} runs away to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name))
            elif (direction == 'w' or direction == 'W'):
                ls[1]+= 10
                print ("{2} runs away to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name))
            else:
                print (("{2} runs away to ({0}, {1})".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), name)))
        else:
            record.append("No Pokemon")
        

def move_pokemon (coord):       
    record = []
    turns = int(input("How many turns? => "))
    print (turns)
    name = (input ("What is the name of your pikachu? => "))
    print (name)
    poketurns = int(input("How often do we see a Pokemon (turns)? => "))
    print (poketurns, "\n")
    ls = [coord[0], coord[1]]
    i = 1
    print ("Starting simulation, turn 0 {} at (75, 75)".format(name))
    while i <= turns:  
        
        direction = input ("What direction does {0} walk? => ".format(name))
        print(direction)
        
        if (direction == 'n' or direction == 'N'):
            ls[0] = ls[0] - 5
            ls[0] = min(max(ls[0], 0), 150)
            battle(poketurns, i, ls, direction, name, record)
            i += 1
        elif (direction == 's' or direction == 'S'):
            ls[0] = ls[0] + 5
            ls[0] = min(max(ls[0], 0), 150)
            battle(poketurns, i, ls, direction, name, record)
            i += 1
        elif (direction == 'e' or direction == 'E'):
            ls[1] = ls[1] + 5
            ls[1] = min(max(ls[1], 0), 150)
            battle(poketurns, i, ls, direction, name, record)
            i += 1
        elif (direction == 'w' or direction == 'W'):
            ls[1] = ls[1] - 5
            ls[1] = min(max(ls[1], 0), 150)
            battle(poketurns, i, ls, direction, name, record)
            i += 1
        else:
            ls[0] += 0
            ls[1] += 0
            battle(poketurns, i, ls, direction, name, record)
            i += 1
        
    return ("{3} ends up at ({0}, {1}), Record: {2}".format(min(max(ls[0], 0), 150), min(max(ls[1], 0), 150), record, name))


row = 75
column = 75
print (move_pokemon((row,column)))
# print (move_pokemon((row,column), 'E', 20))
# print (move_pokemon((row,column), 'S', 20)) 
# print (move_pokemon((row,column), 'W', 20)) i%2 = 0