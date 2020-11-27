# abracadabra
Make your computer execute whatever you want after you say "abracadabra". This is a basic keyword detection program trained using [teachable machine techonology](https://teachablemachine.withgoogle.com/). If your voice is different from mine it might not work so well, and it might be useful if you go to teachable machine and train a new model with your own voice, it takes a few minutes, then you just need to publish the model and update this line.

## Requirements

- Python 3
- Some python packages (To install them try running `pip install -r requeriments.txt`)

## Running it

```
flask run --host=0.0.0.0 --port=8080
```

Once it's running you should be able to access [http://localhost:8080/](http://localhost:8080/) and see the website, after you press the START button it should start working.
