class Clock:
    def __init__(self,hours:int,minutes:int,seconds:int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0  
            self.hours += 1
        if self.hours == 24:
            self.hours = 0

    def set(self,hour,minute,second = 0):
        self.hours = hour
        self.minutes = minute
        self.seconds = second
        

    def __str__(self):
        """Return the time in MM:SS format."""
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)