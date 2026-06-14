# This program finds second largest element in an array.

def Largest(arr):
      largest = arr[0]
      for i in arr:
         if(i>largest):
           largest=i
      return largest
         
n = int(input("Enter number of elements: "))
arr=[]
for i in range(n):
        value = int(input("Enter element: "))
        arr.append(value)
Large1 = Largest(arr)
arr.remove(Large1)
Large2 = Largest(arr)
print("Second largest element in array is:",Large2)




