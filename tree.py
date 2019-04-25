
#Класс - дерево. Дерево состоит из узлов с более чем одной направленной ссылкой
class Tree:

    def __init__(self, value, left=None, right=None):
        """Конструктор - создаёт экземпляр вершины дерева"""
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        """Строковое представление вершины дерева"""
        return str(self.value)


def total(tree):
    """Рекурсивная функция принимает на вход дерево,
    возвращает - сумму значений элементов дерева"""
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.value

def print_tree(tree):
    """Рекурсивная функция принимает на вход дерево,
    распечатывая все его элементы"""
    if tree == None: return
    print(tree.value, end=' ')
    print_tree(tree.left)
    print_tree(tree.right)

#Создаём экземпляр дерева
my_tree = Tree(1, Tree(2), Tree(3))

#Применяем функции и смотрим результат
print("Сумма значений всех элементов дерева - ", end='')
print(total(my_tree))
print("Распечатанные по порядку сверху вниз и слева направо значения вершин дерева - ", end='')
print_tree(my_tree)