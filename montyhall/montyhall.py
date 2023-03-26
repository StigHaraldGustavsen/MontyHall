#%%
import numpy as np
import matplotlib.pyplot as plt
import random

# %%
#Create the games

N = 1000 #number of games
n_doors = 3
win_idx = np.random.choice(a=[i for i in range(n_doors)], size=(N))
base = np.array([False for i in range(n_doors)])
games = []
for i in range(len(win_idx)):
    current = base.copy()
    current[win_idx[i]] = True
    games.append(current)

# %%
# test by sticking it to the first game
first_guess = np.random.choice(a=[i for i in range(n_doors)], size=(N))
first_guess_wins = np.zeros(len(first_guess))
i = 0
for game in games:
    if game[first_guess[i]]:
        first_guess_wins[i] = 1
    i += 1

print(np.cumsum(first_guess_wins)[N-1])

#%%
# test with switch door
first_guess = np.random.choice(a=[i for i in range(n_doors)], size=(N))
switch_wins = np.zeros(len(first_guess))
i = 0
for game in games:
    
    Not_to_remove_set = set([np.where(game == True)[0][0],first_guess[i]])
    doors_set = set([i for i in range(n_doors)])
    removed_door = random.choice(list(doors_set-Not_to_remove_set))

    new_guess = (doors_set-set([removed_door])-set([first_guess[i]])).pop()
    if game[new_guess]:
        switch_wins[i] = 1
    i += 1

print(np.cumsum(switch_wins)[N-1])
# %%

def montyhall(N = 100,n_doors = 3):
    win_idx = np.random.choice(a=[i for i in range(n_doors)], size=(N))
    base = np.array([False for i in range(n_doors)])
    games = []
    for i in range(len(win_idx)):
        current = base.copy()
        current[win_idx[i]] = True
        games.append(current)
    
    first_guess = np.random.choice(a=[i for i in range(n_doors)], size=(N))
    first_guess_wins = np.zeros(len(first_guess))
    switch_wins = np.zeros(len(first_guess))
    i = 0
    for game in games:
        #Remaining on inital guess
        if game[first_guess[i]]:
            first_guess_wins[i] = 1
            
        #Switch doors
        Not_to_remove_set = set([np.where(game == True)[0][0],first_guess[i]])
        doors_set = set([i for i in range(n_doors)])
        removed_door = random.choice(list(doors_set-Not_to_remove_set))
        new_guess = (doors_set-set([removed_door])-set([first_guess[i]])).pop()
        if game[new_guess]:
            switch_wins[i] = 1
            
        i += 1
        
    
    return (np.cumsum(first_guess_wins)[N-1],np.cumsum(switch_wins)[N-1])

# %%
first_guess = []
switch_guess = []
for i in range(25000):
    first, switch = montyhall()
    first_guess.append(first)
    switch_guess.append(switch)

# %%
plt.figure(figsize=(7,7))
plt.hist(first_guess,
         bins=100,
         label='remaining on first guess')
plt.hist(switch_guess,
         bins=100,
         label='switching the guess')
plt.title('simulating montyhall on '+str(25000*100)+' simulation 25000 grouped in 100')
plt.legend()
plt.xlim(0,100)
plt.xlabel('%wins of 100')
plt.ylabel('count')
plt.savefig('res.png')
# %%

# %%
