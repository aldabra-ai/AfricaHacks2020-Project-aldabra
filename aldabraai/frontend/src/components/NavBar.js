import React from "react";
import { Link } from "react-router-dom";
import AppBar from "@material-ui/core/AppBar";
import {
  Toolbar,
  Typography,
  makeStyles,
  fade,
  InputBase,
  Button,
} from "@material-ui/core";
import SearchIcon from "@material-ui/icons/Search";
import purple from "@material-ui/core/colors/purple";
import blue from "@material-ui/core/colors/blue";

const useStyles = makeStyles((theme) => ({
  palette: {
    primary: '#FFFFFF',
    
  },
  grow: {
    flexGrow: 1,
    flex:1
  },
  title: {
    backgroundColor: "#3700B3",
    // , color: '#FFDCE8'
  },
  header: {
    backgroundColor: "#3700B3",
    color: "#FFDCE8",
    boxShadow: "0px 0px 0px 0px",

  },
  header1: {
    backgroundColor: "#E59BBC",
    color: "10px 10px 10px rgba(216,191,216)",
    boxShadow:"0px 0px 0px 0px",
    padding: 0,
    
  },
  search: {
    position: "relative",
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    "&:hover": {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    marginRight: theme.spacing(2),
    marginLeft: 0,
    width: "100%",
    [theme.breakpoints.up("sm")]: {
      marginLeft: theme.spacing(3),
      width: "auto",
    },
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: "100%",
    position: "absolute",
    pointerEvents: "none",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  inputRoot: {
    color: "inherit",
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create("width"),
    width: "100%",
    [theme.breakpoints.up("sm")]: {
      width: "20ch",
    },
    root: {
      maxWidth: 345,
      display: "inline-block",
      margin: "0 2px",
      transform: "scale(0.0)",
    },
    media: {
      height: 140,
    },
    title: {
      fontSize: 14,
    },
    pos: {
      marginButtom: 12,
    },
  },
}));

export default function NavBar() {
  const classes = useStyles();

  return (
    <div>
      <AppBar position="sticky" className={classes.header}>
        <Toolbar>
          <Typography variant="h4" color="priamry" className={classes.palette}>
            aldabra.ai
          </Typography>

          
          <Button component={Link} to="/home" color="inherit">
            Home
          </Button>
          <Button component={Link} to="/about" color="inherit">
            About
          </Button>
          <Button component={Link} to="/pricing" color="inherit">
            Pricing
          </Button>
          <Button component={Link} to="/contact" color="inherit">
            Contact
          </Button>
          <Button component={Link} to="/login" color="inherit">
            Login
          </Button>
          <Button component={Link} to="/signup" color="inherit">
            Sign Up
          </Button>
          {/* <Button color='inherit'></Button> */}
        </Toolbar>
        <AppBar position='sticky' className={classes.header1}>
          <Toolbar align ='center' >
          <div className={classes.search}>
            <div className={classes.searchIcon}>
              <SearchIcon />
            </div>
            <InputBase
              placeholder="Doctor...."
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
              inputProps={{ "aria-label": "search" }}
            />
          </div>
          <div className={classes.search}>
            <div className={classes.searchIcon}>
              <SearchIcon />
            </div>
            <InputBase
              placeholder="Location...."
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
              inputProps={{ "aria-label": "search" }}
            />
          </div>
          </Toolbar>
        </AppBar>
      </AppBar>
      
      {/* <Card/> */}
      {/* {renderMobileMenu}
      {renderMenu} */}
    </div>
  );
}
