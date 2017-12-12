QUERY_EXAMPLE_1 = """
    SELECT id, name
    FROM public.table
    WHERE name = %(name)s
"""

QUERY_EXAMPLE_2 = """
    SELECT name
    FROM {}.{}
"""

QUERY_EXAMPLE_3 = """
    SELECT name
    FROM public.table
"""

QUERY_EXAMPLE_4 = """
    SELECT name
    FROM {}.{}
    WHERE attribute IN %(values)s
"""

LOAD_EXAMPLE = """
    INSERT INTO
    public.table (id)
    values %s
"""
