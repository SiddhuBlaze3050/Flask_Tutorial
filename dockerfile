FROM python:3.9-slim-buster
WORKDIR D:\Studies\Scaler\DSML\Module-16\Containerization - Docker and DockerHub\Flask_Tutorial\flask_working

COPY requirements.txt ./

RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-m", "flask", "--app", "Loan_app","run", "--host=0.0.0.0"]