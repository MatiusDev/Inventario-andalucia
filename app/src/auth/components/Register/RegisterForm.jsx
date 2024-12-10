import "../Login/LoginForm.css";
import "./RegisterForm.css";

import { useState } from "react";
import { useNavigate } from "react-router";

import { apiPost } from "@utils/api";

const RegisterForm = ({ handleClick }) => {
    const [newUser, setNewUser] = useState({ username: "", fullname: "", email: "", password: "" });

    const handleSubmit = async (evt) => {
      evt.preventDefault();
      try {
        if (!newUser.username || !newUser.fullname || !newUser.email || !newUser.password) {
            console.log("Error: Campos vacios");
            return;
        };

        const URL_PATH = "/auth/sign-up";
        const user = { 
          username: newUser.username, 
          full_name: newUser.fullname, 
          email: newUser.email, 
          password: newUser.password
        }
        const response = await apiPost(URL_PATH, user);
        console.log(response)

      } catch (error) {
        console.log(error)
      }
    }

    return (
        <form id="login-form" onSubmit={handleSubmit}>
            <div className="button-container">
                <div className="button">
                    <input type="text" placeholder="Usuario" value={newUser.username} onChange={e => setNewUser({ ...newUser, username: e.target.value })} />
                </div>
                <div className="button">
                    <input type="text" placeholder="Nombre completo" value={newUser.fullname} onChange={e => setNewUser({ ...newUser, fullname: e.target.value })}/>
                </div>
                <div className="button">
                    <input type="email" placeholder="Correo electrónico" value={newUser.email} onChange={e => setNewUser({ ...newUser, email: e.target.value })}/>
                </div>
                <div className="button">
                    <input type="password" placeholder="Contraseña" value={newUser.password} onChange={e => setNewUser({ ...newUser, password: e.target.value })}/>
                </div>
                <div>
                    <span className="icon"></span>
                    <button className="button-login" type="submit">
                        Registrarse
                    </button>
                </div>
                <div className="enlaces-autenticacion register">
                    <a className="button-login-register" onClick={handleClick}>Loguearse</a>
                </div>
            </div>
        </form>
    );
}

export default RegisterForm;