from dataclasses import dataclass


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

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.arrival < other.arrival
        return self.priority < other.priority

    @property
    def response(self):
        return None if self.first_run is None else self.first_run - self.arrival

    @property
    def turnaround(self):
        return None if self.complete is None else self.complete - self.arrival

    @property
    def wait(self):
        return None if self.turnaround is None else self.turnaround - self.burst
