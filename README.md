openvote-restapi
================

Changing RabbitMQ guest account password to 'guest' after installation of RabbitMQ.     
$ sudo rabbitmqctl change_password guest guest    
You should change password at production.     

Install:    

$ virtualenv env    
$ source env/bin/activate
$ git clone https://github.com/sammyfung/openvote-restapi    
$ pip install -r openvote-restapi/requirements.txt    

Run:    

$ python openvote-restapi.py    

Test:     

$ curl -d 'votedata=helloworld' http://localhost:5000/api/v1.0/vote    

