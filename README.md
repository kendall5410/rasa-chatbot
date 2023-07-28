### Start application

Run the line below in the terminal

STEP 1: navigate to the project directory

```shell 
cd /Users/ericharrison/hackthon_project/chatbot_project
```

STEP 2: activate the poetry env
```shell

poetry shell

```

STEP 3: run the command below in the terminal
```shell
rasa run --enable-api --cors "*"
```


STEP 4: open up another terminal (`command + t`), activate the shell again (STEP 2), and run the command below. 
```shell
poetry run uvicorn app:app --reload --host=0.0.0.0 --port=8081
```

STEP 5: Open up the link below in chrome
Navigate to: http://0.0.0.0:8081/docs
