import os
import shutil

if __name__ == "__main__":
    # We can use open command to simply open a file with a mode
    read_file = open("some_path", 'r')
    write_file = open("some_other_path", 'w')
    append_file = open("append_path", "a")
    # Read a list of lines
    lines = read_file.readlines()
    # Write a list of lines
    write_file.write('\n'.join(lines))
    write_file.close()
    # We can use the enter and exit syntax for files
    with open('path', 'r') as f:
        pass

    # We can iterate over a directory in two different ways, recursive or not recursive
    # Both ways require an helper standard package called os
    for f in os.listdir("some_dir_path"):
        pass
    for root, dirs, files in os.walk("some_other_dir_path"):
        pass
    # We can also remove files by using the os package
    # Note that this works in the simillar way that rm works, not recursive or on folders
    os.remove("path")
    # We can make dirs, given a path will make all the dirs for that path
    os.makedirs("other_path")
    # We can also use shutil package to remove a tree of files or copy a tree
    shutil.rmtree("path")
    shutil.copytree("input_path", "out_path")