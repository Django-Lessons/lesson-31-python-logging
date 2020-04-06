import logging
import argparse
from app.units import MB
from app.memory import Memory
from app.disk import Disk


logger = logging.getLogger(__name__)


def get_arguments():
    parser = argparse.ArgumentParser(
        description="""
        Print total and free memory/disk
        on local system
"""
    )
    parser.add_argument(
        "-m", "--memory", action="store_true"
    )
    parser.add_argument(
        "-d", "--disk", action="store_true"
    )
    parser.add_argument(
        "-v", "--verbosity",
        type=int,
        default=0
    )

    return parser.parse_args()


def main():
    args = get_arguments()

    if args.verbosity > 0:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
        level=level
    )

    if args.memory:
        logger.debug("Checking memory...")
        meminfo = Memory()
        print(meminfo.free(unit=MB))
        print(meminfo.total(unit=MB))

    if args.disk:
        diskinfo = Disk()
        print(diskinfo.free())
        print(diskinfo.total())


if __name__ == "__main__":
    main()
