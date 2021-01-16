import React from 'react';
import makeStyles from '@material-ui/styles/makeStyles';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid'; 
import Card from 'react-bootstrap/Card';


const useStyles = makeStyles({
	container: {
		paddingLeft: '60px'
	},
    button: {
		color: 'white',
		textTransform: 'None'
    }
});

function Landing() {
	const classes = useStyles();

	return (

      
		<div style={{width:"60%"}}> 
                <h6> bug fix </h6>
                <h6> bug fix </h6>
                <h6> bug fix </h6>
          
        <Card 
        border="success" 
        style={{ width: '38rem' }}
        >
			<Grid container spacing={2} className={classes.container}>
				<Grid item xs={10}>
					<Typography varaint="h1" style={{color: "pink", fontSize: "110px", fontFamily: "Righteous", marginTop: "50px"}}>Cheernut.</Typography>
                    <Typography varaint="h1" style={{color: "pink", fontSize: "60px", fontFamily: "Righteous", marginTop: "-50px"}}>(cheet-or-nut)</Typography>
					<Typography varaint="h2" style={{color: "pink", fontSize: "20px", marginTop: "20px"}}><strong>An AI tool to detect and pick up potential instances of cheating during exams over Zoom calls</strong></Typography>
					<Typography varaint="h3" style={{color: "pink", fontSize: "17px"}}>Talko will work with you to improve enunciation, pace, volume and much more. Input your speech now, and let's get talking!</Typography>
					<br />
                    <Button href="/Interview" variant="outlined" color="primary" >
						<Typography variant="h4" display="inline"><b>Get Started</b></Typography>&nbsp;&nbsp;
					</Button>
                    </Grid>
                    <Grid item xs={2}>
				</Grid>
                </Grid>
                </Card>

            </div>		
	);
}

export default Landing;
