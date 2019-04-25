

class Node:
    #Класс "узел" со строковой репрезентацией значения
    def __init__(self, value=None, next=None):
        """Конструктор - инициализирует экзхемпляр класса"""
        self.value = value
        self.next = next

    def __str__(self):
        """Строковое представление экземпляра"""
        return str(self.value)

    #Метод распечатки связанного списка
    def print_list(self):
        """Метод применённый к первому в списке узлу
        распечатывает весь список пока есть ссылки"""
        node = self
        while node:
            print(node, end=' ')
            node = node.next

    #Метод узла для распечатки связанного списка в обратном порядке.
    def print_backward(self):
        """Метод начинает с хвоста и распечатывает список
        от хвоста к голове"""
        if self.next != None:
            tail = self.next
            tail.print_backward()
        print(self.value, end=' ')

#Создаём несколько узлов
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

#Устанавливаем ссылки между узлами, создавая связанный список
node1.next = node2
node2.next = node3

#Проверяем атрибуты и методы узла
print("Значение узла node1 - " + str(node1.value))
print("Ссылка узла node1 - " + str(node1.next))
print("Строковое представление узла node1 - " + node1.__str__())
print("Связанный список распечатанный в обычном порядке ", end='')
node1.print_list()
print()
print("Связанный список распечатанный в обратном порядке ", end='')
node1.print_backward()


class LinkedList:
    #Создаём класс "Связанный список с двумя методами
    def __init__(self):
        self.length = 0
        self.head = None

    #Метод распечатки связанного списка
    def print_list(self):
        """Метод применённый к экземпляру класса
        распечатывает весь список пока есть ссылки"""
        node = self.head
        while node:
            print(node, end=' ')
            node = node.next

    #Метод обратной распечатки связанного списка
    def print_backward(self):
        """Метод начинает устанавливает конечный
        элемент в качестве головы списка и выполняет распечатку,
        эксплуатируя метод узла"""
        if self.head != None:
            self.head.print_backward()

    #Метод добавления узла в связанный список
    def add_first(self, value):
        """Метод позволяет создавать и добавлять в список
        узлы со значением. Добавляет узел на место головы"""
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

#Создаём экземпляр связанного списка
linkedlist = LinkedList()

#Вызываем метод и добавляем в начало списка узлы
linkedlist.add_first(1)
linkedlist.add_first(2)
linkedlist.add_first(3)

#Вызываем методы класса над экземпляром связанного списка
print("\n")
print("Применяем метод распечатки листа", end=' ')
linkedlist.print_list()
print()
print("Применяем метод распечатки листа в обратном порядке", end=' ')
linkedlist.print_backward()