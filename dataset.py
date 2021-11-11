import pandas as pd
import random as rd
import csv

filename = 'Fishing.csv'

def createDataSet(filename):
  data_set = {}
  value_of_datas = 100
  data_set['Status'] = [rd.randint(0, 1) for _ in range(value_of_datas)]
  data_set['Month'] = [rd.randint(1, 12) for _ in range(value_of_datas)]
  data_set['Weather'] = [rd.randint(0, 5) for _ in range(value_of_datas)]
  data_set['Fish'] = [rd.randint(1, 5) for _ in range(value_of_datas)]
  data_set['Tackle'] = [rd.randint(1, 3) for _ in range(value_of_datas)]

  frame = pd.DataFrame(data_set)
  print(frame.to_string())

  frame.to_csv(filename, index=False)

def readDataFromCSV(filename):
  
  csv_file = open(filename)
  csv_reader = csv.DictReader(csv_file)

  data = []

  for row in csv_reader:
    data.append(list(map(int, [row['Status'], row['Month'], row['Weather'], row['Fish'], row['Tackle']])))

  
  return data

createDataSet(filename)