docker build -t linkedin_test -f Dockerfile.test .

docker run --rm -t -i -p 8000:8000 linkedin_test
