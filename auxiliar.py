import pyautogui
import time
import pandas as pd


time.sleep(4)
print(pyautogui.position())

Tabela = pd.read_csv("produtos.csv")
