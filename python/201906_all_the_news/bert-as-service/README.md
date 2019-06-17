## Run BERT as service

Clone https://github.com/hanxiao/bert-as-service # cd to top level
ndocker build -t bert-as-service -f ./docker/Dockerfile .
NUM_WORKER=1
PATH_MODEL=/home/eczech/data/bert/uncased_L-12_H-768_A-12 # Must download first from https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip
# Run in foreground
ndocker run -it -p 5555:5555 -p 5556:5556 -v $PATH_MODEL:/model --rm -t bert-as-service $NUM_WORKER 
