  
from input import Model
from processes import Process, ShortestFirstProcess
from queues import Queue, PriorityQueue


class Scheduler:
    is_preemptive = None  # 실행 중간에 프로세스 교체 허용?
    is_priority = None  # ready queue가 priority queue or FIFO queue
    is_time_slice = None  # time slice 적용?
    process_class = Process

    def __init__(self, model: Model):
        self.planned_queue = list(map(self.process_class, model.base_process_list))  # 아직 도착하지 않은 프로세스
        self.ready_queue = PriorityQueue() if self.is_priority else Queue()  # 도착했지만 실행 중이 아닌 프로세스
        self.terminated_queue = []  # 실행이 끝나 종료된 프로세스
        self.running = None  # 실행 중인 프로세스
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
            self.running.enqueued_at = self.now
            self.ready_queue.enqueue(self.running)
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
                    if next_arrival_time == 0 and new_process < self.running:
                        self.dispatch()
                        if self.running.first_run == self.now:
                            self.running.first_run = None
                    elif self.is_preemptive and new_process < self.running:
                        self.dispatch(next_arrival_time)
                    continue

            self.dispatch(next_dispatch_time)

        print(self.now, self.running)  # TODO temp
        
    @property
    def avg_response(self):
        return sum(process.response for process in self.terminated_queue) / len(self.terminated_queue)

    @property
    def avg_turnaround(self):
        return sum(process.turnaround for process in self.terminated_queue) / len(self.terminated_queue)

    @property
    def avg_wait(self):
        return sum(process.wait for process in self.terminated_queue) / len(self.terminated_queue)


class FirstComeFirstServed(Scheduler):
    is_preemptive = False  # 실행 중간에 프로세스 교체 허용?
    is_priority = False  # ready queue가 priority queue or FIFO queue
    is_time_slice = False  # time slice 적용?


class Priority(FirstComeFirstServed):
    is_priority = True


class PriorityPreemptive(Priority):
    is_preemptive = True


class RoundRobin(FirstComeFirstServed):
    is_time_slice = True


class PriorityRR(FirstComeFirstServed):
    is_priority = True
    is_time_slice = True
    is_preemptive = False


class ShortestJobFirst(FirstComeFirstServed):
    is_priority = True
    process_class = ShortestFirstProcess  # 프로세스 객체 안 바꾸면 heap에서 우선순위 비교 시 오류 발생

    # def __init__(self, model: Model):
    #     super().__init__(model)
    #     for process in self.planned_queue:
    #         process.priority = process.burst


class ShortestRemainingTimeFirst(ShortestJobFirst):
    is_preemptive = True

    def run(self):
        run_time = 0  # 현재 실행 중인 프로세스가 실행 시작하고 지난 시간
        while self.check_over():
            # save first_run time
            # context switching 직후에는 now가 왜곡되지 않는다.
            if self.running.first_run is None:
                self.running.first_run = self.now

            next_dispatch_time = self.running.remain

            if self.planned_queue:
                next_arrival_time = self.planned_queue[0].arrival - self.now
                if next_arrival_time <= next_dispatch_time:
                    # arrive
                    new_process = self.planned_queue.pop(0)
                    self.ready_queue.enqueue(new_process)
                    # concurrent arrive
                    if next_arrival_time == 0 and new_process.remain < self.running.remain - run_time:
                        if self.running.first_run == self.now:
                            self.running.first_run = None
                        self.dispatch()
                    # preempt by priority
                    elif self.is_preemptive and new_process.remain < self.running.remain - run_time:
                        self.dispatch(next_arrival_time)
                        run_time = 0
                    else:
                        run_time += next_arrival_time
                    continue

            self.dispatch(next_dispatch_time)
            run_time = 0

        print(self.now, self.running)  # TODO temp; 종료시각 및 None 출력
