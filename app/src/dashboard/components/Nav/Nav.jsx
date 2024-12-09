import "./Nav.css"

import SidebarButton from "../SidebarButton/SidebarButton";

import { faEnvelope, faTruck, faBoxesStacked, faUsers, faUsersLine, faArrowRotateLeft, faTrowel, faNetworkWired, faBoxesPacking, faChartPie } from "@fortawesome/free-solid-svg-icons";
import { faAudible } from "@fortawesome/free-brands-svg-icons"

const Nav = () => {
    return (
        <nav className="nav">
            <ul>
                <SidebarButton icon={faEnvelope} nameSpan={"Notificaciones"} />
                <SidebarButton icon={faTruck} nameSpan={"Proveedores"} />
                <SidebarButton icon={faBoxesPacking} nameSpan={"Inventario"} />
                <SidebarButton icon={faBoxesStacked} nameSpan={"Productos"} />
                <SidebarButton icon={faNetworkWired} nameSpan={"Categorias"} />
                <SidebarButton icon={faUsers} nameSpan={"Clientes"} />
                <SidebarButton icon={faUsersLine} nameSpan={"Usuarios"} />
                <SidebarButton icon={faArrowRotateLeft} nameSpan={"Devoluciones"} />
                <SidebarButton icon={faTrowel} nameSpan={"Herramientas"} />
                <SidebarButton icon={faAudible} nameSpan={"Auditoria"} />
                <SidebarButton icon={faChartPie} nameSpan={"Graficas"} />
            </ul>
        </nav>
    );
};

export default Nav;