# 3)SARCINA NUMARATORUL


# class RangeCounter:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start <= self.end:
#             result = self.start
#             self.start += 1
#             return result
#         else:
#             raise StopIteration
#
# # Exemplu de folosire:
# start_num = 1
# end_num = 100
# counter = RangeCounter(start_num, end_num)
# for num in counter:
#     print(num)



# 4)SARCINA LISTA DE STUDIENTI


# class SchoolClass:
#     def __init__(self, class_name):
#         self.class_name = class_name
#         self.students = {}
#
#     def add_student(self, **kwargs):
#         for name, age in kwargs.items():
#             self.students[name] = age
#
#     def display_students(self):
#         print(f"Studentii din clasa {self.class_name}:")
#         for name, age in self.students.items():
#             print(f"Name: {name}, Age: {age}")
#
#
# if __name__ == "__main__":
#
#     class_12 = SchoolClass("Class 12")
#     class_12.add_student(Alexandru=18, Maxim=18, Said=18)
#     class_12.display_students()
