import requests
user_id=input("Enter user id (1-10):")
response=requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
print("started")
if response.status_code==200:
    user=response.json()
    print("_","\n user details")
    print("name:",user["name"])
    print("id:",user["id"])
    print("username:",user["username"])
    print("email:",user["email"])
    print("city:",user["address"]["city"])
    print("ended")
else:
    print("not found")    
