def minimum_painted_cells(length_of_strip: int, black_cells: int, current_strip: str) -> int:
    if 'B' * black_cells in current_strip:  # первым делом проверяем наличие отрезка
        return 0

    painted = current_strip[0: black_cells].count('W')  # минимальное кол-во черных клеток в первом отрезке
    for cell in range(black_cells, length_of_strip):  # начинаем проверку всей строки
        if len(current_strip[
               cell: black_cells + cell]) < black_cells:  # если окно становится короче кол-ва черных клеток прекращаем проверку
            break
        temp = current_strip[cell: black_cells + cell].count('W')  # кол-во перекрашенных клеток в данном окне
        painted = min(temp, painted)  # записываем минимальное кол-во перекрашенных клеток
    return painted  # возвращаем ответ


def main():
    set_amount: int = int(input('Введите кол-во наборов данных: '))
    for set_ in range(set_amount):
        len_of_strip, b_cells = map(int, input('Введите кол-во клеток в полоске и кол-во черных клеток: ').split())
        strip_bw: str = input('Введи полоску: ')
        result = minimum_painted_cells(len_of_strip, b_cells, strip_bw)
        print(result)


main()
