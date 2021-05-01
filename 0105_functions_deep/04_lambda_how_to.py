tuples = [(1, 'd', 'яблоко'),
          (2, 'b', 'ананас'),
          (4, 'a', 'банан'),
          (3, 'c', 'молоко')]

print(sorted(tuples))
print(sorted(tuples, key=lambda x: x[2]))

print(sorted(
        range(-5, 6), key=lambda x: x * x
    ))
print(sorted((range(-5, 6))))