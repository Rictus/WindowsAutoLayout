import json
import os
import time

from model.Window import Window


def write_json(data):
    with open('./data.json', 'w+') as outfile:
        json.dump(data, outfile)


applications_exclusion_list = [
    "ApplicationFrameHost.exe",
    "explorer.exe",
    "SystemSettings.exe"
]


def callback(hwnd, windows):
    w = Window(hwnd)
    if w.is_workable():
        name = w.get_application_name()
        if name not in applications_exclusion_list:
            windows.append(w)
            print("["+str(w.get_pid())+"/"+str(w.get_tid())+"]","Program", name, "open :\t At", w.get_position(), " Dimensions ", w.get_dimensions())
        else:
            print("["+str(w.get_pid())+"/"+str(w.get_tid())+"]","Program", name, "excluded.")


def main():
    windows = []
    Window.iterate_windows(callback, windows)
    jsons = []
    for window in windows:
        jsons.append(window.dict_output())
        # window.set_geometry(0, 0, 600, 600)
    write_json(jsons)


def loop():
    while True:
        windows = []
        Window.iterate_windows(callback, windows)
        time.sleep(2)
        os.system('cls');


if __name__ == '__main__':
    main()
