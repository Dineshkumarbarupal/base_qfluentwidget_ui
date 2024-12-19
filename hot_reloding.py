from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys
import time

class ReloadHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            print("Detected change in code. Restarting...")
            os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    path = "."  # Watch the current directory
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        os.system("python main.py")  # Replace with your script
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
