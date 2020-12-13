import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Alert, FlatList, Image, SafeAreaView, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

let doc = require('./Doctors.json')

export default class HomeScreen extends React.Component{
    constructor(props){
        super(props);
        this.state={
            allUsers: doc,
            temp: doc,
        }
    }

    SearchBySpeciality (Skill) {

        const usersFiltered = this.state.temp.filter(item => {
            
            let getSkill = (item.noOfBids).toLowerCase()
            let skillInLowerCase = Skill.toLowerCase()
 
            return getSkill.indexOf(skillInLowerCase) > -1
        });
 
        this.setState({allUsers: usersFiltered})
     }

    render(){
        return(
            <SafeAreaView style={styles.container}>
                    <TextInput placeholder="   Search for a Doctor" style={styles.inputContiner}
                    onChangeText={text => this.SearchBySpeciality(text)}/>
                <View style={styles.headerScreen}>
                <Text style={[styles.title,{marginLeft: '5%'}]}>Doctors</Text>
                    <FlatList
                       data={this.state.allUsers}
                       renderItem={({ item}) => (
                           <TouchableOpacity>
                               <View style={styles.wrapUser}>
                                    <Image style={styles.ProfilePic} source={{ uri: item.image}}/>
                                    <View style={styles.infoBoxWrapper} key={item.key}>
                                        <Text style={styles.text}>Dr {item.name}</Text>
                                        <Text style={styles.text}>{item.noOfBids}</Text>
                                        
                                        <Text style={styles.text}>{item.place}</Text>
                                    </View>
                               </View>
                           </TouchableOpacity>
                       )}
                    />
                </View>
                <View style={styles.footerScreen}>
                    <Text style={[styles.title,{marginLeft: '5%'}]}>Health Curve</Text>
                    <Image style={styles.Pic} source={{uri: "data:image/png;base64,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"}}/>
                </View>
            </SafeAreaView>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#e6e6e6'
        //backgroundColor: '#3B26CD'
    },
    ProfilePic:{
        marginTop: 3,
        height: 80,
        borderRadius: 180,
        marginLeft: '5%',
        width: '25%'
    },
    Pic:{
        marginTop: 3,
        height: '85%',
        //borderRadius: 180,
        marginLeft: '5%',
        width: '90%'
    },
    headerScreen:{
        flex: 3,
        backgroundColor: '#fff',
        borderRadius: 20,
        width: '94%',
        marginBottom: '5%',
        marginLeft: '3%',
        //alignContent: 'center',
        //justifyContent: 'center',
        //backgroundColor: '#3B26CD'
    },
    footerScreen:{
        flex: 3,
        backgroundColor: '#fff',
        borderRadius: 20,
        width: '94%',
        marginLeft: '3%',
        marginBottom: '5%'
        //borderTopLeftRadius: 20,
        //borderTopRightRadius: 20
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
        height: 94,
        width: '90%',
        borderBottomColor: '#777',
        marginLeft: '5%'
    },
    title:{
        //marginTop: '3%',
        fontWeight: 'bold',
        fontSize: 15
    }
})