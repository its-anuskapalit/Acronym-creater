"""taking the number of srings from user and making acronym from them"""
# number of elements as input
n = int(input("Enter number of elements : ")) 

lst=[] #empty list

# iterating till the range 

for i in range(0, n):
    ele = input("enter strings:")
    lst.append(ele) # adding the element
#printing list elements
print("list of strings are: ",lst)
#function to find the first characters of string
for i in lst:
    output=""
    st=" "+i
    for j in range(0,len(st)):
        if(st[j]==" "):
            output=output+st[j+1]
    print(output.upper(),end="")
