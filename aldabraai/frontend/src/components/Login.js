import React from "react";
import {
  Avatar,
  Button,
  Checkbox,
  FormControlLabel,
  Grid,
  Link,
  Paper,
  TextField,
  Typography,
} from "@material-ui/core";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";

const Login = ({handleChange}) => {
  const paperStyle = {
    padding: 20,
    height: "63.1vh",
    width: 300,
    margin: "0 auto",
    backgroundColor: 'rgba(255, 255, 255, 0.3)',
    backgroundImage: 'linear-gradient(to bottom right, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0)',
    boxShadow: "10px 10px 10px rgba(214,177,255)",
    backdropFilter: 'blur(7px)',
    boarderRadius:20,
    boarderLeft: 'solid 1px rgba(255, 255, 255, 0.3)',
    boarderTop: 'solid 1px rgba(255, 255, 255, 0.8)',

  };
  const headerStyle = { margin: 0 };
  const avatarStyle = { backgroundColor: "#3700B3" };
  const buttonStyle = { margin: "8px 0", backgroundColor: "#2EC5CE" };
  const checkboxStyle = { backgroundColor: "#FFDCE8" };

  return (
    <Grid>
      <Paper  style={paperStyle}>
        <Grid align="center">
          <Avatar style={avatarStyle}>
            <LockOutlinedIcon />
          </Avatar>
          <h4 style={headerStyle}>Sign In</h4>
         <Typography variant="caption">
            You don’t think you should login first and behave like human not
            robot.
          </Typography>
        </Grid>
        <TextField
          label="Email Address"
          placeholder="Enter email"
          fullWidth
          required
          // variant="outlined"
          autoComplete='email'
          auto
        />
        {/* This h6 tag is for the spacing from top to bottom never delete it*/}
        {/* <h6></h6> */}
        <TextField
          label="Password"
          placeholder="Enter password"
          type="password"
          fullWidth
          required
          // variant="outlined"
        />
        {/* This h6 tag is for the spacing from top to bottom never delete it*/}
        {/* <h6></h6> */}
        <FormControlLabel
          control={<Checkbox name="checkedB"  />}
          label="Remember me"
        />
        <Button type="submit" variant="contained" style={buttonStyle} fullWidth>
          Sign In
        </Button>
        <Typography>
          <Link href="#">
            {" "}
            {/* onClick={preventDefault}*/}
            Forgot Password ?
          </Link>
        </Typography>
        <Typography>
          Do you have an account ?
          <Link href="#" onClick ={() =>handleChange('event',1)}>
            {" "}
            {/* onClick={preventDefault}*/}
            Sign Up
          </Link>
        </Typography>
      </Paper>
    </Grid>
  );
};

export default Login;
//git add  .   git commit -m "deploy my react app to github pages"  npm run deploy  git push -u origin master
