# Python Production Project Bootstrap


# Development 
## PEP8 Python Enhancement Proposal
### PEP 8 – Style Guide for Python Code
https://peps.python.org/pep-0008/

## Debugger
Run the debugger by pressing F5 key while the file of interest is "active".
That is, to run the ./misques/raises.py code, open the file and press F5.

The TERMINAL pane will open to display the output.

## Virtual Environment Local Setup


PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> py -0p
 -V:3.11 *        C:\TechRoot\py\3.11.0\python.exe
 -V:3.10          C:\TechRoot\py\3.10.7\python.exe
 -V:3.8           C:\TechRoot\py\3.8.10\python.exe
 -V:2.7           C:\TechRoot\py\2.7.18\python.exe

### Create the venv
PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> py -3.8 -m venv .venvPy380  <======
PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> ls .\.venvPy380\


    Directory: D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff\.venvPy380


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         6/21/2023   7:39 AM                Include
d-----         6/21/2023   7:39 AM                Lib
d-----         6/21/2023   7:39 AM                Scripts
-a----         6/21/2023   7:39 AM             86 pyvenv.cfg

### Activate
PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> .\.venvPy380\Scripts\Activate.ps1
(.venvPy380) PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> python --version
Python 3.8.10
(.venvPy380) PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff>

Install jupyter Server ie Notebook

(.venvPy380) PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> pip --version
pip 21.1.1 from d:\sourcecode\gitlab\python\codeindex\intermediate_stuff\.venvpy380\lib\site-packages\pip (python 3.8)
(.venvPy380) PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> python.exe -m pip install --upgrade pip   
Requirement already satisfied: pip in d:\sourcecode\gitlab\python\codeindex\intermediate_stuff\.venvpy380\lib\site-packages (21.1.1)
Collecting pip
  Using cached pip-23.1.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.1.1
    Uninstalling pip-21.1.1:
      Successfully uninstalled pip-21.1.1
Successfully installed pip-23.1.2

(.venvPy380) PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> pip install notebook   <======



### Start jupyter Server
(.venvPy380) PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> jupyter notebook   <======
.
.
.
Read the migration plan to Notebook 7 to learn about the new features and the actions to take if you are using extensions.

https://jupyter-notebook.readthedocs.io/en/latest/migrate_to_notebook7.html

Please note that updating to Notebook 7 might break some of your extensions.

[I 08:42:41.944 NotebookApp] Serving notebooks from local directory: D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff
[I 08:42:41.945 NotebookApp] Jupyter Notebook 6.5.4 is running at:
[I 08:42:41.945 NotebookApp] http://localhost:8888/?token=4baae652b697d864e5e1bfefd800115b205d97d69c512234
[I 08:42:41.945 NotebookApp]  or http://127.0.0.1:8888/?token=4baae652b697d864e5e1bfefd800115b205d97d69c512234      
[I 08:42:41.946 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 08:42:42.000 NotebookApp] 

    To access the notebook, open this file in a browser:
        file:///C:/Users/bbandini/AppData/Roaming/jupyter/runtime/nbserver-40832-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=4baae652b697d864e5e1bfefd800115b205d97d69c512234
     or http://127.0.0.1:8888/?token=4baae652b697d864e5e1bfefd800115b205d97d69c512234
[W 08:43:52.314 NotebookApp] Forbidden
[W 08:43:52.315 NotebookApp] 403 GET /api/kernels?1687351432311 (127.0.0.1) 1.010000ms referer=None

### VSCode Point to jupyter localhost server
Click on the upper-right "link" : Python(3.8)
 
This brings up the command pallet.  Click “Select another Kernel…”.
Click “Existing jupyter server”, click “localhost”.  Click “python3”.

Note that the TERMINAL nomenclature changes the “name” from “powershell” to “jupyter” when the notebook is started:
 
To kill the notebook, press Ctl-c in the TERMINAL window pane.

### Powershell
```
PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> py -3.10 -m venv D:\SourceCode\python\virtenv\GitLab\Python\CodeIndex\.intermediate_stuff
PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> D:\SourceCode\python\virtenv\GitLab\Python\CodeIndex\.intermediate_stuff\Scripts\Activate.ps1
(.intermediate_stuff) PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> pip freeze
(.intermediate_stuff) PS D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> date

Wednesday, November 2, 2022 12:44:25 PM
```

### Command Prompt
```
D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> D:\SourceCode\python\virtenv\GitLab\Python\CodeIndex\.intermediate_stuff\Scripts\Activate

(.intermediate_stuff) D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> run_me.py
run as import __name__: module01.containers
Config is: i5 16
Config is: Ryzin 3 8

(.intermediate_stuff) D:\SourceCode\GitLab\Python\CodeIndex\intermediate_stuff> py_main.py
run as import __name__: module01.containers
```

# GitLab
Initial add:
```
/d/SourceCode/GitLab/Python/CodeIndex/intermediate_stuff (master)
$ git add .
warning: in the working copy of '.vscode/settings.json', LF will be replaced by CRLF the next time Git touches it
```



### Windows

### Linux

