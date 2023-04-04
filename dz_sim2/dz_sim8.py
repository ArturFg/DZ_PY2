# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

def show_data() -> str:
    '''Эта функция показывает содержимое справочника'''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book

def new_data() -> None:
    '''добавляет новую информацию в справочник'''
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input(f''))
        file.write(f'\n')

def search_data() -> None:
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
        book = book.split('\n')
        s = str(input('Введи один элимент из записи справочника: '))
        for i in range(len(book)):
            if s in book[i]:
                print(book[i])
                break
            if i == len(book):
                print('Этого контакта нет в справочнике.')

def change_data() -> None:
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
        book = book.split('\n')
        s = str(input('Введи один элимент из записи справочника который хочешь изменить: '))
        for i in range(len(book)):
            if s in book[i]:
                book1 = book[i]
                book1 = book1.split(' ')
                for j in range(len(book1)):
                    if s in book1[j]:
                        print('Если хочешь ИЗМЕНИТЬ элимент то 1')
                        print('Если хочешь УДАЛИТЬ элимент то 2')
                        print('Выход 0')
                        mode2 = input('Выбери режим работы:')

                        if mode2 == '1':
                            print('1 Изменить элимент')
                            print('2 Дописать элемент')
                            print('0 Выход')
                            mode3 = input('Выбери режим работы:')
                            if mode3 == '1':
                                pamena = str(input('В пеши то на что хочешь поменять элимент: '))
                                book1[j] = pamena
                                book1 = ' '.join(book1)

                                book[i] = book1
                                book = '\n'.join(book)

                                with open('data.txt', 'w', encoding='utf-8') as file:
                                    file.write(book)
                                break
                            elif mode3 == '2':
                                book1 = ' '.join(book1)
                                print(book1)
                                book1 = book1.split(' ')
                                before_recording = str(input('В пеши перед каким элиментом, ты хочешь вписать элемент, а если в начеле нужна записять впеши 0: '))
                                ind = 0
                                if before_recording != '0':
                                    for r in range(len(book1)):
                                        if before_recording in book1[r]:
                                            ind = r + 1
                                            break
                                new_element = str(input('Запиши элемен каторый хочешь: '))
                                book1.insert(ind, new_element)
                                book1 = ' '.join(book1)
                                book[i] = book1
                                book = '\n'.join(book)

                                with open('data.txt', 'w', encoding='utf-8') as file:
                                    file.write(book)
                                break

                            elif mode2 == '0':
                                break   

                        elif mode2 == '2':
                            book1.pop(j)
                            book1 = ' '.join(book1)

                            book[i] = book1
                            book = '\n'.join(book)

                            with open('data.txt', 'w', encoding='utf-8') as file:
                                file.write(book)
                            break

                        elif mode2 == '0':
                            break

            if i == len(book):
                print('Этого контакта нет в справочнике.')

while True:
    print('0. Выход из программы.')
    print('1. Работа уже с существующим справочником.')
    print('2. Создать чистый справочник.')
    mode = input('Выбери как хочешь использовать файл:')

    if mode == '1':
        while True:
            print('0. Выход из программы.')
            print('1. Функция показывает содержимое справочника.')
            print('2. Функция добавляет новую информацию в справочник.')
            print('3. Функция ищет опредилённую запись справочника.')
            print('4. Функция изменяет или удоляет опредилённую запись справочника.')
            mode1 = input('Выбери режи работы справочника:')

            if mode1 == '1':
                print()
                print(show_data())
                print()
            elif mode1 == '2':
                new_data()
            elif mode1 == '3':
                search_data()
            elif mode1 == '4':
                change_data()
            elif mode1 == '0':
                break
            else:
                print('No mode1')

    elif mode == '2':
        with open('data.txt', 'w', encoding='utf-8') as file:
            file.write(f'')

    elif mode == '0':
        break

    else:
        print('No mode')