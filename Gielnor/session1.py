from character import me
import random

lou = me()

class item(object):
    def __init__(self , names = None , description = None):
        self.name = names
        self.description = description



x1 = 'Drinking with the gnomes, black out.'

x2 = 'Wake up in a field, go to river notice its flowing north to south. Go north to house. Man says I was somewhere outside varrock'
lou.money = 0
lou.inventory = [item(names = 'frog') , item('Unknown Block')]

x3 = 'Go to Varrock bank and start a bank account.'
x4 = 'Go arround Varrock and notice there is food/weapon shops. Little Pedestrians. Its around 10am. Small market ~10 people'
x5 = 'Try to get some food in blue moon inn. Bread, tuna, Ale. ~2gp, 5gp, 2gp. Do you know of where there is work? He said posting in Varrock square. Or Slayer. Go West then North to Edgeville.'
x6 = 'Check posting in Varrock Square. Hear the king argueing, "alright robert" then asks if I needed some work. I say Yes! Someone wants me to check in on someone.'
x7 = 'Check on the the monasary to the east. Dont have much to spare. Check the posting and see someone is looking for unicorn horn. Someone looking for bear pelt.'
x8 = 'Ask guards where mining is at? Yeah its south east and on south west.'
x9 = 'Go South to the mines. It is approximately 4 pm. Go to south west mines find a bronze pickaxe with a a roll of 11 and got 10 strength to pull the axe out'
x10 = 'Mine some iron and copper and tin. Mine 4 iron. 3 copper. 3 tin. About 6pm.'
x11 = 'Go to the monostary. Find some rats to the northeast. rolled initiative of 9. The rats attack first'

lou.health - 2 - 6

x12 = 'Rats hit half my hp so I run South and get away.'
x13 = 'Hold 24 inventory. Ask one of guards to see if I can sell some iron. Head to chainmail shop. Its closed so Ill head south to take a nap '
x14 = 'Find the a mound outside camp there. build a nice shelter. About midnight to get everything setup. Get through the night without any trouble'
x15 = 'Wake up at 6am. See a glowing blue mushroom and grab it. Ask guards what is North/South of Varrock'

lou.health = me().health

lou.inventory.append('Blue Glowing Mushroom')

x16 = 'They tell me there are farms and champions guild desert to the south. The wilderness is north.'
x17 = 'I head to chainmail shop and ask If I can trade for Iron. I sell him all my iron ore for 180 gp'

lou.money += 180

x18 = 'Go to leather shop to ask if I can buy any armour. I purchase the leather body for 21gp and wizard robes for 35gp'

lou.money-=56

x19 = 'Buy the two breads at 2gp. And the four tuna was half off so 10'

lou.money -= 14

#tuna.health = 10
#bread.health = 1

x20 = 'Head east then north to the paterdomis temple. Get to gate at 9pm. Search to find anything but find a small pond. Camp there and fish'
# roll 14

x21= 'Catch a herring, catch anchovies'

lou.inventory.append(item( 'herring' ) )
lou.inventory.append( item( 'anchovies' ) )

x22 = 'Cant find anything to sleep. Not too cold though. During the night it starts raining. Now have disadvantage on all rolls'

x23 = 'Get to curve in road and hear screaching around the bend. Go around the corner. See bat eating a rat. Sneak around it'

x24 = 'Try to knock and hide. No one answers.'


