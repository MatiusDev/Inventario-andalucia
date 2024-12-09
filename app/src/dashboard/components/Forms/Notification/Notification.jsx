import "./Notification.css";

import Head from "./Head/Head";
import NoficationElement from "./NotificationElement/NoficationElement";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faCircleExclamation,faCheckDouble,faTrash} from "@fortawesome/free-solid-svg-icons";

const Notification = () => {
    return (
        <div className="notification">
            <Head/>
            <div className="list-notifications">
                <NoficationElement/>
            </div>

            <div className="actions">
                <button className="mark-read">
                    <FontAwesomeIcon icon={faCheckDouble} />
                    Marcar todo como leído
                </button>
                <button className="delete-all">
                    <FontAwesomeIcon icon={faTrash} />
                    Borrar todo
                </button>
            </div>
        </div>
    );
};

export default Notification;