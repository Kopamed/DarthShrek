import json

def load_json(file_name):
    with open(file_name, "r") as write_file:
        data = write_file.read()
        data = json.loads(data)
    return data
    
    
    
data = load_json("messages.json")

for i in data:
    if str(i["time"])[0] == "2" and str(i["time"])[0] == ":":
        
        print(f'{i["time"]} - {i["author"]} - {i["content"]}')
        
    