import { Canvas } from "@react-three/fiber";
import { OrbitControls, Environment, useGLTF } from "@react-three/drei";

function Avatar() {
  const { scene } = useGLTF("/models/avatar.glb");

  scene.traverse((object) => {
    if (object.isMesh) {
      console.log("MESH:", object.name);
    }
  });

  return (
    <primitive
      object={scene}
      scale={2}
      position={[0, -2, 0]}
    />
  );

}

export default function App() {
  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <Canvas camera={{ position: [0, 1, 5], fov: 45 }}>
        <ambientLight intensity={1} />

        <directionalLight
          position={[5, 5, 5]}
          intensity={2}
        />

        <Avatar />

        <Environment preset="studio" />

        <OrbitControls />
      </Canvas>
    </div>
  );
}