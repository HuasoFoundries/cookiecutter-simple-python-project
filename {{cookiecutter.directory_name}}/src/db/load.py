import psycopg2
import psycopg2.extras

from . import queries as queries


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
