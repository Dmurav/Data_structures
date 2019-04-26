
class Node:  # Узел состоит из значения и ссылки на другой узел
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class Queue:
    """Класс для создания объектов очереди на основе
    связанного списка. Поддерживает три метода:
    is_empty - проверка наличия элементов в очереди,
    enqueue - вставка элемента в конец очередь,
    dequeue - извлечение элемента из начала очереди"""
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def enqueue(self, value):
        """Метод принимает на вход значение будущего узла очереди,
        создаёт узел со значением и если головной узел отсутствует
        устанавливает новый узел на место головного. Иначе поток
        проходит до конца очереди и устанавливает узел в конце очереди"""
        node = Node(value)
        node.next = None
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.length += 1

    def dequeue(self):
        """Метод при вызове на пустом экземпляре объекта ничего
        не возвращает. Иначе возвращает значение головного узла."""
        if self.length == 0:
            return
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value


def test_queue():
    new_queue = Queue()
    # Добавляем в очередь целые числа от 0 до 4 включительно
    for i in range(5):
        new_queue.enqueue(i)
    # Извлекаем из очереди и складываем в result
    result = []
    for i in range(5):
        x = new_queue.dequeue()
        result.append(x)
    assert (result == [0, 1, 2, 3, 4])

