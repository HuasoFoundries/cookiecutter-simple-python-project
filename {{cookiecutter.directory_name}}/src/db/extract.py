import psycopg2

import pandas as pd

from psycopg2 import sql

from . import queries as queries


def get_data_example_1(name, url):
    with psycopg2.connect(url) as conn:
        conn.autocommit = True
        result = pd.read_sql_query(
                      queries.QUERY_EXAMPLE_1,
                      params={'name': name},
                      con=conn)
        return result


def get_data_example_2(schema, table, url):
    with psycopg2.connect(url) as conn:
        conn.autocommit = True
        result = pd.read_sql_query(sql.SQL(queries.QUERY_EXAMPLE_2).
                                   format(sql.Identifier(schema),
                                          sql.Identifier(table)),
                                   con=conn)
        return result


def get_data_example_3(url):
    with psycopg2.connect(url) as conn:
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(queries.QUERY_EXAMPLE_3)
        result = cur.fetchall()
        return result


def get_data_example_4(name, url):
    with psycopg2.connect(url) as conn:
        conn.autocommit = True

        cur = conn.cursor()
        cur.execute(queries.QUERY_EXAMPLE_1,
                    vars={'name': name})
        rows = cur.fetchall()

        return rows


def get_data_example_5(schema, table, url):
    with psycopg2.connect(url) as conn:
        conn.autocommit = True

        cur = conn.cursor()

        cur.execute(sql.SQL(queries.QUERY_EXAMPLE_2).
                        format(sql.Identifier(schema),
                               sql.Identifier(table)))

        rows = cur.fetchall()

        return rows
