import glob
import pandas as pd

count_sample = 0

for file in glob.glob('./data/*'):
    count_sample += pd.read_csv(file).shape[0]
    print('{}: {}'.format(str(file)[5:][:-4], pd.read_csv(file).shape[0]))

print('final:' + str(count_sample))
    