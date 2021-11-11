import math
from math_func import *

def logistic(x1):
  return 1/(1 + math.exp(-x1))

def logistic_prime(x1):
  return logistic(x1) * (1 - logistic(x1))

def negative_log_likelihood(x1, y1, beta):
  if y1 == 1:
    return -math.log(logistic(dot(x1, beta)))
  else:
    return -math.log(1 - logistic(dot(x1, beta)))

def sum_negative_log_likelihood(x1, y1, beta):
  return sum(negative_log_likelihood(x_i, y_i, beta) for x_i, y_i in zip(x1, y1))

def negative_log_partial_j(x1, y1, beta, j):
  return -(y1- logistic(dot(x1, beta))) * x1[j]

def negative_log_gradient(x1, y1, beta):
  return [negative_log_partial_j(x1, y1, beta, j) for j in range(len(beta))]

def sum_negative_log_gradient(x, y, beta):
  return vector_sum([negative_log_gradient(x_i, y_i, beta) for x_i, y_i in zip(x, y)])