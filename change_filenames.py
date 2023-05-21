import time
import pandas as pd
import os
import datetime
import shutil
import win32com.client
print('Input filename conversion list with path (ex. C:\\Users\\user\\beforeafter.csv )')
list = input('>> ')
Dir=os.path.basename(os.path.dirname(list))
df=pd.read_csv(list, encoding='shift-jis', header=0, engine='python')
OriginalFileNames=[]
NewFileNames=[]
OriginalFileNames=df['before'].to_list()
NewFileNames=df['after'].to_list()
for OriginalFileName, NewFileName in zip(OriginalFileNames, NewFileNames):
    PathOriginalFileNameBk = 'sample_filename_change//ORIGINAL_'+OriginalFileName
    PathOriginalFileName = 'sample_filename_change//'+OriginalFileName
    PathNewFileName = 'sample_filename_change//'+NewFileName
    shutil.copyfile(PathOriginalFileName, PathOriginalFileNameBk)
    os.rename(PathOriginalFileName, PathNewFileName)
os.startfile(Dir, operation='open')