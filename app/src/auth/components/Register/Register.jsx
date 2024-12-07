import "../Login/Login";
import RegisterForm from "./RegisterForm";

const Register = ({ title, handleClick }) => {
    return (
        <div className="form-information">
            <div className="form-information-childs">
                <h2>{title}</h2>
                <RegisterForm title={title} handleClick={handleClick}/>
            </div>
        </div>
    );
};

export default Register;
