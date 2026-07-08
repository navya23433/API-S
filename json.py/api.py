import requests
# data= {
#     "id":1,
#      "name":"navya",
#     "age":24
#     }
response=requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)





