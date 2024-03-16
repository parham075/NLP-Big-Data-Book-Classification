import csv
from csv import DictWriter

import pandas as pd

category_str = ''

list2 = [
    '696', '2455', '2597', '2615', '2507',
    '3098', '3118', '3112',
    '22', '296',
    '3280', '197', '3312', '193', '176',
    '2506', '3113', '364', '2635',
    '1296', '761', '752',
    '2534', '1877', '229',
    '352', '2627', '352',
    '362',
    '350', '351', '2625',
    '284', '2484', '301',
    '213', '214', '222', '215',
    '3134', '3180', '3172',
    '3013', '3023', '2543',
    '2858', '2873', '1738', '2528', '638', '1050', '2583',
    '977', '984', '981', '3102', '217', '980', '2585',
    '233',
    '2819', '2840', '2820',
    '2620', '339', '2492',

]
list_category = []


def open_csv():
    with open('extracted_data_from_book_depository_dataset.csv', 'a', newline='', encoding='utf-8') as f:
        fieled_Name = ['Title', 'Category', 'Description']
        thewriter = csv.DictWriter(f, fieldnames=fieled_Name)
        thewriter.writeheader()
        f.close()


def checking(category_str):
    category = ''
    if int(category_str) in [696, 2455, 2597, 2615, 2507]:
        category = 'Children'
    if int(category_str) in [3098, 3118, 3112]:
        category = 'Travel'
    if int(category_str) in [22, 296]:
        category = 'Classics'
    if int(category_str) in [3280, 197, 3312, 193, 176]:
        category = 'Music'
    if int(category_str) in [2506, 3113, 364, 2635]:
        category = 'Graphic Novels'
    if int(category_str) in [1296, 761, 752]:
        category = 'Psychology'
    if int(category_str) in [2534, 1877, 229]:
        category = 'Science'
    if int(category_str) in [352, 2627, 352]:
        category = 'Science Fiction'
    if int(category_str) == 362:
        category = 'Historical Fiction'
    if int(category_str) in [350, 351, 2625]:
        category = 'Horror'
    if int(category_str) in [284, 2484, 301]:
        category = 'Poetry'
    if int(category_str) in [213, 214, 222, 215]:
        category = 'Biography'
    if int(category_str) in [3134, 3180, 3172]:
        category = 'Christian'
    if int(category_str) in [3013, 3023, 2543]:
        category = 'Sports'
    if int(category_str) in [2858, 2873, 1738, 2528, 638, 1050, 2583]:
        category = 'Cookbooks'
    if int(category_str) in [977, 984, 981, 3102, 217, 980, 2585]:
        category = 'Business'
    if int(category_str) in [1296, 761, 752]:
        category = 'Psychology'

    if int(category_str) == 233:
        category = 'Memoir'
    if int(category_str) in [2819, 2840, 2820]:
        category = 'Self Help'
    if int(category_str) in [2620, 339, 2492]:
        category = 'Thriller'

    return category


def filtering():
    df = pd.read_csv("book_depository.csv")
    df = df[['title', 'categories', 'description']]
    categories = df['categories']
    print("raft tu for")
    for row in range(0, len(categories)):
        category_str = str(categories[row])
        category_str = category_str.replace('[', '').replace(']', '')
        list_category = category_str.split(',')

        category_str = ''
        for cat in list_category:
            if cat in list2:
                category_str = cat
                break

        if category_str != '':
            category_str = checking(int(category_str))
            with open('extracted_data_from_book_depository_dataset.csv', 'a', newline='', encoding='utf-8') as f:
                Dict_writer = DictWriter(f, fieldnames=['Title', 'Category', 'Description'])
                Dict_writer.writerow({
                    'Title': df['title'][row],
                    'Category': category_str,
                    'Description': df['description'][row]
                })
                f.close()
        if row % 15000 == 0:
            print("row: ", row)

        # if index == 10:
        #     break


open_csv()

filtering()

# gener_list = [
#     'art', 'biography', 'business', 'children', 'christian', 'classics', 'comics', 'cookbooks', 'ebooks', 'fantasy',
#     'science fiction', 'nonfiction', 'historical fiction', 'fiction', 'graphic novels', 'history', 'horror', 'memoir', 'music', 'mystery',
#     'poetry', 'psychology', 'romance', 'science', 'self Help', 'sports', 'thriller', 'travel', 'young adult']


# def csv_file_creator():
#     with open('categor.csv', 'a', encoding='UTF8', newline='') as f:
#         fieled_Name = ['Category']
#         thewriter = csv.DictWriter(f, fieldnames=fieled_Name)
#         thewriter.writeheader()
#         f.close()


# def changing_data():
#     df = pd.read_csv("dataset.csv")
#     category = df['Category']
#     print(len(category))
#     for row in range(0, len(category)):
#         category_str = str(category[row])
#         category_str = category_str.lower()
#         if row % 2 == 0:
#             if category_str == np.nan or category_str == 'nan' or category_str == '':
#                 category_str = 'nonfiction'
#         list_category = category_str.split(',')
#         for element in list_category:

#             if element in gener_list:
#                 category_str = element
#                 break
#             else:

#                 category_str = np.nan

#         with open('categor.csv', 'a', newline='', encoding='utf-8') as f:
#             Dict_writer = DictWriter(f, fieldnames=['Category'])
#             Dict_writer.writerow({
#                 'Category': category_str})
#             f.close()
#         if row % 500 == 0:
#             print(row)


# csv_file_creator()
# changing_data()
