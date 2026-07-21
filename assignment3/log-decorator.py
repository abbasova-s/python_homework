import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        pos_par = ()
        keyword_par = {}
        
        if args:
            pos_par = args
        else:
            pos_par = "none"
        
        if kwargs:
            keyword_par = kwargs
        else:
            keyword_par = "none"
        

        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_par}")
        logger.log(logging.INFO, f"keyword parameters: {keyword_par}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper
    
@logger_decorator
def func1 ():
    print("Hello, World!")

@logger_decorator
def func2 (*args):
    return True

@logger_decorator
def func3 (**kwargs):
    return logger_decorator

func1()
func2(3)
func3(name = "Alex")
