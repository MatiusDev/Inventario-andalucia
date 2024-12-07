import "./Login.css";
import LoginForm from "./LoginForm";

const Login = ({ title, handleClick }) => {
    return (
        <div className="form-information">
            <div className="form-information-childs">
                <h2>{title}</h2>
                <LoginForm title={title} handleClick={handleClick} />
            </div>
        </div>
    );
};

export default Login;
