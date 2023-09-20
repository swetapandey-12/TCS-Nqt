def secondsmallestlargest(array):
   small = second_small = 9999999
   large = second_large = -1
   for i in range(0, len(array)):
      small = min(small, array[i])
      large = max(large, array[i])

   for i in range(0, len(array)):
      if array[i]<second_small and array[i]!=small:
         second_small = array[i] 
      if array[i]>second_large and array[i]!=large:
         second_large =array[i]    
   print("Second smallest is ", second_small)
   print("Second largest is ",second_large)


array = []
while True:
  element = input("Enter an element (or press Enter to finish): ")
  if element == "":
    break
  else:
    array.append(int(element))


no = secondsmallestlargest(array)
print(no)


