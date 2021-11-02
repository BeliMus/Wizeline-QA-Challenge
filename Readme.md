
# Wizeline QA Challenge - BMS  
> Technical Challenge for Wizeline QA Bootcamp Nov 2021.  
  
## Table of Contents  
* [General Info](#general-information)  
* [Technologies Used](#technologies-used)  
* [Features](#features) 
* [Requirements](#requirements)  
* [Setup](#setup)  
* [Usage](#usage)  
* [Reports](#reports)
* [Contact](#contact)  
  
## General Information  
  
- Automate QA testing scenarios for Sauce Demo Page included in QA Automation Bootcamp Challenge  
  
## Technologies Used  
- Python - version 3.9.x  
  
  
## Features  
- Login with a valid user  
- Login with an invalid user  
- Logout from the home page  
- Sort products by Price (low to high)  
- Add multiple items to the shopping cart  
- Add the specific product to the shopping cart  
- Complete a purchase  
  
  
## Requirements  
- Python Packages  
  - selenium  
  - pytest  
  - webdriver-manager  
  - pytest-html  
  - pytest-parallel  
  - pytest-xdist  
- WebDrivers:  
  - [Chrome Driver](https://chromedriver.chromium.org/)  
  - [Gecko Driver](https://github.com/mozilla/geckodriver)  
- Browser  
  - Version should match your Web Driver's Version  
  
## Setup  
   
##### Clone the Repo  
  
 $ git clone https://github.com/BeliMus/Wizeline-QA-Challenge.git  

##### Set the Path  
  
- Set your Web Drivers folder into the `Path` Variable
- Set your Python folder into the `Path` Variable if needed

##### Set Browsers for Testing  

- Open file `./conf/settings.json` and set the drivers to use. 
- Values must be strings.
- Values accepted
  - Chrome
  - Firefox
- Example
```
{
  "drivers": ["Chrome", "Firefox"]
}
```

## Usage  
  
Run the script `runAutomation.bat` for Windows and `runAutomation.sh` for macOS  

## Reports
  
Reports will be created in the `log` Folder

  
## Contact  
Created by [@BeliMus](https://www.linkedin.com/in/musb890725) - feel free to contact me!

