import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


a = 0  # Нижня межа інтегрування
b = 2  # Верхня межа інтегрування

# розраховуємо площу фігури теоретично через визначений інтеграл
result, error = spi.quad(f, a, b)

# кількість точок випробування
experiment_qty = 100000

# формування випадкових точок випробування
x_list = list(np.random.uniform(a, b, experiment_qty))
y_list = list(np.random.uniform(0, 4, experiment_qty))

# "кидаємо камінці", рахуємо влучання в площу
i = 0
for x, y in zip(x_list, y_list):
    # print(x, y)
    if y <= f(x):
        i += 1

monte_karlo_squear = (i / experiment_qty) * ((f(b) - f(a)) * (b - a))

# виводимо результати розрахунків
print(f'\nПлоща фігури, розрахована теоретично через визначений інтеграл: {result}')
print(f'Площа прямокутника, в який вписана фігура = {b - a} x {f(b) - f(a)} = {(f(b) - f(a)) * (b - a)}')
print(f'Кількість випробувань: {experiment_qty}')
print(f'Кількість влучань у фігуру: {i}')
print(f'Частка влучань у фігуру: {i / experiment_qty}')
print(f'Площа фігури, розрахована практично методом Монте-Карло: {monte_karlo_squear}')
print(f'Відхилення результату за методом Монте-Карло від результату за методом визначних інтегралів: {round(monte_karlo_squear / result * 100 - 100)}%')

# Створення діапазону значень x для графіка
x = np.linspace(-0.5, 2.5, 300)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції та точок випробування
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

