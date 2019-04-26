

class Queue(object):
    """Класс для создания объектов очереди на основе
        стандартного списка. Поддерживает три метода:
        is_empty - проверка наличия элементов в очереди,
        enqueue - вставка элемента в конец очередь,
        dequeue - извлечение элемента из начала очереди"""
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        first_el = self.items[0]
        del self.items[0]
        return first_el

    def is_empty(self):
        if len(self.items) < 1:
            return True
        else:
            return False


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






