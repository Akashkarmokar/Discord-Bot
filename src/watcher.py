from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        if event.event_type in ('modified', 'created', 'deleted'):
            print(f'Reloading due to {event.event_type} in {event.src_path}')
            self.reload_script()

    def reload_script(self):
        script_path = os.path.join('src', 'main.py')
        subprocess.run(['python', script_path])

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='src', recursive=True)  # Adjust the path as needed
    observer.start()

    # Start the main script initially
    event_handler.reload_script()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
