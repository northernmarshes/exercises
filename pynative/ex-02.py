#!/usr/bin/env python3

previous = 0

for i in range(0, 10):
    print (f'Current Number {i} Previous Number {previous} Sum: {i + previous}')
    previous = i

# to samo ale ze wskazówkami, trudnością było ogarnięcie zmiennej
# previous tak by wskazywała 0 w momencie kiedy numer to też 0

# previous_num = 0

# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     previous_num = i
