import xlrd
import xlsxwriter

workbook = xlrd.open_workbook("moskva_2010.xlsx")
worksheet = workbook.sheet_by_index(0)
sheet_count = workbook.nsheets
sheets_name = workbook.sheet_names()
data = []
total_rows = worksheet.nrows
total_cols = worksheet.ncols
col = 0

for sheet in range(sheet_count):
    worksheet = workbook.sheet_by_index(sheet)
    total_rows = worksheet.nrows
    for row in range(total_rows - 5):
        weather = {
            'date': worksheet.cell(row + 4, col).value,
            'time': worksheet.cell(row + 4, col + 1).value,
            'temperature': worksheet.cell(row + 4, col + 2).value,
            'vlazh': worksheet.cell(row + 4, col + 3).value,
            'Td': worksheet.cell(row + 4, col + 4).value,
            'Pressure': worksheet.cell(row + 4, col + 5).value,
            'Sign of wind': worksheet.cell(row + 4, col + 6).value,
            'Speed_wind': worksheet.cell(row + 4, col + 7).value,
            'Cloud': worksheet.cell(row + 4, col + 8).value,
            'h': worksheet.cell(row + 4, col + 9).value,
            'VV': worksheet.cell(row + 4, col + 10).value,
            'weather_ya': worksheet.cell(row + 4, col + 11).value
        }
        data.append(weather)

n = 0
with open('data.txt', 'w') as f:
    for d in data:
        n += 1
        for k, v in d.items():
            f.write(str(n) + '. ' + str(k) + " => ")
            f.write(str(v) + '. ' + "\n")

# /////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////

lines = []  # list of strings
with open('data.txt', 'r') as f:
    for line in f:
        lines.append(line)

weather1 = {}
a = [line.split() for line in lines]
column = 0
n = 0
outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()
for list in a:
    outSheet.write(0, column, list[1])
    column += 1
    n += 1
    if n == 12:
        break

row = 1
column = 0
for wet in a:
    outSheet.write(row, column, wet[3])
    column += 1
    if column == 12:
        column = 0
        row += 1

outWorkbook.close()
