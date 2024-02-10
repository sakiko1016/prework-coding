def hello_name(user_name):
    print("Hello " + user_name + "!")
hello_name("Sakiko")

def first_odds():
    for i in range(1, 101, 2):
        print(i)
first_odds()

def max_num_in_list(a_list):
    max_num = a_list[0]  # assume first number is the maximum
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num
numbers = [10, 5, 20, 8, 30]
print(max_num_in_list(numbers))

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(2000))

def are_consecutive_numbers(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i+1] - a_list[i] != 1:
            return False
    return True
numbers1 = [2, 3, 4, 5, 6, 7]
numbers2 = [1, 2, 4, 5]


print(are_consecutive_numbers(numbers1))
print(are_consecutive_numbers(numbers2))