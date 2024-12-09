import "./HeadIcon.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import {faPagelines} from "@fortawesome/free-brands-svg-icons" 

const HeadIcon = () => {
    return (
        <div>
            <div className="name-page">
                <FontAwesomeIcon className="icon" id="flower" icon={faPagelines} />
                <span>Vivero</span>
            </div>
        </div>
    );
};

export default HeadIcon;