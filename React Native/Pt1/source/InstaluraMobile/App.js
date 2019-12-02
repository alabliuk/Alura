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

import {
  Header,
  LearnMoreLinks,
  Colors,
  DebugInstructions,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';

// Capturando o tamanho da tela do dispositivo
const width = Dimensions.get('screen').width;

const App: () => React$Node = () => {
  const fotos = [{ id: 1, usuario: 'arara' }
    , { id: 2, usuario: 'papagaio' }
    , { id: 3, usuario: 'tucano' }];

  return (
    <FlatList
      data={fotos}
      keyExtractor={item => String(item.id)}
      renderItem={({ item }) =>
        <View>
          <View style={styles.cabecalho}>
            <Image source={require('./resources/img/arara.jpg')}
              style={styles.fotoDePerfil} />
            <Text>{item.usuario}</Text>
          </View>

          <Image source={require('./resources/img/arara.jpg')}
            style={styles.foto} />
        </View>
      }
    />
  );
};

const styles = StyleSheet.create({
  cabecalho: {
    margin: 10, flexDirection: 'row', alignItems: 'center'
  },
  fotoDePerfil: {
    marginRight: 10, borderRadius: 20, width: 40, height: 40
  },
  foto: {
    width: width, height: width
  }
});

export default App;
