<font size="+2"><b> Flask Gym App</b> </font>

<hr>

<font size="+1"><b>Dev mode:</b></font>

While in the main (flask-gym-app) folder, do the following:
1. Activate your venv
```
.\work_env\Scripts\activate.bat
```
2. Make sure that your venv has all the required packages installed - run only if you're not sure whether your venv has all the required packages
```
pip install -r .\work_env\requirements.txt
``` 
3. Go to the source folder
```
cd dev\src
```
4. Set environmental variable (on Linux change `set` to `export`) - run only if you're not sure whether this variable is already set
```
set FLASK_APP=app.py
```
5. Initialize the database - before you run it make sure that your folder doesn't contain the `data.sqlite` file and `migrations` directory
```
flask db init
```
6. Migrate the database
```
flask db migrate -m "Initial migration"
```
7. Upgrade the database
```
flask db upgrade
```
8. Run the app
```
python app.py
```
The app should be running in developer mode, which results in it refreshing every time you make any change(s) in the code :)
<hr>
<font size="+1"><b>Building:</b></font>

To run this project just:
- [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository
``` 
git clone https://github.com/bfokss/flask-gym-app.git
```
- Go to your repository location (You should be in flask-gym-app/dev folder) and run
```
docker build . -t flask-gym-app-image
```
```
docker run -d --rm --name flask-gym-app -p 5000:5000 flask-gym-app-image
```
- Then just simply head to [App main page](http://localhost:5000/)
- *If you want to stop the project just run*
```
docker stop flask-gym-app
```