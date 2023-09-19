def smallest_no_in_array(array):
  smallest = array[0]
  for i in range(1, len(array)):
    if array[i] < smallest:
      smallest = array[i]
  return smallest
array = []
while True:
  element = input("Enter an element (or press Enter to finish): ")
  if element == "":
    break
  else:
    array.append(int(element))
smallest = smallest_no_in_array(array)
print("The smallest number in the array is:", smallest)
