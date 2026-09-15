import { useState } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Environment, useGLTF } from "@react-three/drei";

const avatars = [
  {
    name: "Default",
    file: "avatar.glb",
  },
  {
    name: "Chill",
    file: "chill_outfit.glb",
  },
  {
    name: "Military",
    file: "military_outfit.glb",
  },
  {
    name: "Business Casual",
    file: "business_casual.glb",
  },
];

function Avatar({ file }) {
  const { scene } = useGLTF(`/models/${file}`);

  return (
    <primitive
      object={scene}
      scale={2}
      position={[0, -2, 0]}
    />
  );
}

export default function App() {
  const [selectedAvatar, setSelectedAvatar] = useState(avatars[0]);

  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <div
        style={{
          position: "absolute",
          top: 20,
          left: 20,
          zIndex: 10,
          display: "flex",
          gap: 10,
        }}
      >
        {avatars.map((avatar) => (
          <button
            key={avatar.file}
            onClick={() => setSelectedAvatar(avatar)}
            style={{
              padding: "10px 16px",
              cursor: "pointer",
            }}
          >
            {avatar.name}
          </button>
        ))}
      </div>

      <Canvas camera={{ position: [0, 1, 6], fov: 45 }}>
        <ambientLight intensity={1} />
        <directionalLight position={[5, 5, 5]} intensity={2} />

        <Avatar file={selectedAvatar.file} />

        <Environment preset="studio" />
        <OrbitControls />
      </Canvas>
    </div>
  );
}