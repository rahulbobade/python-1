import subprocess
cmd="ls -lrth"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()

print(f'The return code: {rc}')
print(f'The output : \n{out}')
print(f'The error : \n{err}')

'''
if shell=True then your cmd is a string (as your os command)
if shell=False then your cmd is a list.

shell=False dont work on os environment variable.

cmd="ls -lrth"  ==>shell=True
shell=False  ==> cmd="ls -lrth".split()     or    ['ls','-lrth']
,
''

'''
