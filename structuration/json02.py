import json

# 此时student是一个dict格式内容，不是json
data={
    "name":"liudana",
    "age":18,
    "mobile":"13802449023"
}

with open("t.json",'w')as f:
    json.dump(data,f)

with open("t.json","r")as f:
    d=json.load(f)
    print(d)
