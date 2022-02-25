#Sample Input List
l1= [1,2,3,4,5,6,7]

#defining the function to get the tripled numbers
def Triple(num):
    return num*3

#Initializing map with function and the iterable list
Triple_Iterator=map(Triple,l1)

#Converting the squared numbers into a List
Tripled_numbers=list(Triple_Iterator)

#Printing the Output 
print(Tripled_numbers)
