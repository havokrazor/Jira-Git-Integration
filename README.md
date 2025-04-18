In this project we will be doing Github- Jira integration in which we will be utilizing the webooks from Github to send a payload to our small Flask web server.

And this web server will communication to Jira using the API calls (Note - You can setup a web server on your ec2 instance and make sure open up port 5000)

You can understand this better by looking at the image below :

![Screenshot 2025-04-19 032213](https://github.com/user-attachments/assets/faf29e36-35e6-412a-b87b-07b4ea4f99e3)


**What is Flask?**

Flask is a lightweight web framework in Python used to build web applications and APIs. Think of it as a way to let your Python code respond to web requests (like when you visit a webpage or send a request from another app).

`app = Flask(__name__)` This initializes your Flask app. It tells Flask: “Hey, I’m setting up a web app using this file.”

`@app.route('/createJira', methods=['POST'])` is a decorator that tells Flask:
“When someone makes a POST request to /createJira, run the `createJira()` function.”

`if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)`

It means:
“If this file is run directly (not imported), start the Flask web server on all network interfaces (0.0.0.0) and use port 5000.”
So once the server is running, you can make a POST request to http://localhost:5000/createJira, and it will trigger the Jira issue creation logic.







