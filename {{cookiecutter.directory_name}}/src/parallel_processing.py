import math
import multiprocessing as mp

from joblib import Parallel, delayed


def do_work(item):
    sqrt = math.sqrt(item)
    return sqrt


def execute(n_jobs=None, backend='multiprocessing'):

    if n_jobs is None:
        n_jobs = mp.cpu_count()

    items = list(range(10))

    result = Parallel(n_jobs=n_jobs, backend=backend)(
                        delayed(do_work)(item) for item in items)

    return result
