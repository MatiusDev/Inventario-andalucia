import "./DarkMode.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import {faMoon}from "@fortawesome/free-solid-svg-icons";

const DarkMode = () => {
    return (
        <div className="dark-mode">
            <div className="info">
                <FontAwesomeIcon className="icon" icon={faMoon} />
                <span>Dark mode</span>
            </div>
            <div className="switch">
                <div className="base">
                    <div className="circle">

                    </div>
                </div>
            </div>
        </div>
    );
};

export default DarkMode;