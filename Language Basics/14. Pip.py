# There is no code here
# Pip is the package manager for python
# Through pip you can install custom external packages that extend your standard python library
# To install a package, simply find its name through pypi.org (the main pip repository)
# And then execute the following command considering pip is on your local computers PATH
# pip install some_package_name
# All of the packages come in a .wheel format, which is a zipped version of the package
# You can also list installed packages by running
# pip list
# And you can only download packages 
# pip download some_package_name
# Usually when working with external packages, one will create a virtual environment to work on
# A virtual env is an empty and isolated environent where you can install packages on
# To use it, we first need to install the package virtualenv
# pip install virtualenv
# Once installed, we can use venv env_name to generate a new env
# Afterwards, we can enter the env by running:
# Linux -> source env_name/bin/activate
# Windows -> .\env\Scripts\activate
# Once inside, we can use pip normally, however packages will be installed on the isolated env
# You can freeze those packages into a requirements file to transfer to different machines
# This is done by using pip freeze command
# You can later use that requirements.txt file to install all of the dependencies on another machines by running
# pip install -r requirements.txt