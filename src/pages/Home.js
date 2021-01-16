import React from 'react';
import makeStyles from '@material-ui/styles/makeStyles';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid'; 
import Card from 'react-bootstrap/Card';


const useStyles = makeStyles({
	container: {
        paddingLeft: '20px',
        align:'center'
	},
    button: {
		color: 'white',
        textTransform: 'None',
        alignContent: 'center'
    }
});

function Landing() {
	const classes = useStyles();

	return (

      
		<div className="this" style={{width:"60%"}}> 
                <h6> bug  </h6>
                <h6> bug  </h6>
                <h6> bug  </h6>
  
        <Card border="success" style={{ width: '38rem' }} align="left"  >
    

			<Grid container spacing={2} className={classes.container} align="center">
				<Grid item xs={200}>
					<Typography varaint="h1" style={{color: "pink", fontSize: "110px", fontFamily: "Righteous", marginTop: "50px"}}>IntAI.</Typography>
                    <Typography varaint="h1" style={{color: "pink", fontSize: "30px", fontFamily: "Righteous", marginTop: "-30px"}}> Your home for interview preparation!</Typography>
					<Typography varaint="h2" style={{color: "pink", fontSize: "20px", marginTop: "20px"}}><strong>Welcome to an AI tool to detect and pick up potential shortcomings and help you prepare to be a better interview taker!</strong></Typography>
					<Typography varaint="h3" style={{color: "pink", fontSize: "17px"}}>IntAI will work with you to improve enunciation, pace, volume and much more. Input your speech now, and let's get talking!</Typography>
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
