import json

def load_json(file_name):
    with open(file_name, "r") as write_file:
        data = write_file.read()
        data = json.loads(data)
    return data
    
    
x = load_json("messages.json")    
print(len(x))
y = load_json("userInfo.json")
print(len(y))
previous= {"user":"", "messages": 0}
nums = []
total=0
users=0
for i in y:
    users+=1
    total += y[i]["messages"]
    nums.append(y[i]["messages"])
    if y[i]["messages"] > previous["messages"]:
        previous["messages"] = y[i]["messages"]
        previous["user"] = str(i)
        
print(str(previous), nums)

print(f"11038 / {users} = {round(11038/users)}")

def bubble_sort(arr):
    moved=1
    while moved!=0:
        moved=0
        dupe=[]
        a = 1
        for i in range(len(arr)):
            pos1 = arr[a-1]
            pos2 = arr[a]
            if len(arr) <= a:
                a+=1
            if pos1 > pos2:
                dupe.append(pos2)
                dupe.append(pos1)
                moved+=1
            else:
                dupe.append(pos1)
                dupe.append(pos2)
                print(dupe)
            arr = dupe
            dupe= []
            print(arr)
    return arr
    
    
print(bubble_sort(nums))
                
        