import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";
import { Card, Grid } from "@material-ui/core";
import React from "react";
import Content from "./components/Content";
import NavBar from "./components/NavBar";

//Pages and their imports
import Home from "./components/Home";
import About from "./components/About";
import Contact from "./components/Contact";
import Pricing from "./components/Pricing";
// import Login from "./components/Login";
// import SignUp from "./components/SignUp";
import { makeStyles } from '@material-ui/core/styles';
import SIgnInOut from "./components/SIgnInOut";


const useStyles =makeStyles({
  gridContainer:{
    paddingLeft:'20px',
    paddingRight:'20px'
  }
});

export default function App() {
  const classes =useStyles();
  return (
    <div><Router>
            <NavBar />
            <Switch>
              <Route exact path="/home" component={Home} />
              <Route exact path="/about" component={About} />
              <Route exact path="/contact" component={Contact} />
              <Route exact path="/pricing" component={Pricing} />
              {/* <Route exact path="/login" component={Login} />
              <Route exact path="/signup" component={SignUp} /> */}
              <SIgnInOut/>
            </Switch>
          </Router>
      <Grid  container spacin={4} className={classes.gridContainer} >
        <Grid item>
          
        </Grid>
        <Grid item container spacin={4} className={classes.gridContainer}>
          <Grid item xs={12} sm={6} md={4}/>
          <Grid item xs={12} sm={6} md={4}>
            {/* <Content/> */}
         
          </Grid>
          <Grid item xs={12} sm={6} md={4}/>
          
        </Grid>
      </Grid>
    </div>
  );
}
