'''
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newline=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    print("out is: ",0)
else:
    print("command was failed and error is: ",e)    
'''
'''
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newline=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
        print(each_line): 
else:
    print("command was failed and error is: ",e) 

'''
''' 
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newline=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
        if "version" in each_line:
            print(each_line) 
else:
    print("command was failed and error is: ",e) 

'''
'''
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newline=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
        if "version" in each_line and "release" in each_line:
            print(each_line) 
else:
    print("command was failed and error is: ",e) 
'''
'''
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newline=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
        if "version" in each_line and "release" in each_line:
            print(each_line.split()) 
else:
    print("command was failed and error is: ",e) 
'''    
'''
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newline=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
        if "version" in each_line and "release" in each_line:
            print(each_line.split()[3]) 
else:
    print("command was failed and error is: ",e) 
'''
'''    
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newline=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
        if "version" in each_line and "release" in each_line:
            print(each_line.split()[3]).split('(')) 
else:
    print("command was failed and error is: ",e) 
'''    
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newline=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
        if "version" in each_line and "release" in each_line:
            print(each_line.split()[3]).split('(')[0]) 
else:
    print("command was failed and error is: ",e) 