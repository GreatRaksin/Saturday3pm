from worker import Caesar

m1 = Caesar('Привет, Андрей!')
m2 = Caesar('Hello, Andrew!')
m2.set_language('English')
m2.set_language('suakhili')

print(m1.encrypt())
print(m2.encrypt(4))

