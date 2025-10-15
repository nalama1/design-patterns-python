import os
import datetime
from typing import Optional

class Logger:
    """
    Class responsible for logging events to a log file.
    Automatically creates the 'audit' folder if it does not exist
    """

    def __init__(self, base_dir: Optional[str]=None, filename:str = "factory_log.txt"):
        # Uses the provided base directory or the current file's directory.
        self.base_dir = base_dir or os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.audit_dir = os.path.join(self.base_dir, "audit")
        os.makedirs(self.audit_dir, exist_ok= True)

        self.logfile = os.path.join(self.audit_dir, filename)

    def log(self, message:str) -> None:
        """ Writes a timestamped message to the log file."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(self.logfile, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {message}\n")
        except (OSError, IOError) as e:
            print(f"[Logger Error] Could not write to log: {e}")


