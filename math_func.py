from functools import reduce
import math
def dot(v, w): # скалярное произведение векторов
  return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v): # квадрат модуля вектора
  return dot(v, v)

def vector_add(v,w): # сложение векторов
  return [v_i + w_i for v_i,w_i in zip(v, w)]

def scalar_multiply(c, v): # умножение вектора v на число c
  return [round(c * v_i) for v_i in v]

def vector_sum(vectors): # суммирование векторов из списка vectors
  return reduce(vector_add,vectors)

def mean(x): # среднее значение
  return sum(x)/len(x)

def vector_mean(vectors): # покомпонентное среднее
  return scalar_multiply(1/len(vectors), vector_sum(vectors))

def de_mean(x): # отклонения от среднего
  return [x_i - mean(x) for x_i in x]

def variance(x) : # дисперсия
  return sum_of_squares(de_mean(x))/(len(x)-1)

def standard_deviation(x): # стандартное отклонение
  return math.sqrt(variance(x))