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
    while True:
        image = drone.get_frame_read().frame
        image = cv2.resize(image, (480, 360))
        ret, jpeg = cv2.imencode('.jpg', image)

        frame = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def moveDrone(command):
    match command:
        case 'button up':
            return None
        case 'button down':
            return None
        case 'button left':
            return None
        case 'button right':
            return None
        case 'A':
            drone.takeoff()
        case 'B':
            drone.land()
        case 'X':
            return None
        case 'Y':
            return None
        case 'LB':
            return None
        case 'RB':
            return None
        case 'LT':
            return None
        case 'RT':
            return None
        case 'left stick up':
            return None
        case 'left stick down':
            return None
        case 'left stick right':
            return None
        case 'left stick left':
            return None
        case 'right stick up':
            return None
        case 'right stick down':
            return None
        case 'right stick right':
            return None
        case 'right stick left':
            return None


@app.route('/stream')
def video_feed():
    global video

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
