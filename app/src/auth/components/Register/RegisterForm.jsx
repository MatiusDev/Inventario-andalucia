import "../Login/LoginForm.css";
import "./RegisterForm.css";

import { useForm } from "@/common/hooks/useForm.jsx";

import { apiPost } from "@utils/api";

const defaultUser = { username: "", fullname: "", email: "", password: "" };

const RegisterForm = ({ handleClick }) => {
    const validate = (values) => {
        const errors = {};
        if (!values.username) errors.name = "El nombre de usuario es obligatorio";
        if (!values.fullname) errors.fullname = "El nombre completo es obligatorio";
        if (!values.email) errors.email = "El correo electrónico es obligatorio";
        if (!values.password) errors.password = "La contraseña es obligatoria";
        return errors;
    };

    const { values, errors, handleChange, resetForm } = useForm(defaultUser, validate);

    const handleSubmit = async (evt) => {
      evt.preventDefault();
      try {
        if (Object.keys(errors).length > 0) {
          console.log("Error: Campos vacios");
          return;
        };
        const user = { 
          username: values.username, 
          full_name: values.fullname, 
          email: values.email, 
          password: values.password
        }

        const URL_PATH = "/auth/sign-up";
        const response = await apiPost(URL_PATH, user);
        console.log(response);
        if (response) {
          resetForm();
          handleClick();
          alert(response);
        }
      } catch (error) {
        console.log(error)
      }
    }

    return (
        <form id="login-form" onSubmit={handleSubmit}>
            <div className="button-container">
                <div className="button">
                    <input
                        type="text"
                        placeholder="Usuario"
                        name="username"
                        value={values.username}
                        onChange={handleChange}
                    />
                </div>
                <div className="button">
                    <input
                        type="text"
                        placeholder="Nombre completo"
                        value={values.fullname}
                        name="fullname"
                        onChange={handleChange}
                    />
                </div>
                <div className="button">
                    <input 
                        type="email"
                        placeholder="Correo electrónico"
                        value={values.email}
                        name="email"
                        onChange={handleChange}
                    />
                </div>
                <div className="button">
                    <input
                        type="password"
                        placeholder="Contraseña"
                        value={values.password}
                        name="password"
                        onChange={handleChange}
                    />
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