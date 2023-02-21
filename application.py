from itertools import groupby
from controller import WorkerController
from utils import reader
import sys


lines = reader.read_file(sys.argv[1])
lines.sort()

workers = [
    {key: [work_day.split("=")[1] for work_day in list(group)]}
    for key, group in groupby(lines, key=lambda x: x.split("=")[0])
]

WorkerController(workers).present()
