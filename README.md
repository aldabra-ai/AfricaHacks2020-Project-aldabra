# AfricaHacks2020-Project-aldabra

## Virtual environment setup
  cd into **./cli-scripts** in project root and run:
  **assuming you have python3 installed on your system**
  ````
  .\envset.ps1
  ````
  
  to activate environment run:
  ````
  .\envactive.ps1
  ````
  deactive environment using
  ````
  deactive
  ````
  
  
## start dev server
  in **.\cli-scripts** run:
  ````
  .\runserver.ps1
  ````
  
  
## React Frontend
   the react frontend was manually integrated into the django application
   it lives in 
   ````
   .\frontend
   ````
   there you'll find the **\src** folder etc
   
   **main.js** lives in
   ````
   .\frontend\static\frontend\public
   ````
   html templates lives in
   ````
   .\frontend\templates\
   ````
   there you can adjust template structure or add all html files
   
   since the react was manually integrated, you can only run
   ````
   npm run-scripts dev
   ````
   or
   ````
   npm run-scripts build
   ````
   

**Happy Hacking (o_o)**
   
   
