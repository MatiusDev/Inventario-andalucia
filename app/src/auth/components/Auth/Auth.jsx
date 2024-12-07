import "./Auth.css";
import image from "@/assets/fondo4.png";
import Login from "../Login/Login"
import Register from "../Register/Register";
import { useState } from "react";

const Auth = () => {
    const [isLogin,setIsLogin] = useState(true)

    const handleClick = () => {
        setIsLogin(!isLogin) 
    }
    return (
        <div className="container-form">
            <img className="image-form" src={image} />
            <div className="information">
                <div className="info-childs">
                    <img src="" alt="" />
                    <h2>Vivero Andalucia</h2>
                </div>
            </div>
            {isLogin ? <Login title={"Iniciar sesion"} handleClick={handleClick} /> : <Register title={"Registrar"} handleClick={handleClick} />}
        </div>
    );
};

export default Auth;
