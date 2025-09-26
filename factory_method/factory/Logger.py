import datetime

class Logger:

    def __init__(self, logfile="factory_log.txt"):
        self.logfile = logfile

    def log(self, message:str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")