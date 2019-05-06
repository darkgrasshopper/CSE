import csv


def remove_last_num(num: str):
    rest_of_nums = num[:15]
    return rest_of_nums


def reverse(num: str):
    print(num)
    rest_of_nums = num[0:15]
    print(rest_of_nums)
    return True


def validate(num: str):
    last_d_num = remove_last_num(num)
    reverse_num = reverse(last_d_num)
    for number in range(len(reverse_num)):
        if number % 2 != 0:
            reverse_num[number] *= 2

    for number in range(len(reverse_num)):
        if number > 9:
            reverse_num[number] -= 9

    reverse("1224849018103250")


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            cc_num = row[0]
            validate(cc_num)
