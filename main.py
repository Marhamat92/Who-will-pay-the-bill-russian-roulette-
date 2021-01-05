import random

names_string=input("Please type friends names seperated by comma: ")
names=names_string.split(", ")
number_names=len(names)

random_choice=random.randint(0,number_names-1)
who_will_pay=names[random_choice]
print(who_will_pay + " is gonna pay the meal today")