import React, { Component } from 'react';
import Webcam from "react-webcam";
import './Interview.css';


export class Interview extends Component {
    // state = {
    //     timerOn: false, //timer will not start automatically
    //     timerStart: 0, //timer will count up from 0
    //     timerTime: 0,
    //     output: ''

    // };
    constructor(props) {
        // Required step: always call the parent class' constructor
        super(props);
    
        // Set the state directly. Use props if necessary.
        this.state = {
            timerOn: false, //timer will not start automatically
            timerStart: 0, //timer will count up from 0
            timerTime: 0,
            output: null
        };
      }

    // This function fetch the api
    addStuffFromApi = () => {
        fetch("/output").then(response=>response.json()).then(data =>{console.log(data); this.setState({output: data.output})})
    }


    // This function update the state (this.state)
    componentDidMount = () => {
        this.addStuffFromApi();
        console.log(this.state)
    }

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
            <div class="flex-container">
                <div class="instructions">
                    <h5>Instructions</h5>
                    <p>
                        Time for some interview practice! The questions will be displayed at the bottom of the webcam video one at a time.
                        When you're done answering the question, click the 'next' button for the next question. The webcam video will analyze
                        your interview behaviours and there will be some feedback at the end of your practice on what you can improve on based
                        on the analysis. There is also a timer that will count up and tell you how much time your "interview" took.
                        Whenever you're ready to start, click the 'Ready!' button. All the best!
                    </p>
                </div>
                <div class="time">
                    <div class="time-display">  
                        <h2>
                            {hours} : {minutes} : {seconds}
                        </h2>
                    </div>

                    <div class="time-button">
                        {this.state.timerOn === false && this.state.timerTime === 0 && 
                        (<button type="button" class="btn btn-success" onClick={this.startTimer}>Ready!</button>)}

                        {this.state.timerOn === true && this.state.timerTime > 0 && 
                        (<button type="button" class="btn btn-primary" onClick={this.stopTimer}>Pause</button>)}

                        {this.state.timerOn === false && this.state.timerTime > 0 && 
                        (<button type="button" class="btn btn-primary" onClick={this.startTimer}>Resume</button>)}
                    </div>
                </div>

                <h1>Flask says {this.state.output}</h1>

                <div class="video">
                    <Webcam
                        audio={true}
                        videoConstraints={videoConstraints}
                    />
                </div>
            </div>
        )
    }
}

export default Interview
