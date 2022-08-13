import time

def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int((end - start)* 1000)} ms')
        return result

    return wrapper

@time_it
def some_op():
    print("Starting up")
    time.sleep(1)
    print('We are done')



if __name__ == '__main__':
    some_op()
    #time_it(some_op)()
