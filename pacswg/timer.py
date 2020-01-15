import time

seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
def get_time_in_secs(s):
    """get_time_in_secs converts the string given to seconds, e.g. 1h is converted to 3600.
    
    :param s: input string of the format "Nu" where N is a number and u is a unit (s/m/h/d/w).
    :type s: string
    :return: Number of seconds
    :rtype: float
    """    
    return float(s[:-1]) * seconds_per_unit[s[-1]]

class TimerClass:
    """TimerClass is an object that can help with timing different components of the execution.
    
    :return: TimerClass object
    :rtype: object
    """    
    def __init__(self):
        self.tic()

    def tic(self):
        """tic resets the starting time fo the timer. toc() will get seconds past since calling tic().
        """        
        self.start_time = time.time()

    def toc(self):
        """toc calculates the number of seconds passed since tic() has been called, or object has been created,
            whichever is more recent.
        
        :return: elapsed time since time reference
        :rtype: float
        """        
        elapsed = time.time() - self.start_time
        return elapsed

    def toc_str(self):
        """toc_str returns the time elapsed in string with 2 digits of precision.
        This is for user printing mainly.
        
        :return: number of seconds elapsed with 2 digits of precision.
        :rtype: string
        """        
        elapsed = time.time() - self.start_time
        return '{:4.02f}'.format(elapsed)
    
    def toc_print(self):
        """toc_print prints the value returned by toc_str
        
        :return: number of seconds elapsed with 2 digits of precision.
        :rtype: string
        """        
        print(self.toc_str())
        return self.toc()

if __name__ == '__main__':
    import random

    timer = TimerClass()
    timer.tic()
    print('starting...')
    time.sleep(random.random() * 10)
    print('elapsed time:', timer.toc_str())

