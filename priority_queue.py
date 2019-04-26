
class PriorityQueue:
    """Класс для создания объектов очереди с приоритетом
    на основе стандартного списка. Поддерживает три метода:
    is_empty - проверка наличия элементов в очереди,
    enqueue - вставка элемента в конец очередь,
    dequeue - извлечение элемента из начала очереди"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        """Метод проводит итерацию по очереди и
        сравнивая значения очереди определяет индекс
        максимального значения. Затем максимальное
        значение по индексу возвращает и удаляет из
        очереди"""
        maxim = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxim]:
                maxim = i
        item = self.items[maxim]
        self.items[maxim:maxim + 1] = []
        return item


def test_queue():
    """Тест создаёт экземпляр очереди и наполняет
    её значениями вызывая метод enqueue. Затем
    тест вызывает метод dequeue и наполняет result
    значениями из очереди. Затем проверяет результат
    на соответствие эталону"""
    new_queue = PriorityQueue()
    # Добавляем в очередь целые числа от 0 до 4 включительно
    for i in [4, 3, 5, 1, 7]:
        new_queue.enqueue(i)
    # Извлекаем из очереди и складываем в result
    result = []
    for i in range(5):
        x = new_queue.dequeue()
        result.append(x)
    assert (result == [7, 5, 4, 3, 1])

