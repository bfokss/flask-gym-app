#flask-gym-app image
FROM python:3

# Application directory
WORKDIR /usr/src/app

# Sourcecode copies
COPY .  ./

#Dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


#ENTRYPOINT [ "python" ]
CMD [ "python", "src/app.py" ]