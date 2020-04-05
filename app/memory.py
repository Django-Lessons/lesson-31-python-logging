import re

MB = 'mb'
KB = 'kb'
BYTES = 'b'


class Memory:
    def __init__(self):
        self._total_kb = 0
        self._free_kb = 0

        self._read()

    def _read(self):
        with open("/proc/meminfo", "r") as f:
            lines = f.readlines()

        self._total_kb = self._extract(lines[0].strip())
        self._free_kb = self._extract(lines[1].strip())

    def _extract(self, line):
        if not line:
            return 0

        match = re.search(f"\d+", line)
        if match:
            return int(match.group(0))

    def free(self, unit=KB):
        if unit == KB:
            return self._free_kb

        if unit == MB:
            return self._free_kb / 1024
