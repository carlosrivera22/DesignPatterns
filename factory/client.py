from factory import Factory

f = Factory()

p1 = f.createProduct(1)
p2 = f.createProduct(2)

p1.execute()
p2.execute()
