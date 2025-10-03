import { useState } from "react";

function PythonAPITest() {
  const [message, setMessage] = useState<string>("");

  const getMessage = async () => {
    const response = await fetch("http://127.0.0.1:5000/hello");
    const text = await response.text(); // 👈 plain text, not JSON
    setMessage(text);
  };

  return (
    <div>
      <button onClick={getMessage}>Get Message</button>
      <p>{message}</p>
    </div>
  );
}

export default PythonAPITest;
