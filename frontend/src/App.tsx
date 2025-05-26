import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import RegisterPage from "./pages/RegisterPage";
import LoginPage from "./pages/LoginPage";
import './App.css'

function App() {
  return (
    <Router>
      <div>
        <nav>
          <Link to="/register">註冊</Link> | <Link to="/login">登入</Link>
        </nav>
        <Routes>
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
