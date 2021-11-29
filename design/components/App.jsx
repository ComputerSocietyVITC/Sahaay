import { StatusBar } from "expo-status-bar";
import React, { useState } from "react";
import { Button, StyleSheet, Text, View, Modal } from "react-native";

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Welcome to Sahaay, by IEEE Computer Society, VIT Chennai!</Text>
      <StatusBar style="auto" />

      <Button title="click me" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
