#this code calculates the area of triangle

#take input from user
a = int(input("Enter side length: "))
b = int(input("Enter side length: "))
c = int(input("Enter side length: "))

#calculate area of triangle
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)

#display output to user
print("Area of the triangle is ", area)
