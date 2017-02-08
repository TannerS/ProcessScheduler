import queue
from Process import Process
from SchedulingAlgorithm import SchedulingAlgorithm

class FCFS(SchedulingAlgorithm):
    queue = None

    def __init__(self, filename):
        super().__init__()
        self.queue = queue.Queue()
        # http://stackoverflow.com/questions/17949508/python-read-all-text-file-lines-in-loop
        with open(filename) as file:
            for line in file:
                # http://stackoverflow.com/questions/4319236/remove-the-newline-character-in-a-list-read-from-a-file
                inputs = line.strip().split(',')
                pid = inputs[0]
                cycles = inputs[1]
                self.queue.put(Process(pid, cycles))

    def execute(self):
        size = self.queue.qsize()

        while not self.queue.empty():
            try:
                process = self.queue.get(block=False)
                self.cycles += int(process.cycles)
                self.turnover += self.cycles
                print('Process ' + str(process.pid) + ' finishes on cycle ' + str(self.cycles))
            except Exception as e:
               print("Failure to run process: " + str(e))

        print("Average turnaround time: " + str(self.turnover / size))



