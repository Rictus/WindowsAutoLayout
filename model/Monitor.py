#
# class Monitor:
#     def __init__(self):
#         monitors = win32api.EnumDisplayMonitors()
#         self.monitor_handle, self.device_context_handle, (self.x, self.y, self.width, self.height) = monitors[0]
#         print(monitors)
#
#     @staticmethod
#     def iterate_monitors(callback, on_window_found):


import win32api
import win32con
import win32gui

hwin = win32gui.GetDesktopWindow()
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
print(width, height, left, top,hwin)
