
API implementation for Spleeter:
[https://github.com/deezer/spleeter](https://github.com/deezer/spleeter)

# Docker for API

You can build and run the docker using the following process:

Cloning
```console
git clone https://github.com/jqueguiner/spleeter-as-a-service.git spaas
```

Building Docker
```console
cd spaas && docker build -t spaas -f Dockerfile .
```

Running Docker
```console
echo "http://$(curl ifconfig.io):5000" && docker run -p 5000:5000 -d spaas
```

Calling the API
```console
curl -X POST "http://MY_SUPER_API_IP:5000/process" -H "accept: application/json" -H "Content-Type: application/json" -d '{"url": "https://github.com/deezer/spleeter/raw/master/audio_example.mp3", "nb_stems": 5}'
```
