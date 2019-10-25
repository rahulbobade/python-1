import os 
import sys
path=input("Enter your path: ")
if os.path.exists(path):
    df_l=os.listdir(path)
else:
    print("please provide valid path")
    sys.exit()
rahul=os.listdir(path)
print("all files and dir: ",rahul)
for each_file_dir in rahul:
    print(each_file_dir)
    file_dir_path=os.path.join(path,each_file_dir)
    print(file_dir_path)
    if os.path.isfile(file_dir_path):
        print(f"{file_dir_path} is a file")
    else: 
        print(f"{file_dir_path} is dir")
        
