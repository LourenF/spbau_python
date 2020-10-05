#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импортирует модуль math, чтобы необходимые функции работали
import math
# Аналогично импоритирует модуль numpy
import numpy
# И импортирует из библиотеки matplotlib модуль pyplot, присваивая ему в этой программе более корткую переменную mpp
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

# Оператор if проверяет, действительно ли __name__ равно __main__
if __name__=='__main__':     
    # Присваивает значение переменной arguments
    arguments = numpy.r_[0:100:0.1]
    # Вызывает функцию plot, которая рисует график по заданным аргументам
    mpp.plot(
        arguments,
        [math.cos(a) for a in arguments]
    )
    # Запускает функцию show, которая выводит график
    mpp.show()