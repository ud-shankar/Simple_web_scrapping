##
# **Copy followers list of twitter users into .CSV file using PyTest framework**

The Test Automation Framework is created for automating test cases - login, search and copying followers to a file.

### Scripting Language

Python is used as the scripting language. 
Selenium Webdriver is used to perform browser automation. The front end automation is achieved by implementing pytest test cases using webdriver based automation.

### Folder Structure

The Test Automation Suite is having below folders.

- **Features** : Feature files have been created based on each feature which is under test. The different scenarios and corresponding steps in each test case that is linked to the particular feature have been listed in the same feature file.
- **Source** : Source folder has been used to list the modules used to implement the source files for corresponding feature files steps. Emphasis has been kept to reuse the codes wherever possible using file level methods.
- **Pages** : This folder has been used to save the locators for each page in case of Front End Automation. Each file corresponds to each page in the UI and contains classes which groups the locators in each subsection or action.
- **Drivers** : Folder used to save driver details, docker configuration etc. used to link selenium to the corresponding browser driver.


### conftest.py file

The conftest file houses all the common functions and common steps which are used inside the folder. The teardown for the framework is implemented here.

### Creation of a test case

The following steps briefly describe how a new test case can be added to the framework.

1. Create a feature file, if required. Add the scenario and steps in the .feature file in Gherkin format.
2. Map the required page locators to the corresponding page class in the Pages folder. Do create a new page file in .py format if required.
3. Add the test cases scripts in the corresponding file in the Source folder. Do create a new script file if required. The steps and classes which are already implemented may be reused to reduce duplicate scripting.

Whenever there are repeated scripts to be used across multiple files, the code is expected to be added to the corresponding helper class discussed above.

### Project description

1) Login into Twitter.
2) Once you login, Redirect to your favorite Twitter profile.
3) Print all the names of followers of that favourite twitter profile in csv/excel file.

The csv files are stored inside the source folder under csvfiles.


