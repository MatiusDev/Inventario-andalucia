import "./DarkMode.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faMoon} from "@fortawesome/free-solid-svg-icons";
import { useTheme } from "@/dashboard/context/ThemeContext";

const DarkMode = () => {

    const { isDarkMode, toggleDarkMode } = useTheme();

    return (
        <div className="dark-mode" onClick={toggleDarkMode}>
            <div className="info">
                <FontAwesomeIcon className="icon" icon={faMoon} />
                <span>{isDarkMode ? "Ligth Mode" : "Dark Mode" }</span>
            </div>
            <div className={`switch ${isDarkMode ? "active" : ""}`}>
                <div className="base">
                    <div className="circle">

                    </div>
                </div>
            </div>
        </div>
    );
};

export default DarkMode;