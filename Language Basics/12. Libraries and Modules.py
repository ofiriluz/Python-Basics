# Each python file is called a module and can be imported using the following syntax
# import module_name
# This will import the file from the PYTHONPATH list, and from where the current python file resides
# A Package is a folder that contains an __init__.py file, and you can import every module from the package
# You can also import the package itself only, which will import the __init__.py file and anything inside it
# You can alias imports with the as operator
# import package_name.module_name as alias
# import package_name
# Lastly, you can import specific classes and functions from modules by using the from
# from module_name import Class
# from package_name import module_name
import os
import platform

def some_func():
    # The import will only live in this scope
    import pprint
    pprint.pprint("something")

if __name__ == "__main__":
    print(os.getcwd())
    print(platform.system())