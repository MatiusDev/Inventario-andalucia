import "./SidebarButton.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const SidebarButton = ({icon,nameSpan}) => {
    return (
        <li>
            <a>
                <FontAwesomeIcon className="icon" icon={icon} />
                <span>{nameSpan}</span>
            </a>
        </li>
    );
}

export default SidebarButton;