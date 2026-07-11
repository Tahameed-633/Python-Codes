user_name=input("Enter your name:")
age=int(input("Enter your age:"))
greetings=input("Enter your greetings:")
def my_function(user_name,age,greetings):
    print("Hello,%s! Your age is %d.I wish you %s"%(user_name,age,greetings))
my_function(user_name,age,greetings)