from input import Model
from processes import Process, ShortestFirstProcess
from queues import Queue, PriorityQueue


class FirstComeFirstServed:
    is_preemptive = False  # 실행 중간에 프로세스 교체 허용?
    is_priority = False  # ready queue가 priority queue or FIFO queue
    is_time_slice = False  # time slice 적용?

    def __init__(self, model: Model, process_class=Process):
        self.planned_queue = list(map(process_class, model.base_process_list))
        self.ready_queue = PriorityQueue() if self.is_priority else Queue()  # heap 제약이 적용될 수 있음
        self.terminated_queue = []
        self.running = None
        self.time_slice = model.time_slice if self.is_time_slice else max(p.burst for p in model.base_process_list)

        try:
            self.running = self.planned_queue.pop(0)
            self.now = self.running.arrival
        except IndexError:
            raise IndexError('프로세스를 하나 이상 입력하세요.')

    def execute_times(self, time):
        self.now += time
        self.running.remain -= time

    def dispatch(self, time=None):
        if time:
            print(self.now, self.running)
            self.running.set_log(self.now, time)  # gantt chart
            self.execute_times(time)

        if self.running.remain > 0:
            self.ready_queue.enqueue(self.running)
            self.running.enqueued_at = self.now
        else:
            self.terminated_queue.append(self.running)
            self.running.complete = self.now
        self.running = self.ready_queue.dequeue() if self.ready_queue.not_empty() else None

    def check_over(self):
        return self.running or self.ready_queue.not_empty() or self.planned_queue

    def run(self):
        while self.check_over():
            # save first_run time
            if self.running.first_run is None:
                self.running.first_run = self.now

            # TODO time slice 지나면 self.now는 증가하지만 실행 프로세스는 그대로
            next_dispatch_time = self.running.remain
            if self.is_time_slice and self.time_slice < self.running.remain:
                next_dispatch_time = self.time_slice

            if self.planned_queue:
                next_arrival_time = self.planned_queue[0].arrival - self.now
                if next_arrival_time <= next_dispatch_time:
                    # arrive
                    new_process = self.planned_queue.pop(0)
                    self.ready_queue.enqueue(new_process)
                    # preempt by priority
                    if self.is_preemptive and new_process < self.running:
                        self.dispatch(next_arrival_time)
                    continue

            self.dispatch(next_dispatch_time)

        print(self.now, self.running)  # TODO temp


class Priority(FirstComeFirstServed):
    is_priority = True


class PriorityPreemptive(FirstComeFirstServed):
    is_priority = True
    is_preemptive = True


class RoundRobin(FirstComeFirstServed):
    is_time_slice = True


class PriorityPreemptiveRR(FirstComeFirstServed):
    is_priority = True
    is_preemptive = True
    is_time_slice = True


class ShortestJobFirst(FirstComeFirstServed):
    is_priority = True

    def __init__(self, model: Model):
        super().__init__(model, ShortestFirstProcess)


# class ShortestRemainingTimeFirst(ShortestJobFirst):
#     is_preemptive = True
#
#     def run(self):
#         while self.check_over():
#             # save first_run time
#             if self.running.first_run is None:
#                 self.running.first_run = self.now
#
#             # TODO time slice 지나면 self.now는 증가하지만 실행 프로세스는 그대로
#             next_dispatch_time = self.running.remain
#
#             if self.planned_queue:
#                 next_arrival_time = self.planned_queue[0].arrival - self.now
#                 if next_arrival_time <= next_dispatch_time:
#                     # arrive
#                     new_process = self.planned_queue.pop(0)
#                     self.ready_queue.enqueue(new_process)
#                     print('before', self.now, new_process.remain, self.running.remain)
#                     self.execute_times(next_arrival_time)
#                     print('after', self.now, new_process.remain, self.running.remain)
#                     # preempt by priority
#                     if self.is_preemptive and new_process < self.running:
#                         print(self.now - next_arrival_time, self.running)
#                         self.running.set_log(self.now - next_arrival_time, next_arrival_time)
#                         self.dispatch()
#                     continue
#
#             self.dispatch(next_dispatch_time)
#
#         print(self.now, self.running)  # TODO temp