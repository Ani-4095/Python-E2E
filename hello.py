print("Hello Good Morning")
a = "Good"
b = "Afternoon"
print(a + " " +b)

arn1 = "arn:aws:iam::123456789012:user/johndoe"
username = arn1.split("/")[1]
print(username)