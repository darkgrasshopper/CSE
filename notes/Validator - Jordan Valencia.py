import csv


def remove_last_num(num: str):
    print(num)
    rest_of_nums = num[:15]
    print(rest_of_nums)


def validate(num: str):
    print(num)
    print(num[0:15])


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            cc_num = row[0]
            remove_last_num(cc_num)


remove_last_num("1224849018103250")


def reverse(num: str):
    print(num)
    print(num[::-1])
