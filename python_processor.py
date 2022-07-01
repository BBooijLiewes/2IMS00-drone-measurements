import csv
import os
import statistics

distances = [20,40, 100]

for distance in distances:
    files =sorted(os.listdir(f'{distance}_cm')) 
    print(f'Currently doing esp copter with distance {distance} cm')
    for file in files:
         values = [] 
         filename = os.fsdecode(file)
         if filename.endswith(".csv"):
            degree = filename.split('_')[0]
            with open(f'{distance}_cm/{filename}', 'r') as file:
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
