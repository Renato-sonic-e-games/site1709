import pyautogui
import time

# abrir o gugou cromi

pyautogui.press("win")
pyautogui.write("Google")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.write("http://127.0.0.1:5500/index.html")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.click(x=450, y=454)
pyautogui.write("nome nomeado por um nomeador que nomeiou e ainda nomeia e continuará nomeando")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("email@gmail.email")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("senha secreta (código kojima)")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.press("space")
pyautogui.press("tab")
pyautogui.press("enter")