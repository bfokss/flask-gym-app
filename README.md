<font size="+2"><b> Flask Gym App</b> </font>


To run this project just:
- [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository
``` 
git clone https://github.com/bfokss/flask-gym-app.git
```
- Go to your repository location (You should be in flask-gym-app/dev folder) and run
```
docker build . -t flask-gym-app-image
docker run -d --rm --name flask-gym-app -p 5000:5000 flask-gym-app-image
```
- Then just simply head to [App main page](http://localhost:5000/)
- *If you want to stop the project just run*
```
docker stop flask-gym-app
```