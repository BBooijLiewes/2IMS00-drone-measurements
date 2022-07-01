import csv
import os
import statistics

copters = [1,2]

for copter in copters:
    files =sorted(os.listdir(f'esp_copter_{copter}')) 
    print(f'Currently doing esp copter {copter}')
    for file in files:
         values = [] 
         filename = os.fsdecode(file)
         if filename.endswith(".csv"):
            degree = filename.split('_')[0]
            with open(f'esp_copter_{copter}/{filename}', 'r') as file:
                reader = csv.reader(file)
                header = False
                for row in reader:
                    if not header:
                        header = True
                        continue
                    value = int(row[1].replace('dBm', ''))
                    values.append(value)
            print(f'{degree}: {round(statistics.median(values),2)}')
         else:
             continue
    print('\n')
