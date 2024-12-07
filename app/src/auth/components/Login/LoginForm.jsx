import "./LoginForm.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser,faLock } from "@fortawesome/free-solid-svg-icons";

const LoginForm = ({title, handleClick}) => {
    return (
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
                        {title}
                    </button>
                </div>
                <div className="enlaces-autenticacion">
                    <a href="">Recuperar Contraseña</a>
                    <a onClick={handleClick}>Registrarse</a>
                </div>
            </div>
        </form>
    )
};

export default LoginForm