# пункт 1 - делала с Гошко Я.И.
import os

secret_key1 = os.environ.get("MURZAGALIEVA_1")
secret_key2 = os.environ.get("MURZAGALIEVA_E_2")
secret_key3 = os.environ.get("MURZAGALIEVA_ASK_3")
print(secret_key1)
print(secret_key2)
print(secret_key3)


# пункт 2 - делала с Ватутиной С.А. (вариант 5)
# Контейнер расчета
from sympy import *

k, T, C, L = symbols("k C T L")

# Линейный способ
C_ost = 20000  # изменение первоначальной стоимости в соответствии с вариантом №5/ Ватутина С.А.
Am_lst = []
C_ost_lst = []
for i in range(
    6
):  # изменение количества итераций в соответствии с числом лет эксплуатации для 5 варианта/ Ватутина С.А.
    Am = (C - L) / T
    C_ost -= Am.subs(
        {C: 20000, T: 6, L: 0}
    )  # изменение входных данных (первоначальной стоимости, числа лет эксплуатации, остаточной стоимости), подставляемых в формулу в соответствии с вариантом №5/ Ватутина С.А.
    Am_lst.append(
        round(Am.subs({C: 20000, T: 6, L: 0}), 2)
    )  # изменение входных данных (первоначальной стоимости, числа лет эксплуатации, остаточной стоимости)/ Ватутина С.А.
    C_ost_lst.append(round(C_ost, 2))
print("Am_lst:", Am_lst)
print("C_ost_lst:", C_ost_lst)

# Способ уменьшающего остатка
Aj = 0
C_ost = 20000  # изменение первоначальной стоимости в соответствии с вариантом №5/ Ватутина С.А.
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(
    6
):  # изменение количества итераций в соответствии с числом лет эксплуатации для 5 варианта/ Ватутина С.А.
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs(
        {C: 20000, T: 6, k: 2}
    )  # изменение входных данных (первоначальной стоимости, числа лет эксплуатации, остаточной стоимости), подставляемых в формулу в соответствии с вариантом №5/ Ватутина С.А.
    Am_lst_2.append(
        round(Am.subs({C: 20000, T: 6, k: 2}), 2)
    )  # изменение входных данных (первоначальной стоимости, числа лет эксплуатации, остаточной стоимости)/ Ватутина С.А.
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print("Am_lst_2:", Am_lst_2)
print("C_ost_lst_2:", C_ost_lst_2)

# Контейнер для табличного вывода
import pandas as pd

Y = range(
    1, 7
)  # изменение количества итераций в соответствии с числом лет эксплуатации для 5 варианта/ Ватутина С.А.
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=["Y", "C_ost_lst", "Am_lst"])
tfame2 = pd.DataFrame(table2, columns=["Y", "C_ost_lst_2", "Am_lst_2"])
print(tfame)
print(tfame2)

# Контейнер визуализации
import numpy as np
import matplotlib.pyplot as plt

plt.plot(tfame["Y"], tfame["C_ost_lst"], label="Am")
plt.savefig("chart1.png")
plt.figure()
plt.plot(tfame2["Y"], tfame2["C_ost_lst_2"], label="Am_2")
plt.savefig("chart2.png")

vals = Am_lst
labels = [
    str(x) for x in range(1, 7)
]  # изменение количества итераций в соответствии с числом лет эксплуатации для 5 варианта/ Ватутина С.А.
explode = (
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
)  # изменение количества секторов в соответствии с СПИ 6 лет/ Ватутина С.А.
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart3.png")

vals = Am_lst_2
labels = [
    str(x) for x in range(1, 7)
]  # изменение количества итераций в соответствии с числом лет эксплуатации для 5 варианта/ Ватутина С.А.
explode = (
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
)  # изменение количества секторов в соответствии с СПИ 6 лет/ Ватутина С.А.
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart4.png")

plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1, columns=["Y", "Am_lst"])
tfame2_am = pd.DataFrame(table2, columns=["Y", "Am_lst_2"])
plt.bar(tfame["Y"], tfame["Am_lst"])
plt.savefig("chart5.jpeg")
plt.figure()
plt.bar(tfame["Y"], tfame2["Am_lst_2"])
plt.savefig("chart6.png")

# Внесенные изменения полностью соответствуют исходным данным для варианта №5 ЛР 2. Работа контейнеров реализована в полном объеме, выводится корректный результат/ Ватутина С.А. ИТОГОВАЯ ОЦЕНКА: 5 баллов!

# пункт 3 - удалила контейнер визуализации и восстановаила с помощью встроенных инструментов

# пункт 4 - делала с Марикян А.П.
# вариант 6
# Контейнер расчета
from sympy import *

k, T, C, L = symbols("k C T L")

# Линейный способ
C_ost = 15000
Am_lst = []
C_ost_lst = []
for i in range(8):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 15000, T: 8, L: 0})
    Am_lst.append(round(Am.subs({C: 15000, T: 8, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print("Am_lst:", Am_lst)
print("C_ost_lst:", C_ost_lst)

# Способ уменьшающего остатка
Aj = 0
C_ost = 15000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(8):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 15000, T: 8, k: 2})
    Am_lst_2.append(round(Am.subs({C: 15000, T: 8, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print("Am_lst_2:", Am_lst_2)
print("C_ost_lst_2:", C_ost_lst_2)

# Контейнер для табличного вывода
import pandas as pd

Y = range(1, 9)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=["Y", "C_ost_lst", "Am_lst"])
tfame2 = pd.DataFrame(table2, columns=["Y", "C_ost_lst_2", "Am_lst_2"])
print(tfame)
print(tfame2)

# Контейнер визуализации
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
plt.plot(tfame["Y"], tfame["C_ost_lst"], label="Am")
plt.savefig("chart7.png")
plt.figure()
plt.plot(tfame2["Y"], tfame2["C_ost_lst_2"], label="Am_2")
plt.savefig("chart8.png")

vals = Am_lst
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart9.png")  # Что это значит?
# ответ: команда библиотеки matplotlib.pyplot, которая сохраняет график в файл с именем chart9.png

vals = Am_lst_2
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")  # Что это значит?
# ответ: команда библиотеки matplotlib.pyplot, которая устанавливает равные масштабы по осям x и y, чтобы график был круглым
plt.savefig("chart10.png")

plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1, columns=["Y", "Am_lst"])
tfame2_am = pd.DataFrame(table2, columns=["Y", "Am_lst_2"])
plt.bar(tfame["Y"], tfame["Am_lst"])  # Что это значит?
# ответ: команда библиотеки matplotlib.pyplot, которая строит столбчатую диаграмму с данными из столбцов 'Y' по оси Х и 'Am_lst' по оси У DataFrame tfame
plt.savefig("chart11.jpeg")
plt.figure()
plt.bar(tfame["Y"], tfame2["Am_lst_2"])
plt.savefig("chart12.png")
# все правильно, твердые 5 баллов. Эльмира умничка!(проверила Марикян)
