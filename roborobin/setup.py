import os
import sys

from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need
# fine tuning.
include_files = ['help',
         'Minimap',
         'images',
         'buildings']
exclude_modules = ['tcl',
				   'tk',
				   'tkinter',
           'PySide']

packages = ['asyncio','idna','six','pkg_resources']
# if sys.platform == 'darwin':
#     packages += ['asyncio',
#                  'idna',
#                  '_sysconfigdata_m_darwin_darwin',
#                  'six',
#                  'pkg_resources']


buildOptions = dict(packages = packages,excludes = exclude_modules,include_files=include_files, optimize=2)
otheroptions = dict(icon="images/icon.ico")

name = 'RoboRobin by upload.farm'
version = '1.0'

base = 'Win32GUI' if sys.platform=='win32' else None

targetName = 'RoboRobin'
if sys.platform == 'win32':
    targetName = '{}.exe'.format(targetName)

if __name__ == "__main__":    
    if sys.platform == 'darwin':
        print('reminder: cx_Freeze struggled to make executables on Mac; use PyInstaller!')

    os.environ['TCL_LIBRARY'] = r'C:\Users\Femto\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
    os.environ['TK_LIBRARY'] = r'C:\Users\Femto\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

    executables = [
        Executable('gui.py', base=base, targetName = targetName,**otheroptions)
    ]
    setup(name=name,
          version = version,
          description = name,
          options = dict(build_exe = buildOptions),
          executables = executables)