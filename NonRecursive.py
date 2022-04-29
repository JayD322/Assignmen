# Program to display the Fibonacci sequence up to n-th term
nterms = int(input("Enter Number of terms? "))
# first two terms
a, b = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return a
if nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
print(a)
# generate fibonacci sequence
else:
print("Fibonacci sequence:")
while count < nterms:print(a)
nth = a + b
# update values
a = b
n2 = nth
count += 1