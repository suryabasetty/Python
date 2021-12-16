def convertToTitle(self, columnNumber):
    excel_list = []

    while columnNumber >= 0:
        columnNumber -= 1
        bit = columnNumber % 26
        excel_list.append(chr(bit + 65))
        columnNumber /= 26
        columnNumber = int(columnNumber)
        if columnNumber == 0:
            break
    excel_list.reverse()
    return "".join(excel_list)