import logging

def log_funcation_call(func):
  def decorated(*args, **kwargs):
    logging.info(f"calling {func.__name__} with arge={args}, kwargs={kwargs}")
    result = func(*args, **kwargs)
    logging.info(f"{func.__name__} returned {result}")
    return result
  return decorated
@log_funcation_call
def my_funcation(a, b):
  return a + b
    
