def performance_test(exit_flag=True):
    """
    Performance wrapper
    Usage:
        from frame.data_inspection import performance_test

        @performance_test(True)
        def func():
            ...

    :param exit_flag: True(exit)/False(continue) if target function is over.
    """

    def func_layer(func):
        def wrapper(*args, **kwargs):
            from line_profiler import LineProfiler
            lp = LineProfiler()
            lpw = lp(func)  # function need to be analysed
            func_output = lpw(*args, **kwargs)  # the parameters of target function
            lp.print_stats()  # print analyse results
            if exit_flag:
                exit()
            return func_output

        return wrapper

    return func_layer


@performance_test()
def func_test():
    a = [i for i in range(10000)]
    b = sum(a)
    return b


if __name__ == '__main__':
    func_test()
