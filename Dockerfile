# Python image
FROM python:3

WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Add the Django app
COPY . .

EXPOSE 80

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Start the app
ENTRYPOINT [ "./docker-entrypoint.sh" ]