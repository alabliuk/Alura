/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, { Component } from 'react';
import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  View,
  Text,
  StatusBar,
  Image,
  Dimensions,
  ListView,
  FlatList
} from 'react-native';

import Post from './src/components/Post'

// Capturando o tamanho da tela do dispositivo
const width = Dimensions.get('screen').width;

class InstaluraMobile extends Component {
  // const fotos = [{ id: 1, usuario: 'arara' }
  //   , { id: 2, usuario: 'papagaio' }
  //   , { id: 3, usuario: 'tucano' }];

  constructor() {
    super();
    this.state = {
      fotos: []
    }
  }

  componentDidMount() {
    fetch('https://instalura-api.herokuapp.com/api/public/fotos/rafael')
      .then(resposta => resposta.json())
      .then(json => this.setState({ fotos: json }))
  }

  render() {
    return (
      <FlatList
        data={this.state.fotos}
        keyExtractor={item => String(item.id)}
        renderItem={({ item }) =>
          <Post foto={item} />
        }
      />
    );
  };
}

export default InstaluraMobile;