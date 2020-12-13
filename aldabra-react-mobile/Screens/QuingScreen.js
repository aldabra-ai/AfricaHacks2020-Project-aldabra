import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Ionicons } from '@expo/vector-icons';
import { Alert, Image, Modal, Picker, SafeAreaView, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

export default class QuingScreen extends React.Component{
    constructor(props){
        super(props);
        this.state={
            modalState: false,
            choosenIndex: 0,
            switchValue: false  
        }
    }

    handleModal () {
        this.setState({
            modalState: !this.state.modalState ? true: false
        })
    }

    render(){
        return(
            <SafeAreaView style = {styles.container}>
                <Modal
                  visible={this.state.modalState}    
                >
                    <View style={styles.headerScreen}>
                        <Image style={styles.logoContainer} source={require("../assets/AldabraLogo.jpg")}/>
                        <Text style={[styles.text,{color: '#fff',marginBottom: '10%', fontSize: 20, marginLeft: '10%'}]}>Welcome to online Quing</Text>
                    </View>
                    <View style={styles.footerScreen}>
                    <View style={styles.slot}>
                        <Text style={[styles.text,{color: 'green', marginTop: 5}]}>Queue is open : 16 total people</Text>
                        <Text style={styles.normText}>We are closing earlier today at 17 : 00</Text>
                    </View>
                    <View style={styles.slot}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-calendar" color="black" size={25} /> 
                            <Text style={[styles.text, {marginLeft: '5%', fontSize: 15}]}>December 13, 2020</Text>
                        </View>
                        <Text style={styles.normText}>Today's Date</Text>
                    </View>
                    <View style={styles.slot}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-people" color="black" size={25} /> 
                            <Text style={[styles.text, {marginLeft: '5%', fontSize: 15}]}>6 people</Text>
                        </View>
                        <Text style={styles.normText}>People infront of you</Text>
                    </View>
                    <View style={styles.slot}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-people" color="grey" size={25} /> 
                            <Text style={[styles.text, {marginLeft: '5%', fontSize: 15, color: 'grey'}]}>9 people (behind you)</Text>
                        </View>
                        <Text style={[styles.normText,{color: 'grey'}]}>People behind you</Text>
                    </View>
                    <View style={styles.slot}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-time" color="black" size={25} /> 
                            <Text style={[styles.text, {marginLeft: '5%', fontSize: 15}]}>37 minutes</Text>
                        </View>
                        <Text style={styles.normText}>Estimated waiting time</Text>
                    </View>
                    <View style={[styles.slot,{marginBottom:'5%'}]}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-alert" color="black" size={25} /> 
                            <Text style={[styles.text, {marginLeft: '5%', fontSize: 15}]}>Your urgent level</Text>
                        </View>
                        <Text style={[styles.normText,{color: 'green'}]}>Regular check-up</Text>
                    </View>
                        <TouchableOpacity style={[styles.button,{marginTop: 1, backgroundColor: 'red'}]} onPress={() => {this.handleModal()}}>
                            <Text style={[styles.text,{color: '#fff', fontSize: 20}]}>Exit Queue</Text>
                        </TouchableOpacity>
                    </View>
                </Modal>
                <View style={styles.headerScreen}>
                    <Image style={styles.logoContainer} source={require("../assets/AldabraLogo.jpg")}/>
                    <Text style={[styles.text,{color: '#fff',marginBottom: '10%', fontSize: 20, marginLeft: '10%'}]}>Let's Queue for you</Text>
                </View>

                <View style={styles.footerScreen}>
                    <View style={styles.slot}>
                        <Text style={[styles.text,{color: 'green', marginTop: 5}]}>Queue is Open</Text>
                        <Text style={styles.normText}>We are closing earlier today at 17 : 00</Text>
                    </View>
                    <View style={styles.slot}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-calendar" color="black" size={25} /> 
                            <Text style={[styles.text, {marginLeft: '5%', fontSize: 17}]}>December 13, 2020</Text>
                        </View>
                        <Text style={styles.normText}>Today's Date</Text>
                    </View>
                    <View style={styles.slot}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-people" color="black" size={25} /> 
                            <Text style={[styles.text, {marginLeft: '5%', fontSize: 17}]}>6 people</Text>
                        </View>
                        <Text style={styles.normText}>Queue length</Text>
                    </View>
                    <View style={styles.slot}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-time" color="black" size={25} /> 
                            <Text style={[styles.text, {marginLeft: '5%', fontSize: 17}]}>22 minutes</Text>
                        </View>
                        <Text style={styles.normText}>Estimated waiting time</Text>
                    </View>
                    <Text style={[styles.text,{marginLeft: '5%', marginBottom: 2,marginTop: 3}]}>Why are you coming? (optional)</Text>
                    <TextInput placeholder="  Symptoms" style={styles.inputContiner}/>
                    <Text style={[styles.text,{marginLeft: '5%', marginBottom: 2,color: 'red'}]}>Urgent level (compulsory)</Text>
                    <View style={[styles.inputContiner,{backgroundColor: '#e6e6e6'}]}>
                    <Picker  
                        selectedValue={this.state.language}  
                        onValueChange={(itemValue, itemPosition) =>  
                            this.setState({language: itemValue, choosenIndex: itemPosition})}  
                    >  
                    <Picker.Item label="Regular check-up" value="java" />  
                    <Picker.Item label="Serious sickness" value="js" />  
                    <Picker.Item label="Critical condition" value="rn" />  
                    </Picker> 
                    </View>
                    <TouchableOpacity style={[styles.button,{marginTop: 1}]} onPress={() => {this.handleModal()}}>
                        <Text style={[styles.text,{color: '#fff', fontSize: 20}]}>Join Queue</Text>
                    </TouchableOpacity>
                </View>
            </SafeAreaView>
        )
    }
}

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
        //alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#3B26CD'
    },
    footerScreen:{
        flex: 3,
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
        marginTop: '5%',
        marginBottom: 10,
        borderRadius: 20,
    },
    slot:{
        height: '13%',
        marginLeft: '5%',
        borderBottomWidth: 1,
        width: '90%',
        borderBottomColor: '#dddddd'
    },
    text:{
        fontSize: 15,
        fontWeight: 'bold'
    },
    normText:{
        color: '#3B26CD',
        marginTop: '3%',
        fontSize: 13
    }
})