# tello-gamepad (work in progress)
## 🎮🛸 fly tello drones with a gamepad

*using the [JS Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API), [Flask](https://flask.palletsprojects.com/en/2.1.x/), and [DJITelloPy](https://github.com/damiafuentes/DJITelloPy/)*

### Installation
- Clone the repository and install the requirements with `pip -r requirements.txt`
- Connect to a Tello drone and a gamepad
- Run `python main.py`; the command line output will show that the server is running on `http://127.0.0.1:5000` - run the browser and test if everything is working properly

### Known issues
- [ ] Streaming the video is not done very well and causes lagging
- [ ] Smooth movement is not possible (drone moves 20 cm at a time)