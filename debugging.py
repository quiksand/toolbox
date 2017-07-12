import inspect

debug = True

def main():
    msg = Message()
    todo()

def todo(msg="Do something!"):
    def get_line_number():
        return inspect.currentframe().f_back.f_back.f_lineno
    def get_calling_function_name():
        return inspect.getframeinfo(inspect.currentframe().f_back.f_back).function
    if debug:
        print("TODO ({:4d}): {:.15}() - {}".format(get_line_number(), get_calling_function_name(), msg))
    else:
        pass

class Message():
    """Basic object that prints debug info to console"""
    def __init__(self):
        self.get_line_number()
        self.get_calling_function_name()
    def get_line_number(self):
        self.line_number =  inspect.currentframe().f_back.f_back.f_lineno
    def get_calling_function_name(self):
        self.calling_func = inspect.getframeinfo(inspect.currentframe().f_back.f_back).function

class Todo(Message):
    def __init__(self):
        Message.__init__()

if __name__ == '__main__':
    main()
