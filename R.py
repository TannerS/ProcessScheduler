from Process import Process
from SchedulingAlgorithm import SchedulingAlgorithm
from random import randint


class R(SchedulingAlgorithm):
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

        index = -1

        while len(self.processes) > 0:
            try:
                # http://stackoverflow.com/questions/1761626/weighted-random-numbers
                total_weight = 0
                for process in self.processes:
                    total_weight += process.cycles

                ran = randint(0, total_weight)

                for i in range(0, len(self.processes)):
                    if ran < self.processes[i].cycles:
                        index = i
                        break
                    ran -= int(self.processes[i].cycles)



                temp_cycles = self.processes[index].cycles
                temp_cycles -= int(self.quantum)

                if(temp_cycles < 0):
                    pos_cycle_offset = temp_cycles * -1
                    temp_cycles += pos_cycle_offset
                    self.processes[index].cycles = temp_cycles
                    self.cycles += pos_cycle_offset
                else:
                    self.processes[index].cycles = temp_cycles
                    self.cycles += self.quantum

                if (int(self.processes[index].cycles) <= 0):
                    print('Process ' + str(self.processes[index].pid) + ' finishes on cycle ' + str(self.cycles))
                    del self.processes[index]
                    self.turnover += self.cycles

            except Exception as e:
                print("Failure to run process: " + str(e))

        print("Average turnaround time: " + str(self.turnover / size))