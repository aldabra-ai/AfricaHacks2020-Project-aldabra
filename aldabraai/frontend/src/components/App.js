import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

// import layout components
import NavBar from './layout/Nav'
import Footer from './layout/Footer'

class App extends Component {
    render() {
        return(
            <Fragment>
              <NavBar />
              <h1> React + Django Integration Test </h1>
              <Footer />
            </Fragment>
        ); 
    }
}

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
  );

export default App;