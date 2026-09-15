import { useState, useEffect } from "react";
import { fetchClothing } from "./api";

export default function Catalog() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchClothing()
      .then(setItems)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading catalog...</p>;
  if (error) return <p>Error: {error}</p>;
  if (items.length === 0) return <p>No items yet — seed the backend first.</p>;

  return (
    <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", gap: 16, padding: 20 }}>
      {items.map((item) => (
        <div key={item.id} style={{ border: "1px solid #ddd", borderRadius: 8, padding: 12 }}>
          <img
            src={item.image_url}
            alt={item.name}
            style={{ width: "100%", height: 200, objectFit: "cover", borderRadius: 4 }}
          />
          <h3 style={{ margin: "8px 0 4px" }}>{item.name}</h3>
          <p style={{ margin: 0, color: "#666" }}>{item.brand}</p>
          <p style={{ margin: "4px 0" }}>${item.price.toFixed(2)}</p>
          <span style={{ fontSize: 12, color: "#999" }}>{item.category} · {item.fit_type}</span>
        </div>
      ))}
    </div>
  );
}