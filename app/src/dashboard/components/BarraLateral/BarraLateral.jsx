import "./BarraLateral.css";

import BotonBarraLateral from "../BotonBarraLateral/BotonBarraLateral";
import image from "@/assets/user.png";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

// import {faBars,
//         faX,
//         faEnvelope,
//         faTruck,
//         faBoxesStacked,
//         faUsers,
//         faUsersLine,
//         faArrowRotateLeft,
//         faTrowel,
//         faNetworkWired,
//         faEllipsisVertical,
//         faBoxesPacking,
//         faPowerOff,
//         faChartPie,
//         faMoon}from "@fortawesome/free-solid-svg-icons";

// import {faPagelines,faAudible} from "@fortawesome/free-brands-svg-icons" 

const BarraLateral = () => {
    return (
        <div>
            <div className="menu">
                <FontAwesomeIcon className="icon" icon={faBars} />
                <FontAwesomeIcon className="icon" icon={faX} />
            </div>

            <div className="barra-lateral">
                <div>
                    <div className="nombre-pagina">
                        <FontAwesomeIcon className="icon" id="flower" icon={faPagelines} />
                        <span>Vivero</span>
                    </div>
                </div>
                <nav className="navegacion">
                    <ul>
                        <BotonBarraLateral FontAwesomeIcon icon={faEnvelope} nameSpan={"Notificaciones"}/>
                        {/* <li>
                            <a href="./index.html">
                                <FontAwesomeIcon className="icon" icon={faEnvelope} />
                                <span>Notificaciones</span>
                            </a>
                        </li>
                        <li>
                            <a href="./proveedores.html">
                                <FontAwesomeIcon className="icon" icon={faTruck} />
                                <span>Proveedores</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                                <FontAwesomeIcon className="icon" icon={faBoxesPacking} />
                                <span>Inventario</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                                <FontAwesomeIcon className="icon" icon={faBoxesStacked} />
                                <span>Productos</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                                <FontAwesomeIcon className="icon" icon={faNetworkWired} />
                                <span>Categorias</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                                <FontAwesomeIcon className="icon" icon={faUsers} />
                                <span>Clientes</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                                <FontAwesomeIcon className="icon" icon={faUsersLine} />
                                <span>Usuarios</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                                <FontAwesomeIcon className="icon" icon={faArrowRotateLeft} />
                                <span>Devoluciones</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                                <FontAwesomeIcon className="icon" icon={faTrowel} />
                                <span>Herramientas</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                                <FontAwesomeIcon className="icon" icon={faAudible} />
                                <span>Auditoria</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                            <FontAwesomeIcon className="icon" icon={faChartPie} />  
                            <span>Graficas</span>
                            </a>
                        </li> */}
                    </ul>
                </nav>

                <div>
                    <div className="linea"></div>

                    <div className="modo-oscuro">
                        <div className="info">
                            <FontAwesomeIcon className="icon" icon={faMoon} />
                            <span>Dark mode</span>
                        </div>
                        <div className="switch">
                            <div className="base">
                                <div className="circulo">

                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="usuario">
                        <img src={image} />
                        <div className="info-usuario">
                            <div className="nombre-rol">
                                <span className="nombre">juan daniel</span>
                                <span className="rol">admin</span>
                            </div>
                            <button className="menu-user" type="button" data-bs-toggle="modal" data-bs-target="#perfilUsuarios">
                                <FontAwesomeIcon className="icon" icon={faEllipsisVertical} />
                            </button>
                        </div>
                    </div>
                    <div>
                        <li className="cerrar-sesion">
                            <a>
                                <FontAwesomeIcon className="icon" icon={faPowerOff} />
                                <span>Cerrar sesion</span>
                            </a>
                        </li>
                    </div>
                </div>
            </div>

            <main>
                
            </main>
        </div>
    );
};

export default BarraLateral;