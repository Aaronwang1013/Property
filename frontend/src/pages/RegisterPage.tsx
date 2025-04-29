import { useState } from "react";
import { register } from "../api/auth";

function RegisterPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const data = await register(email, password);
      setMessage(JSON.stringify(data));
    } catch (error) {
      console.error(error);
      setMessage("註冊失敗");
    }
  };

  return (
    <div>
      <h2>註冊</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required /><br/>
        <input type="password" placeholder="密碼" value={password} onChange={(e) => setPassword(e.target.value)} required /><br/>
        <button type="submit">註冊</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default RegisterPage;
