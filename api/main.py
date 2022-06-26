"""
uvicorn main:app --reload

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

https://fastapi.tiangolo.com/tutorial/first-steps/
https://www.datacamp.com/tutorial/machine-learning-models-api-python
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Welcome to machine learning model APIs!"


# if __name__ == '__main__':
#     app.run(debug=True)
