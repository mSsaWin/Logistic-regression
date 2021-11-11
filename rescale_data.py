from math_func import *
from dataset import *
from copy import deepcopy

def scale(data):
  return vector_mean(data), [round(standard_deviation([vector[i] for vector in data])) for i in range (len(data[0]))] 

def rescale(data):
  means, s_devs = scale(data)
  rescaled = deepcopy(data)

  for vector in rescaled:
    for i in range(len(vector)):
      
      if s_devs[i] > 0:
        vector[i] = round((vector[i] - means[i]) / s_devs[i])
  
  return rescaled

fishing_data = readDataFromCSV(filename)

rescale_data = rescale(fishing_data)

print("Check scale:",scale(rescale_data))
print("\nRescale data: ")

for vector in rescale_data:
  print(vector)