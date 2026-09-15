import React from "react";
import { View, Text, Image, FlatList, StyleSheet } from "react-native";

const mockItems = [
  {
    id: "1",
    name: "Classic Hoodie",
    brand: "Aritzia",
    category: "hoodie",
    price: 68.0,
    image_url: "https://placehold.co/300x400?text=Hoodie",
    fit_type: "oversized",
  },
  {
    id: "2",
    name: "Slim Fit Tee",
    brand: "Uniqlo",
    category: "tee",
    price: 19.99,
    image_url: "https://placehold.co/300x400?text=Tee",
    fit_type: "slim",
  },
  {
    id: "3",
    name: "Straight Leg Jeans",
    brand: "Levi's",
    category: "jeans",
    price: 89.5,
    image_url: "https://placehold.co/300x400?text=Jeans",
    fit_type: "regular",
  },
  {
    id: "4",
    name: "High Top Sneakers",
    brand: "Nike",
    category: "sneakers",
    price: 110.0,
    image_url: "https://placehold.co/300x400?text=Sneakers",
    fit_type: "regular",
  },
];

function ClothingCard({ item }) {
  return (
    <View style={styles.card}>
      <Image source={{ uri: item.image_url }} style={styles.image} />
      <Text style={styles.name}>{item.name}</Text>
      <Text style={styles.brand}>{item.brand}</Text>
      <Text style={styles.price}>${item.price.toFixed(2)}</Text>
      <Text style={styles.meta}>{item.category} · {item.fit_type}</Text>
    </View>
  );
}

export default function Catalog() {
  return (
    <FlatList
      data={mockItems}
      keyExtractor={(item) => item.id}
      numColumns={2}
      contentContainerStyle={styles.list}
      renderItem={({ item }) => <ClothingCard item={item} />}
    />
  );
}

const styles = StyleSheet.create({
  list: {
    padding: 12,
  },
  card: {
    flex: 1,
    margin: 6,
    borderWidth: 1,
    borderColor: "#ddd",
    borderRadius: 8,
    padding: 10,
    backgroundColor: "#fff",
  },
  image: {
    width: "100%",
    height: 150,
    borderRadius: 4,
    marginBottom: 8,
  },
  name: {
    fontWeight: "600",
    fontSize: 14,
  },
  brand: {
    color: "#666",
    fontSize: 12,
  },
  price: {
    marginTop: 4,
    fontWeight: "500",
  },
  meta: {
    fontSize: 11,
    color: "#999",
    marginTop: 2,
  },
});