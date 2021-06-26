### Dockerfile
[Here](Dockerfile)

### Build image:latest
```
# docker rmi tuiladat/socialfeeder
docker build --tag tuiladat/socialfeeder:latest .
```

### Run containter
```
# remove exists container:
docker rm socialfeeder

# run with default arguments
docker run --name "socialfeeder" tuiladat/socialfeeder

# run with custom arguments
docker run \
    --name "socialfeeder" \
    --env SOCIAL="facebook" \
    --env CONFIG="/samples/noexist.xml" \
    tuiladat/socialfeeder
```


### Publish to Hub
```
docker push tuiladat/socialfeeder:latest
```
