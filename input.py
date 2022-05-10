from dataclasses import dataclass, field

# TODO 전략 패턴 사용

@dataclass
class Model:
    p_num: int = field(init=False)
    process_list: dict = field(init=False)
    time_slice: int = field(init=False)

    @classmethod
    def create_from_file(cls, path):
        cls.__init__ = cls.file_input
        instance = cls(path)
        return instance

    def file_input(self, path):
        with open(path, 'r') as f:
            self.p_num = int(f.readline())

            self.process_list = {}
            for _ in range(self.p_num):
                row = f.readline().split()
                row[1:] = map(int, row[1:])
                self.process_list[row[0]] = Process(*row)

            self.time_slice = int(f.readline())


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
        for process in self.model.process_list.values():
            process.init_fields()

    def main(self):
        print(self.model)


@dataclass
class Process:
    pid: str
    arrival: int
    burst: int
    priority: int
    remain: int = None
    complete: int = None
    first_run: int = None

    # def __init__(self, pid, arrival, burst, priority):
    #     self.pid = pid
    #     self.arrival = arrival
    #     self.burst = burst
    #     self.priority = priority

    def init_fields(self):
        self.remain = self.burst
        self.complete = None
        self.first_run = None

    @property
    def response(self):
        return None if self.first_run is None else self.first_run - self.arrival

    @property
    def turnaround(self):
        return None if self.complete is None else self.complete - self.arrival

    @property
    def wait(self):
        return None if self.turnaround is None else self.turnaround - self.burst

    def __str__(self):
        return self.pid


if __name__ == '__main__':
    handler = Handler('input.txt')
    print(handler.model.process_list['P0'].remain)
    handler.run_scheduler()
    handler.main()
