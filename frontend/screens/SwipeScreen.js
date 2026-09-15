import React, { useState } from "react";
import { View, Text, StyleSheet } from "react-native";
import SwipeCard from "../components/SwipeCard";

const mockShirts = [
  { id: "s1", name: "Classic Hoodie", brand: "Aritzia", price: 68.0, image_url: "https://placehold.co/300x400?text=Hoodie" },
  { id: "s2", name: "Slim Fit Tee", brand: "Uniqlo", price: 19.99, image_url: "https://placehold.co/300x400?text=Tee" },
];

const mockPants = [
  { id: "p1", name: "Straight Leg Jeans", brand: "Levi's", price: 89.5, image_url: "https://placehold.co/300x400?text=Jeans" },
  { id: "p2", name: "Cargo Pants", brand: "Zara", price: 59.9, image_url: "https://placehold.co/300x400?text=Cargo" },
];

const mockShoes = [
  { id: "sh1", name: "High Top Sneakers", brand: "Nike", price: 110.0, image_url: "https://placehold.co/300x400?text=Sneakers" },
  { id: "sh2", name: "Chelsea Boots", brand: "Dr. Martens", price: 150.0, image_url: "https://placehold.co/300x400?text=Boots" },
];

const CATEGORIES = [
  { key: "shirt", label: "Shirts", items: mockShirts },
  { key: "pants", label: "Pants", items: mockPants },
  { key: "shoes", label: "Shoes", items: mockShoes },
];

export default function SwipeScreen({ navigation }) {
  const [categoryIndex, setCategoryIndex] = useState(0);
  const [cardIndex, setCardIndex] = useState(0);
  const [outfit, setOutfit] = useState({});

  const category = CATEGORIES[categoryIndex];
  const currentItem = category.items[cardIndex];

  function handleSwipe(direction) {
    const liked = direction === "right";
    const updatedOutfit = liked
      ? { ...outfit, [category.key]: currentItem }
      : outfit;

    const nextCardIndex = cardIndex + 1;

    if (nextCardIndex < category.items.length) {
      setOutfit(updatedOutfit);
      setCardIndex(nextCardIndex);
    } else {
      const nextCategoryIndex = categoryIndex + 1;
      if (nextCategoryIndex < CATEGORIES.length) {
        setOutfit(updatedOutfit);
        setCategoryIndex(nextCategoryIndex);
        setCardIndex(0);
      } else {
        navigation.navigate("AvatarPreview", { outfit: updatedOutfit });
      }
    }
  }

  if (!currentItem) {
    return (
      <View style={styles.container}>
        <Text>No more items in this category.</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.categoryLabel}>{category.label}</Text>
      <View style={styles.cardArea}>
        <SwipeCard item={currentItem} onSwipe={handleSwipe} />
      </View>
      <Text style={styles.hint}>Swipe right to keep, left to skip</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fafafa",
    paddingTop: 20,
  },
  categoryLabel: {
    textAlign: "center",
    fontSize: 20,
    fontWeight: "700",
    marginBottom: 12,
  },
  cardArea: {
    flex: 1,
    justifyContent: "center",
  },
  hint: {
    textAlign: "center",
    color: "#999",
    marginBottom: 24,
  },
});