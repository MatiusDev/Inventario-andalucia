import "./Login.css";

import { useNavigate } from 'react-router';

import LoginForm from "./LoginForm.jsx";

const Login = ({ title, handleClick }) => {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate('/dashboard');
  };

  return (
    <div className="form-information">
      <div className="form-information-childs">
        <h2>{title}</h2>
        <LoginForm handleSubmit={handleSubmit} handleClick={handleClick} />
      </div>
    </div>
  );
};

export default Login;
