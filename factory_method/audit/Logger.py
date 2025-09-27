import datetime, os

class Logger:

    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        audit_dir = os.path.join(base_dir, "audit")
        os.makedirs(audit_dir, exist_ok=True)
        self.logfile = os.path.join(audit_dir, "factory_logs.txt")

        # os.makedirs("audit", exist_ok=True)
        # self.logfile = os.path.join("audit", "factory_logs.txt")


    def log(self, message:str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")