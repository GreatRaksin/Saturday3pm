a = ['one', 'two', 'three', 'four']
b = [1, 2, 3, 4, 5]

# (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, None)
res = list(zip(b, a))
print(res)


cars = ['Audi', 'BMW', 'Mercedes', 'Honda', 'Mazda', 'VW']
men = ['John', 'Noah', 'Sarah', 'Mike', 'Jacob', 'Bob', 'Bill']
cars_of_men = dict(zip(men, cars))
#for key, value in zip(cars, men):
#    print(key, value)
#    cars_of_men[key] = value

print(cars_of_men)

##########
a = 'abcd'
t = (10, 15, 20)
u = (-10, -15, -20)
z = [6, 14, 82]
# a 10, b 15, c 20
print(list(zip(a, t, u, z)))
