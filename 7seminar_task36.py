
def print_operation_table(operation, num_rows=6, num_columns=6):
    # Печать заголовка
    header = "   |"
    for j in range(1, num_columns + 1):
        header += f" {j:2d} |"
    print(header)
    print("-" * (5 + 6 * num_columns))

    # Печать таблицы
    for i in range(1, num_rows + 1):
        row_str = f"{i:2d} |"
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            row_str += f" {result:2d} |"
        print(row_str)
        print("-" * (5 + 6 * num_columns))

print_operation_table(lambda x, y: x * y) 