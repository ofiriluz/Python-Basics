# Subprocess is a library for creating child processes
# Those processes will execute anything we'd like
# A similar more simple way to do that is with os.system, however we have not much control with that
# With subprocess we can control where the stdout and stderr goes and control the process itself
import os
import subprocess

rc = os.systme("exec_path")

# We can simplay use subprocess in the following manner
# This will block until the binary ends
# Note that we can pass shell=True if we want the binary to open up on a new shell
rc = subprocess.call(['df', '-h'])

# We can control where the output goes with opening a subprocess but not blocking
# And telling where to output the stdout and stderr
# In this example we are only piping the stdout into our program
# The stderr will be printed into the screen and None will return to us
# Lastly, we can do the same for stdin and pipe data to the process
p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
# The communicate returns a tuple of (stdout, stderr) and blocks the program
data = p.communicate()
print(data[0]) # stdout
print(data[1]) # stderr
# We can access the return code straight out
p.returncode

# We can use this to pipe one process to another:
# In this example we are opening an rst file and getting all the included files from it
cat = subprocess.Popen(['cat', 'index.rst'], stdout=subprocess.PIPE)
grep = subprocess.Popen(['grep', '.. include::'], stdin=cat.stdout, stdout=subprocess.PIPE,)
cut = subprocess.Popen(['cut', '-f', '3', '-d:'],stdin=grep.stdout,stdout=subprocess.PIPE,)

end_of_pipe = cut.stdout

print('Included files:')
for line in end_of_pipe:
    print('\t', line.strip())

# We can lively communicate with the process and not halt for it to end
# This program will write indices into it
# And will read the return lines
proc = subprocess.Popen('python some_repeat_program.py', 
                        shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
for i in range(10):
    proc.stdin.write('%d\n' % i)
    output = proc.stdout.readline()
    print(output.strip())

# Lastly, os library contains abit more then just system
# You can fork a process into a child unix style with os.fork
# You can also use os.exec in the same manner
os.fork()