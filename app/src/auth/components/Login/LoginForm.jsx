import "./LoginForm.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser, faLock } from "@fortawesome/free-solid-svg-icons";

import { useNavigate } from "react-router";
import { useForm } from "@/common/hooks/useForm.jsx";
import { useAuth } from "@auth/context/AuthProvider";

import { apiPost, apiFetch } from "@utils/api";

const LoginForm = ({ handleClick }) => {
  const navigate = useNavigate();
  const { changeAuthState } = useAuth();

  const validate = (values) => {
    const errors = {};
    if (!values.username) errors.name = "El nombre de usuario es obligatorio";
    if (!values.password) errors.password = "La contraseña es obligatoria";
    return errors;
  };

  const { values, errors, handleChange, resetForm } = useForm(
    { username: "", password: "", rememberMe: false },
    validate
  );

  const handleSubmit = async (evt) => {
    evt.preventDefault();
    try {
      if (errors.name || errors.password) {
        console.log("Error: Campos vacios");
        return;
      }
      const data = { username: values.username, password: values.password };

      const URL_PATH = "/auth/login";
      const response = await apiPost(URL_PATH, data);
      if (!response) {
        console.log(response);
        return;
      }
      const URL_PATH_PROFILE = "/auth/profile";
      const response_profile = await apiFetch(URL_PATH_PROFILE);
      if (response_profile) {
        const data = response_profile;
        const user = {
          id: data.id,
          type: data.type,
          username: data.username,
          fullName: data.full_name,
          email: data.email,
          permissions: data.permissions,
          active: data.active,
          authenticated: data.is_logged_in,
        };

        changeAuthState(user);
        resetForm();
        navigate("/dashboard", { replace: true });
      }
    } catch (error) {
      console.log(error);
    }
  };

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
          <label className="form-check-label" htmlFor="remember-me">
            Recordarme
          </label>
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
          <a className="button-login-register" onClick={handleClick}>
            Registrarse
          </a>
        </div>
      </div>
    </form>
  );
};

export default LoginForm;
