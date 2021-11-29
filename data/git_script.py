import os
import re
files = os.listdir('hudredk_synthea_covid19_csv')
gitX = 'git add hudredk_synthea_covid19_csv/{} .gitignore'
regex = re.compile('(.*dvc$)')
#dvc = 'dvc add hudredk_synthea_covid19_csv/{}'
for f in files:
    if regex.match(f):
        #print(gitX.format(f))
        os.system(gitX.format(f))
