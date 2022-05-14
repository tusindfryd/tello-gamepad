let buttonEvent = (button) => {
    fetch(`/getdata/${button}`)
        .then((response) => {
            return response.text();
        })
}

gameControl.on('connect', function (gamepad) {
        // d-pad
        gamepad.after('button12', () => {
            buttonEvent("button_up")
        });
        gamepad.after('button13', () => {
            buttonEvent("button_down")
        });
        gamepad.after('button14', () => {
            buttonEvent("button_left")
        });
        gamepad.after('button15', () => {
            buttonEvent("button_right")
        });

        // action buttons
        gamepad.after('button0', () => {
            buttonEvent("A")
        });
        gamepad.after('button1', () => {
            buttonEvent("B")
        });
        gamepad.after('button2', () => {
            buttonEvent("X")
        });
        gamepad.after('button3', () => {
            buttonEvent("Y")
        });

        // shoulder buttons
        gamepad.after('button4', () => {
            buttonEvent("LB")
        });
        gamepad.after('button5', () => {
            buttonEvent("RB")
        });
        gamepad.after('button6', () => {
            buttonEvent("LT")
        });
        gamepad.after('button7', () => {
            buttonEvent("RT")
        });

        // left stick
        gamepad.after('up0', () => {
            buttonEvent("left_stick_up")
        });
        gamepad.after('down0', () => {
            buttonEvent("left_stick_down")
        });
        gamepad.after('right0', () => {
            buttonEvent("left_stick_right")
        });
        gamepad.after('left0', () => {
            buttonEvent("left_stick_left")
        });

        // right stick
        gamepad.after('up1', () => {
            buttonEvent("right_stick_up")
        });
        gamepad.after('down1', () => {
            buttonEvent("right_stick_down")
        });
        gamepad.after('right1', () => {
            buttonEvent("right_stick_right")
        });
        gamepad.after('left1', () => {
            buttonEvent("right_stick_left")
        });

        // gamepad visualization

        for (let x = 0; x < Math.min(17, gamepad.buttons); x++) {
            gamepad.on('button' + x, function () {
                document.querySelector('#button-' + x).classList.toggle('active', true);
            });
        }
        for (let x = 0; x < Math.min(2, gamepad.axes); x++) {
            const directions = ['up', 'down', 'right', 'left'];
            for (let d = 0; d < directions.length; d++) {
                gamepad.on(directions[d] + x, function () {
                    document
                        .querySelector('#axe-' + x + '-' + directions[d])
                        .classList.toggle('active', true);
                });
            }
        }
    })
    .on('beforeCycle', function () {
        const active = document.querySelectorAll('.active');
        for (let x = 0; x < active.length; x++) {
            active[x].classList.toggle('active', false);
        }
    });