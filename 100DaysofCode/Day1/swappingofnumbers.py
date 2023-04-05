A = int(input("A:\n"))
B = int(input("B:\n"))

temp = 0

print("A : {}".format(A))
print("B : {}".format(B))

temp = A
A = B
B = temp

print("*********Values after swapping")
print("A : {}".format(A))
print("B : {}".format(B))
