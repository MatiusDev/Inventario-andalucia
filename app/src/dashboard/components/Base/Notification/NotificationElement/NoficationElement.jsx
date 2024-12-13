import "./NoficationElement.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faCircleExclamation} from "@fortawesome/free-solid-svg-icons";

const NoficationElement = () => {
    return (
        <div className="notification-element not-read">
            <div className="notification-icon warning">
                <FontAwesomeIcon icon={faCircleExclamation} />
            </div>
            <div className="content-notification">
                <div className="title-notification">
                    <h3>Stock Bajo: Abono Organico</h3>
                    <span className="time">hace 10 min</span>
                </div>
                <p>Quedan solo 3 unidades en inventario. Se recomienda realizar un nuevo pedido.</p>
                <div className="meta-notification">
                    <span className="priority high">Alta</span>
                    <span className="type warning">Advertencia</span>
                </div>
            </div>
        </div>
    );
};

export default NoficationElement;