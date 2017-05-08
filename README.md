We have to install the uwgsi (#apt-get install nginx-full uwsgi uwsgi-plugin-python) for run the script througn the nginx.
Also we install the sysstat (#apt-get install sysstat) to get the statistics ##This command works only for Ubuntu and Debian
Small note about the sysstat when you install the command it's by default "ENABLED = false" on your vi /etc/default/sysstat you have to change it to "ENABLED = true"

