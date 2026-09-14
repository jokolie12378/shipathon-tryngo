import { Canvas } from "@react-three/fiber";
import { OrbitControls, Environment, useGLTF } from "@react-three/drei";

function Avatar() {
  const { scene } = useGLTF("/models/avatar.glb");

  return (
    <primitive
      object={scene}
      scale={2}
      position={[0, -2, 0]}
    />
  );
}

function Hoodie() {
  const { scene } = useGLTF("/models/clothing/tops/hoodie.glb");

  scene.traverse((object) => {
    if (object.isMesh || object.isSkinnedMesh) {
      console.log(
        "HOODIE:",
        object.name,
        "skinned:",
        object.isSkinnedMesh
      );
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

        <Hoodie />

        <Environment preset="studio" />

        <OrbitControls />
      </Canvas>
    </div>
  );
}