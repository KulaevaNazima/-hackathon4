# # Задание 4
# Напишите Программу - которая работает по принципу алгоритма Шифр Цезаря.
# Нужно создать класс состоящий из 2 методов:
# 1. Метод который ШИФРУЕТ данные.
# 2. Метода который ДЕШИФРУЕТ эти же данные.
# Представим что ваш метод получает слово состоящее из ЛЮБЫХ символов.
# Ваш 1-й метод должен вернуть зашифрованную строку.
# Алгоритм Шифрования: ASCII позиция + 7.
# Алгоритм Дешифровки: Обратная операция Алгоритма Шифрования.

ALPHABET = ('абвгдеёжзиклмнопрстуфхчшщъыьэюя'
            'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
def encryption_caesar(msg, offset):
    """
    Возвращает сообщение зашифрованное шифром Цезаря.
    :param msg Сообщение
    :param offset Смещение в алфавите
    :return Зашифрованное сообщение
    """
    encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
    encrypted = []
    for char in msg:
        index = get_char_index(char, ALPHABET)
        encrypted_char = encrypted_alphabet[index] if index >= 0 else char
        encrypted.append(encrypted_char)
    return ''.join(encrypted)
def get_char_index(char, alphabet):
    """
    Возвращает индекс первого вхождения символа с сторку алфавита.
    :param char: Символ
    :return: Индекс
    """
    char_index = alphabet.find(char)
    return char_index
def decryption_caesar(msg, offset=None):
    """
    Возвращает расшифрованное сообщение, зашифрованное шифром Цезаря.
    Если shift = None, будет пробовать расшифровывать без смещения
    :param msg Сообщение
    :param offset Смещение в алфавите
    :return Расшифрованное сообщение
    """
    encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
    decrypted = []
    if offset:
        # Если известно смещение, просто дешифруем сообщение по обратно
        for char in msg:
            index = get_char_index(char, encrypted_alphabet)
            encrypted_char = encrypted_alphabet[index - offset] \
                if index >= 0 else char
            decrypted.append(encrypted_char)
        return ''.join(decrypted)
    else:
        # Если нет, то будем дешифровать и искать вхождение слов из словаря
        # Так как это просто пример, словарь маленький
        dictionary = ['Привет', 'пока', 'что']
        for offset in range(len(ALPHABET)):
            # Каждого смещения, начиная с 0 создаем смещенный алфавит
            encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
            for char in msg:
                index = get_char_index(char, encrypted_alphabet)
                encrypted_char = ALPHABET[index] if index >= 0 else char
                decrypted.append(encrypted_char)
            decrypted = ''.join(decrypted)
            for word in dictionary:
                # Если слово из словаря входит в дешифрованную строку,
                # возвращаем её
                if word in decrypted:
                    return decrypted
            decrypted = []  # Обнуляем расшифрованное сообщение
    return 'Не удалось расшифровать сообщение %s' % msg
if __name__ == '__main__':
    message = input("Введите слово: ")
    shift = 5  # Смещение алфавита
    encrypted_message = encryption_caesar(message, shift)
    print('Сообщение: %s' % message)
    print('Зашифрованное сообщение: %s' % encrypted_message)
    print('Расшифрованное сообщение: %s' % decryption_caesar(encrypted_message))
