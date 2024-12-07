import "./BotonBarraLateral.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const BotonBarraLateral = (icono,nameSpan,) => {
    return (
        <li>
            <a>
                <FontAwesomeIcon className="icon" icon={icono} />
                <span>{nameSpan}</span>
            </a>
        </li>
    );
}

export default BotonBarraLateral;