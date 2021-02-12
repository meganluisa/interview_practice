# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

# user1 = User("Megs", "White")
# print(user1)

# Input: [5, 2, 9, 7, 2, 6]
# Output: 2

# def duplicates(input_array):
#     i = 0
#     j = 1
#     while i < len(input_array):
#         if j == len(input_array):
#             i += 1
#             j = i + 1
#         elif input_array[i] != input_array[j]: 
#             print(input_array[j])
#             j += 1
#         elif input_array[i] == input_array[j]:
#             print("Samesies")
#             print(input_array[j])
#             break

#         # elif input_array[i] == 9
#         #     print("This is 9 and equal")
#         #     break


# duplicates([5, 2, 9, 7, 2, 6])


# scifi_authors = ["Issac Asimov", "Ray B Bradbury", "Rob Hens", "Orson Scott Card"]

# def bubble_sort(list):
#     unsorted_until_index = len(list) - 1
#     sorted = False

#     while not sorted:
#         sorted = True
#         for i in range(unsorted_until_index):
#           if list[i] > list[i+1]:
#               list[i], list[i+1] = list[i+1], list[i]
#               sorted = False
#         unsorted_until_index -= 1
#     return list

# print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))


# def has_duplicates(list):
#     steps = 0
#     dict = {}
#     for i in range(len(list)):
#         steps += 1
#         if list[i] in dict:
#             print(dict)
#             return True, steps
#         else:
#             dict[list[i]] = 1
#     return False

# print(has_duplicates([4, 2, 3, 8, 7, 5, 3]))

# list = [2, 6, 4, 1, 9, -1, 9, 10]
# def selection_sort(list):
#     for i in range(len(list)):
#         lowest_index = i
#         j = i + 1
#         while j < len(list):
#             if list[j] < list[lowest_index]:
#                 lowest_index = j
#             j += 1
#         if lowest_index != i:
#             temp = list[i]
#             list[i] = list[lowest_index]
#             list[lowest_index] = temp
#         i += 1
#     return list


# print(selection_sort(list))

# choices = ['pizza', 'pasta', 'salad', 'nachos']

# print('Your choices are:')
# for index, item in enumerate(choices):
#   print(index + 1), 
#   print(item)


# class Person():
#     def __init__(self, name, age):
#         self.actual_name = name
#         self.age = age
#     def get_name(self):
#         return self.actual_name
        
#     def get_age(self):
#         return self.age
    
# meg = Person("Megan", 23)
# print(meg.get_name)




# def pipeline(*funcs):
#     def helper(arg):
#         for i in range(length(fun)):
#         return pipline(x)
#     return helper
            
# fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
# print(fun(3)) #should print 5.0

# fun(8)
# 24
# 25
# 12.5

class Solution(object):
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        print(set(nums))
        return len(set(nums)) < len(nums)

print(Solution.containsDuplicate([2, 5, 3, 8, 7, 2]))