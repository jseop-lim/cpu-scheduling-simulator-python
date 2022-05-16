from input import Model
from schedulers import FCFS, RR, Priority, PriorityPreemptive, PriorityPreemptiveRR


class Handler:
    def __init__(self, path=None):
        if path:
            self.model = Model.create_from_file(path)
        else:
            raise ValueError('파일 경로를 입력하세요.')

    def run_scheduler(self, scheduler_class):
        """
        arrival_time list로 갖고 있으면서 수시로 검사
        현재 실행 중인 프로세스의 remain burst_time이 0이 될 때까지
        time_slice 지났는지 수시로 검사
        """
        scheduler = scheduler_class(self.model)
        # gantt_data = {}
        scheduler.run()

        response_times = {process.pid: process.response for process in scheduler.terminated_queue}
        turnaround_times = {process.pid: process.turnaround for process in scheduler.terminated_queue}
        waiting_times = {process.pid: process.wait for process in scheduler.terminated_queue}

        print()
        for ps in sorted(scheduler.terminated_queue, key=lambda p: p.pid):
            print(ps)

        return response_times, turnaround_times, waiting_times
        # TODO 스케줄러 모듈이랑 이 함수랑 연결하기 - 입력? 필드?

    def main(self):
        print('FCFS')
        self.run_scheduler(FCFS)
        print('\nRR')
        self.run_scheduler(RR)
        print('\npriority')
        self.run_scheduler(Priority)
        print('\npriority preemptive')
        self.run_scheduler(PriorityPreemptive)
        print('\npriority preemptive + RR')
        self.run_scheduler(PriorityPreemptiveRR)


if __name__ == '__main__':
    handler = Handler(path='input.txt')

    # handler.run_scheduler()
    handler.main()
