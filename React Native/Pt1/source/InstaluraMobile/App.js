/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React from 'react';
import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  View,
  Text,
  StatusBar,
  Image,
  Dimensions
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
    , { id: 2, usuario: 'papagaio' }];

  return (
    <ScrollView>
      {fotos.map(foto =>
        <View key={foto.id}>
          <Text>{foto.usuario}</Text>
          <Image source={require('./resources/img/arara.jpg')}
            style={{ width: width, height: width }} />
        </View>
      )}
    </ScrollView>
  );
};

export default App;
