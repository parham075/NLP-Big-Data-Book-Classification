from csv import DictWriter
import pandas as pd
# reading the csv file
fieledNames = ['Title','Category','Description']
csv_file_names=["new_extracted_data_from_goodreads.csv","Crowled_Data_from_goodreads.csv"]
def csv_reader(csv_file_name):
    df = pd.read_csv(csv_file_name)
    category_ = df['Category']
    title_ = df['Title']
    disc = df ['Description']
    print(len(category_))
    return category_,title_,disc
def merger(category_,title_,disc):
    for row in range(0,len(category_)):
        title = str(title_[row])
        description = str(disc[row]) 
        category = str(category_[row])
        with open('finaldataset.csv', 'a',newline='', encoding='utf-8') as f:
                            Dict_writer = DictWriter(f,fieldnames=fieledNames)
                            Dict_writer.writerow({'Title': title ,
                            'Category':category,
                            'Description':description
                            })
                            f.close()

for csv_file_name in csv_file_names:
    category_,title_,disc=csv_reader(csv_file_names)
    merger(category_,title_,disc)