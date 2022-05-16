from dataclasses import dataclass, field


@dataclass
class BaseProcess:
    pid: str
    arrival: int
    burst: int
    priority: int

    # def __str__(self):
    #     return self.pid


@dataclass
class Process(BaseProcess):
    remain: str
    complete: int
    first_run: int
    enqueued_at: int
    log: dict = field(repr=False)

    def __init__(self, process: BaseProcess):
        super().__init__(process.pid, process.arrival, process.burst, process.priority)
        self.remain = self.burst
        self.complete = None
        self.first_run = None
        self.enqueued_at = self.arrival
        self.log = []

    def __lt__(self, other):
        return (self.priority, self.enqueued_at) < (other.priority, other.enqueued_at)

    @property
    def response(self):
        return None if self.first_run is None else self.first_run - self.arrival

    @property
    def turnaround(self):
        return None if self.complete is None else self.complete - self.arrival

    @property
    def wait(self):
        return None if self.turnaround is None else self.turnaround - self.burst

    def set_log(self, start, time):
        self.log.append([start, start+time, time])  # TODO gantt input에 따라 수정

