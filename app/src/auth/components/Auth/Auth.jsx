import "./Auth.css";

import image from "@/assets/fondo4.png";

import Login from "../Login/Login";
import Register from "../Register/Register";

import { useState } from "react";

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