class Process:
    pid = None
    cycles = None

    def __init__(self, pid, cycles):
        self.pid = pid
        self.cycles = cycles

    # def __str__(self):
    #     return (str(self.pid) + " : " + str(self.cycles))

    def __repr__(self):
        return repr((self.pid, self.cycles))