import pyautogui
import time
import pandas as pd


time.sleep(4)
print(pyautogui.position()) #Usamos isso para descobrir a posição de X e Y do cursor.

Tabela = pd.read_csv("produtos.csv")
