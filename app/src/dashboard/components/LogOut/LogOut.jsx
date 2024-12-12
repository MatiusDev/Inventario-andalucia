import './LogOut.css'

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import { faPowerOff } from "@fortawesome/free-solid-svg-icons";

const LogOut = ({ handleLogout }) => {
    return (
        <li className="log-out">
            <button className="button" onClick={handleLogout}>
                <FontAwesomeIcon className="icon" icon={faPowerOff} />
                <span>Cerrar sesion</span>
            </button>
        </li>
    );
};

export default LogOut;