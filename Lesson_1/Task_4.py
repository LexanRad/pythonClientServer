def alteration(word):
    word_bytes = word.encode('utf-8')
    print(word_bytes)
    print(type(word_bytes))
    word_str = word_bytes.decode('utf-8')
    print(word_str)
    print(type(word_str))


word_1 = 'разработка'
alteration(word_1)
word_2 = 'администрирование'
alteration(word_2)
word_3 = 'protocol'
alteration(word_3)
word_4 = 'standard'
alteration(word_4)
