To run:

sudo docker-compose run sender

sudo docker-compose run receiver

Sender and receiver are stored in cloud. Files here are not needed (only docker-compose is enough).


NB: to edit sender and receiver

 sudo docker build -t receive . --network=host

 sudo docker tag receive:latest sooobus/receive:v1
 
 sudo docker push sooobus/receive:v1
