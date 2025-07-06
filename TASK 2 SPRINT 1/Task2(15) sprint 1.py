numbers = [ 5, 7, -8 ,4 ,-5, -7]
print (numbers)
positive_numbers=[]
negative_numbers=[]

for num in numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
print("Positive Numbers" , positive_numbers)
print("Negative Numbers" , negative_numbers)
        
