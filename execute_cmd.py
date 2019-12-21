import subprocess
cmd="ls -lrth"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()

print(f'The return code: {rc}')
print(f'The output : \n{out}')
print(f'The error : \n{err}')

