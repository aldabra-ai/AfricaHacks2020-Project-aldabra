import {
  Avatar,
  Button,
  Checkbox,
  FormControl,
  FormControlLabel,
  FormLabel,
  Grid,
  Paper,
  Radio,
  RadioGroup,
  TextField,
  Typography,
} from "@material-ui/core";
import React from "react";
import AssignmentIndOutlinedIcon from "@material-ui/icons/AssignmentIndOutlined";

//Component for sign up
const SignUp = () => {
  const paperStyle = {
    padding: 20,
    width: 300,
    margin: "0 auto",
    backgroundColor: "rgba(255, 255, 255, 0.3)",
    backgroundImage:
      "linear-gradient(to bottom right, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0)",
    boxShadow: "10px 10px 10px rgba(214,177,255)",
    backdropFilter: "blur(7px)",
    boarderRadius: 20,
    boarderLeft: "solid 1px rgba(255, 255, 255, 0.3)",
    boarderTop: "solid 1px rgba(255, 255, 255, 0.8)",
  };
  const headerStyle = { margin: 0 };
  const avatarStyle = { backgroundColor: "#3700B3" };
  const buttonStyle = { margin: "8px 0", backgroundColor: "#2EC5CE" };
  const checkboxStyle = { backgroundColor: "#FFDCE8" };
  const marginTop = { marginTop: 5 };
  return (
    <Grid>
      <Paper style={paperStyle}>
        <Grid align="center">
          <Avatar style={avatarStyle}>
            <AssignmentIndOutlinedIcon />
          </Avatar>
          <h4 style={headerStyle}>Sign Up!</h4>
          <Typography variant="caption">
            You have chance to create new account if you really want to.
          </Typography>
        </Grid>
        <form>
          <TextField
            fullWidth
            label="Name"
            placeholder="Enter Name"
            // variant="outlined"
          />
          {/* This h6 tag is for the spacing from top to bottom never delete it*/}
          {/* <h6></h6> */}
          <TextField
            fullWidth
            label="Email"
            placeholder="Enter Email"
            // variant="outlined"
          />
          {/* This h6 tag is for the spacing from top to bottom never delete it*/}
          {/* I want to create a style for the radioBTNS to complement the theme as for the color purple */}
          <h6></h6>
          <FormControl component="fieldset">
            <FormLabel component="legend">Gender</FormLabel>
            <RadioGroup
              aria-label="gender"
              name="gender"
              style={{ display: "Initial" }}
            >
              <FormControlLabel
                value="female"
                control={<Radio />}
                label="Female"
              />
              <FormControlLabel value="male" control={<Radio />} label="Male" />
              <FormControlLabel
                value="other"
                control={<Radio />}
                label="Other"
              />
            </RadioGroup>
          </FormControl>
          {/* This h6 tag is for the spacing from top to bottom never delete it*/}
          <TextField
            fullWidth
            label="Phone Number"
            placeholder="Enter Phone Number"
            // variant="outlined"
          />
          {/* This h6 tag is for the spacing from top to bottom never delete it*/}
          {/* <h6></h6> */}
          <TextField
            fullWidth
            label="Password"
            placeholder="Enter Password"
            // variant="outlined"
          />
          {/* This h6 tag is for the spacing from top to bottom never delete it*/}
          {/* <h6></h6> */}
          <TextField
            fullWidth
            label="Confirm Password"
            placeholder="Confirm Password"
            // variant="outlined"
          />
          {/* //CheckBox insertions */}
          {/* This h6 tag is for the spacing from top to bottom never delete it
          <h6></h6> */}
          <FormControlLabel
            control={<Checkbox name="checkedA" />}
            label="I accept the terms and conditions"
          />
          <Button
            type="submit"
            // variant="contained"
            style={buttonStyle}
            fullWidth
          >
            Sign Up!
          </Button>
        </form>
      </Paper>
    </Grid>
  );
};

export default SignUp;

//git add  .   git commit -m "deploy my react app to github pages"  npm run deploy  git push -u origin master
