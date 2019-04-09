import pyautogui

#jpg파일은 매크로가 안된다.
#매크로를 만드려면 png 확장자로
folder = pyautogui.locateCenterOnScreen('folder.PNG')
print(folder)
pyautogui.click(folder[0], folder[1], clicks = 2)
