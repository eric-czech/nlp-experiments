## Running remote USE service

ndocker build -t guse-as-service -f Dockerfile .
# Bind anything local to /app/cache so that tf-hub models are persisted across runs
ndocker run -ti -p 5000:5000 -v /home/eczech/repos/misc/tfhubserver/cache:/app/cache guse-as-service
