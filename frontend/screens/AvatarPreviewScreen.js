import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default function AvatarPreviewScreen({ route }) {
  const { outfit } = route.params;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Your Outfit</Text>
      <Text>Shirt: {outfit.shirt?.name ?? "None selected"}</Text>
      <Text>Pants: {outfit.pants?.name ?? "None selected"}</Text>
      <Text>Shoes: {outfit.shoes?.name ?? "None selected"}</Text>
      <Text style={styles.note}>3D avatar rendering coming next</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: "center", alignItems: "center", padding: 24 },
  title: { fontSize: 22, fontWeight: "700", marginBottom: 16 },
  note: { marginTop: 24, color: "#999" },
});