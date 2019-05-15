import json


a = {
    "a": "liu@565.com",
    "b": "liu@565.com",
    "c": "liu@565.com",
    "d": "liu@565.com"
}

a2 = {
    "a": [[1,2,3,4], 34],
    "b": [[1,4,52,3], 45]
}

b = json.dumps(a)       # 使用json.dumps(dict) 将字典转换成json字符串
print(type(b))      # str

c = json.loads(b)       # 使用 json.loads(json_str)将json 字符串转换成字典
print(type(c))      # dict

# value值是数组时也可以转化为json
b2 = json.dumps(a2)
print(type(b2))

filePath = "F:\\AWorkSpace\\Python-Learning-Data\\json.json"

# json 数据写入文件中  格式为"{\"a\": [[1, 2, 3, 4], 34], \"b\": [[1, 4, 52, 3], 45]}"
with open(filePath, "w") as f :
    json.dump(b2, f)

# 打开json文件, 读取数据
with open(filePath, "r") as f:
    data = json.load(f)
print(data)
print(type(data))