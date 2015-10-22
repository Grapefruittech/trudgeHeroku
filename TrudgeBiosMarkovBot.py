
# coding: utf-8

# In[73]:

# configs
keyLen = 3
outputLen = 36


# In[56]:

# imports
import random


# In[57]:

# read in data and clean it

### change to grab file from server
# read in bios file
biosRAW = open('bios')

# read in bios to list
bios = biosRAW.read()
# make punctuation all the same
bios = bios.replace(". ","~\n") 
bios = bios.replace(".\n","~\n") 
bios = bios.replace("? ","~\n")
bios = bios.replace("?","~")
bios = bios.replace("! ","~\n")
bios = bios.replace("!","~")
bios = bios.replace("; ","~\n")
# these aren't phrase terminating punctuation
bios = bios.replace(": "," ")
bios = bios.replace("- "," ")
bios = bios.replace(",","")
bios = bios.replace('"',"")

# special cases
bios = bios.replace('~~~', '~')

# \xe2\x80

bios = bios.split('\n') # split on new lines
bios.pop(-1) # remove empty string


# In[90]:

# create first words array
first = [line.split(' ')[:keyLen] for line in bios]
# create dictionary of n-grams
grams = {}
for line in bios:
    l = line.split(' ')
    for i in range(len(l)-keyLen):
        key = ' '.join(l[i:i+keyLen])
        if key in grams:
            grams[key].append(l[i+keyLen])
        else:
            grams[key] = [l[i+keyLen]]
        


# In[101]:


for i in xrange(outputLen):
    # print out example
    output = []
    test = random.choice(first)
    
    # if key is too short
    if len(test) < keyLen:
        continue
    
    
    for i in range(keyLen):
        output.append(test[i])
    while 1:
        if output[-1].find('~') > -1:
            output[-1] = output[-1].replace('~', '')
            break
        n = random.choice(grams[' '.join(test)])   
        
        # add new word
        output.append(n)
        # shift test to capture next key
        test.pop(0)
        test.append(n)


    print ' '.join(output) + '.',

