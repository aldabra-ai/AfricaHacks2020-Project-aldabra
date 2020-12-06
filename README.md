# AfricaHacks2020-Project-aldabra

## aldabra.ai

### Problem statement 

Public hospitals all over the world are often being flooded with patients that need medical attention due to COVID-19 and they often have to wait for hours before receiving medication or a doctor's consultant. With the help of our SaaS Platform, aldabra.ai, public clinics and hospitals will be able to automate repetitive tasks that nurses and doctors do that steal their precious time. The improved efficiency will allow patients to wait only a few minutes at clinics and aid doctors and nurses to spend their time and efforts on trying to save lives.


### To contribute
 --> create folder('AfricaHacks2020...etc)
 --> clone codebase in folder
 
 ## for linux users
 # Creat developement virtual Environment
   cd git root folder --> cd AfricaHacks2020-project-aldabra.../
   install python3 if not installed --> sudo apt install python3
   install virtualenv --> sudo apt install python3-virtualenv
   run **envcreate.sh** --> ./envcreate.sh
   activate venv(note: activate-env not working yet so manual method adviced) --> source ../aldabra-env/bin/activate
   
 ## Install requirements
   --> pip3 install -r requirements.txt
  
 ## run migrate codes if needed
  from ./AfricaHacks2020-project-aldabra... folder/
  
   run --> cd aldabraai && ./migrate.sh
   manually --> cd aldabraai && python manage.py makemigrations && python manage.py migrate
 
 ## run developement server to see if all worked well
   from ./aldabraai/(folder)
   run script --> ./runserver.sh
   manually --> python manage.py runserver
   
 
    
    
