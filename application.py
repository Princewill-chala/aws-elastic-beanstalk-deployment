from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Welcome to my AWS Elastic Beanstalk deployment!"

if __name__ == "__main__":
    application.run()