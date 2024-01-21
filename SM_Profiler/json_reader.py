import json
 
# Opening JSON file
f = open('./SM_Profiler/API_Keys/api_keys.json')
 
data = json.load(f)
 
print(data["reddit"]["client_id"])

# Closing file
f.close()

# toWrite = {"father":"anand","mother":"prti"}

# save_file = open("./SM_Profiler/written/sample_data_2.json", "w+")  
# json.dump(toWrite, save_file, indent = 4)  
# save_file.close()  


 
