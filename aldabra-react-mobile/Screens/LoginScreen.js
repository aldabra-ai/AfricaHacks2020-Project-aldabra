import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Alert, Image, SafeAreaView, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

const LoginScreen = ({navigation}) => {
    return(
        <View style={styles.container}>
           <Image style={styles.logoContainer} source={require("../assets/AldabraLogo.jpg")}/>
           <View style={styles.footerScreen}>
               <Text style={[styles.text,{marginLeft: '15%', marginTop: '15%'}]}>Welcome to aldabra.ai</Text>
               <TouchableOpacity style={styles.button}>
                   <Text style={[styles.text,{color: '#fff'}]}>Start</Text>
               </TouchableOpacity>
           </View>
        </View>
    )
}
export default LoginScreen;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        backgroundColor: '#3B26CD',
        alignItems: 'center',
        justifyContent: 'center', 
    },
    logoContainer:{
        marginTop: '10%',
        marginBottom: '10%',
        height: '50%',
        borderRadius: 180,
        width: '80%'
    },
    text: {
        color: 'black',
        fontSize: 25,
        fontWeight: 'bold',
        alignItems: 'center',
        justifyContent: 'center', 
    },
    button:{
        width: '60%',
        marginLeft: '20%',
        alignContent: 'center',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#3B26CD',
        height: '20%',
        marginTop: '5%',
        marginBottom: 10,
        borderRadius: 30,
    },
    footerScreen:{
        height: '40%',
        width: '100%',
        backgroundColor: '#3B26CD',
        backgroundColor: '#fff',
        borderTopLeftRadius: 25,
        borderTopRightRadius: 25
    }
})