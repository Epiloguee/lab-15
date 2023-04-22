# Открывает файл для чтения с указанием полного пути к файлу
with open('d:/хлам/f.txt', 'r') as f:
    # Читает файл f, split преобразует элементы в список, map float превращает всё в числа с плавающей точкой
    components = list(map(float, f.read().split()))    # list преобразует полученный объект типа map в список

    # Вычисляет сумму компонентов и модуль этой суммы
    sum_components = sum(components)
    abs_sum_components = abs(sum_components)

    # Вычисляет произведение компонентов и квадрат этого произведения
    product_components = 1
    for component in components:
        product_components *= component
    square_product_components = product_components ** 2

    # Выводит результаты
    print('Модуль суммы компонентов файла:', abs_sum_components)
    print('Квадрат произведения компонентов файла:', square_product_components)