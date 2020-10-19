#!/usr/bin/env python
# coding: utf-8

# In[58]:


from character import me as me
import session1 as s1
me = s1.lou


# # Last thing that happened!

# In[59]:


s1.x24


# In[60]:


stats = []
for i in dir(me):
    stats.append( eval('me.'+i) )
stats = stats[2]
for i in stats:
    print(i , '------>' ,stats[i])


# In[76]:


import numpy as np
import pandas as pd
x = np.array( stats['all'])
x.shape = (8,3)

pd.DataFrame(x)
# #squelchy cam eup out of the dungeon

# In[106]:


me.roll(20) + (me.thieving/10)


# me.roll(20) + (me.theiving/10)

# Took off all my clothes and tried lock picking in

# In[108]:


me.roll(20) + (me.thieving/10)


# # Put sword in in middle and push the timber locking the door

# In[109]:


me.roll(20) + (me.strength/10)


# Look arround to see some robes, a ladder to decond story.

# In[110]:


me.roll(20)


# go up the ladder, I say " There is a half orc down stairs!". Shot a fireball at me

# In[128]:


me.health -= 5


# # Attack initiative roll

# In[121]:


me.roll(20) + me.attack_m


# # Tried tipping over bookshelf, I fail... ha!

# In[116]:


me.roll(20) + me.strength_m


# # turn prayer on to boost strength modifer by 1

# Squelchi hits the zamarak monk by 2

# - squlchi gets hit by 7
# 
# - squlchi attempts to retrieve his weapon, then tries to push down the bookshelf, rolls a 17
# 
# - they are trapped
# 
# - I wake him up and he tells be to go to hell. I hit him hard with a book.
# 
# - go upstairs to check on munk calling out
# 
# - tried hitting him in head with pickaxe

# In[123]:


me.roll(20) + me.attack_m


# In[125]:


me.health -= 6


# In[129]:


me.health


# In[130]:


# Oh no!


# In[131]:


me.roll(20) + me.attack_m


# In[132]:


me.roll(4)


# In[134]:


3 + me.strength_m + 1 # prayer modifier


# # Zamarok monk hit me with a 8 and took me unconcious

# In[135]:


me.roll(20) #first Savings throw , needs a 5


# In[136]:


me.roll(20) #first Savings throw , needs a 5


# In[137]:


me.roll(20) #first Savings throw , needs a 5


# In[141]:


me.health = 1


# # go downstairs and kill the Munk with a pickaxe

# In[138]:


me.roll(20)


# In[139]:


me.roll(20)


# In[140]:


me.roll(4)


# # kill him

# - go up stairs and do a perseption check

# In[142]:


me.roll(20)


# - Turn to squlchi and ask him to open the coffin
# 
# - He opens the lid with a 14

# In[ ]:


# eat anchovies and herring to heal 6 


# In[143]:


me.health +=6


# In[157]:


temp = s1.lou


# In[160]:


me.inventory = temp.inventory[0:3]


# In[161]:


me.inventory


# In[165]:


me.roll(20) + me.strength_m


# # I couldnt lift the lid with the vampyre so this guy told me to whack him with the pickaxe

# In[167]:


me.roll(20) + me.theiving


# In[168]:


# picked up 100 air and 100 mind runes


# In[186]:


me.inventory.append('100 air runes')
me.inventory.append('100 mind runes')


# In[169]:


# I take a steel scimitar


# In[184]:


me.inventory.append( 'steel scimmitar' )


# In[ ]:





# In[171]:


me.roll(20)


# In[172]:


me.roll(20)


# In[173]:


# catch 1 trout


# In[174]:


me.roll(20)


# In[175]:


# catch raw herring


# # I feel sick

# In[176]:


me.roll(20) + ( me.construction / 10)


# I'm leaking! help!

# In[177]:


me.roll(20) + ( me.firemaking/ 10)


# In[178]:


# cook my food


# # Each food is cooked so well that it each heals +2 hp !!!!!!!!!!

# - I was shitting all night

# In[181]:


# I have a second point of exhuastion from not sleeping well twice!


# In[187]:


me.inventory.append('trout')
me.inventory.append('herring')


# In[ ]:




