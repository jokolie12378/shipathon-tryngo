import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

export default function MeasurementsScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Measurements</Text>
      <Text style={styles.subtitle}>Coming next</Text>

      <TouchableOpacity
        style={styles.button}
        onPress={() =>
          navigation.navigate("AvatarPreview", {
            outfit: { shirt: null, pants: null, shoes: null },
          })
        }
      >
        <Text style={styles.buttonText}>Skip to Preview (test)</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  title: {
    fontSize: 24,
    fontWeight: "700",
  },
  subtitle: {
    color: "#666",
    marginTop: 8,
    marginBottom: 24,
  },
  button: {
    backgroundColor: "#111",
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 8,
  },
  buttonText: {
    color: "#fff",
    fontWeight: "600",
  },
});