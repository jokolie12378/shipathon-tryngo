import React from "react";
import { View, Text, StyleSheet } from "react-native";
import AvatarViewer from "../components/AvatarViewer";

export default function AvatarPreviewScreen({ route }) {
  const { outfit } = route.params;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Your Outfit</Text>

      <AvatarViewer modelKey="avatar" />

      <View style={styles.summary}>
        <Text>Shirt: {outfit.shirt?.name ?? "None selected"}</Text>
        <Text>Pants: {outfit.pants?.name ?? "None selected"}</Text>
        <Text>Shoes: {outfit.shoes?.name ?? "None selected"}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: "center", paddingTop: 20 },
  title: { fontSize: 22, fontWeight: "700", marginBottom: 12 },
  summary: { marginTop: 16, alignItems: "center" },
});