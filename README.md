# Работы по курсу "Компьютерная графика".

Все работы выполнены на языке Python с использованием библиотеки Qt (PyQt5) для оконного интерфейса.

Запуск:
```
pip install -r requirements.txt
python3 main.py
```
Конвертирование ui ресурса в python код:
```
pyuic5 ui.ui -o ui.py
```

# Задания
1) [Аналитеческая геометрия.](https://github.com/Sergkon99/computer-graphics/tree/master/1)    
    1.1 Прямые заданы своими коэффициентами. Определить их взаимное расположение (пересекаются, не пересекаются, совпадают).    
    1.2 Даны четыре точки A, B, C и D, лежащие на одной прямой. Определить пересекаются ли луч [AB) и отрезок [CD].    
    1.3 Угол задан тремя точками А, В, С (точка В – вершина угла). Определить вид угла (острый, тупой или прямой).   
    1.4 Даны три точки в пространстве, своими координатами, определить лежат ли они на одной прямой.    
2) [Геометрические преобразования.](https://github.com/Sergkon99/computer-graphics/tree/master/2)    
    2.1 Реализовать с заданной совокупностью фигур все виды аффинных преобразований:    
    * перенос вдоль оси OX,
    * перенос вдоль оси OY,
    * отражение относительно оси OX,
    * отражение относительно оси OY,
    * отражение относительно прямой Y=X,
    * масштабирование независимо по обеим осям, 
    * поворот на заданный угол относительно центра координат
    * поворот на заданный угол относительно произвольной точки, указываемой в ходе выполнения программы.

    2.2 Разработать программу, реализующую двухмерные трансформации с любой двухмерной фигурой (квадрат, окружность, ромб, звезда). Фигура выбирается из списка.    
3) [Растеризация отрезка и окружности.](https://github.com/Sergkon99/computer-graphics/tree/master/3)    
Реализовать алгоритмы Брезенхема растеризации отрезка и окружности.




