def minimum_painted_cells(length_of_strip: int, black_cells: int, current_strip: str) -> int:
    if 'B' * black_cells in current_strip:
        return 0

    painted = current_strip[0: black_cells].count('W')
    min_paints = painted
    for cell in range(black_cells, length_of_strip):
        if current_strip[cell - black_cells] == 'W':
            painted -= 1
        if current_strip[cell] == 'W':
            painted += 1
        min_paints = min(min_paints, painted)

    return min_paints


def main():
    set_amount: int = int(input('Введите кол-во наборов данных: '))
    for set_ in range(set_amount):
        len_of_strip, b_cells = map(int, input('Введите кол-во клеток в полоске и кол-во черных клеток: ').split())
        strip_bw: str = input('Введи полоску: ')
        result = minimum_painted_cells(len_of_strip, b_cells, strip_bw)
        print(result)


main()
