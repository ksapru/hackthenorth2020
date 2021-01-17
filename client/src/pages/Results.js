import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import React, { Component } from 'react';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid'
 
// import Logo from "../../assets/icons/logow.webp";

export class Results extends Component {

    constructor(props) {
        // Required step: always call the parent class' constructor
        super(props);
    
        // Set the state directly. Use props if necessary.
        this.state = {
            text: "",
            sentiment: 0,
            smiling: 0,
            looking_at_camera: 0,
            eyes_visible: 0
        };
      }
    
    getDataFromGCD = () => {
        fetch("/render").then(response=>response.json()).then(data =>{console.log(data); this.setState({text: data.text, sentiment: data.sentiment, smiling: data.smiling, looking_at_camera: data.looking_at_camera, eyes_visible: data.eyes_visible})});
    }

    componentDidMount = () => {
        this.getDataFromGCD();
        console.log(this.state);
    }

    render() {
        // const state = {
        //     labels: ['1', '2', '3', '4', '5'],
        //     datasets: [
        //         {
        //             label: 'Energy',
        //             fill: false,
        //             lineTension: 0.5,
        //             backgroundColor: '#324F5D',
        //             borderColor: 'white',
        //             borderWidth: 2,
        //             data: [35, 21, 18, 37, 26]
            
        //         }
        //     ],
        //     height: '100px'
        // };
        return (
            <div>
               <h1>34</h1>
               <h6>''</h6>
               <h1>Congrats! You are now done!</h1>

               <button class="btn btn-primary" type="button" disabled>
                 <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                Loading...
                </button>

                <Grid container spacing={1} style={{ height: '100%' }}>
                    <Grid item xs={3} style={{marginLeft:"50px"}}>
                        <Box style={{height: "370px", width: "370px", borderRadius: "50%", backgroundColor: "#1B372D", marginTop:"-25px"}}/>
                        <Box style={{height: "285px", width: "285px", borderRadius: "50%", backgroundColor: "#3C7C64", marginTop: "-326px", marginLeft: "44px"}}/>
                        <Box style={{height: "230px", width: "230px", borderRadius: "50%", backgroundColor: "#52AA8A", marginTop: "-259px", marginLeft:"71px"}}/>
                        <Typography varaint="h3" style={{color: "white", fontSize: "70px", fontFamily: "Montserrat", marginTop: "-170px", marginLeft: "114px"}}><strong> {(this.state.eyes_visible + this.state.sentiment + this.state.smiling + this.state.looking_at_camera)/4}%</strong></Typography>
                    </Grid>
                    <Grid item xs={3}>
                        <Typography varaint="h3" style={{color: "white", fontSize: "20px", fontFamily: "Montserrat", marginTop: "85px", marginLeft: "99px"}}>
                            Excellent speaking! From our analysis, the tone of your speech was {(this.state.eyes_visible + this.state.sentiment + this.state.smiling + this.state.looking_at_camera)/4}% positive, which matches your initial selection.
                        </Typography>
                    </Grid>
                    
                    <Grid item xs={1}>
                        <Box style={{border: "9px solid #E76F51", height: "145px", width: "145px", borderRadius: "50%", marginTop:"100px", marginLeft: "45px"}}/>
                        <Typography varaint="h3" style={{color: "white", fontSize: "20px", fontFamily: "Montserrat", marginTop: "-172px", marginLeft: "81px", marginTop: "10px"}}><strong> Eye Visiblility </strong></Typography>
                        <Typography varaint="h3" style={{color: "white", fontSize: "45px", fontFamily: "Montserrat", marginTop: "-181px", marginLeft: "94px"}}><strong>{this.state.eyes_visible}%</strong></Typography>
                    </Grid>
                </Grid>

                <Grid item xs={2}>
                        <Box style={{border: "9px solid #E76F51", height: "145px", width: "155px", borderRadius: "50%", marginTop:"100px", marginLeft: "45px"}}/>
                        <Typography varaint="h3" style={{color: "white", fontSize: "20px", fontFamily: "Montserrat", marginTop: "-172px", marginLeft: "81px", marginTop: "10px"}}><strong> Sentiments </strong></Typography>
                        <Typography varaint="h3" style={{color: "white", fontSize: "45px", fontFamily: "Montserrat", marginTop: "-181px", marginLeft: "94px"}}><strong>{this.state.sentiment}%</strong></Typography>
               
                        <Box style={{border: "9px solid #E76F51", height: "145px", width: "145px", borderRadius: "50%", marginTop:"100px", marginLeft: "45px"}}/>
                        <Typography varaint="h3" style={{color: "white", fontSize: "20px", fontFamily: "Montserrat", marginTop: "-172px", marginLeft: "81px", marginTop: "10px"}}><strong> Smiling </strong></Typography>
                        <Typography varaint="h3" style={{color: "white", fontSize: "45px", fontFamily: "Montserrat", marginTop: "-181px", marginLeft: "94px"}}><strong>{this.state.smiling}%</strong></Typography>
                
                        <Box style={{border: "9px solid #E76F51", height: "145px", width: "145px", borderRadius: "50%", marginTop:"100px", marginLeft: "45px"}}/>
                        <Typography varaint="h3" style={{color: "white", fontSize: "20px", fontFamily: "Montserrat", marginTop: "-172px", marginLeft: "81px", marginTop: "10px"}}><strong> Looking at the Camera</strong></Typography>
                        <Typography varaint="h3" style={{color: "white", fontSize: "45px", fontFamily: "Montserrat", marginTop: "-181px", marginLeft: "94px"}}><strong>{this.state.looking_at_camera}%</strong></Typography>
                </Grid>
                
                <Grid container spacing={6}>
                    <Grid item md={6}>
                        <Button style={{backgroundColor: "#1A2930", height: "50px", width: "200px", border: "2px solid #F2C407", color: "white", borderRadius: "15px", marginLeft: "200px", marginTop: "120px"}}>
                            <Typography variant="h3" style={{fontFamily: "Montserrat", fontSize: "18px"}}>One more time!  </Typography> 
                        </Button>
                    </Grid>
                </Grid>
    

 
                
            </div>

            
        );
    };
}

export default Results;
