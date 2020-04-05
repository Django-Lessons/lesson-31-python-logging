import argparse
from app.units import MB
from app.memory import Memory
from app.disk import Disk


def main():
    parser = argparse.ArgumentParser(prog='mgmail')
    parser.add_argument(
        "-m", "--memory", action="store_true"
    )
    parser.add_argument(
        "-d", "--disk", action="store_true"
    )
    parser.add_argument(
        "-v", "--verbosity", type=int
    )
    args = parser.parse_args()
    if args.memory:
        meminfo = Memory()
        print(meminfo.free(unit=MB))
    if args.disk:
        diskinfo = Disk()
        print(diskinfo.free())


if __name__ == "__main__":
    main()
