import "./Notificaiones.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faCircleExclamation,faCheckDouble} from "@fortawesome/free-solid-svg-icons";

const Notificaiones = () => {
    return (
        <div className="notificaciones">
            <div className="cabecera">
                <h2>Notificaciones</h2>
                <span className="contador">0</span>
            </div>

            <div className="lista-notificaciones">
                <div className="elemento-notificacion no-leida">
                    <div className="icono-notificacion advertencia">
                        <FontAwesomeIcon icon={faCircleExclamation} />
                    </div>
                    <div className="contenido-notificacion">
                        <div className="titulo-notificacion">
                            <h3>Stock Bajo: Abono Organico</h3>
                            <span className="tiempo">hace 10 min</span>
                        </div>
                        <p>Quedan solo 3 unidades en inventario. Se recomienda realizar un nuevo pedido.</p>
                        <div className="meta-notificacion">
                            <span className="prioridad alta">Alta</span>
                            <span className="tipo advertencia">Advertencia</span>
                        </div>
                    </div>
                </div>
            </div>

            <div className="acciones">
                <button className="marcar-leidas">
                    <FontAwesomeIcon icon={faCheckDouble} />
                    Marcar todo como leído
                </button>
                <button className="borrar-todo">
                    <FontAwesomeIcon icon={faTrash} />
                    Borrar todo
                </button>
            </div>
        </div>
    );
};

export default Notificaiones;