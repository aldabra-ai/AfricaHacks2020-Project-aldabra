import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from '../store';


import HorizontalNav2 from '../components/horizontal-navs/HorizontalNav2';

export default function Index() {
  return (
    <Provider store={store}>
    <React.Fragment>
      <HorizontalNav2
        content={{
          brand: {
            text: 'aldabra.ai',
            image: 'nereus-assets/img/nereus-light.png',
            width: '110',
          },
          link1: 'About',
          link2: 'Princing',
          link3: 'Team',
          'primary-action': 'Login',
        }}
      />
    </React.Fragment>
    </Provider>
  );
}

