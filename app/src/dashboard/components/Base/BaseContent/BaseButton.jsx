import "./BaseButton.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import {
    faEye,
    faPenToSquare,
    faTrash,
} from "@fortawesome/free-solid-svg-icons";

const BaseButton = ({ id, handleView, handleEdit, handleDelete }) => {
    return (
    <div className="btn-actions">
        <a onClick={() => handleView(id)} className="btn btn-primary " data-bs-toggle="modal" data-bs-target="#">
            <FontAwesomeIcon className="icon" icon={faEye} />
        </a>    
        <a onClick={() => handleEdit(id)} className="btn btn-warning " data-bs-toggle="modal" data-bs-target="#">
            <FontAwesomeIcon className="icon" icon={faPenToSquare} />
        </a>
        <a onClick={() => handleDelete(id)} className="btn btn-danger " data-bs-toggle="modal" data-bs-target="#">
             <FontAwesomeIcon className="icon" icon={faTrash} />
        </a>
    </div>);
};

export default BaseButton;