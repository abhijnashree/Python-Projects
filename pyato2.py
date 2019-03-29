import pyautogui,time
loc1=list(pyautogui.locateOnScreen("cortana_search.png"))
loc2=pyautogui.center(loc1)
pyautogui.click(loc2)
pyautogui.typewrite("Notepad")
time.sleep(3)
pyautogui.hotkey("Enter")
time.sleep(3)
pyautogui.typewrite("Hello World")
