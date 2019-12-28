# OS is a standard helper library used for operating system interfaces
# Those include files and path utilities
# Environment variables, pids uids and gids and file descriptors
# And many more
import os
# Its main use is for files and paths mostly
some_path = "a/b/c"
# Check whether the path exists file / dir
os.path.exists(some_path)
os.path.isdir(some_path)
os.path.isfile(some_path)
# Retrieves the dirname of the path or the last path (filename)
os.path.dirname(some_path)
os.path.basename(some_path)
# Retrieves the path and the file extensions as a tuple
os.path.splitext(some_path)
# sys library is system specific functionality, mostly related to system paths, dlls/so, and version info
# sys is mostly common used for args of the executable and exiting a program
import sys
# Normal args of a program
sys.argv
# Normal exit of a program with return code
sys.exit(-1)
# Streams we can use to write and read from
sys.stdout
sys.stderr
# Platfor is used for getting computer information
# Such as the os we are working on, which CPU we are using and extra specific OS info
# This is good when you want to investigate the machine you are running on
import platform
# Returns the OS name
platform.system()
# Returns the release of the OS depending on the type
platform.release()
# Returns the machine type i.e i386 ppc and so on
platform.machine()
# Returns the processor name (amd, intel)
platform.processor()