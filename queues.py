from heapq import heappush, heappop


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def not_empty(self):
        return bool(self.queue)


class PriorityQueue(Queue):
    def enqueue(self, item):
        heappush(self.queue, item)

    def dequeue(self):
        return heappop(self.queue)
