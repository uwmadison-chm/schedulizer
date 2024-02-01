class Time:
    hours: int
    minutes: int

    def __lt__(x,y):
        return x.hours < y.hours or \
            (x.hours == y.hours and x.minutes < y.minutes)
    
    def __gt__(x,y):
        return x.hours > y.hours or \
            (x.hours == y.hours and x.minutes > y.minutes)
    
    def __eq__(x,y):
        return x.hours == y.hours and x.minutes == y.minutes


def schedulize(start: Time, end: Time):
    pass