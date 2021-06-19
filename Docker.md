### Dockerfile
[Here](Dockerfile)

### Build image:latest
```
# docker rmi socialfeeder
docker build --tag tuiladat/socialfeeder:latest .
```

### Run containter
```
# remove exists container:
docker rm socialfeeder

# run with default arguments
docker run --name "socialfeeder" --env CONFIG="/samples/noexist.xml" socialfeeder

# run with custom arguments
docker run \
    --name "socialfeeder" \
    --env SOCIAL="facebook" \
    --env CONFIG="/samples/noexist.xml" \
    socialfeeder
```

