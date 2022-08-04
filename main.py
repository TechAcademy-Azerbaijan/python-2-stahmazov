#  args kwargs

from datetime import datetime
from multiprocessing.sharedctypes import Value
from os.path import exists

if not exists('sample.txt'):
    with open('sample.txt', 'a') as f:
        f.write('Function name | worked time | arguments as list | arguments as dictionary | function result\n')

def logger(f):
    """Write task solution here"""
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except ZeroDivisionError as e:
            result = f'ZeroDivisionError: {e}'
        except TypeError as e:
            result = f'TypeError: {e}'
        except ValueError as e:
            result = f'ValueError: {e}'
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")     
         
        with open('sample.txt', 'a') as file:
            if kwargs and args:
                file.write(f'{f.__name__} | {date} | {args} | {kwargs} | {result}\n')
            elif args:
                file.write(f'{f.__name__} | {date} | {args} |          | {result}\n')
            else:
                file.write(f'{f.__name__} | {date} |        | {kwargs} | {result}\n')
            
        
    return wrapper


@logger
def sum(a,b):
    return a+b

@logger
def divide(a,b):
    return a/b
        

sum(1,2)
divide(a=4,b=2)
divide(10,0)
sum(1,'a')
sum(1,b=2)