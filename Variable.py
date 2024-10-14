### **Basic Tasks:**

"""1. **Simple Variable Assignment:**
   - Create a variable called `name` and assign your name to it. Print the variable."""
name = "Ace"
print(name)
print()

"""2. **Variable Naming Conventions:**  
   - Create variables using different valid naming conventions: `camelCase`, `snake_case`, and `PascalCase`. Assign each a different value and print them."""
#CamelCase
myName = "Ace"
print("CamelCase - myName = ",myName)
#PascalCase
MyName = "Ace"
print("PascelCase - MyName = ",MyName)
#SnakeCase
My_Name = "Ace"
print("SnakeCase - My_Name = ",My_Name)
print()

"""3. **Assign Multiple Values (Basic):**  
   - Create three variables: `x`, `y`, and `z`, and assign them the values `5`, `10`, and `15` in one line. Print each variable."""
x,y,z = 5,10,15
print(x)
print(y)
print(z)
print()

"""4. **Swap Variables:**  
   - Assign two variables `a` and `b` with values `3` and `7`. Swap their values without using a temporary variable, then print the swapped values."""
a,b = 3,7
print("a = ",a," b = ",b)
a,b = b,a
print("a = ",a," b = ",b)
print()

"""5. **Print Variables Together:**  
   - Create three variables with different data types (e.g., `int`, `string`, `float`) and print them together in one line using a single `print()` function."""
c = int(10)
d = str("Ace")
e = float(10.1)
print("Integer = ",c," ,String = ",d," ,Float = ",e)
print()

### **Intermediate Tasks:**

"""6. **Concatenate Strings:**  
   - Create two string variables, `first_name` and `last_name`. Concatenate them into a new variable called `full_name` and print the result."""
first_name = 'Ace'
last_name = ' Ashzul'
full_name = first_name + last_name
print("Full Name = ", full_name)
print()

"""7. **Reassign Variables:**  
   - Assign an integer value to a variable `num`, then reassign a string value to the same variable `num`. Print the variable after each assignment."""
num = 10
print("Number = ", num)
num = "Number Change String"
print("String = ", num)
print()

"""8. **Type Casting:**  
   - Create a variable `age` with a string value `"25"`. Convert this variable to an integer, add 5 to it, and print the result."""
age = "25"
Age = int(age) + 5
print("Age = ", Age)
print()

"""9. **Multiple Assignment (Intermediate):**  
   - Assign four different values to four variables in one line. Print the sum of the first two and the product of the last two."""
f,g,h,i = 10,11,12,13
print("Sum = ",f+g," Product = ",h*i)
print()

"""10. **Global vs Local Variables (Basic):**  
    - Create a global variable `x = 10`. Inside a function, create a local variable `x = 20`, print both the global and local variables."""
x = 10
def fun():
    x = 20
    return x
print("Global variable = ",x,"Local variable = ",fun())
print()

"""11. **Access Global Variable in Function:**  
    - Define a global variable `counter = 5`. Create a function that prints the global variable and modifies it within the function using `global`."""
counter = 5
def fun1():
    global counter
    print(counter)
    counter = 10
    print(counter)
fun1()
print()

"""12. **Formatted Output (f-strings):**  
    - Assign values to variables `name` and `age`. Use f-strings to print a sentence like "Hello, my name is `name` and I am `age` years old."""""
result = f"My name is {name} and I am {age} years old,".format(name="Ace",age=21)
print(result)
#Format
name = "Sheick"
age = 54
result1 = "My father name is {} and He is {} years old."
print(result1.format(name,age))
print()

"""13. **Global Variable Modification:**  
    - Define a global variable `balance`. Write two functions: one to add money to `balance` and another to subtract from it. Ensure both functions modify the global `balance` variable."""
balance = 10
def add_money(a):
    global balance
    balance += a
   # print(balance + 10)
def sub_money(b):
    global balance
    balance -= b
    #print(balance - 15)
add_money(10)
sub_money(15)
print("Final Balance ",balance)
print()


### **Advanced Tasks:**

"""14. **Dynamic Variables:**  
    - Create a list of names `["Alice", "Bob", "Charlie"]`. Dynamically assign each name to a variable using a loop and print each variable."""
name = ["Alice", "Bob", "Charlie"]



"""15. **Variable Scope in Loops:**  
    - Write a function that contains a loop. Inside the loop, modify a global variable `sum` by adding values. Print the value of `sum` inside and outside the loop."""
sum = 0
def fun2():
    global sum
    for i in range(1,6):
        sum = sum + i
        print(f"Sum inside loop: {sum}")
    print(f"Sum outside loop: {sum}")
fun2()
print()

"""16. **Multiple Assignments with Complex Expressions:**  
    - Assign variables `a`, `b`, and `c` the values `2`, `4`, and `8`. In one line, assign the values of `a + b`, `b * c`, and `c - a` to three new variables. Print the new variables."""
a,b,c = 2,4,8
e,f,g = a+b, b*c, c-a
print(e,f,g)
print()

"""17. **Return Multiple Values from a Function:**  
    - Write a function that takes two numbers as input and returns three variables: the sum, difference, and product of the two numbers. Print the returned values."""
def fun3(a,b):
    sum = a + b
    diff = a / b
    pro = a * b
    return sum,diff,pro
a = int(input("Enter the Value: "))
b = int(input("Enter the Value: "))
print(fun3(a,b))
print()

"""18. **Variable Length Assignment:**  
    - Create a list with more than three elements and use unpacking to assign the first two elements to variables and the rest to another list."""
list1 = [1,2,3,4,5]
first,second,*rest = list1
print("Fisrt list element ",first, " and Second list element ",second, " and the rest of List ", *rest)
print()

"""19. **Nested Function with Global Variables:**  
    - Create a global variable `status = "pending"`. Write a nested function inside another function that changes the value of `status` to "complete"."""
status = 'pending'
def fun5():
    def fun4():
        global status
        status = "complete"
        #return status
    fun4()
fun5()
print(status)
print()

"""20. **Advanced Global and Local Scope:**  
    - Create a global variable `points`. Inside a function, create a local variable with the same name and modify it. Return the local value and print both the local and global variables to observe the difference."""
points = 10
def fun6():
    points = 11
    return points
print("Global Variable = ",points," and Local Variable = ",fun6())

