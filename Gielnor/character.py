import numpy as np
import random

class me(object):
    def __init__(self):
        self.name = "Lou Tenant"
        self.age = 42.0
        self.hairColor = "blue"
        self.scars = None
        self.tattoos = {
            'Left Leg Sleeve full of Gielinor Items':
                ['whole black demon', 'brutal blue dragon' , 'hell hound' , 'mud runes' ]
        }
        self.handicaps = 'color-blind'
        self.clothes = ['kraken shirts' , 'fishing' ]
        self.retirement = 'hang out at the dcosk at Port Sarim'
        self.catchPhrase = 'I do it for gnomes'
        self.outlook = 'Peseemistic'
        self.personality = 'extroverted' # outgoing
        self.badHabits = 'Mort Myre Mushrooms'
        self.lol = ['']
        self.seenByOthers = ['Strong' , 'Rich' , 'Humble' , 'Relatable']
        self.seeHimself = ['Weak' , 'Just moved out from his parents house' ]
        self.bestTraits = ['Sneaky'  ]
        self.worstTraits = ['Not the best at the Gnome Stronghold Agility Course']
        self.competive = 7/10
        self.judge = 'Time to consider others actions'
        self.fears = ['Wilderness']
        self.philosophy = 'Live strong, be happy, dont get testicle cancer -Lance Armstrong'
        self.cried = 'Went to sneak to Troll Stronghold to get some goutweed and the troll hit him with a rock.'
        self.lust = 'Psychonaut'
        self.topSense = 'Vision'
        self.valuesInAFriend= ['Helpful' , 'Being There' ]
        self.familySize = 4
        self.mom = 'Amanda Mount (Tenant)'
        self.dad = 'Howie Tenant'
        self.sister = 'Sharon Tenant'
        self.friends = ['Harry Dong' , 'Dill Doe Jr.']
        self.raisedNeglected = True
        self.adviceForYoungerSelf = 'Do more agility'
        self.bestChildMemory = ''
        self.worstChildMemory = 'Battle of Khazard'
        self.respondToThreat = 'Fight with words unless needed to fight with violence'
        self.cryptonite = 'Taking an arrow to the knee'
        self.perseptionStrangers = 'Different but Interested'
        self.choiceOfWeapon = 'Bow'
        self.inPockets = ['Lockpick' , 'Lint' , 'Swamp Toad']
        self.religiousViews = 'Zaros'
        self.reincarnation = 'Kraken'
        self.howILikeToDie = 'Drowning'
        self.viewOfFreedom = 'Being able to raid whatever you want'
        self.viewOfLying = 'Whatever it takes'
        self.minimallist = True
        self.halloweenCostume = 'Back portion of the horse costume'
        self.saveOfPersonWhoWouldItBe = 'Nieve'
        self.whyNeverKill = None
        self.thingsWontDo = 'Kill Fellow Gnomes'
        self.believeInHappyEndings = True
        self.startingSkills = self.setupSkills()
        self.modifiers = self.modifiers()


    def setupSkills(self):
        self.attack = 11 + 6
        self.strength = 2
        self.defence = 16
        self.range = 10
        self.prayer = 6
        self.magic = 1 + 10
        self.runecrafting = 16
        self.construction = 18
        self.health = 16
        self.agility = 13 + 5
        self.herblore = 8
        self.theiving = 13 + 15
        self.crafting = 13 + 5
        self.fletching = 15
        self.slayer = 18
        self.hunting = 7
        self.mining = 9+11
        self.smithing = 8+12
        self.fishing = 2+9
        self.cooking = 11+17
        self.firemaking = 15+15
        self.woodcutting = 3+13
        self.farming = 13+15

        self.all = np.array([self.attack , self.strength , self.defence , self.range , self.prayer , self.magic , self.runecrafting ,\
            self.construction , self.health , self.agility , self.herblore , self.theiving , self.crafting , self.fletching ,\
                self.slayer , self.hunting , self.mining , self.smithing , self.fishing , self.fishing , self.cooking , self.firemaking ,\
                    self.woodcutting , self.farming ] )
        self.total = self.all.sum()

    def modifiers(self):
        self.attack_m = self.attack * 0.1
        self.strength_m = self.strength *0.1
        self.range_m    = self.range  *0.1
        self.magic_m    = self.magic *0.1
        self.defence_m  = self.defence  *0.1
        
    def roll(self, number):
        return random.randint( 1 , number ) 










        

    

