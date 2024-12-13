import "./Login.css";

import LoginForm from "./LoginForm.jsx";

const Login = ({ title, handleClick }) => {
  return (
    <div className="form-information">
      <div className="form-information-childs">
        <h2>{title}</h2>
        <LoginForm handleClick={handleClick} />
      </div>
    </div>
  );
};

export default Login;
