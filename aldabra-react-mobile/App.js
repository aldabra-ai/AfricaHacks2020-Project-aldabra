import 'react-native-gesture-handler';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import BookingScreen from './Screens/BookingScreen';
import HomeScreen from './Screens/HomeScreen';
import { enableScreens } from 'react-native-screens';
enableScreens();
import LoginScreen from './Screens/LoginScreen';
import MentalHealthScreen from './Screens/MentalHealthScreen';
//import MainScreen from './Screens/MainScreen';
import QuingScreen from './Screens/QuingScreen';
import SignInScreen from './Screens/SignInScreen';
import MainScreen from './Screens/MainScreen';
import WelcomeScreen from './Screens/WelcomeScreen';

export default function App() {
  return (
    //<WelcomeScreen/>
    <MainScreen/>
    //<MentalHealthScreen/>
    //<MainScreen/>
    //<RunScr/>
    //HomeScreen/>
    //<SignInScreen/>
    //<QuingScreen/>
    //<BookingScreen/>
    //<LoginScreen/>
    //<View style={styles.container}>
      //<Text>Open up App.js to start working on your app!</Text>
      //<StatusBar style="auto" />
    //</View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
