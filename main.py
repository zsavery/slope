from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

# x = np.random.randint(0, 20, 20)
# y = np.random.randint(5, 30, 20)
x = np.random.randint(0,20, 40)
y = np.random.randint(55,100, 40)

slope, intercept, r, p, std_err = stats.linregress(x, y)
def get_slope(arr):
    return slope * arr + intercept

my_model = list(map(get_slope, x))

plt.plot(x, my_model, 'b-')

plt.scatter(x, y)
plt.show()

print(get_slope(21))
print(f"Relationship: {r}")

my_line = np.linspace(0, 20, 20)
my_model2 = np.poly1d(np.polyfit(x, y, 3))
plt.plot(my_line, my_model2(my_line), 'r--')
plt.scatter(x, y)
plt.show()