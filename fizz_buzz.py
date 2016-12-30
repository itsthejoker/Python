fizzbuzz = []

start = int(input("Start Value:"))
end = int(input("End Value:"))

for i in range(start,end+1):
    entry = ''
    if i%3 == 0:
        entry += "fizz"
    if i%5 == 0:
        entry += "buzz"
    if i%3 != 0 and i%5 != 0:
        entry = i

    fizzbuzz.append(entry)

for i in fizzbuzz:
    print(i)
