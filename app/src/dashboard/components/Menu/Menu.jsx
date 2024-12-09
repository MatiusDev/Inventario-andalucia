import "./Menu.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import {faBars,faX,}from "@fortawesome/free-solid-svg-icons";

const Menu = () => {
    return (
        <div className="menu">
            <FontAwesomeIcon className="icon" icon={faBars} />
            <FontAwesomeIcon className="icon" icon={faX} />
        </div>
    );
};

export default Menu;