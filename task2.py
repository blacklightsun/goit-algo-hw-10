import matplotlib.pyplot as plt
import numpy as np

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа


experiment_qty = 1000
x_list = list(np.random.uniform(a, b, experiment_qty))
y_list = list(np.random.uniform(0, 5, experiment_qty))

i = 0
for x, y in zip(x_list, y_list):
    # print(x, y)
    if y <= f(x):
        i += 1

print(f'Кількість влучань: {i / experiment_qty}')

# plt.scatter(x_list, y_list)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 300)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)
ax.scatter(x_list, y_list)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

