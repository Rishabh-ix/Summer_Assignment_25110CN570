# This program finds and prints duplicate elements in an array.

n= int(input("Enter number of elements: "))
arr=[]
for i in range(n):
        value = int(input("Enter element: "))
        arr.append(value)
print("Duplicate elements are:")
duplicate=[]
for i in range(n):
        for j in range(i+1,n):
                if(arr[i]==arr[j] and arr[i] not in duplicate):
                        duplicate.append(arr[i])
                        print(arr[i])

                        
 




    