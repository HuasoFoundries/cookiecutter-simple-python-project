import multiprocessing
import pandas as pd
import numpy as np


def _apply_df(args):
    """
    To execute a pandas apply in a parallel way.
    """
    df, func, num, kwargs = args
    return num, df.apply(func, **kwargs)


def apply_by_multiprocessing(df, func, **kwargs):
    """
    To execute a pandas apply in a parallel way
    """
    workers = kwargs.pop('workers')
    pool = multiprocessing.Pool(processes=workers)
    result = pool.map(_apply_df, [(d, func, i, kwargs)
                      for i, d in enumerate(np.array_split(df, workers))])
    pool.close()
    return pd.concat([i[1] for i in result])


def calculate(df, threads):
    """
    TODO
    """
    df_normalize = apply_by_multiprocessing(df,
                                            score,
                                            axis=1,
                                            workers=threads)
    return df_normalize


def score(df):
    """
    TODO
    """
    df['z'] = df['x'] - df['y']

    return df
