import psycopg2
import psycopg2.extras

from . import queries as queries
from io import StringIO


def load_data(data, url):

    with psycopg2.connect(url) as conn:
        conn.autocommit = True
        cur = conn.cursor()

        psycopg2.extras.execute_values(
            cur,
            queries.LOAD_EXAMPLE,
            data,
            template=None, page_size=100
        )


def load_data_pd(df, url):
    TABLE_OUTPUT = ''

    with psycopg2.connect(url) as conn:
        conn.autocommit = True

        cursor = conn.cursor()
        f = StringIO(df.to_csv(index=False,
                               header=False,
                               sep=';'))
        cursor.copy_from(f, TABLE_OUTPUT,
                         sep=';', null='')
