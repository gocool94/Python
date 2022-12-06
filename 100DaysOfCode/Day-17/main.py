class User:
    def __init__(self,user,password):
        self.user = user
        self.password = password
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers +=1
        self.following +=1


user_1 = User(user="Gokul",password="12345")
user_2 = User(user="dharani",password="11111")
user_1.follow(user_2)
print(user_1.following)


print(user_1.user)
print(user_1.password)