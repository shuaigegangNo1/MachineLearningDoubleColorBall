import os
import sys
from com.sgg.mldcb.util.ConstUtil import const
BASE_DIR = os.path.dirname(__file__)  # acquire direct path
print(BASE_DIR)
fileList = os.listdir(BASE_DIR)  # show all files in a folder
print(fileList)
os.chdir(const.project_path)
filelist1=os.listdir()
print(filelist1[2])
# file_path=os.path.dirname(filelist1[2])
# print("file_path",file_path)
path = sys.path[1]
print("path",path)