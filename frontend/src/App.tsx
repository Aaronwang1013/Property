import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";
import LoginModal from "./pages/LoginModal";
import LoginPage from "./pages/LoginPage";
import "./App.css"; 

function App() {
  const [showLogin, setShowLogin] = useState(false);

  return (
    <Router>
      <div className="relative min-h-screen">
        <button
          onClick={() => setShowLogin(true)}
          className="login-button"
        >
          Login
        </button>

        <Routes>
          <Route path="/login" element={<LoginPage />} />
        </Routes>

        <LoginModal isOpen={showLogin} onClose={() => setShowLogin(false)} />
      </div>
    </Router>
  );
}

export default App;
