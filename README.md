# DevOps Python Example

A demo project for showing off DevOps tools and processes like GitHub Actions and Dependabot alerts.

Note that this repository has dependencies with known security vulnerabilities, which is purposeful to show off things like GitHub Security Advisories.

## Installation and setup

### With Docker

### Without Docker

Activate the python venv by running `venv\Scripts\activate.bat`. To install the required python packages using the 
requirements.txt, run `pip install -r requirements.txt`

#### Django

If changes are made to the models, run `python manage.py makemigrations` to generate any required database migrations, and 
then `python manage.py migrate` to apply.

#### Huey and redis

Huey is used as a multi-threaded task queue for tasks such as generating charts or fetching weather data without blocking the 
web application thread. Redis is used as the message broker between threads.

To install redis on windows, activate WSL by running the following in an elevated Powershell prompt 
`Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`

After rebooting, install Ubuntu from the Microsoft Store.

Next, launch bash for windows and install build-essential and tcl using `sudo apt-get install build-essential tcl8.5`

Now that we have the required packages to install redis, run `wget download.redis.io/releases/redis-5.0.0.tar.gz` to 
download a compressed version of redis, and `tar xzf redis-5.0.0.tar.gz` to uncompress it. `cd` into the newly uncompressed
directory and compile redis into a binary by running `sudo make distclean` and `sudo make -j`.

Copy the compiled binary over to `/usr/local/bin` by running `sudo make install -j`. Next, `cd` into the utils folder and
run `sudo ./install_server.sh` to run the installation script. This will create a service for our redis server.

To start the redis service, run `sudo service redis_6379 start`, and `sudo service redis_6379 stop` to stop the service.

If the redis service is running, executing `python manage.py run_huey` from our venv will start huey and connect it to our
redis service.


