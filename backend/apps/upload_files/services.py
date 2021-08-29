from openpyxl import load_workbook

# from .constants import WORKBOOK_COLUMNS

WORKBOOK_COLUMNS = ['before', 'after']


def process_excel_file(file):
    wb = load_workbook(filename='example_test.xlsx')
    columns = []
    for sheet_name in wb.sheetnames:
        headers = [
            c
            for c in next(wb[sheet_name].iter_rows(min_row=1, max_row=1))
            if c.value in WORKBOOK_COLUMNS
        ]
        if headers:
            columns = headers
            break

    res_1 = []
    res_2 = []

    for x in range(2, columns[0].parent.max_row + 1):
        column_1 = columns[0].parent.cell(row=x, column=columns[0].col_idx)
        column_2 = columns[1].parent.cell(row=x, column=columns[1].col_idx)
        res_1.append(column_1.value)
        res_2.append(column_2.value)

    x = 0
    status = f'added: {x}'
    return status


process_excel_file(None)
