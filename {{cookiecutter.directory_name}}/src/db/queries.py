QUERY_EXAMPLE_1 = """
    SELECT id, name
    FROM public.table
    WHERE name = %(name)s
"""

QUERY_EXAMPLE_2 = """
    SELECT name
    FROM {}.{}
"""

LOAD_EXAMPLE = """
    INSERT INTO
    public.table (id)
    values %s
"""

QUERY_EXAMPLE_3 = """
	SELECT name
	FROM public.table
"""
