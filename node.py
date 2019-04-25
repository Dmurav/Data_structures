
#Класс "узел" - основной элемент связанного списка
class Node:
    #Узел состоит из значения и ссылки на другой узел
    def __init__(self, value=None, next=None):
        """Конструктор - инициализирует экзхемпляр класса"""
        self.value = value
        self.next = next

    def __str__(self):
        """Строковое представление экземпляра"""
        return str(self.value)

#Создаём экземпляр узла
node = Node("test")

#Создаём ещё несколько услов
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

#Устанавливаем ссылки, создавая связанный список
node1.next = node2
node2.next = node3
node3.next = node4

#Функция для распечатки связанного списка
def print_list(node):
    """Функция применённая к первому в списке узлу
            распечатывает весь список пока есть ссылки"""
    while node:
        print(node, end=' ')
        node = node.next

#Вызываем функцию и распечатываем связанный список
print_list(node1)
print(end='\n')

#Функция для распечатки связанного списка в обратном порядке
def print_backward(list):
    """Рекурсивная функция применённая к первому в списке узлу
                распечатывает весь список начиная с конца"""
    if list == None:
        return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=' ')

#Вызываем функцию и распечатываем связанный список
print_backward(node1)

#Функция для удаления второго элемента в связанном списке
def remove_second(list):
    """Функция получает на взход связанный список
    и удаляет второй элемент в списке, переустанавливая
    ссылки"""
    if list == None:
        return
    first = list
    second = list.next
    first.next = second.next
    second.next = None
    return second

print(end='\n')

#Вызываем функцию и распечатываем связанный список
remove_second(node1)
print(print_list(node1))