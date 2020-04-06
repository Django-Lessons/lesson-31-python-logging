import logging
import re
from app.units import (MB, KB)

logger = logging.getLogger(__name__)


class Memory:
    def __init__(self):
        self._total_kb = 0
        self._free_kb = 0
        logger.debug("Memory class instanciated")
        self._read()

    def _read(self):
        with open("/proc/meminfo", "r") as f:
            lines = f.readlines()

        self._total_kb = self._extract(lines[0].strip())
        self._free_kb = self._extract(lines[1].strip())

    def _extract(self, line):
        logger.debug(f"_extracting from **{line}**")

        if not line:
            return 0

        logger.debug(f"searching digits in **{line}**")
        match = re.search("\d+", line)

        if match:
            logger.debug("matched!")
            return int(match.group(0))

    def free(self, unit=KB):
        if unit == KB:
            return self._free_kb

        if unit == MB:
            return self._free_kb / 1024

    def total(self, unit=KB):
        if unit == KB:
            return self._total_kb

        if unit == MB:
            return self._total_kb / 1024
