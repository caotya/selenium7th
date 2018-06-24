import csv
class csvfileManager2:
    @classmethod
    def readfile(self):
        path = r'C:\Users\51Testing\PycharmProjects\selenium7th\date\test_date.csv'
        file = open(path)
        date_table =csv.reader(file)
        for item in date_table:
            print(item)

if __name__ == '__main__':
    csvr = csvfileManager2.readfile()