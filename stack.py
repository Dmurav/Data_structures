
#Создаём класс "стек"
class myStack(object):
    """Класс имеет три метода, которые
    позволяют добавлять элемент в конец стека,
    брать последний добавленный элемент и
    проверять наличие в стеке элементов"""
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        pop_el = self.items[-1]
        del self.items[-1]
        return pop_el

    def is_empty(self):
        if len(self.items) < 1:
            return True
        else:
            return False

#Создаём экземпляр стека
new_stack = myStack()

#Добавляем в стек целые числа - 4 и 5
new_stack.push(4)
new_stack.push(5)
#Применяем методы и наблюдаем что происходит
print("Этот стек пустой? - ", end='')
print(new_stack.is_empty())
print("Какой последний элемент довален в стек? - ", end='')
print(new_stack.pop())
print("А следующий? - ", end='')
print(new_stack.pop())
print("А теперь этот стек пустой? - ", end='')
print(new_stack.is_empty())