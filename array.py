#create new array
my_list = []  #better
my_list = list()  

#navigating thru the list
animals = ['dog', 'cat', 'rat']
for i in animals:
  print(i)
for i in range(0:len(animals)):
  print animals[i]
  
a = [1,2,3,4,5]
for i in range(0,2):
    print(a[i])  #1,2
  
#add element to array
my_list.append("dummy")

#add array to array
a = [1,2,3]
a.extend([4,5])
print(a)   # [1, 2, 3, 4, 5] 

#max element of array
candies = [1,5,2,7,2]
maxC = max(candies)  # 7
  
