import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

export default function AvatarSetupScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Set Up Your Avatar</Text>
      <Text style={styles.subtitle}>
        We'll use this to show you how clothes actually look on you.
      </Text>

      {/* Placeholder for future photo/3D avatar UI */}
      <View style={styles.placeholderBox}>
        <Text style={styles.placeholderText}>Avatar preview coming soon</Text>
      </View>

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Measurements")}
      >
        <Text style={styles.buttonText}>Continue</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 24,
    backgroundColor: "#fff",
  },
  title: {
    fontSize: 24,
    fontWeight: "700",
    marginBottom: 8,
    textAlign: "center",
  },
  subtitle: {
    fontSize: 14,
    color: "#666",
    textAlign: "center",
    marginBottom: 32,
  },
  placeholderBox: {
    width: 220,
    height: 320,
    borderWidth: 2,
    borderColor: "#ddd",
    borderStyle: "dashed",
    borderRadius: 12,
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 40,
  },
  placeholderText: {
    color: "#aaa",
  },
  button: {
    backgroundColor: "#111",
    paddingVertical: 14,
    paddingHorizontal: 48,
    borderRadius: 8,
  },
  buttonText: {
    color: "#fff",
    fontWeight: "600",
    fontSize: 16,
  },
});