import time,datetime
from functools import wraps

def timer(time):
    def timer_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            task(func,time)
            return func(*args, **kwargs)
        return wrapper
    return timer_decorator
 

def task(func,run_time):
    run_time = ' '.join([str(datetime.datetime.now().date()),run_time])
    run_time = datetime.datetime.strptime(run_time,'%Y-%m-%d %H:%M:%S')
    now_time = datetime.datetime.now().replace(microsecond=0)
    delay_time = (run_time - now_time).seconds
    print("up to run time has %s second" %(delay_time))
    time.sleep(delay_time)
    print("begin to run task")
    return 0
