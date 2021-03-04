FROM python:3.7.3-stretch

# working dir
WORKDIR /app

# copy source code to working dir
COPY . app.py /app/

# install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt