import React from "react";
import { GestureHandlerRootView } from "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import AvatarSetupScreen from "./screens/AvatarSetupScreen";
import MeasurementsScreen from "./screens/MeasurementsScreen";
import SwipeScreen from "./screens/SwipeScreen";
import AvatarPreviewScreen from "./screens/AvatarPreviewScreen";

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="AvatarSetup">
          <Stack.Screen
            name="AvatarSetup"
            component={AvatarSetupScreen}
            options={{ title: "Avatar" }}
          />
          <Stack.Screen
            name="Measurements"
            component={MeasurementsScreen}
            options={{ title: "Measurements" }}
          />
          <Stack.Screen
            name="Swipe"
            component={SwipeScreen}
            options={{ title: "Pick Your Fit" }}
          />
          <Stack.Screen
            name="AvatarPreview"
            component={AvatarPreviewScreen}
            options={{ title: "Your Outfit" }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </GestureHandlerRootView>
  );
}