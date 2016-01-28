import time


def autolog(message, from_func=None):
    "Automatically log the current function details."
    import inspect, logging
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    if not from_func:
        from_func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logging.debug("-" * 40)
    logging.debug("  %s  %s in %s:%i" % (
        message, 
        from_func.co_name,
        from_func.co_filename.split("/")[-1],
        from_func.co_firstlineno
    ))

    # TODO: find a way to print when executed from console instead of command line
    # print "%s: %s in %s:%i" % (
    #     message, 
    #     from_func.co_name,
    #     from_func.co_filename,
    #     from_func.co_firstlineno
    # )


def timeit_comma(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r), %2.2f,' %
              (method.__name__, args, kw, te-ts),)
        return result

    return timed


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r), %2.2f,' %
              (method.__name__, args, kw, te-ts))
        autolog('%r (%r, %r) %2.2f sec' %
                (method.__name__, args, kw, te-ts))

        return result

    return timed


def add_if_exists(update_dict, key, results):

    if results:
        update_dict[key] = results

    return update_dict


def remove_first(generator, default=None):
    """This function only works once for each generator
    - because it pops returned items from generator"""
    if generator:
        for item in generator:
            return item
    return default


def ResultIter(cursor, arraysize=1000000):
    'An iterator that uses fetchmany to keep memory usage down'
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result


class MaxLogger:

    def __init__(self, error_max=5):

        self.error_max = error_max
        self.error_counts = dict()
        self.suppress_logging = False

    def error(self, message):
        import inspect
        from_func = inspect.currentframe().f_back.f_code
        if self.error_counts.get(message):
            if self.error_counts[message] < self.error_max:
                autolog(message, from_func)
                self.error_counts[message] += 1
            elif not self.suppress_logging:
                autolog('Max reached, suppressing ' + message, from_func)
                self.suppress_logging = True
        else:
            autolog(message, from_func)
            self.error_counts[message] = 1



