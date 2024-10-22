## Running the app through docker

```docker
# build
$ docker build -t iris-dockerization .

# run
# we have to match the port 9999 that is used in the script
$ docker run -p 9999:9999 iris-dockerization

# test is it's working, on another terminal
$ telnet 127.0.0.1 9999
```