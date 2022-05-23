from dataclasses import dataclass, field
from processes import BaseProcess

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
                self.base_process_list.append((row))
            # arrival time의 오름차순으로 정렬
            self.base_process_list.sort(key=lambda p: p.arrival)
            self.time_slice = int(f.readline())

    
    def add_input(self, inputs):
        row = inputs.split()
        row[1:] = map(int, row[1:])
        self.base_process_list.append(BaseProcess(*row))
    
    def sort_inputs(self,timeslice):
        self.base_process_list.sort(key=lambda p:p.arrival )
        self.time_slice = int(timeslice)

    def delete_all(self):
        self.base_process_list.clear()