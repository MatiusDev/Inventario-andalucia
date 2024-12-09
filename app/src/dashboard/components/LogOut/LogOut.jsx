import './LogOut.css'

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import { faPowerOff } from "@fortawesome/free-solid-svg-icons";

const LogOut = () => {
    return (
        <li className="log-out">
            <a>
                <FontAwesomeIcon className="icon" icon={faPowerOff} />
                <span>Cerrar sesion</span>
            </a>
        </li>
    );
};

export default LogOut;