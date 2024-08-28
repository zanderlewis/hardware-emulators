import time

class Clock:
    def __init__(self, timezone="UTC"):
        self.timezone = timezone
        self.time = time.time()
    
    def set_timezone(self, timezone):
        self.timezone = timezone
    
    def get_time(self, format="%Y-%m-%d %H:%M:%S"):
        t = time.time()
        # Adjust time based on timezone
        timezone = self.timezone
        if timezone == "UTC":
            pass
        elif timezone == "PST":
            t -= 8 * 3600
        elif timezone == "EST":
            t -= 5 * 3600
        else:
            pass
        return time.strftime(format, time.gmtime(t))
    
    def get_timezone(self):
        return self.timezone