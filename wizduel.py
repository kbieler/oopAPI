###Wizards' Duel###
#info from HP API: call by character name for:
    #name (str)
    #house (str)
    #patronus (str)
    #wand {dict of wand wood, core and length}

#Class 1 - Wizards (Characters for Vs)
#user will be able to add 2 characters to compete against each other: player and opponent
    #attributes: (see above)
    #methods: select spell, cast spell, cast patronus(if char does not have one, action fails)
#Class 2 - Spells
#info added by me from HP Wiki (5-7 spells)
    #attributes: name, description, type
    #methods:
        #power_spell - points given in relation to type of spell and wizard house
        #wand_power - points given in relation to wizard wand core
#Class 3 - Main
#driver code for beginning play
    #give instructions for game
    #-select characters to duel, first player then opponent
    #-select which char to play as
        #then user can select and cast spell 
        #cast spell starts funct for wand_power and spell_power, totals added
    #other character's spell is randomly selected and auto cast
    #winner is determined by highest points from spell cast
    #play again y/n?

import requests as r

import random

request = r.get('http://hp-api.herokuapp.com/api/characters')
if request.status_code == 200:
    request = request.json()

#for i in range(23):
   #print(request[i]['name'])

wiz_opt = ['Harry Potter','Hermione Granger','Ron Weasley','Draco Malfoy','Minerva McGonagall','Cedric Diggory',
'Cho Chang','Severus Snape','Rubeus Hagrid','Neville Longbottom','Luna Lovegood','Ginny Weasley','Sirius Black',
'Remus Lupin','Arthur Weasley','Bellatrix Lestrange','Lord Voldemort','Horace Slughorn','Kingsley Shacklebolt',
'Dolores Umbridge','Lucius Malfoy','Vincent Crabbe','Gregory Goyle']

wd1 = {}
wd2 = {}


class Wizards:
    def __init__(self, d):
        self.name = d['name']
        self.house = d['house']
        self.patronus = d['patronus']
        self.wand = d['wand']


    
def select_wiz():
    print(wiz_opt)
    name = input('\nPlease select a wizard from the provided list to be your player. ')
    if name.title() not in wiz_opt:
        print('Your selection is not valid. ')
        select_wiz()
    else:
        w = wiz_opt.index(name.title())
        getWiz1(w)
        return Wizards(wd1)

    
def getWiz1(x):
    data = r.get(f'http://hp-api.herokuapp.com/api/characters')
    if data.status_code == 200:
        data = data.json()
        my_wiz = data[x]
        wd1.update({'name': [my_wiz['name']],'house': [my_wiz['house']],'patronus': [my_wiz['patronus']],'wand': [my_wiz['wand']]})
        print(f"{data[x]['name']} was added to your wizard selections!\n")
        getWiz2()
        return Wizards(wd2)
        
        
                  
def getWiz2():
    choice2 = input('Please select another wizard from the list to be your opponent. ')
    if choice2.title() not in wiz_opt:
        print('Your selection is not valid. ')
        getWiz2()
    else:
        data = r.get(f'http://hp-api.herokuapp.com/api/characters')
        if data.status_code == 200:
            data = data.json()
            x = wiz_opt.index(choice2.title())
            my_wiz = data[x]
            wd2.update({'name': [my_wiz['name']],'house': [my_wiz['house']],'patronus': [my_wiz['patronus']],'wand': [my_wiz['wand']]})
            print(f"{data[x]['name']} was added to your wizard selections! ")
            print('Thank you. Your selection is complete.')
            prep_duel()
            

player = Wizards(wd1)
opponent = Wizards(wd2)


class Spells:
    def __init__(self, name, desc, category):
        self.name = name
        self.desc = desc
        self.category = category
        
        
    def power_spell(self, wz):
        
        if wz.house == ['Gryffindor']:
            if self.category == 'jinx':
                pow_points = random.randint(25, 100)
            elif self.category == 'transfiguration':
                pow_points = random.randint(20, 95)
            elif self.category == 'hex':
                pow_points = random.randint(15, 90)
            elif self.category == 'curse':
                pow_points = random.randint(10, 85)
            else:
                pow_points = random.randint(5, 80)
            return pow_points
       
        
        elif wz.house == ['Slytherin']:
            if self.category == 'curse':
                pow_points = random.randint(25, 100)
            elif self.category == 'hex':
                pow_points = random.randint(20, 95)
            elif self.category == 'charm':
                pow_points = random.randint(15, 90)
            elif self.category == 'jinx':
                pow_points = random.randint(10, 85)
            else:
                pow_points = random.randint(5, 80)
            return pow_points
        
        elif wz.house == ['Hufflepuff']:
            if self.category == 'charm':
                pow_points = random.randint(25, 100)
            elif self.category == 'jinx':
                pow_points = random.randint(20, 95)
            elif self.category == 'transfiguration':
                pow_points = random.randint(15, 90)
            elif self.category == 'hex':
                pow_points = random.randint(10, 85)
            else:
                pow_points = random.randint(5, 80)
            return pow_points
        
        elif wz.house == ['Ravenclaw']:
            if self.category == 'transfiguration':
                pow_points = random.randint(25, 100)
            elif self.category == 'charm':
                pow_points = random.randint(20, 95)
            elif self.category == 'jinx':
                pow_points = random.randint(15, 90)
            elif self.category == 'curse':
                pow_points = random.randint(10, 85)
            else:
                pow_points = random.randint(5, 80)
            return pow_points
        
        
aa = Spells('alarte ascendare', 'shoots the target high into the air', 'charm')
imd = Spells('impedimenta', 'slows movement of the target', 'hex')
flp = Spells('flipendo', 'knock opponent over', 'jinx')
inc = Spells('incarcerous', 'conjures ropes or chains around opponent', 'transfiguration')
ptr = Spells('petrificus totalus', 'instantly paralyze opponent', 'curse')
con = Spells('confundo', 'causes target to be confused', 'charm')
        
spell_list = [aa, imd, flp, inc, ptr, con]


def cast_spell(s):
    print("Wands at the ready! Here we go! ")
    wp1 = (wand_power(player))
    ps1 = (s.power_spell(player))
    wp2 = (wand_power(opponent))
    x = random.choice(spell_list)
    ps2 = (x.power_spell(opponent))
    duel()

def wand_power(wz):
    if (wz.wand[0]['core']) == 'phoenix feather':
        w_pow = random.randint(30, 100)
    elif (wz.wand[0]['core']) == 'dragon heartstring':
        w_pow = random.randint(25, 95)
    elif (wz.wand[0]['core']) == 'unicorn tail-hair':
        w_pow = random.randint(20, 90)
    else:
        w_pow = random.randint(15, 85)
    return w_pow


def duel():
    player_pow = ps1 + wp1
    opponent_pow = ps2 + wp2
    if player_pow == opponent_pow:
        print("It's a draw! Prepare another spell. ")
    elif player_pow > opponent_pow:
        print(f"{player.name} won the duel! You are the winner!\n")
        reply = input("Would you like to play again? (y/n) ")
        if reply.lower() == 'y':
            new = input("Would you like to duel with the same player and opponent? (y/n) ")
            if new.lower() == 'y':
                prep_duel()
            else:
                select_wiz()
        else:
            print("Thank you for playing Wizards' Duel! Cheers!") 
    else:
        print(f"Oh no! {opponent.name} bested {player.name}. You lost the duel.\n")
        again = input("Would you like to play again? (y/n) ")
        if again.lower() == 'y':
            same = input("Would you like to duel with the same player and opponent? (y/n) ")
            if same.lower() == 'y':
                prep_duel()
            else:
                select_wiz()
        else:
            print("Thank you for playing Wizards' Duel! Cheers!")


def prep_duel():
    print(f"Wizards' Duel: {player.name} vs. {opponent.name} is about to begin!\n")
    print('Prepare for your duel by selecting a spell from the following list: \n')
    print("[a] Alarte Ascendare: (charm) Shoots the target high into the air.\
    [b] Impedimenta: (hex) Slows movement of the target. \
    [c] Flipendo: (jinx) Knock opponent over. \
    [d] Incarcerous: (transfiguration) Conjures ropes or chains around opponent. \
    [e] Petrificus Totalus: (curse) Instantly paralyze opponent. \
    [f] Confundo: (charm) Causes target to be confused. \n")
    choice = input("Which spell would you like to cast? a, b, c, d, e, or f? ")
    if choice.lower() == 'a':
        spell = spell_list[0]
        cast_spell(spell)
    elif choice.lower() == 'b':
        spell = spell_list[1]
        cast_spell(spell)
    elif choice.lower() == 'c':
        spell = spell_list[2]
        cast_spell(spell)
    elif choice.lower() == 'd':
        spell = spell_list[3]
        cast_spell(spell)
    elif choice.lower() == 'e':
        spell = spell_list[4]
        cast_spell(spell)
    elif choice.lower() == 'f':
        spell = spell_list[5]
        cast_spell(spell)
    else:
        print('Invalid selection.')
        prep_duel()
        
    
    
def start_game():
    print("Welcome to the Wizards' Duel game!\
    You will be asked to select two wizards from the list below.\
    Your first choice will be the wizard you control. \
    Your second choice will be the wizard you duel.\
    After making your selections, you will be able to choose a spell to cast. \
    When you cast your spell, your opponent will cast theirs as well. \
    The spell cast with the most power wins!\n")
    ready = input("Ready to play? (y/n) ")
    if ready.lower() == 'y':
        select_wiz()
    else:
        print("No worries! Goodbye!")
 

start_game()