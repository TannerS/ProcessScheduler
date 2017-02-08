# import sys
from FCFS import FCFS
from SF import  SF


def main(filename):
    print('Running First-come, first-served scheduler')
    # fcfs = FCFS(filename)
    # fcfs.execute()

    fs = SF(filename)
    fs.execute()




if __name__ == '__main__':
    # args = sys.argv
    # filename = str(args[0])
    filename = "input.csv"
    main(filename)
