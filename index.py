# Question 1
def countdown(num):
    arr= []
    count_range= range(num, 0, -1)
    for i in count_range:
        arr.append(i)
    return arr
print(countdown(5))


# Question 2
def print_and_return(number_list):
    print(number_list[0])
    return  number_list[1]

number_list= [1, 2]
print(print_and_return(number_list))


# Question 3
def first_plus_length(arr):
    sum = 0
    sum= arr[0] + len(arr)
    return sum
print(first_plus_length([1, 2, 3, 4, 5]))


# Question 4
def values_greater_than(arr1):
    arr2= []
    if len(arr1) < 2:
        return False
    else:
        for i in range(0, len(arr1)):
            if arr1[i] > arr1[1]:
                arr2.append(arr1[i])
    return arr2
print(values_greater_than([1, 2, 3, 4, 5]))

# Question 5
def this_length_that_value(size, value):
    value_list= []
    for i in range(0, size):
        value_list.append(value)
    return value_list
print(this_length_that_value(3, 5))

