# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску.
# Отметьте положение ферзя и атакуемые клетки цветами.

import numpy as np
import matplotlib.pyplot as plt

'''
x = np.array([5, 10, 15, 20, 25])
y = np.array([43, 21, 63, 7, 39])

mat.plot(x, y, color='orange', marker='o', markersize=7, linestyle='dashed', linewidth=15)
mat.title('AAAAAAAAAAAAAAAAAAAA')
#mat.plot(x, y, 'go--', linewidth=2, markersize=12)
mat.plot(x, y, color='blue', marker='o', linestyle='dashed',
     linewidth=0.5, markersize=12)
mat.xlabel('ось Х')
mat.ylabel('ось Y')
mat.show()
'''

'''
categories = np.array(['a', 'b', 'c'])
values = np.array([3, 7, 4])
'''

'''
x = np.linspace(-10, 10, 100)  # 100 точек от -10 до 10
y1 = np.sin(x)
y2 = np.cos(x)

# Построение графиков
plt.plot(x, y1, label="sin(x)", color="blue")
plt.plot(x, y2, label="cos(x)", color="green")

# Настройка
plt.title("Графики sin(x) и cos(x)")
plt.xlabel("Значения X")
plt.ylabel("Значения Y")
#plt.legend()
plt.grid(True)  # Сетка на графике
plt.show()
'''

a = list()
for i in range(8):
    if i % 2 == 0:
        a.append([1, 0, 1, 0, 1, 0, 1, 0])
    else:
        a.append([0, 1, 0, 1, 0, 1, 0, 1])
pole = np.array(a)
print(pole)
plt.xticks(range(8), labels=[f"{i}" for i in range(1, 9)])
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
plt.imshow(pole, cmap='gray')
plt.show()
