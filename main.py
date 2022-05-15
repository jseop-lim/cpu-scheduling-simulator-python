from input import Model
from schedulers import FCFS, RR, Priority, PriorityPreemptive, PriorityPreemptiveRR


class Handler:
    def __init__(self, path=None):
        if path:
            self.model = Model.create_from_file(path)
        else:
            raise ValueError('파일 경로를 입력하세요.')

    def run_scheduler(self):
        """
        arrival_time list로 갖고 있으면서 수시로 검사
        현재 실행 중인 프로세스의 remain burst_time이 0이 될 때까지
        time_slice 지났는지 수시로 검사
        """
        print('FCFS')
        scheduler = FCFS(self.model)
        scheduler.run()
        print('\nRR')
        scheduler = RR(self.model)
        scheduler.run()
        print('\npriority')
        scheduler = Priority(self.model)
        scheduler.run()
        print('\npreemptive priority')
        scheduler = PriorityPreemptive(self.model)
        scheduler.run()
        print('\npriority + RR')
        scheduler = PriorityPreemptiveRR(self.model)
        scheduler.run()
        # TODO 스케줄러 모듈이랑 이 함수랑 연결하기 - 입력? 필드?

    def main(self):
        self.run_scheduler()


if __name__ == '__main__':
    handler = Handler(path='input.txt')

    # handler.run_scheduler()
    handler.main()
