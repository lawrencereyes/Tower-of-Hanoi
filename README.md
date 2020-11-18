# Tower of Hanoi

The Tower of Hanoi (also called the Tower of Brahma or Lucas' Tower and sometimes pluralized as Towers) is a mathematical game or puzzle. It consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No larger disk may be placed on top of a smaller disk.

## Getting Started

Dependencies:

- Python 3.x
- Flask
    - command 'pip install Flask'
- Flask-RESTful
    - command 'pip install flask-restful'

As soon as you run the API file, api.py, a new game has been started.

## REST API

#### Documentation

- Definition
    - **GET** 'http://127.0.0.1:5000/'

- Response
    - **200 OK** on success. Will print the entire documentation in the browser.

- Python Example

    ```sh
    #Need to install the requests library
    #To install, run 'pip install requests'
    import requests

    r = requests.get('http://127.0.0.1:5000/')

    print(r.text)

#### Start a new game

- Definition
    - **GET** 'http://127.0.0.1:5000/game/new'

- Response
    - **200 OK** on success.
        - Example:
            ```sh
            {
                "message": "You have started a new game the game",
                "status": 200
            }

    - **500 Internal Server Error** on failure.
        - Example:
            ```sh
            {
                "message": "Not able to get the start a new game",
                "status": 500
            }

- Python Example

    ```sh
    #Need to install the requests library
    #To install, run 'pip install requests'
    import requests

    r = requests.get('http://127.0.0.1:5000/game/new')

    print(r.json())

#### Get state of the game

- Definition
    - **GET** 'http://127.0.0.1:5000/game/state'

- Response
    - **200 OK** on success.
        - Example:
            ```sh
            {
                "current_state": {
                    "a": [
                        1,
                        2,
                        3,
                        4
                    ],
                    "b": [],
                    "c": []
                },
                "winner": false,
                "status": 200
            }

    - **500 Internal Server Error** on failure.
        - Example:
            ```sh
            {
                "message": "Not able to get the state of the game",
                "status": 500
            }

- Python Example

    ```sh
    #Need to install the requests library
    #To install, run 'pip install requests'
    import requests

    r = requests.get('http://127.0.0.1:5000/game/state')

    print(r.json())

#### Restart the game

- Definition
    - **GET** 'http://127.0.0.1:5000/game/restart'

- Response
    - **200 OK** on success.
        - Example:
            ```sh
            {
                "message": "You have restarted the game",
                "status": 200
            }

    - **500 Internal Server Error** on failure.
        - Example:
            ```sh
            {
                "message": "Not able to get the start a new game",
                "status": 500
            }

- Python Example

    ```sh
    #Need to install the requests library
    #To install, run 'pip install requests'
    import requests

    r = requests.get('http://127.0.0.1:5000/game/restart')

    print(r.json())

#### Move a disk

- Definition
    - **POST** 'http://127.0.0.1:5000/game/move'

- Response
    - **200 OK** on success.
        - Example:
            ```sh
            {
                "message": "You have made a move. Check the state",
                "status": 200
            }

    - **400 Bad Request** on failure.
        - Examples:
            - If from_rod is empty, meaning we are not able to get a disk to move.
                ```sh
                {
                    "message": "The from_rod you is empty",
                    "status": 400
                }

            - If from_rod and to_rod are the same.
                ```sh
                {
                    "message": "The from_rod and to_rod cannot be the same",
                    "status": 400
                }

            - If the from_rod or to_rod input is wrong.
                ```sh
                {
                    "message": "The rod input is wrong. The only available options are 'a', 'b' or 'c'",
                    "status": 400
                }
            
            - If the to_rod is not empty, check that the disk_to_move is smaller than the top disk in to_rod.
                ```sh
                {
                    "message": "You are only allowed to put a smaller disk on top of another disk",
                    "status": 400
                }

- Python Example

    ```sh
    #Need to install the requests library
    #To install, run 'pip install requests'
    import requests

    d = {
        "from_rod": "a",
        "to_rod": "b"
    }

    r = requests.post('http://127.0.0.1:5000/game/move', data=d)

    print(r.json())