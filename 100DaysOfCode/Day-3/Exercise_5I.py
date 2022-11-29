a = input("Enter the your name :").lower()
b = input("Enter the partners name").lower()

c =a+b
print(c)
count_t = c.count("t")
count_r = c.count("r")
count_u = c.count("u")
count_e = c.count("e")


true_value = count_t +count_r +count_u + count_e
count_l = c.count("l")
count_o = c.count("o")
count_v = c.count("v")
count_e = c.count("e")

love_value = count_l+count_o+count_v+count_e

final_value = str(true_value)+ str(love_value)

print(final_value)
