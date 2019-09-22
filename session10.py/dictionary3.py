while True:
    dictionary = {
        "context": '''the situation within which something exists or happens, and that can help explain it''',
        "appeal": '''a request to the public for money, information, or help''',
        "engage": '''to employ someone''',
        "mature": '''Mature people behave like adults in a way that shows they are well developed emotionally'''
    } 
    word = input("search for a word: ").lower()
    print(word, dictionary[word], sep=': ')