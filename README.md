# Python  :snake:

We require you to solve the following tasks. Remember to read the requirements first.

#### Topics you need to know and use to solve tasks

* Working with files
* Exception handling
* Decorators in Python

**Final Notes**: *Remember to solve and send assignments on time* :hourglass_flowing_sand:

# Assignments' list 

## Assignment 1  :star:  :star:  :star:  :star:  :star2:

### Description

The ```sum``` and ```divide``` functions are given.

You must complete a decorator named ```@logger```.

The following information about the functions used by the decorators should be written in the form of logs in the file.

* names of function
* arguments
* call date
* function results
* error messages (if any)

Example:

![result](https://i.ibb.co/gtxVjnb/screenshot-docs-google-com-2020-09-03-15-37-01.png)

```
def logger(f):
    “““Write task solution here”””
    pass

@logger
def sum(a,b):
    return a+b

@logger
def divide(a,b):
    return a/b


sum(1,2)

divide(a=4,b=2)

divide(10,0)
```

**Powered by [TechAcademy](https://www.tech.edu.az/)**

