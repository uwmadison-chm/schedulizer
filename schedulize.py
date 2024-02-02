"""Script to generate pseudorandom EMA schedules.

Main function schedulize takes a start Time, end Time, block length in minutes,
and a minumum separation between alerts in minutes. It returns an alert schedule
represented as a list of Times.

Usage example:

start_time = Time(7,30)
end_time = Time(19,30)
block_len = 120
min_separation = 30

schedule = schedulize(start_time, end_time, block_len, min_separation)
"""

from random import randint
from itertools import starmap

class Time:
    def __init__(self, hours=0, minutes=0):
        self._total_minutes = hours * 60 + minutes

    @property
    def hours(self):
        return (self._total_minutes // 60) % 24
    
    @property
    def minutes(self):
        return self._total_minutes % 60
    
    @property
    def total_minutes(self):
        return self._total_minutes
    
    def __repr__(self):
        return f'{self.hours}:{str(self.minutes).zfill(2)}'        
    
def schedulize(start: Time,
               num_alerts: int,
               block_len: int,
               min_separation: int
) -> list[Time]:
    """Generates a pseudorandom EMA schedule given constraints.
    
    Args:
        start:
            A Time object indicating the start of the time range
        num_alerts:
            An integer representing the number of alerts / blocks
            in the schedule.
        block_len:
            An integer representing the length of the block in
            minutes in which each alert may be sent.
        min_separation:
            An integer representing the minumum amount of separation
            in minutes between consecutive alerts.

    Returns:
        A list of Time objects representing the alert schedule.
    """

    end = Time(0, start.total_minutes + block_len * num_alerts)

    time_blocks = [(x, x + block_len) \
                   for x in range(start.total_minutes, end.total_minutes, block_len)]
    
    time_pts = list(starmap(get_random_time, time_blocks))

    while not are_valid_times(time_pts, min_separation):
        time_pts = list(starmap(get_random_time, time_blocks))
    
    return time_pts

def get_random_time(start_minutes: int, end_minutes: int) -> Time:
    rand_minutes = randint(start_minutes, end_minutes)
    return Time(0,rand_minutes)

def are_valid_times(times: list[Time], min_separation: int) -> bool:
    separations = [j.total_minutes - i.total_minutes for i, j in \
             zip(times[:-1], times[1:])]
    return all(x >= min_separation for x in separations)