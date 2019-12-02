
API implementation for CamemBERT:
[https://camembert-model.fr/](https://camembert-model.fr/)

# Docker for API

You can build and run the docker using the following process:

Cloning
```console
git clone https://github.com/jqueguiner/camembert-as-a-service.git caas
```

Building Docker
```console
cd caas && docker build -t caas -f Dockerfile .
```

Running Docker
```console
echo "http://$(curl ifconfig.io):5000" && docker run -p 5000:5000 -d caas
```

Calling the API
```console
curl -X POST "http://MY_SUPER_API_IP:5000/process" -H "accept: application/json" -H "Content-Type: application/json" -d '{"text":"Le camembert est <mask> :)", "top_k": 5}'
```
