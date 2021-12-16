def generate(self, numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]

    pascal_list = [[1], [1, 1]]
    rows = 2
    while rows < numRows:
        cur_row = [1] * (rows + 1)
        index = 1
        prev_row = pascal_list.__getitem__(len(pascal_list) - 1)
        while index < rows:
            cur_row[index] = prev_row[index - 1] + prev_row[index]
            index += 1
        pascal_list.append(cur_row)
        rows += 1
    return pascal_list