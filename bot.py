import pyautogui
import subprocess
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID, kCGWindowListExcludeDesktopElements

# Запуск Firefox
subprocess.Popen(["/Applications/Firefox.app/Contents/MacOS/firefox-bin"])

# Очікування завантаження Firefox
firefox_window_title = "Mozilla Firefox"
active_window_title = ""

while active_window_title != firefox_window_title:
    window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly | kCGWindowListExcludeDesktopElements, kCGNullWindowID)
    for window in window_list:
        window_title = window.get("kCGWindowName", "")
        if window_title == firefox_window_title:
            active_window_title = window_title
            break

# Затримка для завантаження повного вікна Firefox
pyautogui.sleep(2)

# Відкриття налаштувань Firefox
url_settings = "about:preferences"
pyautogui.hotkey('command', 'l')  # Вибрати адресний рядок
pyautogui.typewrite(url_settings)  # Ввести URL
pyautogui.press('return')  # Натиснути клавішу Return

# Затримка, поки сторінка налаштувань Firefox завантажиться
pyautogui.sleep(2)
