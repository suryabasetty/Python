def getRow(self, rowIndex):
    count = 0
    num = rowIndex
    den = 1
    add_num = 1
    pascal_row = [1]
    while count < rowIndex:
        add_num = (add_num * num) / den
        pascal_row.append(add_num)
        num -= 1
        den += 1
        count += 1
    return pascal_row