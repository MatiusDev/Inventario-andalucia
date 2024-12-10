import "./LoginForm.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faLock } from "@fortawesome/free-solid-svg-icons";

import { useState } from "react";
import { useNavigate } from "react-router";

import { apiPost } from "@utils/api";

const LoginForm = ({ handleClick }) => {
  const [user, setUser] = useState({ username: "", password: "", rememberMe: false });
  const navigate = useNavigate()
  const handleSubmit = async (evt) => {
    evt.preventDefault();
    try {
      if (!user.username || !user.password) {
        console.log("Error: Campos vacios");
        return;
      };

      const URL_PATH = "/auth/login";
      const response = await apiPost(URL_PATH, { username: user.username, password: user.password });
      console.log(response)
      navigate("/dashboard")
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <form id="login-form" onSubmit={handleSubmit}>
      <div className="button-container">
        <div className="button">
          <FontAwesomeIcon className="icon" icon={faUser} />
          <input type="text" placeholder="Usuario" value={user.username} onChange={e => setUser({ ...user, username: e.target.value })}/>
        </div>
        <div className="button">
          <FontAwesomeIcon className="icon" icon={faLock} />
          <input type="password" placeholder="Contraseña" value={user.password} onChange={e => setUser({ ...user, password: e.target.value })} />
        </div>
        <div className="form-check form-switch">
          <label className="form-check-label" htmlFor="remember-me">Recordarme</label>
          <input 
            type="checkbox"
            className="form-check-input" 
            role="switch"
            id="remember-me"
            checked={user.rememberMe}
            onChange={e => setUser({ ...user, rememberMe: e.target.checked })}
          />
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