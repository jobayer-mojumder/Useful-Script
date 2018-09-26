# @Author: Jobayer Mojumder
# @Date:   2018-09-24 10:23:40
# @Last Modified by:   jobayer
# @Last Modified time: 2018-09-24 10:24:06
sudo a2dismod php5.6 && sudo a2enmod php7.1 && sudo update-alternatives --set php /usr/bin/php7.1 && sudo service apache2 restart
