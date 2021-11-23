import { StatusBar } from "expo-status-bar";
import React, { useState } from "react";
import { Button, StyleSheet, Text, View, Modal } from "react-native";
import Typography from "../primitives/Typography";

export default function App() {
  return (
    <View style={styles.container}>
      <Typography textSize="h1" textColor="black1" textWeight="400">Welcome to Sahaay, by IEEE Computer Society, VIT Chennai!</Typography>
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

