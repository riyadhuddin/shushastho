url = 'https://www.dropbox.com/sh/0rmfi5or38gcvz2/AADtN2EC6CUzMiJ2OQgx11mMa?dl=0'
dropX = 'dvc remote add -d storage {}'
import os
os.system(dropX.format(url))