import "./LoginForm.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faLock } from "@fortawesome/free-solid-svg-icons";

const LoginForm = ({ handleSubmit, handleClick }) => {
  return (
    <form id="login-form" onSubmit={handleSubmit}>
      <div className="button-container">
        <div className="button">
          <FontAwesomeIcon className="icon" icon={faUser} />
          <input type="text" placeholder="Usuario" />
        </div>
        <div className="button">
          <FontAwesomeIcon className="icon" icon={faLock} />
          <input type="password" placeholder="Contraseña" />
        </div>
        <div className="form-check form-switch">
          <input type="checkbox" className="form-check-input" role="switch" id="remember-me" />
          <label className="form-check-label" htmlFor="remember-me">Recordarme</label>
        </div>
        <div>
          <span className="icon"></span>
          <button className="button-login" type="submit">
            Iniciar Sesión
          </button>
        </div>
        <div className="enlaces-autenticacion">
          <a className="button-forgot" href="">Recuperar contraseña</a>
          <a className="button-login-register" onClick={handleClick}>Registrarse</a>
        </div>
      </div>
    </form>
  );
}

export default LoginForm;