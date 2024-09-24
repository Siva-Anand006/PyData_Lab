class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        """Increment the stopwatch by one second."""
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0  # Reset after 59:59

    def __str__(self):
        """Return the time in MM:SS format."""
        return f"{self.minutes:02}:{self.seconds:02}"

# Example usage
watch = Stopwatch()

for i in range(3600):
    print(watch)
    watch.tick()