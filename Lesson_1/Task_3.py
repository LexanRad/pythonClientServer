# Если я правильно понял задание, то требуется выяснить какие слова можно получить в байтовом виде, ибо в байтовый тип
# можно перевести все
def is_can_bytes(word):
    word_bytes = word.encode('utf-8')
    if str(word_bytes) == f"b'{word}'":
        return print(f'Слово "{word}" нельзя получить в байтовом представлении')
    else:
        return print(f'Слово "{word}" в байтовом представлении: {word_bytes}')


word_1 = 'attribute'
is_can_bytes(word_1)
word_2 = 'класс'
is_can_bytes(word_2)
word_3 = 'функция'
is_can_bytes(word_3)
word_4 = 'type'
is_can_bytes(word_4)
