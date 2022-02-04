FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .
CMD ["flask", "run", "--host=0.0.0.0"]