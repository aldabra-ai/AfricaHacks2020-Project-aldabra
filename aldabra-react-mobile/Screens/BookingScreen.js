import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Alert, SafeAreaView, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';


export default class BookingScreen extends React.Component{
    constructor(){
        super();

    }

    handleAppointment(){
        alert("you will be sent a remainder a week before your appointment")
    }

    render(){
        return(
            <SafeAreaView style={styles.container}>
                <Text style={[styles.text,{marginTop: '30%', fontSize: 20, marginBottom: '10%'}]}>Book your Doctor's appointment</Text>
                <View style={styles.innerScreen}>
                <Text style={[styles.text,{marginTop: 15}]}>Please fill in the form</Text>
                <TextInput style={styles.inputContiner} placeholder="   Date"/>
                <TextInput style={styles.inputContiner} placeholder="   Time"/>
                <TextInput style={styles.inputContiner} placeholder="   Phone Number"/>
                <TextInput style={styles.inputContiner} placeholder="   Emergency contact"/>

                <TouchableOpacity style={styles.button} onPress={()=>Alert.alert("You've been booked!","you will be sent a remainder a week before your appointment",
                [{text: "Cancel"},{text: "Accept"}])}>
                    <Text style={[styles.text,{color: '#fff'}]}>Book</Text>
                </TouchableOpacity>
                
                </View>

                
            </SafeAreaView>
        )
    }

}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#8C30F5', 
    },
    innerScreen: {
        flex: 1,
        backgroundColor: '#fff',
        borderTopLeftRadius: 25,
        borderTopRightRadius: 25
    },
    inputContiner: {
        width: '90%',
        height: '10%',
        marginLeft: '5%',
        borderRadius: 10,
        borderWidth: 1,
        borderColor: 'purple',
        marginBottom: 5,
    },
    button:{
        width: '50%',
        marginLeft: '23%',
        alignContent: 'center',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'purple',
        height: '10%',
        marginTop: 5,
        marginBottom: 10,
        borderRadius: 10,
    },
    text: {
        fontSize: 20,
        fontWeight: 'bold',
        marginLeft: '5%',
        marginBottom: 10,
    }
  });