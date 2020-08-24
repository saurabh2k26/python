#create new array
my_list = []  #better
my_list = list()  

#navigating thru the list
animals = ['dog', 'cat', 'rat']
for i in animals:
  print(i)
for i in range(0:len(animals)):
  print animals[i]
  
#add element to array
my_list.append("dummy")

#add array to array
a = [1,2,3]
a.extend([4,5])
print(a)   # [1, 2, 3, 4, 5] 
  
