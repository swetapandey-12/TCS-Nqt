def reverse(arr):
  left = 0
  right = len(arr) - 1
  while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1



arr = []
while True:
  element = input("Enter an element (or press Enter to finish): ")
  if element == "":
    break
  else:
    arr.append(int(element))


reverse(arr)
print(arr)
