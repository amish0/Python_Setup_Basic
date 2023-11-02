# Python Workflow
This is basic tutorial for python setup creation
***********************************************************************
***********************************************************************
-----------------------------------------------------------------------
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
=======================================================================

# Refrences:
- https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
- https://www.geeksforgeeks.org/what-is-setup-py-in-python/
- https://www.pythoncheatsheet.org/cheatsheet/setup-py
- https://pypi.org/project/Sphinx-PyPI-upload/
- https://pythonhosted.org/an_example_pypi_project/setuptools.html
- https://setuptools.pypa.io/en/stable/references/keywords.html
- https://setuptools.pypa.io/en/stable/userguide/quickstart.html
- https://setuptools.pypa.io/en/stable/userguide/datafiles.html
- https://packaging.python.org/en/latest/tutorials/packaging-projects/

"Regarding Init File"
- https://iq-inc.com/importerror-attempted-relative-import/


## basic Directory Structure
```
some_root_dir
|-- README
|-- setup.py
|-- data
|-- packagecustom_A
|-- |-- __init__.py
|-- |-- numpy_module_a.py
|-- |-- numpy_module_b.py
|-- packagecustom_B
|-- |-- __init__.py
|-- |-- opencv_module_a.py
|-- |-- opencv_module_b.py
|-- |-- module_c
|-- |-- |-- __init__.py
|-- |-- |-- arithmatic.py
```

## Build setup
```
# Go to code directory
cd some_root_dir

# create build

python -m build
# or
# python setup.py sdist bdist_wheel
```
It will create build in your dist directory. if dist is not present it will create it.

## Install Packages
 
 if you have not made any build, please follow the command

 ```
 python setup.py install
 ```

 If build has been created, please follow the instruction below
 ```
 cd dist
 pip install package_name*.whl
 ```
 Please replace "package_name*.whl" with .whl file present in dist directory
