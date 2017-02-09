import queue
from Process import Process
from SchedulingAlgorithm import SchedulingAlgorithm

class SF(SchedulingAlgorithm):
    processes = None

    def __init__(self, filename):
        super().__init__()
        self.processes = queue.Queue()
        list = []

        with open(filename) as file:
            for line in file:
                inputs = line.strip().split(',')
                pid = inputs[0]
                cycles = inputs[1]
                list.append(Process(pid, cycles))

        list = (sorted(list, key=lambda process: int(process.cycles)))

        for i in range(len(list)):
            self.processes.put(list[i])

    def execute(self):
        size = self.processes.qsize()

        while not self.processes.empty():
            try:
                process =  self.processes.get_nowait()
                self.cycles += int(process.cycles)
                self.turnover += self.cycles
                print('Process ' + str(process.pid) + ' finishes on cycle ' + str(self.cycles))
            except Exception as e:
               print("Failure to run process: " + str(e))

        print("Average turnaround time: " + str(self.turnover / size))



