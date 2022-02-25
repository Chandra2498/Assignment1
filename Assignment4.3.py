#Sample Input List
l1=[4,5,2,9]

#defining the function to get the square numbers
def Square1(x):
    return x*x

#Initializing map with function and the iterable list
Square_Iterator=map(Square1,l1)

#Converting the squared numbers into a List
Squared_numbers=list(Square_Iterator)

#Printing the Output 
print(Squared_numbers)
