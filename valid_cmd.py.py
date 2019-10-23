import os
cmd="date"
rt=os.system(cmd)
if rt==0:
    print("your command was sucessfully executed")
else:
    print("your command was failed")    

