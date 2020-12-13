import 'react-native-gesture-handler';
import { createAppContainer, createSwitchNavigator } from "react-navigation";
import { createMaterialBottomTabNavigator } from "react-navigation-material-bottom-tabs";
import 'react-native-paper';
import { Ionicons } from '@expo/vector-icons';
import LoginScreen from './LoginScreen';
import SignInScreen from './SignInScreen';
import WelcomeScreen from './WelcomeScreen';
//import MentalHealthScreen from './Screens/MentalHealthScreen';
//import HomeScreen from './Screens/HomeScreen';
//const { createMaterialBottomTabNavigator } = require("react-navigation-material-bottom-tabs");
const { default: HomeScreen } = require("./HomeScreen");
const { default: MentalHealthScreen } = require("./MentalHealthScreen");
const { default: QuingScreen } = require("./QuingScreen");
//const { default: LoginScreen } = require("./LoginScreen");
//const { default: LoginScreen } = require("./LoginScreen");

const bottomNavigator = createMaterialBottomTabNavigator({
    Health: { screen: HomeScreen,
          navigationOptions: {
              tabBarLabel: 'Health',
              //tabBarIcon: ({tintColor})=>(
                //<Ionicons name="md-home" color={tintColor} size={30} />
              //)
            }
    },
    Queue: { screen: QuingScreen,
      //navigationOptions: {
        //tabBarIcon: ({tintColor})=>(
          //<Ionicons name="md-search" color={tintColor} size={28} />
        //)
      //}
     },
     Coping: { screen: MentalHealthScreen
     }
  },
   {
    initialRouteName: 'Health',
    activeColor: 'red',
    //activeColor: '#f0edf6',
    inactiveColor: '#3e2465',
    barStyle: { backgroundColor: '#fff' },//backgroundColor: '#694fad' },
  });

  const switchScreens = createSwitchNavigator({
    Welcome: WelcomeScreen,
    SignIn: SignInScreen,
    Home: bottomNavigator
});

  export default createAppContainer(switchScreens);