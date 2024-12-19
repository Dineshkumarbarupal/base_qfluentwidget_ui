from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys
import subprocess
import time
from threading import Timer

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.timer = None  # Timer to manage delay
        self.wait_time = 10  # Wait time in seconds after a change before execution

    def on_any_event(self, event):
        # If it's a Python file change
        if event.src_path.endswith(".py"):
            print("Change detected. Waiting for further changes...")

            # If there is an existing timer, cancel it
            if self.timer is not None:
                self.timer.cancel()

            # Set a new timer to run after 10 seconds of no further changes
            self.timer = Timer(self.wait_time, self.run_code)
            self.timer.start()

    def run_code(self):
        """Function to run the code after the waiting period"""
        print("No further changes detected. Restarting...")
        subprocess.run(['python', 'c:/Users/NSG/Desktop/base ui/practice/ui_practice.py'])  # Change to your script path

if __name__ == "__main__":
    path = "."  # Watch the current directory
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        subprocess.run(['python', 'c:/Users/NSG/Desktop/base ui/practice/ui_practice.py'])  # Initial run
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
