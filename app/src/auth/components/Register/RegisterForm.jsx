import "../Login/LoginForm.css"

const RegisterForm = ({handleClick}) => {
    return (
        <form id="login-form">
            <div className="button-container">
                <div className="button">
                    <input type="text" placeholder="Nombre completo" />
                </div>
                <div className="button">
                    <input type="email" placeholder="Email" />
                </div>
                <div className="button">
                    <input type="text" placeholder="Usuario" />
                </div>
                <div className="button">
                    <input type="password" placeholder="Contraseña" />
                </div>
                <div>
                    <span className="icon"></span>
                    <button className="button-login" type="submit">
                        Registrar
                    </button>
                </div>
                <div className="enlaces-autenticacion">
                    <a onClick={handleClick}>Iniciar sesion</a>
                </div>
            </div>
        </form>
    )
};

export default RegisterForm