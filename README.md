openvote-restapi
================

Install:    

$ virtualenv env    
$ source env/bin/activiate    
$ git clone https://github.com/sammyfung/openvote-restapi    
$ pip install -r openvote-restapi/requirements.txt    

Run:    

$ python openvote-restapi.py    

Test:     

$ curl -d 'votedata=helloworld' http://localhost:5000/api/1.0/vote    

