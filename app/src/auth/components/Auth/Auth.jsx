import "./Auth.css";

import image from "@/assets/fondo4.png";

import Login from "../Login/Login";
import Register from "../Register/Register";

import { useEffect, useState } from "react";

import { apiFetch, apiPost } from "@utils/api";

const URL_PATH = "/auth/login";
const user = { username: "matiusdev", password: "12345" }

const Auth = () => {
  const [IsLoginIn, setLoginIn] = useState(true);

  const handleClick = () => {
    setLoginIn(!IsLoginIn);
  };

  return (
    <div className="container-form">
      <img className="image-form" src={image} />
      <div className="information">
        <div className="info-childs">
          <img src="" alt="" />
          <h2>Vivero Andalucía</h2>
        </div>
      </div>
      {IsLoginIn ? <Login title="Iniciar Sesión" handleClick={handleClick} /> : <Register title="Registrarse" handleClick={handleClick} />}
    </div>
  );
};

export default Auth;