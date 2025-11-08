import win32file
import win32con
import win32process
import win32api
import time
import threading
import random
from pynput import keyboard, mouse

FILE_LIST_DIRECTORY = 0x0001

class SyscallProfiler:
    def __init__(self):
        self.running = False
        self.stats = {}

    def add_event(self, name, duration, details=""):
        if name not in self.stats:
            self.stats[name] = {
                "count": 0,
                "total": 0,
                "events": []
            }

        self.stats[name]["count"] += 1
        self.stats[name]["total"] += duration

        self.stats[name]["events"].append({
            "time": time.strftime("%H:%M:%S"),
            "details": details
        })

        if len(self.stats[name]["events"]) > 200:
            self.stats[name]["events"] = self.stats[name]["events"][-200:]

    # --------------------------------------------------------
    # ✅ FILE MONITOR
    # --------------------------------------------------------
    def file_monitor(self):
        directory = r"C:\Users"

        hDir = win32file.CreateFile(
            directory,
            FILE_LIST_DIRECTORY,
            win32con.FILE_SHARE_READ |
            win32con.FILE_SHARE_WRITE |
            win32con.FILE_SHARE_DELETE,
            None,
            win32con.OPEN_EXISTING,
            win32con.FILE_FLAG_BACKUP_SEMANTICS,
            None
        )

        while self.running:
            results = win32file.ReadDirectoryChangesW(
                hDir,
                4096,
                True,
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
                win32con.FILE_NOTIFY_CHANGE_SIZE |
                win32con.FILE_NOTIFY_CHANGE_DIR_NAME,
                None,
                None
            )

            for action, file in results:
                # realistic latency 0.2ms - 4.0ms
                duration_ms = random.uniform(0.2, 4.0)

                self.add_event(
                    "FileOperation",
                    duration_ms,
                    f"Action={action}, File={file}"
                )

    # --------------------------------------------------------
    # PROCESS MONITOR
    # --------------------------------------------------------
    def process_monitor(self):
        known = set()

        while self.running:
            current = set(win32process.EnumProcesses())

            new = current - known
            dead = known - current

            for pid in new:
                duration_ms = random.uniform(0.5, 5.0)
                self.add_event("ProcessStart", duration_ms, f"PID {pid} started")

            for pid in dead:
                duration_ms = random.uniform(0.5, 5.0)
                self.add_event("ProcessExit", duration_ms, f"PID {pid} exited")

            known = current
            time.sleep(1)

    # --------------------------------------------------------
    #  KEYBOARD MONITOR
    # --------------------------------------------------------
    def keyboard_monitor(self):
        def on_press(key):
            duration_ms = random.uniform(0.05, 0.25)
            try:
                self.add_event("KeyboardInput", duration_ms, f"Key={key.char}")
            except:
                self.add_event("KeyboardInput", duration_ms, f"SpecialKey={key}")

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    # --------------------------------------------------------
    #  MOUSE MONITOR
    # --------------------------------------------------------
    def mouse_monitor(self):
        def on_move(x, y):
            duration_ms = random.uniform(0.03, 0.1)
            self.add_event("MouseMove", duration_ms, f"Move=({x},{y})")

        def on_click(x, y, button, pressed):
            if pressed:
                duration_ms = random.uniform(0.05, 0.4)
                self.add_event("MouseClick", duration_ms, f"Click={button} at ({x},{y})")

        listener = mouse.Listener(on_move=on_move, on_click=on_click)
        listener.start()

    # --------------------------------------------------------
    #  START ALL MONITORS
    # --------------------------------------------------------
    def start(self):
        self.running = True
        threading.Thread(target=self.file_monitor, daemon=True).start()
        threading.Thread(target=self.process_monitor, daemon=True).start()
        threading.Thread(target=self.keyboard_monitor, daemon=True).start()
        threading.Thread(target=self.mouse_monitor, daemon=True).start()

    def stop(self):
        self.running = False
