""" 1. list less than 150 and divisable by 5"""
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i%5 == 0 and i<=150:
        print(i)

""" 2. Reverse the following list using for loop"""
list1 = [10, 20, 30, 40, 50]
list1.reverse()
print(list1)

""" 3. Display numbers from -10 to -1 using for loop """
for i in range(-10,0):
    print(i)
    
""" 4. Display a message “Done” after successful execution of for loop """  
for i in range(5):
    print(i)
else:
    print("Done!")

""" 5. Create a function that can accept two arguments name and age and print its value"""
def person(name,age):
    print(name,age)
person('Aishu', 27)
person("Tommy", 30)   

""" 6. Returns addition and subtraction in single return call"""
def calculation(x,y):
    return (x+y,x-y)
res = calculation(40,10)
print(res)

""" 7. showEmployee() name and salary  """
def showEmployee(name, salary=9000):
    print("Employee Ben salary is:",salary)

showEmployee('Ben', 9000)
showEmployee("Ben")

""" 8. Generate a Python list of all the even numbers between 4 to 30 """
i=list(range(4,30,2))
print(i)      

""" 9. Return the largest item from the given list """
aList = [4, 6, 8, 24, 12, 2]
print(max(aList))

""" 10. Below are the two lists convert it into the dictionary """
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys,values))
print(dictionary)