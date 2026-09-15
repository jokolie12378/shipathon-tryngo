import React, { Suspense, useEffect, useState } from "react";
import { View, StyleSheet, Text } from "react-native";
import { Canvas } from "@react-three/fiber/native";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { Asset } from "expo-asset";

const MODELS = {
  avatar: require("../assets/models/avatar.glb"),
  business_casual: require("../assets/models/business_casual.glb"),
  chill_outfit: require("../assets/models/chill_outfit.glb"),
  military_outfit: require("../assets/models/military_outfit.glb"),
};

function Model({ modelKey, onError }) {
  const [scene, setScene] = useState(null);

  useEffect(() => {
    let isMounted = true;

    async function loadModel() {
      try {
        const asset = Asset.fromModule(MODELS[modelKey]);
        await asset.downloadAsync();
        console.log("Model URI:", asset.localUri);

        const loader = new GLTFLoader();
        loader.load(
          asset.localUri,
          (gltf) => {
            if (isMounted) setScene(gltf.scene);
          },
          undefined,
          (error) => {
            console.error("Error loading model:", error);
            if (isMounted) onError(error.message ?? "Unknown error");
          }
        );
      } catch (err) {
        console.error("Error preparing asset:", err);
        if (isMounted) onError(err.message ?? "Unknown error");
      }
    }

    loadModel();
    return () => {
      isMounted = false;
    };
  }, [modelKey]);

  if (!scene) return null;

  return <primitive object={scene} scale={2} position={[0, -2, 0]} />;
}

export default function AvatarViewer({ modelKey = "avatar" }) {
  const [error, setError] = useState(null);

  if (error) {
    return (
      <View style={[styles.container, styles.centered]}>
        <Text style={{ color: "red", textAlign: "center", padding: 16 }}>
          Failed to load model: {error}
        </Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Canvas camera={{ position: [0, 1, 6], fov: 45 }}>
        <ambientLight intensity={1} />
        <directionalLight position={[5, 5, 5]} intensity={2} />
        <Suspense fallback={null}>
          <Model modelKey={modelKey} onError={setError} />
        </Suspense>
      </Canvas>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: "100%",
    height: 400,
  },
  centered: {
    justifyContent: "center",
    alignItems: "center",
  },
});