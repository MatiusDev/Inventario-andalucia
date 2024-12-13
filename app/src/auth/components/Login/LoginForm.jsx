import "./LoginForm.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser, faLock } from "@fortawesome/free-solid-svg-icons";

import { useNavigate } from "react-router";
import { useForm } from "@/common/hooks/useForm.jsx";
import { useContext } from "react";

// import { AuthContext } from "@auth/context/AuthProvider";

import { apiPost } from "@utils/api";

const LoginForm = ({ handleClick }) => {
  const navigate = useNavigate();
  // const { user, setUser } = useContext(AuthContext);

  const validate = (values) => {
    const errors = {};
    if (!values.username) errors.name = "El nombre de usuario es obligatorio";
    if (!values.password) errors.password = "La contraseña es obligatoria";
    return errors;
  }

  const { 
    values, 
    errors, 
    handleChange, 
    resetForm 
  } = useForm({ username: "", password: "", rememberMe: false }, validate);

  const handleSubmit = async (evt) => {
    evt.preventDefault();
    try {
      if (errors.name || errors.password) {
        console.log("Error: Campos vacios");
        return;
      };
      const data = { username: values.username, password: values.password }
      
      const URL_PATH = "/auth/login";
      const response = await apiPost(URL_PATH, data);
      console.log(response);
      if (response) {
        resetForm();
        navigate("/dashboard");
      }
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <form id="login-form" onSubmit={handleSubmit}>
      <div className="button-container">
        <div className="button">
          <FontAwesomeIcon className="icon" icon={faUser} />
          <input
            type="text"
            placeholder="Usuario"
            name="username"
            value={values.username}
            onChange={handleChange}
          />
        </div>
        <div className="button">
          <FontAwesomeIcon className="icon" icon={faLock} />
          <input
            type="password"
            placeholder="Contraseña"
            name="password"
            value={values.password}
            onChange={handleChange}
          />
        </div>
        <div className="form-check form-switch">
          <label className="form-check-label" htmlFor="remember-me">Recordarme</label>
          <input 
            type="checkbox"
            className="form-check-input" 
            role="switch"
            id="remember-me"
            name="rememberMe"
            checked={values.rememberMe}
            onChange={handleChange}
          />
        </div>
        <div>
          <span className="icon"></span>
          <button className="button-login" type="submit">
            Iniciar Sesión
          </button>
        </div>
        <div className="enlaces-autenticacion">
          <a className="button-forgot">Recuperar contraseña</a>
          <a className="button-login-register" onClick={handleClick}>Registrarse</a>
        </div>
      </div>
    </form>
  );
}

export default LoginForm;