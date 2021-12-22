"""
შექმენი სია სადაც ჩაყრი რენდომად 20რიცხვს

შემდეგ შექმენი ფუნქცია რომელიც სიას გადაუვლის და დაყოფს მას ორ ნაწილად, ლუწებად და კენტებად,
(ანუ შექმენი დამატებით ორი სია და მანდ განათავსე  ლუწები და კენტები)
"""






















import random

my_list = []

for i in range(20):
    my_list.append(random.randint(1, 100))

print(my_list)

list_of_odd_numbers = []
list_of_even_numbers = []

for number in my_list:
    if number % 2 == 0:
        list_of_even_numbers.append(number)
    else:
        list_of_odd_numbers.append(number)


print("even list: ", list_of_even_numbers)
print("odd list: ", list_of_odd_numbers)

