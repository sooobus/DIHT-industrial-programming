A simple to-do list.

Functionality:
1. Add tasks
2. Show tasks
All on localhost/8000

TODO:
1. Mark tasks as completed (not finished)

sudo docker build -t todolist . --network=host
sudo docker run -it -p 8000:8000 todolist
