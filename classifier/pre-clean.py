import pyexcel as pe


def main():
    sheet = pe.get_sheet(file_name="./classifier/dataset.csv", row_limit=20)
    sheet.name_columns_by_row(0)
    print(sheet.row[1][3])


if __name__ == "__main__":
    main()
