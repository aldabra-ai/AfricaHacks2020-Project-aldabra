# AfricaHacks2020-Project-aldabra (Aldabra Public Repo, This no longer managed)

## Virtual environment setup
  ## For Windows  
  
  cd into **.\cli-scripts** in project root and run:
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
  
  ## For Linux(Ubuntu)
    ```
    ./envset
    ````
    
 ## Database setup
  ## Windows
  Run following scripts in admin windows **powershell**
  
  In .\cli-scripts run:
  ````
  .\dbset.ps1
  ````
  
  run migration to see if db is correctly installed
  ````
  .\migration.ps1
  ````
  
## start dev server
  ## Windows
  in **.\cli-scripts** run:
  ````
  .\runserver.ps1
  ````
  
  ## Linux(Ubuntu)
  ```
  ./runserver
  ```
  
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
   
   
