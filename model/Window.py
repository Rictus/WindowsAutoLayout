import win32gui
import win32process

import win32con
import wmi


# TODO : Trouver sur quel ecran est la fenêtre
# TODO : Trouver sur quel bureau virtuel est la fenêtre
class Window:
    def __init__(self, hwnd):
        self.wmi = wmi.WMI()
        self.hwnd = hwnd
        self.threadId, self.pid = win32process.GetWindowThreadProcessId(self.hwnd)
        self.rect = win32gui.GetWindowRect(self.hwnd)
        self.text = win32gui.GetWindowText(self.hwnd)
        self.x = self.rect[0]
        self.y = self.rect[1]
        self.height = self.rect[3] - self.y
        self.width = self.rect[2] - self.x
        self.visible = not not win32gui.IsWindowVisible(self.hwnd)
        self.enabled = not not win32gui.IsWindowEnabled(self.hwnd)
        self.isWindow = not not win32gui.IsWindow(self.hwnd)
        self.isMinimize = not not win32gui.IsIconic(self.hwnd)
        self.application = False

    def compute_application(self):
        try:
            for p in self.wmi.query('SELECT * FROM Win32_Process WHERE ProcessId = %s' % str(self.pid)):
                self.application = {
                    "name": p.Name,
                    # "path": p.ExecutablePath
                }
                break
        except:
            pass

    # Lazy loading of application data
    def get_application_name(self):
        if self.application is False:
            self.compute_application()
        return self.application["name"]

    @staticmethod
    def iterate_windows(callback, on_window_found):
        win32gui.EnumWindows(callback, on_window_found)

    def set_geometry(self, x, y, width, height):
        self.normal()
        win32gui.MoveWindow(self.hwnd, x, y, width, height, True)

    def maximize(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_MAXIMIZE)
        self.isMinimize = not not win32gui.IsIconic(self.hwnd)

    def minimize(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_MINIMIZE)
        self.isMinimize = not not win32gui.IsIconic(self.hwnd)

    def normal(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_NORMAL)
        self.isMinimize = not not win32gui.IsIconic(self.hwnd)

    def is_workable(self):
        return len(self.text) > 0 \
               and self.visible \
               and self.enabled \
               and self.height > 0 \
               and self.width > 0

    def dict_output(self):
        return {
            "_": {
                "hwnd": self.hwnd,
                "threadId": self.threadId,
                "processId": self.pid
            },
            "dimensions": {
                "width": self.width,
                "height": self.height
            },
            "position": {
                "x": self.x,
                "y": self.y
            },
            "state": {
                "visible": self.visible,
                "enabled": self.enabled,
                "isWindow": self.isWindow,
                "minimize": self.isMinimize
            },
            "text": self.text,
            "application": self.application
        }

    def get_position(self):
        return self.x, self.y

    def get_dimensions(self):
        return self.width, self.height

    def get_pid(self):
        return self.pid

    def get_tid(self):
        return self.threadId
