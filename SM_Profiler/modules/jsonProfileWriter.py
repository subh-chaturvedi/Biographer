import json
import os

def writeSMRecord(id,toAdd):

    pathToWrite = "./SM_Profiler/written/"+id+".json"
    # pathToWrite = "./SM_Profiler/written/test2.json"


    #TODO: rewrite and optimise following code:
    # First check if file exists and has any pre-existing values 
    # and initiate a file otherwise and then write the json data accordingly
    f = open(pathToWrite,"w+")
    f.close()

    f = open(pathToWrite,"r")
    content = f.read()
    print(content,"&")
    f.close()

    f = open(pathToWrite,"w")
    if content == "":
        f.write('{"initialized": "true"}')
    f.close()
  
    f = open(pathToWrite,"r")
    current_data = json.load(f)
    print(current_data)

    f.close()


    current_data.update(toAdd)
    toWrite = current_data
    print(toWrite)

    save_file = open(pathToWrite, "w+")  
    json.dump(toWrite, save_file, indent = 4)  
    save_file.close()  

# writeSMRecord("test3",{"success":"true"})