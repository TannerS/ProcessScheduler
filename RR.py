import queue
from Process import Process
from SchedulingAlgorithm import SchedulingAlgorithm

class RR(SchedulingAlgorithm):
    processes = None
    quantum = None

    def __init__(self, filename, quantum):
        super().__init__()
        self.processes = []
        self.quantum = quantum

        with open(filename) as file:
            for line in file:
                inputs = line.strip().split(',')
                pid = inputs[0]
                cycles = inputs[1]
                self.processes.append(Process(pid, cycles))

    def execute(self):
        size = len(self.processes)
        i = 0

        while len(self.processes) > 0:
            try:
                temp_cycles = self.processes[i].cycles
                temp_cycles -= int(self.quantum)

                if(temp_cycles < 0):
                    pos_cycle_offset = temp_cycles * -1
                    temp_cycles += pos_cycle_offset
                    self.processes[i].cycles = temp_cycles
                    self.cycles += pos_cycle_offset
                else:
                    self.processes[i].cycles = temp_cycles
                    self.cycles += self.quantum

                if (int(self.processes[i].cycles) <= 0):
                    print('Process ' + str(self.processes[i].pid) + ' finishes on cycle ' + str(self.cycles))
                    del self.processes[i]
                    self.turnover += self.cycles
                # above will move the current iteration into proper position so no need to increment i like we do below
                else:
                    i += 1
                    i %= len(self.processes)

            except Exception as e:
                print("Failure to run process: " + str(e))

        print("Average turnaround time: " + str(self.turnover / size))