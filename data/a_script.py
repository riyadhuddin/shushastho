import os
files = os.listdir('hudredk_synthea_covid19_csv')
dvc = 'dvc add hudredk_synthea_covid19_csv/{}'
for f in files:
    #print(dvc.format(f))
    os.system(dvc.format(f))
