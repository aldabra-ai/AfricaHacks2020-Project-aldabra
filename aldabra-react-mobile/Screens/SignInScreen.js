import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Alert, Image, SafeAreaView, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

const SignInScreen = ({navigation}) => {
        return(
            <SafeAreaView style={styles.container}>
                <View style={styles.headerScreen}>
                    <Image style={styles.logoContainer} source={require("../assets/AldabraLogo.jpg")}/>
                    <Text style={[styles.text,{color: '#fff',marginBottom: '10%', fontSize: 25, marginLeft: '10%'}]}>Sign In</Text>
                </View>

                <View style={styles.footerScreen}>
                    <Text style={[styles.text,{marginLeft: '5%', marginBottom: 2,marginTop: '8%'}]}>Email address</Text>
                    <TextInput placeholder="  email address or username" style={styles.inputContiner}/>
                    <Text style={[styles.text,{marginLeft: '5%', marginBottom: 2,marginTop: 3}]}>Password</Text>
                    <TextInput secureTextEntry={true} placeholder="  Enter Password" style={[styles.inputContiner,{marginBottom:'5%'}]}/>
                    <Text style={[styles.normText,{marginLeft: '15%', marginBottom: '5%', color: 'green'}]}>Forgot your Password? Recover here</Text>
                    <TouchableOpacity style={[styles.button,{marginTop: 1}]} onPress={()=>navigation.navigate('Home')}>
                        <Text style={[styles.text,{color: '#fff', fontSize: 20}]}>Sign In</Text>
                    </TouchableOpacity>
                    <Text style={[styles.text,{marginLeft: '48%', marginBottom: 2,marginTop: 3}]}>Or</Text>
                    <TouchableOpacity style={[styles.button,{borderWidth: 1, backgroundColor: '#fff'}]}>
                        <Text style={[styles.text,{color: '#3B26CD', fontSize: 20}]}>Sign Up</Text>
                    </TouchableOpacity>
                </View>

            </SafeAreaView>
        )
    }

    export default SignInScreen;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#3B26CD'
    },
    logoContainer:{
        marginTop: '15%',
        height: '50%',
        borderRadius: 180,
        marginLeft: '10%',
        width: '80%'
    },
    headerScreen:{
        flex: 1,
        alignContent: 'center',
        justifyContent: 'center',
        backgroundColor: '#3B26CD'
    },
    footerScreen:{
        flex: 2,
        backgroundColor: '#fff',
        borderTopLeftRadius: 20,
        borderTopRightRadius: 20
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
        width: '60%',
        marginLeft: '20%',
        alignContent: 'center',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#3B26CD',
        height: '10%',
        //marginTop: '5%',
        //marginBottom: 10,
        borderRadius: 20,
    },
    slot:{
        height: '13%',
        marginLeft: '5%',
        borderBottomWidth: 1,
        borderBottomColor: '#dddddd'
    },
    text:{
        fontSize: 15,
        fontWeight: 'bold'
    },
    normText:{
        //marginTop: '3%',
        fontSize: 15
    }
})