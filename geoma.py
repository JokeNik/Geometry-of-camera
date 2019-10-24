import math
import os

PI = 3.14159265359


def torad(x):
    return x * PI / 180


def solve(h, x, y, twobeta, twogama, yaw, pitch, roll):
    beta = twobeta / 2#узнаем половинные углы
    gama = twogama / 2#узнаем половинные углы
    alpha = pitch
    phi = yaw
    #Переводим в радианы
    alpha = torad(alpha)
    beta =  torad(beta)
    gama = torad(gama)
    phi = torad(phi)
    mx = torad(70)
    angle = alpha + gama
    #Считаеаем координаты трапеции
    x1 = x + (math.tan(alpha - gama) * h) * math.cos(-phi) - (- h / (math.cos(alpha - gama)) * math.tan(beta)) * math.sin(-phi)
    y1 = y + (math.tan(alpha - gama) * h) * math.sin(-phi) + (- h / (math.cos(alpha - gama)) * math.tan(beta)) * math.cos(-phi)
    x2 = x + (math.tan(alpha - gama) * h) * math.cos(-phi) - (h / (math.cos(alpha - gama)) * math.tan(beta)) * math.sin(-phi)
    y2 = y + (math.tan(alpha - gama) * h) * math.sin(-phi) + (h / (math.cos(alpha - gama)) * math.tan(beta)) * math.cos(-phi)

    x3 = x + (math.tan(angle) * h) * math.cos(-phi) - (- h / (math.cos(angle)) * math.tan(beta)) * math.sin(-phi)
    y3 = y + (math.tan(angle) * h) * math.sin(-phi) + (- h / (math.cos(angle)) * math.tan(beta)) * math.cos(-phi)
    x4 = x + (math.tan(angle) * h) * math.cos(-phi) - (h / (math.cos(angle)) * math.tan(beta)) * math.sin(-phi)
    y4 = y + (math.tan(angle) * h) * math.sin(-phi) + (h / (math.cos(angle)) * math.tan(beta)) * math.cos(-phi)

    #print(alpha, beta, gama, phi, sep = " ")
    #Вывод вершин трапеции в порядке обхода
    print(x1, y1, sep = " ")
    print(x2, y2, sep = " ")
    print(x4, y4, sep = " ")
    print(x3, y3, sep = " ")

h = float(input());#высота надо объектом
x = float(input());#х координата дрона
y = float(input());#у координата дрона
twobeta = 70
twogama = 90
yaw = float(input());#угол поворота дрона относительно прямоугольный координат против часовой стрелки
pitch = float(input()) #Угол наклона дрона относительно вертикальной линии против часовой стрелки
roll = 0
solve(h, x, y, twobeta, twogama, yaw, pitch, roll)
