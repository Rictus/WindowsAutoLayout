import json

from model.Window import Window


def write_json(data):
    with open('./data.json', 'w+') as outfile:
        json.dump(data, outfile)


applications_exclusion_list = []


def callback(hwnd, cb):
    w = Window(hwnd)
    if w.is_workable():
        cb(w)
    else:
        cb(False)


def main():
    def on_window_found(w):
        if not w:
            pass
        else:
            windows.append(w)

    windows = []
    Window.iterate_windows(callback, on_window_found)
    for window in windows:
        print(window.get_application_name())
        # if window.get_application_name() == "pycharm.exe":
        #     window.set_geometry(0, 0, 600, 600)


if __name__ == '__main__':
    main()
