restfull-web-service-python-tornado
=======

this is test branch, just for test program

use python tornado make restfull web service, include ORM, use python mysqldb

you should install tornado-3.1 and python-mysqldb

cd tornado-3.1/  
python setup.py build  
sudo python setup.py install  

~make sure tornado can be work

sudo apt-get install python-mysqldb  

open you mysql phpmyadmin and creat a database pay  
CREATE TABLE IF NOT EXISTS `test` (  
  `id` int(11) NOT NULL AUTO_INCREMENT,  
  `name` varchar(20) NOT NULL,  
  `pwd` varchar(32) NOT NULL,  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;  

INSERT INTO `test` (`id`, `name`, `pwd`) VALUES  
(1, 'python-test', '123456'),  
(2, 'python-test', '123456'),  
(3, 'python-test', '123456');  

change model/table.py __init__ function to you mysql server information  

sudo chmod -R 777 *  

python server.py

use start.sh or supervisor manage web service restart  
main.port just notes tornado port  

说好了，拍砖随意但不能拍脸。联系方式直接喊一声吧。谢谢
