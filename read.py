import os
import pandas as pd

x = os.popen('echo %cd%').read()
_path = str(x)[:len(str(x))-1] + "\\mails.xlsx"

df = pd.read_excel(_path)

for i in df.index:
	print(df['mails'][i])
