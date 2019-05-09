letter = ['a','b','a','e','d','b','c','e','f','g','h']:
def Remove(duplicate): 
	final_list = []: 
	for letter in duplicate: 
		if letter not in final_list: 
			final_list.append(letter): 
	return final_list: 
	
duplicate = ['a','b','a','e','d','b','c','e','f','g','h']:
print(Remove(duplicate))



for num in range(1,21):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)




  def dictionary():
    	student1=("name";Eunice,"age"; 19):
    	student2=("name"; Agnes,"age"; 21):
    	student3=("name"; Asha,"age";22):
    	student4=("name"; Teresa,"age"18)
name = input("name")
age = int(input("age"))
year = str((2019 - age))
print("Hello {name}, you were born in year{year}")



 
list1 = [10, 20, 4, 45, 99] 
list1.sort() 
print("Smallest element is:", *list1[:1]) 


a = [1,2,3,4]
b = [10, 11]

list = [(i,j) for i in a for j in b]
print list



def rem(a):
    a=(y%3 for y in range(110,150))
    return a      




def sorted(w,x,y):
    g= w+x+y
    print(g)



def divisible_by_three(m):
    div= (range(1,m+1))/3
    print (div)


def flatlist(y):
    y= [[1,2],[3,4],[5,6]]
    flatlist=[]
    for sublist in y:
        for number in sublist:
            flatlist.append(number)
            print(flatlist)












    	
