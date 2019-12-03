FROM tensorflow/tensorflow:1.14.0-gpu-py3

RUN apt-get update -y

RUN apt-get install vim -y
ADD src /src

WORKDIR /src

# Spleeter installation.
RUN apt-get update && apt-get install -y ffmpeg libsndfile1 wget
RUN pip install musdb museval
RUN pip install spleeter-gpu==1.4.5
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]
