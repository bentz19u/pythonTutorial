## Running the app through docker

```docker
# build
$ docker build -t neural-api .

# run
# we have to match the port 8000 of the API
$ docker run -p 8000:8000 neural-api

# test is it's working, on another terminal
check http://127.0.0.1:8000 
```