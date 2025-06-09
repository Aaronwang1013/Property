import "../App.css";

export default function LoginModal({ isOpen, onClose }: { isOpen: boolean; onClose: () => void }) {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <button className="close-button" onClick={onClose}>×</button>
        <h2 className="modal-title">Member Sign In</h2>

        <div className="social-buttons">
          <button className="social">
            <img src="/icons/google.svg" className="icon" /> Sign in with Google
          </button>
          <button className="social">
            <img src="/icons/apple.svg" className="icon" /> Sign in with Apple
          </button>
          <button className="social">
            <img src="/icons/facebook.svg" className="icon" /> Sign in with Facebook
          </button>
        </div>

        <div className="divider">or</div>

        <input className="input" placeholder="Email" />
        <input className="input" placeholder="Password" type="password" />

        <button className="signin-button">Sign in</button>

        <div className="bottom-text">
          <p>Don't have an account? <a href="#">Create free account</a></p>
          <p className="small">
            By signing in you agree to the <a href="#">Terms of Use</a> & <a href="#">Privacy Policy</a>.
          </p>
          <p>Other issues? <a href="mailto:contactus@seekingalpha.com">qazxsw523625@gmail.com</a></p>
        </div>
      </div>
    </div>
  );
}
