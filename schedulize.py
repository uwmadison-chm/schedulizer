class Time:
    def __init__(self, hours, minutes):
        if hours not in range(0, 24):
            raise ValueError('hours must be in the range [0..23]')
        if minutes not in range(0, 60):
            raise ValueError('minutes must be in the range [0..59]')
        self._minutes = hours * 60 + minutes

    def __lt__(x,y):
        return x._minutes < y._minutes
        
    def __gt__(x,y):
        return x._minutes > y._minutes
    
    def __eq__(x,y):
        return x._minutes == y._minutes
    
    def __repr__(self):
        return f'{self._minutes // 60}:{str(self._minutes % 60).zfill(2)}'        

def schedulize(start: Time, end: Time):
    if not (isinstance(start, Time) and isinstance(end, Time)):
        raise TypeError("start and end must be instances of Time")
    
    