# abracadabra
Make your computer execute whatever you want after you say "abracadabra".

## How it works?

This is a basic keyword detection program trained using [teachable machine techonology](https://teachablemachine.withgoogle.com/). If your voice is different from [mine](https://github.com/mathigatti/abracadabra/blob/main/data/1.wav) it might not work so well, and it might be better if you go to the teachable machine website and train a new model with your own voice (it takes just a few minutes), then you just need to publish the model and update [this line](https://github.com/mathigatti/abracadabra/blob/main/templates/index.html#L12).

## Requirements

- Python 3
- Some python packages (To install them try running `pip install -r requeriments.txt`)

## Running it

```
flask run --host=0.0.0.0 --port=8080
```

Once it's running you should be able to access [http://localhost:8080/](http://localhost:8080/) and see the website, after you press the START button it should start working.
