import pyautogui
import time

print("5초 후에 마우스 위치를 캡처합니다. 원하는 위치에 마우스를 놓으세요.")
time.sleep(5)
x, y = pyautogui.position()
print(f"({x}, {y})")
