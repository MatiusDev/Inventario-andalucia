import "./Login.css";
import image from "@/assets/fondo4.png";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faLock } from "@fortawesome/free-solid-svg-icons";


const Login = () => {
  return (
    <>
      <div className="container-form">
        <img className="image-form" src={image} />
        <div className="information">
          <div className="info-childs">
            <img src="" alt="" />
            <h2>Vivero Andalucia</h2>
          </div>
        </div>
        <div className="form-information">
          <div className="form-information-childs">
            <h2>Inicia Sesión</h2>
            <form id="login-form">
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
                  <a href="">Recuperar Contraseña</a>
                  <a href="">Registrarse</a>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default Login;
