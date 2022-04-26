list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# 1
# the_5_first_days
print(list[0:5])
# the week ends
# indexes
# positive indexes : 0:monday 6:sunday
# negative indexes : -1: sunday
print(list[5:])
# 2
# negative indexes : -1: sunday
# the_5_first_days
print(list[-7:])
# the week ends
print(list[-2:])
# 3
# the last day of the week
print(list[6])
# 4
# we use the function reverse to reverse a list
list.reverse()
#we print the new list i mean the list after reverse
print(list)
#