import pyexcel as pe

# We have used this script to map the Kaggle dataset with our own dataset

genre_list = [
    'Art', 'Biography', 'Business', 'Children', 'Christian', 'Classics', 'Comics', 'Cookbooks', 'Ebooks', 'Fantasy',
    'Fiction', 'Graphic Novels', 'Historical Fiction', 'History', 'Horror', 'Memoir', 'Music', 'Mystery', 'Nonfiction',
    'Poetry', 'Psychology', 'Romance', 'Science', 'Science Fiction', 'Self Help', 'Sports', 'Thriller', 'Travel',
    'Young Adult'
]


def main():
    sheet = pe.get_sheet(file_name="./classifier/dataset.csv", row_limit=20)
    sheet.name_columns_by_row(0)
    print(sheet.row[1][3])


if __name__ == "__main__":
    main()
