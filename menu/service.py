def database_debug(func):
    def inner_func(*args, **kwargs):
        from django.db import connection
        from django.db import reset_queries
        reset_queries()
        res = func(*args, *kwargs)
        query_info = connection.queries
        print('function_name: {}'.format(func.__name__))
        print('query_count: {}'.format(len(query_info)))
        # queries = ['{}\n'.format(query['sql']) for query in query_info]
        # print('queries: \n{}'.format(''.join(queries)))
        return res

    return inner_func
