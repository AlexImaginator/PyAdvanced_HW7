class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        top_element = self.stack.pop()
        return top_element
    
    def peek(self):
        top_element = self.stack[-1]
        return top_element
    
    def size(self):
        size = len(self.stack)
        return size


def text_menu():
    print('1 - Ввести новую строку для анализа')
    print('2 - Выход')
    choice = input('Выберете нужное действие: ')
    return choice


if __name__ == '__main__':
    print('Анализ последовательностей скобок на сбалансированность')
    open_brackets = '([{'
    close_brackets = ')]}'
    while True:
        choice = text_menu()
        if choice == '1':
            input_string = input('Введите последовательность скобок для анализа: ')
            if len(input_string) < 2:
                print(f'Строка из {len(input_string)} элементов слишком короткая для анализа')
            else:
                stack = Stack()
                balance = True
                unexpected = False
                for br in input_string:
                    if br in open_brackets:
                        stack.push(br)
                    elif br in close_brackets:
                        close_index = close_brackets.find(br)
                        if not stack.is_empty():
                            top_el = stack.pop()
                            open_index = open_brackets.find(top_el)
                            if open_index != close_index:
                                balance = False
                        else:
                            balance = False
                    else:
                        balance = False
                        unexpected = True
                if not stack.is_empty():
                    balance = False
                if balance:
                    print('Строка сбалансирована')
                elif unexpected:
                    print('Введенная строка содержит недопустимые символы')
                else:
                    print('Строка несбалансирована')
        elif choice == '2':
            break
        else:
            print('Команда введена неверно, попробуйте снова')
