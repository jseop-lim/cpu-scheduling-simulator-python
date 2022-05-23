from input import Model
from schedulers import (
    FirstComeFirstServed, RoundRobin,
    Priority, PriorityPreemptive, PriorityPreemptiveRR,
    ShortestJobFirst#, ShortestRemainingTimeFirst
)
from gantt import Gantt

class Handler:
    scheduler_list = (
        FirstComeFirstServed, RoundRobin,
        Priority, PriorityPreemptive, PriorityPreemptiveRR,
        ShortestJobFirst#, ShortestRemainingTimeFirst
    )
    def __init__(self):
        self.outputs = []
        self.gantts = []
    #def __init__(self):#, path=None):
        #if path:
        #self.model = Model()#.create_from_file(path)
        #else:
        #    raise ValueError('파일 경로를 입력하세요.')

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
        gantt_data = {process.pid: process.log for process in scheduler.terminated_queue}

        print()
        for ps in sorted(scheduler.terminated_queue, key=lambda p: p.pid):
            print(ps)

        return response_times, turnaround_times, waiting_times, gantt_data
        # TODO 스케줄러 모듈이랑 이 함수랑 연결하기 - 입력? 필드?

    def main(self):
        for i, Scheduler in enumerate(self.scheduler_list):
            print(Scheduler.__name__, i)
            self.outputs.append(self.run_scheduler(Scheduler))
            #print('result:  ', self.outputs[i][3], '\n')
            print('response time : ',self.outputs[i][0],'\n')
            print('turnaround time: ', self.outputs[i][1], '\n')
            print('waiting ime : ' , self.outputs[i][2], '\n')
            self.gantt[i] = Gantt(self.outputs[i][3])
            self.gantt[i].create_image(Scheduler.__name__)
if __name__ == '__main__':
    handler = Handler(path='input.txt')
    handler.main()
