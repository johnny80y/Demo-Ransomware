import ctypes

def desktop_changer():
    path = "meow_tmp.png"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

desktop_changer()

print("Script executed. Now terminating.")