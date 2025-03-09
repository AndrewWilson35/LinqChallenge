# LinqChallenge
Challenge for Linq Software Engineering Internship

1. Ensure that all requirements listed in requirements.txt are installed

2. Install the two Python files, the two yaml files, and the database JSON file from this repository. 

3. In the Linux command line (or a fascimile of it such as WSL2), cd to the directory containing the docker-compose.yaml file. The two yaml files should be in the same directory.

4. Type into the command line docker compose up

5. After the command has finished, run the two python files.

6. In the internet browser, go to local host 3000.

7. Enter in admin for both the username and password fields. Skip the next screen to make a new password, unless you really care about that, in that case make your own username and password.

8. In the top left menu, navigate to connections. and then to "Create a new Connection". Select Prometheus. Within the address field, plug in http://host.docker.internal:9090/. Then save the connection.

9. Using the top left menu, navigate to Dashboards. Click new, then import. Import the JSON file from this repository.

10. Go to edit the imported dashboard. Click the Data source bar, then choose the prometheus data connection made in step 8. After this, the running sums of each color should populate! 

   
