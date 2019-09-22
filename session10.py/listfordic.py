film = {
    'name': ' dragon ball',
    'year': '1990',
    'characters': 'goku, goten, gohan',
}
film['country'] = 'japan'
print(film)
for k, v in film.items():
    print(k, v, sep = ' - ')