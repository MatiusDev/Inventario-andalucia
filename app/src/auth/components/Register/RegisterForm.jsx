import "../Login/LoginForm.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser, faLock, faCircleInfo } from "@fortawesome/free-solid-svg-icons";

const RegisterForm = ({ handleSubmit, handleClick }) => {
  return (
    <form id="login-form" onSubmit={handleSubmit}>
      <div className="button-container">
        <div className="button">
          {/* <FontAwesomeIcon className="icon" icon={faCircleInfo}  /> */}
          <input type="text" placeholder="Usuario" />
        </div>
        <div className="button">
          {/* <FontAwesomeIcon className="icon" icon={faCircleInfo} /> */}
          <input type="text" placeholder="Nombre completo" />
        </div>
        <div className="button">
          {/* <FontAwesomeIcon className="icon" icon={faCircleInfo} /> */}
          <input type="email" placeholder="Correo electrónico" />
        </div>
        <div className="button">
          {/* <FontAwesomeIcon className="icon" icon={faCircleInfo} /> */}
          <input type="password" placeholder="Contraseña" />
        </div>
        <div>
          <span className="icon"></span>
          <button className="button-login" type="submit">
            Registrarse
          </button>
        </div>
        <div className="enlaces-autenticacion">
          <a className="button-forgot">Recuperar contraseña</a>
          <a className="button-login-register" onClick={handleClick}>Loguearse</a>
        </div>
      </div>
    </form>
  );
}

export default RegisterForm;