characters = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': 'Shield, Bread Loaf',
    'Gold': 100,
    'Level': 2,
}
for k, v in characters.items():
    print(k, v, sep= ': ')
print("you got 50 gold")
characters['Gold'] += 50
characters['Backpack'] = 'Shield, Bread Loaf, Flint Stone'
for k, v in characters.items():
    print(k, v, sep= ': ')