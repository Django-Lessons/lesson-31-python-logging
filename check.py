from app.memory import (Memory, MB)


def main():
    meminfo = Memory()
    print(meminfo.free(unit=MB))


if __name__ == "__main__":
    main()
