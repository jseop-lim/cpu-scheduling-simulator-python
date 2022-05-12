from dataclasses import dataclass, field

# TODO 전략 패턴 사용

@dataclass
class Model:
    p_num: int = field(init=False)
    base_process_list: list = field(default_factory=list, init=False)
    time_slice: int = field(init=False)

    @classmethod
    def create_from_file(cls, path):
        cls.__init__ = cls.file_input
        instance = cls(path)
        return instance

    def file_input(self, path):
        with open(path, 'r') as f:
            self.p_num = int(f.readline())

            self.base_process_list = []
            for _ in range(self.p_num):
                row = f.readline().split()
                row[1:] = map(int, row[1:])
                self.base_process_list.append(BaseProcess(*row))

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
        process_list = list(map(Process, self.model.base_process_list))


    def main(self):
        print(self.model)


@dataclass
class BaseProcess:
    pid: str
    arrival: int
    burst: int
    priority: int

    def __str__(self):
        return self.pid


@dataclass
class Process(BaseProcess):
    remain: str
    complete: int
    first_run: int

    def __init__(self, process: BaseProcess):
        super().__init__(process.pid, process.arrival, process.burst, process.priority)
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


if __name__ == '__main__':
    handler = Handler(path='input.txt')

    handler.run_scheduler()
    handler.main()
