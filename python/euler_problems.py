sum = 0
for i in range(3, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print("Problem 1: ", sum)

max_val = 4000000
first = 1
second = 2
sum = second
new = first + second

# loop till new reach max_val
while new <= max_val:
    if new % 2 == 0:
        sum += new
    
    first = second
    second = new
    new = first + second

print("Problem 2: ", sum)
