"""Первый класс, реализующий циклический буфер FIFO
Время выполнения операций O(1), так как не требуется выделение новой памяти"""
import timeit


class Queue:
    def __init__(self, n):
        self.queue = [None] * n  # заполняем очередь None
        self.max_n = n  # максимальный размер очереди
        # индекс, по которому нужно извлекать элемент, если очередь не пустая
        self.head = 0
        # индекс, по которому нужно добавлять элемент,
        # если в очереди есть место
        self.tail = 0
        self.size = 0  # размер очереди.

    def is_empty(self):  # метод, который определяет пуста ли очередь.
        return self.size == 0

    def push(self, x):  # метод, который добавляет элемент в очередь
        if self.size != self.max_n:
            self.queue[self.tail] = x
            # Значение tail берётся по модулю max_n. Это делается для того,
            # чтобы первая ячейка следовала за последней.
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def pop(self):  # метод, который извлекает элемент из очереди;
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        # Значение поля head изменяется аналогично полю tail в методе push()
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


time = timeit.timeit(Queue.pop(8), number=10000)
print(time)
