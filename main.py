from rescale_data import *
from logistic_regression_func import *
import matplotlib.pyplot as plt
def split_data(data, prob):
  copy_data = deepcopy(data)

  rd.shuffle(copy_data)
  cut = int(len(copy_data) * prob)

  return copy_data[:cut], copy_data[cut:]

def train_test_split(x, y, test_pct):
  indexes = [i for i in range(len(x))]
  train_indxs, test_indxs = split_data(indexes, 1 - test_pct)

  return ([x[i] for i in train_indxs],
          [x[i] for i in test_indxs],
          [y[i] for i in train_indxs],
          [y[i] for i in test_indxs])

x = [[1] + row[1:] for row in rescale_data]
y = [row[0] for row in fishing_data]

rd.seed(0)

x_train, x_test, y_train, y_test =  train_test_split(x, y, 0.2)

beta = [rd.random() for _ in range(5)]
learning_rate = 0.01

for _ in range(5000):
  gradient = sum_negative_log_gradient(x_train, y_train, beta)
  bеtа = gradient_step(beta, gradient, -learning_rate)

print("Beta:", beta)

true_positives = false_positives = true_negatives = false_negatives = 0

for x_i, y_i in zip(x_test, y_test):
  prediction = logistic(dot(beta, x_i))

  if y_i == 1 and prediction >= 0.5:
    true_positives += 1
  elif y_i == 1:
    false_negatives += 1
  elif prediction >= 0.5:
    false_positives += 1
  else:
    true_negatives += 1

precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)

print("Precision:", precision)
print("Recall:", recall)

predictions = [logistic(dot(beta, x_i)) for x_i in x_test]
plt.scatter(predictions, y_test, marker= '+')
plt.xlabel("Предсказанная вероятность")
plt.ylabel("Фактический результат")
plt.title("Логистическая регрессия: предсказания и факт")
plt.show() 