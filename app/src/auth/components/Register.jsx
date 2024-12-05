import "./Login.css";

import { useNavigate } from 'react-router';

import RegisterForm from "./RegisterForm.jsx";

const Register = ({ title, handleClick }) => {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate('/inventory');
  };

  return (
    <div className="form-information">
      <div className="form-information-childs">
        <h2>{title}</h2>
        <RegisterForm handleSubmit={handleSubmit} handleClick={handleClick} />
      </div>
    </div>
  );
};

export default Register;
