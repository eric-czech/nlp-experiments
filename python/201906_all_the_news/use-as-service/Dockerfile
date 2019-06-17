FROM tensorflow/tensorflow:1.12.0-gpu-py3
RUN pip install flask tensorflow-hub
COPY ./* /app/
RUN mkdir /app/cache
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV TFHUB_CACHE_DIR /app/cache
ENV FLASK_APP universal_sentence_encoder.py
WORKDIR /app
CMD flask run --host=0.0.0.0
