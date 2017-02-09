# import sys
from FCFS import FCFS
from SF import  SF
from RR import RR
from R import R

def main(filename):
    print('Running First-come, first-served scheduler')
    fcfs = FCFS(filename)
    fcfs.execute()
    print()

    print("Running shortest first scheduler.")
    fs = SF(filename)
    fs.execute()
    print()

    print("Running round robin scheduler with quantum 50")
    rr = RR(filename, 50)
    rr.execute()
    print()

    print("Running round robin scheduler with quantum 100")
    rr = RR(filename, 100)
    rr.execute()
    print()

    print("Running random scheduler with quantum 50")
    r = R(filename, 50)
    r.execute()

if __name__ == '__main__':
    # args = sys.argv
    # filename = str(args[0])
    filename = "input.csv"
    main(filename)
