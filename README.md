Running a Flask Application on Boot with Systemd
This guide will show you how to create a systemd service that will automatically start a Flask application on boot.

Prerequisites
Before you begin, you will need:

A Linux system with systemd installed
A Flask application that you want to run on boot
The path to the Python binary that you want to use to run your Flask application
Steps
Open a terminal and create a new service file in the /etc/systemd/system directory. Use a command like this:

sudo nano /etc/systemd/system/myflaskapp.service


Replace myflaskapp with a name for your service.

In the service file, add the following lines:

[Unit]
Description=My Flask Application
After=network.target

[Service]
User=<your username>
WorkingDirectory=/path/to/your/flask/app
ExecStart=/path/to/your/python/binary /path/to/your/flask/app/app.py
Restart=always

[Install]
WantedBy=multi-user.target

Replace <your username> with your Linux username, /path/to/your/flask/app with the path to your Flask application directory, and /path/to/your/python/binary with the path to your Python binary. Make sure to set the ExecStart command to the path of your Flask application's entry point (e.g. app.py).

Save and close the file: Press Ctrl+X, then Y and Enter to save and exit the file.

Reload systemd: Run the following command to reload the systemd daemon and make it aware of the new service:

sudo systemctl daemon-reload


Enable the service: Run the following command to enable the service to start automatically at boot:


sudo systemctl enable myflaskapp.service

Replace myflaskapp with the name you gave to your service.

Start the service: Run the following command to start the service:

sudo systemctl start myflaskapp.service

Replace myflaskapp with the name you gave to your service.

Check the status of your service by running the command:

Replace myflaskapp with the name you gave to your service.

Check the status of your service by running the command:
sudo systemctl status myflaskapp.service
