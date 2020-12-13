import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Ionicons } from '@expo/vector-icons';
import { Alert, FlatList, Image, SafeAreaView, StyleSheet, 
    Text, TextInput, TouchableOpacity, View } from 'react-native';

export default class MentalHealthScreen extends React.Component{

    constructor(props){
        super(props);
        this.state={
            
        }
    }

    render(){
        return(
            <View style={styles.container}>
                <View style={styles.headerScreen}>
                    <Image style={styles.logoContainer} source={require("../assets/AldabraLogo.jpg")}/>
                    <Text style={[styles.title,{color: '#fff',marginBottom: '10%', fontSize: 25, marginLeft: '10%'}]}>Coping</Text>
                    
                </View>
            <View style={styles.footerScreen}>
                <Text style={[styles.title,{marginLeft: '5%', marginTop:"5%"}]}>Mental health problems are common here are some tips to reduce stress</Text>
                <Text style={styles.underLine}></Text>
                <TouchableOpacity>
                    <View style={[styles.wrapUser,{flexDirection: 'column'}]}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-pause" color="purple" size={20} />
                            <Text style={[styles.title,{marginLeft:'5%', marginTop:'1%'}]}>Pause Breate Reflect</Text>
                        </View> 
                        <Text style={{marginLeft:'10%', marginBottom:'2%'}}>Take some slow breathe. Slow breathing is one of the best ways to lower stress, because it signals to your brain to relax your body.</Text>
                    </View> 
                </TouchableOpacity>
                <TouchableOpacity>
                    <View style={[styles.wrapUser,{flexDirection: 'column'}]}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-people" color="purple" size={20} />
                            <Text style={[styles.title,{marginLeft:'5%', marginTop:'1%'}]}>Connect with others</Text>
                        </View> 
                        <Text style={{marginLeft:'10%', marginBottom:'2%'}}>Talking to people you trust can help. Keep in contact with people close to you, tell them how you are feeling and share concers</Text>
                    </View> 
                   
                </TouchableOpacity>
                <TouchableOpacity>
                    <View style={[styles.wrapUser,{flexDirection: 'column'}]}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-time" color="purple" size={20} />
                            <Text style={[styles.title,{marginLeft:'5%', marginTop:'1%'}]}>Keep to a health routine</Text>
                        </View> 
                        <Text style={{marginLeft:'10%', marginBottom:'2%'}}>Exercise regulary. Make time for doing things you enjoy. Take regular breaks from on-screen activities</Text>
                    </View> 
                    
                </TouchableOpacity>
                <TouchableOpacity>
                    <View style={[styles.wrapUser,{flexDirection: 'column'}]}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-heart" color="purple" size={20} />
                            <Text style={[styles.title,{marginLeft:'5%', marginTop:'1%'}]}>Reach out for help</Text>
                        </View> 
                        <Text style={{marginLeft:'10%', marginBottom:'2%'}}>Don't expect too much of yourself on difficult days. Accept some days you may be more productive than others</Text>
                    </View>  
                </TouchableOpacity>
                <TouchableOpacity>
                    <View style={[styles.wrapUser,{flexDirection: 'column'}]}>
                        <View style={{flexDirection: 'row'}}>
                            <Ionicons name="md-call" color="purple" size={20} />
                            <Text style={[styles.title,{marginLeft:'5%', marginTop:'1%'}]}>Reach out for help</Text>
                        </View> 
                        <Text style={{marginLeft:'10%', marginBottom:'2%'}}>Don't hesitate to seek professional help if you think you need it. A good place to start is your local health worker.</Text>
                    </View>
                </TouchableOpacity>
                <Text style={[styles.title,{marginTop: '1%',marginLeft: '5%', color: 'red'}]}>NB : For informational purposes only</Text>
                <Text style={[styles.title,{marginLeft: '5%', color: 'green'}]}>Contact your local medical authority for advice</Text>
            </View>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        //backgroundColor: '#e6e6e6'
        backgroundColor: '#3B26CD'
    },
    underLine:{
        borderBottomWidth: 1,
        //marginTop: 1,
        marginLeft: '5%',
        width:'90%'
    },
    ProfilePic:{
        marginTop: 3,
        height: 80,
        borderRadius: 180,
        marginLeft: '5%',
        width: '25%'
    },
    headerScreen:{
        flex: 1,
        alignContent: 'center',
        justifyContent: 'center',
        backgroundColor: '#3B26CD'
    },
    footerScreen:{
        flex: 3,
        backgroundColor: '#fff',
        //borderRadius: 20,
        width: '100%',
        //marginLeft: '3%',
        //marginBottom: '5%'
        borderTopLeftRadius: 20,
        borderTopRightRadius: 20
    },
    infoBoxWrapper: {
        marginLeft: '5%',
        marginTop: '2%',
        marginBottom: '3%'
    },
    inputContiner: {
        width: '90%',
        height: '5%',
        marginLeft: '5%',
        borderRadius: 15,
        borderWidth: 1,
        marginTop: '10%',
        backgroundColor: '#fff',
        borderColor: '#dddddd',
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
        fontSize: 13,
        //fontWeight: 'bold'
    },
    wrapUser:{
        flexDirection: 'row', 
        borderBottomWidth: 1, 
        height: 76,
        width: '90%',
        borderBottomColor: '#777',
        marginLeft: '5%'
    },
    title:{
        //marginTop: '3%',
        fontWeight: 'bold',
        fontSize: 15
    },
    logoContainer:{
        marginTop: '15%',
        height: '50%',
        borderRadius: 180,
        marginLeft: '10%',
        width: '80%'
    },
})