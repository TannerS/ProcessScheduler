import sys
from FCFS import FCFS


def main(filename):
    print('Running First-come, first-served scheduler')
    fcfs = FCFS(filename)
    fcfs.execute()


if __name__ == '__main__':
    # args = sys.argv
    # filename = str(args[0])
    filename = "input.csv"
    main(filename)
