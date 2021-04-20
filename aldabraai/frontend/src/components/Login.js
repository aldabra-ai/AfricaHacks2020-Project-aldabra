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

const Login = () => {
  const paperStyle = {
    padding: 5,
    height: "70vh",
    width: 280,
    margin: "20px auto",
    backgroundColor: 'rgba(255, 255, 255, 0.3)',
    backgroundImage: 'linear-gradient(to bottom right, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0)',
    boxShadow: "10px 10px 10px rgba(216,191,216)",
    backdropFilter: 'blur(7px)',
    boarderRadius:20,
    boarderLeft: 'solid 1px rgba(255, 255, 255, 0.3)',
    boarderTop: 'solid 1px rgba(255, 255, 255, 0.8)',

  };
  const headerStyle = { margin: 0 };
  const avatarStyle = { backgroundColor: "#3700B3" };
  const buttonStyle = { margin: "8px 0", backgroundColor: "#FFDCE8" };
  const checkboxStyle = { backgroundColor: "#FFDCE8" };

  return (
    <Grid>
      <Paper elevation={10} style={paperStyle}>
        <Grid align="center">
          <Avatar style={avatarStyle}>
            <LockOutlinedIcon />
          </Avatar>
          <h2 style={headerStyle}>Sign In</h2>
          <h5>
            You don’t think you should login first and behave like human not
            robot.
          </h5>
        </Grid>
        <TextField
          label="Email Address"
          placeholder="Enter email"
          fullWidth
          required
          variant="outlined"
          autoComplete='email'
          auto
        />
        {/* This h6 tag is for the spacing from top to bottom never delete it*/}
        <h6></h6>
        <TextField
          label="Password"
          placeholder="Enter password"
          type="password"
          fullWidth
          required
          variant="outlined"
        />
        {/* This h6 tag is for the spacing from top to bottom never delete it*/}
        <h6></h6>
        <FormControlLabel
          control={<Checkbox name="checkedB" style={checkboxStyle} />}
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
          <Link href="#">
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
