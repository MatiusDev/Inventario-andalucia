import "./SidebarButton.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const SidebarButton = ({icon, nameSpan, handleMenuClick, path}) => {
    return (
        <li>
            <a onClick={() => handleMenuClick(path)}>
                <FontAwesomeIcon className="icon" icon={icon} />
                <span>{nameSpan}</span>
            </a>
        </li>
    );
}

export default SidebarButton;