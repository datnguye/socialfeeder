# socialfeeder
Mini CLI to feed social activities with supported actions:
* click
* fill
* browse
* scroll down
* wait
* save-text

Installation:
* From [pip](https://pypi.org/project/socialfeeder/) 
```
python -m pip install socialfeeder --upgrade

# install from git
python -m pip install git+https://github.com/datnguye/socialfeeder.git --upgrade

# check version
python -m socialfeeder --version
```

* From [docker hub](https://hub.docker.com/repository/docker/tuiladat/socialfeeder/general)
```
docker pull tuiladat/socialfeeder:latest
```


## Usage
```
python -m socialfeeder --help
```

Sample commands:
* Run facebook:
```
python -m socialfeeder --social "facebook" --config "C:\Users\DAT\Documents\Sources\socialfeeder\samples\like_top_5-share_2-posts.xml" --feed
```

## Development Enviroment
Virtual enviroment:
```
python -m venv env
```

Activate virtual env:
```
Windows: 	.\env\Scripts\activate
Linux:		source env/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```


