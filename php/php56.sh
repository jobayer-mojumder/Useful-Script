# @Author: Jobayer Mojumder
# @Date:   2018-09-24 10:22:32
# @Last Modified by:   jobayer
# @Last Modified time: 2018-09-24 10:23:22

sudo a2dismod php7.1 && sudo a2enmod php5.6 && sudo update-alternatives --set php /usr/bin/php5.6 && sudo service apache2 restart
