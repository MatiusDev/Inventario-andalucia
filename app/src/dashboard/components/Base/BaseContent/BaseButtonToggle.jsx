import "./BaseButton.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import {
    faEye,
    faPenToSquare,
    faBan,
} from "@fortawesome/free-solid-svg-icons";

const BaseButtonToggle = ({ id, active, handleView, handleEdit, handleDelete }) => {
    return (
        <div className="btn-actions">
            <a onClick={() => handleView(id)} className="btn btn-primary">
                <FontAwesomeIcon className="icon" icon={faEye} />
            </a>    
            <a onClick={() => handleEdit(id)} className="btn btn-warning">
                <FontAwesomeIcon className="icon" icon={faPenToSquare} />
            </a>
            {active ? (
                <a onClick={() => handleDelete(id)} className="btn btn-danger">
                    <FontAwesomeIcon className="icon" icon={faBan} />
                </a>
            ):
            (
                <a className="btn btn-secondary disabled" disabled>
                    <FontAwesomeIcon className="icon" icon={faBan} />
                </a>
            )}
        </div>
    );
};

export default BaseButtonToggle;