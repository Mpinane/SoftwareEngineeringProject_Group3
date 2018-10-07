# AVI System: 
The AVI System is a web based Courses Recommender app for Postgraduate Students in Computer Science. The system further predict the grades the students are likely to get in the recommended courses.
Avi means grandfather in Catalan.


### Prerequisites:
The System requires python3 and Django-Framework to be compiled successfully.


### Installing:

#### 1. Python:
##### Windows: https://www.python.org/downloads/windows/
run 'python3 --version' to check if installation was successful.

##### Extra required libraries:
             ~$: pip install pandas
             ~$: pip install numpy
             ~$: pip install sklearn

##### Linux: 
             ~$: sudo apt-get update
             ~$: sudo apt-get dist-upgrade 
             ~$: sudo apt-get install python3.6
run 'python3 --version' to check if installation was successful.
    
     
##### Extra required libraries:
             ~$: sudo pip install pandas
             ~$: sudo pip install numpy
             ~$: sudo pip install sklearn

##### Mac OS: https://www.python.org/downloads/mac-osx/
run 'python3 --version' to check if installation was successful.

    
##### Extra required libraries:
             ~$: sudo pip install pandas
             ~$: sudo pip install numpy
             ~$: sudo pip install sklearn

#### 2. Django:
##### Windows: 
              ~$: python3 -m pip install --upgrade pip
              ~$: python -m pip install Django
run 'django-admin --version' to check if installation was successful.

##### Linux and Mac OS:
              ~$: sudo python3 -m pip install --upgrade pip
              ~$: sudo python -m pip install Django
        
run 'django-admin --version' to check if installation was successful.


### Built With:
                i. Python - High Level Programming Language
               ii. Django - The web framework used
              iii. CSS - Style Sheet Language
               iv. HTML - Markup Language


### Additional System Features:
              i. New Users can sign-up.
             ii. Existing users can login and add academic infomation.
            iii. Existing Users can edit user infomation and course detail.
             iv. Machine Learning is used extensively in course and grade Predictions. These machine learning algorithms were fed training, validation and testing data of past post graduate students.


### How to use:
              i. Run and install all required libraries.
             ii. Download and Extract.
            iii. Run '~$: python manage.py runserver' in the terminal in the folder containing the manage.py file.
             iv. After successful compilation, open your browswer and type in 'localhost:8000' in the browser url bar.
              v. Register and Relish.   


### Running the tests: Unit Tests


#### Django Tests:
              Run '~$: python manage.py test' in the terminal in the folder containing the manage.py file.
###### This will return the number of test cases evaluated and display the number of those passed and those failed.



#### PyTest Tests:


##### Requires Pytest to be installed.
##### Windows:
              ~$: pip install pytest
              ~$: pip install pytest-django
              ~$: pip instsall pytest-cov
              ~$: pip install mixer

##### Linux and MacOS:
              ~$: sudo pip install pytest
              ~$: sudo pip install pytest-django
              ~$: sudo pip instsall pytest-cov
              ~$: sudo pip install mixer

##### Running Pytests: 

               i. Ensure successul installation of the above.
              ii. From the Avi_project directory run '~$: py.test' in your terminal
###### This will return the number of test cases and display the number of those passed and those failed.


### Authors: 

              Mohale Mpinane - 1363679 
              Shipyana Thulisile - 916781
              Mahlangu Lucky - 1395125
              Mkhombe Sbusiso - 1154046


### Acknowledgments:


http://softwaretestingfundamentals.com/unit-testing/ - Testing Documentation Reference
