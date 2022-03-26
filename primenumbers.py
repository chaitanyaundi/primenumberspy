def factors(number):
    factorList = []
    for i in range(1, number + 1):
        if number % i == 0:
            factorList.append(i)
    return factorList

put = int(input("Enter the number: "))
primes = []
for j in range(2, put + 1):
    if len(factors(j)) == 2:
        primes.append(j)
print(primes)
print(f"Total prime numbers till {put} are {len(primes)}")