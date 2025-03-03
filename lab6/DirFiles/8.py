import os  

path = "W.txt"  
if os.path.exists(path):      
    os.remove(path)  
    print("File deleted successfully.")  
else:  
    print("File not found.")  
  
