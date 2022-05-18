from flask import Flask, Response, render_template, request
import threading
import socket
from djitellopy import Tello
import cv2

app = Flask(__name__, static_folder='static')

drone = Tello()
drone.connect()
drone.streamon()


def generate_frame():
    counter = 1

    while True:
        if counter % 100 == 0:
            counter = 1
            image = drone.get_frame_read().frame
            image = cv2.resize(image, (480, 360))
            ret, jpeg = cv2.imencode('.jpg', image)

            frame = jpeg.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            counter = counter + 1


def moveDrone(command):
    print(f'Command: {command}')
    print(f'Battery: {drone.get_battery()}')

    match command:
        case 'button_up':
            return None
        case 'button_down':
            return None
        case 'button_left':
            return None
        case 'button_right':
            return None
        case 'A':
            drone.takeoff()
            return None
        case 'B':
            drone.land()
            return None
        case 'X':
            return None
        case 'Y':
            return None
        case 'LB':
            return None
        case 'RB':
            return None
        case 'LT':
            drone.move_down(20)
            return None
        case 'RT':
            drone.move_up(20)
            return None
        case 'left_stick_up':
            drone.move_forward(20)
            return None
        case 'left_stick_down':
            drone.move_back(20)
            return None
        case 'left_stick_right':
            drone.move_right(20)
            return None
        case 'left_stick_left':
            drone.move_left(20)
            return None
        case 'right_stick_up':
            return None
        case 'right_stick_down':
            return None
        case 'right_stick_right':
            drone.rotate_clockwise(30)
            return None
        case 'right_stick_left':
            drone.rotate_counter_clockwise(30)
            return None


@app.route('/stream')
def video_feed():
    return Response(generate_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/getdata/<button>', methods=['GET', 'POST'])
def data_get(button):

    if request.method == 'POST':
        return 'OK', 200

    else:
        moveDrone(button)
        return (button)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        host = '0.0.0.0'
        port = 9000
        s.bind((host, port))

        def recv():
            global tello_response
            while True:
                try:
                    tello_response, server = s.recvfrom(1518)
                    tello_response = tello_response.decode(
                        encoding="utf-8")
                except Exception:
                    print('\nExit...\n')
                    break

        recvThread = threading.Thread(target=recv)
        recvThread.start()

        app.run(host='0.0.0.0', threaded=True)
