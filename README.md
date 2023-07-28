### Start application

Run the line below in the terminal

STEP 1
```shell
rasa run --enable-api --cors "*"
```


STEP 2
```shell
poetry run uvicorn app:app --reload --host=0.0.0.0 --port=8080
```

STEP 3
Navigate to: http://0.0.0.0:8080/docs
