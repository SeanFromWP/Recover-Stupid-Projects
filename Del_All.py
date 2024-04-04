# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:26:49 2024

@author: Sean
"""
import os
#Recover batch files open while turn on
require = str(input(
'''You want to delete:\n
.) Proj Wink
1) Rickroll
2) Shutdown
3) Stuck
M) Proj Memories
X) Proj Mix
So what do you want to delete:_'''))
Options = {"1": "Rick.bat","2": "Shut.bat", "3": "Stuck.bat", "M": "Memories.bat", "X": "Mix.py"}
os.system('cd %AppData%\Microsoft\Windows\Start Menu\Programs\Startup')
for char in require:
    if char.isalnum():
        files = Options.get(char.upper())  # 將字母或數字轉換為大寫並獲取對應的值
        if files is not None:
            os.system('cd %AppData%\Microsoft\Windows\Start Menu\Programs\Startup')
            os.system(f"del {files}")
            print(f"{files}已經刪除")
        else:
            print(f"{files}XD")