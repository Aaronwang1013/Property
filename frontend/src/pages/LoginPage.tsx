import { useState } from "react";
import { login } from "../api/auth";

function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const data = await login(email, password);
      setMessage(JSON.stringify(data));
      // localStorage.setItem("token", data.access_token); // 這邊可以順便存token
    } catch (error) {
      console.error(error);
      setMessage("登入失敗");
    }
  };

  return (
    <div>
      <h2>登入</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required /><br/>
        <input type="password" placeholder="密碼" value={password} onChange={(e) => setPassword(e.target.value)} required /><br/>
        <button type="submit">登入</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default LoginPage;
