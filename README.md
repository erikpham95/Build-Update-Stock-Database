# Build Update Stock Database
Build a PostgreSQL Stock Database, and update it everyday with latest market data using python scripts &amp; crontab


## I.  Technical Pre-requisite / Reference

### 1.  SQL Pre-requisite

#### a.  SQL Fundamentals & Tools

-   MySQL

    -   General Reference: [MySQL Tutorial](https://www.mysqltutorial.org/) + [javatpoint](https://www.javatpoint.com/mysql-tutorial)

    -   MySQL Workbench: [Guideline](https://www.guru99.com/introduction-to-mysql-workbench.html) + [Documentation](https://www.mysql.com/products/workbench/)

    -   MySQL Python: [Reference](https://www.mysqltutorial.org/python-mysql/) + [Youtube Instruction](https://www.youtube.com/playlist?list=PLzMcBGfZo4-l5kVSNVKGO60V6RkXAVtp-)

-   PostgreSQL

    -   General Reference: [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)

    -   pgAdmin4: [Reference](https://linuxhint.com/pgadmin4_tutorial_beginners/) + [Youtube Instruction](https://www.youtube.com/watch?v=WFT5MaZN6g4&ab_channel=DatabaseStar)

    -   PostgreSQL Python: [Reference](https://www.postgresqltutorial.com/postgresql-python/) + [Youtube Instruction](https://www.youtube.com/watch?v=M2NzvnfS-hI&ab_channel=techTFQ)

#### b.  DBMS

-   Reference

    -   Database Design: [tutorialspoint](https://www.tutorialspoint.com/dbms/index.htm) + [javatpoint](https://www.javatpoint.com/dbms-tutorial)

    -   Database Administration: [Wiki](https://en.wikipedia.org/wiki/Database_administration) + [Reference](https://www.mysqltutorial.org/mysql-administration/)

-   Key Concepts

    -   RDBMS vs NoSQL

    -   ER Model & Relational Model

    -   3-tier DBMS Architecture

### 2.  Python Pre-requisites

#### a.  Python Programing Concepts & Tools

-   Python 101

    -   Reference (Python-Specific): [pythontutorial.net](https://www.pythontutorial.net/), [pynative.com](https://pynative.com/), [pythonbasics.org](https://pythonbasics.org/)

    -   Reference (Generic): [studytonight](https://www.studytonight.com/python/), [w3schools](https://www.w3schools.com/python/default.asp), [javatpoint](https://www.javatpoint.com/python-tutorial), [tutorialspoint](https://www.tutorialspoint.com/python3/index.htm)

-   Python 102

    -   Theoretical: [Python OOP](https://www.tutorialspoint.com/python/pdf/python_classes_objects.pdf), [Python Data Structure](https://intellipaat.com/mediaFiles/2019/02/Python-Data-structures-cheat-sheet.pdf?US)

    -   Practical: [Python Database](https://pynative.com/python/databases/)

-   Python Development Environment & Tools

    -   VS Code: [Guideline](https://adamtheautomator.com/visual-studio-code-tutorial/), [Cheatsheet](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf), [Reference](https://code.visualstudio.com/docs)

    -   Jupyter Notebooks: [Guideline 1](https://realpython.com/jupyter-notebook-introduction/), [Guideline 2](https://www.datacamp.com/tutorial/tutorial-jupyter-notebook), [Cheatsheet](https://miro.medium.com/v2/resize:fit:1400/1*totJoCc3l7BdeY-mEQ6HHQ.png), [Reference](https://www.tutorialspoint.com/jupyter/index.htm)

    -   JupyterLab: [Guideline](https://towardsdatascience.com/getting-the-most-out-of-jupyter-lab-9b3198f88f2d?gi=e5cf49abd26f), [Cheatsheet](https://blog.ja-ke.tech/assets/jupyterlab-shortcuts/Shortcuts.png), [Reference](https://jupyterlab.readthedocs.io/en/stable/)

#### b.  Python Libraries

-   Data Manipulation

    -   numpy: [Manual](https://numpy.org/doc/stable/index.html), [Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf), [Reference](https://www.studytonight.com/numpy/)

    -   pandas: [Manual](https://pandas.pydata.org/pandas-docs/stable/index.html), [Cheatsheet](https://www.javatpoint.com/pandas-cheat-sheet), [Reference](https://www.studytonight.com/pandas/)

-   Data Visualization

    -   matplotlib: [Manual](https://matplotlib.org/stable/index.html), [Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf), [Reference](https://www.studytonight.com/matplotlib/)

    -   seaborn: [Manual](https://seaborn.pydata.org/index.html), [Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf), [Reference](https://www.tutorialspoint.com/seaborn/index.htm)

-   Financial Data:

    -   pandas-datareader: [Review](https://thecleverprogrammer.com/2021/03/22/pandas-datareader-using-python-tutorial/), [Main Page](https://github.com/pydata/pandas-datareader), [Reference](https://buildmedia.readthedocs.org/media/pdf/pandas-datareader/latest/pandas-datareader.pdf)

    -   yfinance: [Review](https://algotrading101.com/learn/yfinance-guide/), [Main Page](https://aroussi.com/post/python-yahoo-finance), [Reference](https://pypi.org/project/yfinance/)

### 3.  Linux / Bash Scripting Pre-requisites

#### a.  General

-   Linux OS

    -   [Tutorialspoint - LINUX / UNIX](https://www.tutorialspoint.com/unix/index.htm)

    -   [Ryan\'s Tutorials - Linux Tutorial](https://ryanstutorials.net/linuxtutorial/)

-   Bash / Shell Scripting

    -   [Ryan\'s Tutorials - Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/)

    -   [Tutorialspoint - LINUX / UNIX Shell Programming](https://www.tutorialspoint.com/unix/shell_scripting.htm)

    -   [Javatpoint - Bash Scripting Tutorial](https://www.javatpoint.com/bash)

#### b.  Hands-on (for this project)

-   Bash Script Execution

    -   [Make a Bash Script Executable](https://www.andrewcbancroft.com/blog/musings/make-bash-script-executable/)

    -   [How To Run the .sh File Shell Script In Linux / UNIX](https://www.cyberciti.biz/faq/run-execute-sh-shell-script/)

-   Using cron

    -   [How To Add Jobs To cron Under Linux or UNIX](https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/)

    -   [How to Automate Tasks with cron Jobs in Linux](https://www.freecodecamp.org/news/cron-jobs-in-linux/)

## II. Project Breakdown

### 1.  Create SQL Database

#### a.  Overview

-   PostgreSQL & pgAdmin4 will be used

-   The table will consist of 7 columns

    -   Ticker Name (Primary Key)

    -   Company Name

    -   Market Cap

    -   Country

    -   PE Ratio

    -   PB Ratio

    -   PEG Ratio

#### b.  Notes

-   Column 1-4 will remain constant after data is first put
    in

-   Column 5-7 will be updated everyday

### 2.  Using Python to update SQL table

#### a.  Overview

-   2 Python Scripts will be used

    -   S1 (initialize): Used to first fill the SQL table
        with data

    -   S2 (update): Used to update the PE / PB / PEG column
        every day with latest market data (scheduled using
        crontab)

-   When list of S&P500 companies is being changed, S1 is
    run again

#### b.  Notes

-   The company list is updated from <https://en.wikipedia.org/wiki/List_of_S%26P_500_companies>

-   yfinance is used to get market data

-   psycorg2 is used to update PostgreSQL database using Python

-   "localhost" (127.0.0.1) & port 5432 is used for PostgreSQL.

### 3.  Using cron to automatically run S2 everyday

#### a.  Overview

-   **update\_stock\_data.sh** is created to execute S2

    -   Navigate to the directory containing the Python script: **cd /path/to/python/script**

    -   Virtual environment need to be activated, containing the required Python package 
    **source /path/to/virtual/environment/bin/activate**

-   crontab is used to schedule the update

    -   Open your crontab file: **crontab --e**

    -   Schedule everyday update at 8AM using crontab file: 
    **0 8 \* \* \* /path/to/update\_stock\_data.sh**

#### b.  Notes

-   The database should be updated every day after trading hours (let say 8AM, as I'm living in Asia)

-   update\_stock\_data.sh need to be make executable withadministrator permission using:
**chmod +x update\_stock\_data.sh**
