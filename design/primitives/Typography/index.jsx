import React from "react";
import { StyleSheet, Text } from "react-native";
import {
    widthPercentageToDP as wp,
    heightPercentageToDP as hp,
} from "react-native-responsive-screen";
import AppLoading from 'expo-app-loading';
import {
    useFonts,
    OpenSans_300Light,
    OpenSans_400Regular,
    OpenSans_600SemiBold,
    OpenSans_700Bold,
    OpenSans_800ExtraBold,
} from '@expo-google-fonts/open-sans';

export default function Typography({ textSize, textColor, textWeight, children }) {

    let [fontsLoaded] = useFonts({
        OpenSans_300Light,
        OpenSans_400Regular,
        OpenSans_600SemiBold,
        OpenSans_700Bold,
        OpenSans_800ExtraBold,
    });

    const themeTextSize =
        textSize === "h1"
            ? styles.h1
            : textSize === "h2"
                ? styles.h2
                : textSize === "h3"
                    ? styles.h3
                    : textSize === "h4"
                        ? styles.h4
                        : textSize === "h5"
                            ? styles.h5
                            : styles.p;
    const themeTextColor =
        textColor === "black1"
            ? styles.black1
            : textColor === "grey1"
                ? styles.grey1
                : textColor === "white1"
                    ? styles.white1
                    : textColor === "blue1"
                        ? styles.blue1
                        : textColor === "green1"
                            ? styles.green1
                            : styles.black1;

    const themeTextWeight =
        textWeight === "800"
            ? "OpenSans_800ExtraBold"
            : textWeight === "700"
                ? "OpenSans_700Bold"
                : textWeight === "600"
                    ? "OpenSans_600SemiBold"
                    : textWeight === "400"
                        ? "OpenSans_400Regular"
                        : "OpenSans_300Light";

    if (!fontsLoaded) {
        return <AppLoading />;
    } else
        return <Text style={[themeTextColor, themeTextSize, { letterSpacing: 0.5, fontFamily: themeTextWeight, paddingVertical: '1%' }]}>{children}</Text>;
}

const styles = StyleSheet.create({
    //size
    h1: {
        fontSize: hp('2.8%'),
    },
    h2: {
        fontSize: hp('2.5%'),
    },
    h3: {
        fontSize: hp("2%"),
    },
    h4: {
        fontSize: hp("1.8%"),
    },
    h5: {
        fontSize: hp("1.6%"),
    },
    p: {
        fontSize: hp("1.4%"),
    },
    //color
    black1: {
        color: "#262626",
    },
    white1: {
        color: "#ffffff",
    },
    grey1: {
        color: "#808080",
    },
    blue1: {
        color: "#0076FE"
    },
    green1: {
        color: '#00C88C',
    },
});