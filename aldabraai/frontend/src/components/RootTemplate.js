import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from '../store';

// import layout components
import NavBar from './layout/Nav'
import Footer from './layout/Footer'

class RootTemplate extends Component {
    render() {
        return(
            <Provider store={store}>
                <Fragment>
                    <NavBar />
                    
                    <Footer />
                </Fragment>
            </Provider>
        ); 
    }
}

ReactDOM.render(
    <React.StrictMode>
        <RootTemplate />
    </React.StrictMode>,
    document.getElementById('root')
  );

export default RootTemplate;