import React, { Component } from 'react'
import Webcam from "react-webcam"


export class Interview extends Component {
    state = {
        timerOn: false, //timer will not start automatically
        timerStart: 0, //timer will count up from 0
        timerTime: 0
    };

    startTimer = () => {
        this.setState({
            timerOn: true,
            timerTime: this.state.timerTime,
            timerStart: Date.now() - this.state.timerTime
        });
        this.timer = setInterval ( () => {
            this.setState({
                timerTime: Date.now() - this.state.timerStart
            });
        }, 10);
    };

    stopTimer = () => {
        this.setState({
            timerOn: false
        });
        clearInterval(this.timer);
    };

    resetTimer = () => {
        this.setState({
            timerStart: 0,
            timerTime: 0
        });
    };

    render() {
        const videoConstraints = {
            width: 575,
            height: 375,
            mirrored: true,
            facingMode: "user" //front-facing camera
        };

        const {timerTime} = this.state;
        let hours = ("0" + (Math.floor(timerTime / 3600000) % 60)).slice(-2);
        let minutes = ("0" + (Math.floor(timerTime / 60000) % 60)).slice(-2);
        let seconds = ("0" + Math.floor(timerTime / 1000)).slice(-2);

       

        return (
            <div>
                <h2 style={{
                    position: 'absolute', left: '33.75%', top: '33%',
                    transform: 'translate(-50%, -50%)'
                }}>
                    {hours} : {minutes} : {seconds}
                </h2>

                {this.state.timerOn === false && this.state.timerTime === 0 && 
                (<button style={{
                    position: 'absolute', left: '70%', top: '33%',
                    transform: 'translate(-50%, -50%)'
                }} type="button" class="btn btn-success" onClick={this.startTimer}>Ready!</button>)}

                {this.state.timerOn === true && this.state.timerTime > 0 && 
                (<button style={{
                    position: 'absolute', left: '70%', top: '33%',
                    transform: 'translate(-50%, -50%)'
                }} type="button" class="btn btn-primary" onClick={this.stopTimer}>Pause</button>)}

                {this.state.timerOn === false && this.state.timerTime > 0 && 
                (<button style={{
                    position: 'absolute', left: '70%', top: '33%',
                    transform: 'translate(-50%, -50%)'
                }} type="button" class="btn btn-primary" onClick={this.startTimer}>Resume</button>)}

                <Webcam
                    style={{ //centering the videofeed
                        position: 'absolute', left: '50%', top: '70%',
                        transform: 'translate(-50%, -50%)'
                    }}
                    audio={true}
                    videoConstraints={videoConstraints}
                />
            </div>
        )
    }
}

export default Interview
