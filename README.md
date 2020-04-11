# website_blocker

## Getting Started:
This is a python program that runs in background and block certain website to open for given time period.
To run this program for testing you can run `website_blocker.py` file as usual.
To run the program in background you have to run `website_blocker.pyw` file by `double click` on it. This file is run by `pythonw.exe`, this is sub-version of python and used for running program in background. This program modify the `hosts` file on your computer to block website thats why `admistrator permission` is required. To run the program as an admistrator you have to create a task for this and you can do that by the following way - 
* Open `Task Scheduler` and click on `Create Task`.
* Under `General` do the following - 
    * `Name = Website Blocker` 
    * cinfigure for your windows version.
    * Check `Run with highest priviliges` to run the script as admistrator otherwise Windows will run the script as a normal user.
* Under `Trigger` do the following - 
    * Click `New` and `New Task` window will pop up.
    * In the above window do `Begin the task = At startup` and click `Ok`.
* Under `Action` do the following -
    * Click `New` and `New Action` window will pop up.
    * In the above window do `Action = Start a program` and `Browse` for the `website_blocker.pyw` file and after that click `Ok`.
* Under `Condition` uncheck `Start the task only if the compter is on AC power`.
* And finally click on `Ok` and you will see the created Task `Website Blocker` in the task list.



## License:
This project is under _MIT License_ see more in [LICENSE](https://github.com/codeslash21/website_blocker/blob/master/LICENSE)
