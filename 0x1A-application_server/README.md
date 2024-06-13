# 0x1A. Application Server

This project is part of the ALX System Engineering & DevOps curriculum. It focuses on setting up a development environment for testing and debugging before deploying to production.

## Setup Instructions

1. **Install net-tools on the server**:
    ```sh
    sudo apt update
    sudo apt install -y net-tools
    ```

2. **Clone the AirBnB clone repository**:
    ```sh
    git clone https://github.com/yourusername/AirBnB_clone_v2.git
    cd AirBnB_clone_v2
    ```

3. **Install necessary packages**:
    ```sh
    sudo apt install -y python3 python3-pip
    sudo pip3 install Flask SQLAlchemy Flask-SQLAlchemy pymysql
    ```

4. **Modify the Flask application**:
    - Navigate to `web_flask` directory.
    - Create or edit `0-hello_route.py` with the following content:
    ```python
    #!/usr/bin/python3
    from flask import Flask

    app = Flask(__name__)

    @app.route('/airbnb-onepage/', strict_slashes=False)
    def hello_hbnb():
        return "Hello HBNB!"

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
    ```

5. **Run the Flask application**:
    ```sh
    python3 -m web_flask.0-hello_route
    ```

6. **Verify the setup**:
    ```sh
    curl 127.0.0.1:5000/airbnb-onepage/
    ```

## Expected Output

When you run the curl command, you should see:

