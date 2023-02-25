def lat():
    inputed_list = list(input())
    string = ''
    for i in inputed_list:
        if i in dictionary.keys():
            string += dictionary.get(i)
    return string


def kir():
    inputed_list = list(input())
    string = ''
    for i in inputed_list:
        if i in dictionary_mirrored.keys():
            string += dictionary_mirrored.get(i)
    return string


dictionary = {'A': 'А', 'a': 'а', 'B': 'Б', 'b': 'б', 'C': 'Ц', 'c': 'ц', 'Č': 'Ч', 'č': 'ч',
              'Ć': 'Ћ', 'ć': 'ћ', 'D': 'Д', 'd': 'д', 'Dž': 'Џ', 'dž': 'џ', 'Đ': 'Ђ', 'đ': 'ђ',
              'E': 'Е', 'e': 'е', 'F': 'Ф', 'f': 'ф', 'G': 'Г', 'g': 'г', 'H': 'Х', 'h': 'х',
              'I': 'И', 'i': 'и', 'J': 'Ј', 'j': 'ј', 'K': 'К', 'k': 'к', 'L': 'Л', 'l': 'л',
              'Lj': 'Љ', 'lj': 'љ', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н', 'Nj': 'Њ', 'nj': 'њ',
              'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р', 'S': 'С', 's': 'с',
              'Š': 'Ш', 'š': 'ш', 'T': 'Т', 't': 'т', 'U': 'У', 'u': 'у', 'V': 'В', 'v': 'в',
              'Z': 'З', 'z': 'з', 'Ž': 'Ж', 'ž': 'ж', ' ': ' '}

dictionary_mirrored = dict(zip(dictionary.values(), dictionary.keys()))

print('Добро пожаловать в Сербизатор! Эта программа поможет осуществить '
      'транслитерацию сербской кириллической азбуки в латинскую или наоборот, с учётом регистра.'
      'Введите слово или фразу, чтобы увидеть результат.')

if __name__ == '__main__':
    while True:
        print(lat())
    print('helloworld')

    print('aboba')