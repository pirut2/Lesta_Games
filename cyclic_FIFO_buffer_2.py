"""Второй класс, реализующий циклический буфер FIFO"""

from collections import deque  # Данный класс реализует двусвязный список


class Queue:
    def __init__(self, max_size: int):
        self.max_size = max_size  # Устанавливаем максимальную длину очереди
        self.queue = deque([], maxlen=max_size)  # обращение к классу

    def push(self, value):
        # Данный метод добавляет новый элемент слева.
        # Согласно документации время выполнения О(1)
        return self.queue.appendleft(value)

    def pop(self):
        try:
            # Данный метод убирает элемент справа.
            # Согласно документации время выполнения О(1)
            return self.queue.pop()
        # Отлавливаем ошибку,
        # которая возникает при извлечении элемента из пустой очереди
        except IndexError as error:
            return print(error)
