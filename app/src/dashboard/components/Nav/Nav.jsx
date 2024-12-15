import "./Nav.css"

import SidebarButton from "../SidebarButton/SidebarButton";

import { faEnvelope,faFan,faDolly, faTruck,faBoxesPacking,faBoxesStacked, faUsers, faUsersLine, faArrowRotateLeft, faTrowel, faNetworkWired, faChartPie } from "@fortawesome/free-solid-svg-icons";
import { faAudible } from "@fortawesome/free-brands-svg-icons"

const Nav = ({ handleMenuClick }) => {
    return (
        
        <nav className="nav">
            <ul>
                <SidebarButton handleMenuClick={handleMenuClick} path={"/notifications"} icon={faEnvelope} nameSpan={"Notificaciones"} />
                <SidebarButton handleMenuClick={handleMenuClick} path={"/users"} icon={faUsersLine} nameSpan={"Usuarios"} />
                <SidebarButton handleMenuClick={handleMenuClick} path={"/suppliers"} icon={faTruck} nameSpan={"Proveedores"} />
                {/* <SidebarButton handleMenuClick={handleMenuClick} path={"/"} icon={faBoxesPacking} nameSpan={"Inventario"} /> */}
                <SidebarButton handleMenuClick={handleMenuClick} path={"/products"} icon={faBoxesStacked} nameSpan={"Productos"} />
                <SidebarButton handleMenuClick={handleMenuClick} path={"/orders"} icon={faDolly} nameSpan={"Ordenes"} />
                <SidebarButton handleMenuClick={handleMenuClick} path={"/tools"} icon={faTrowel} nameSpan={"Herramientas"} />
                <SidebarButton handleMenuClick={handleMenuClick} path={"/plants"} icon={faFan} nameSpan={"Plantas"} />
                <SidebarButton handleMenuClick={handleMenuClick} path={"/inputs"} icon={faBoxesPacking} nameSpan={"Insumos"} />
                {/* <SidebarButton handleMenuClick={handleMenuClick} path={"/customers"} icon={faUsers} nameSpan={"Clientes"} /> */}
                {/* <SidebarButton handleMenuClick={handleMenuClick} path={"/notifications"} icon={faArrowRotateLeft} nameSpan={"Devoluciones"} /> */}
                {/* <SidebarButton handleMenuClick={handleMenuClick} path={"/notifications"} icon={faAudible} nameSpan={"Auditoria"} /> */}
                {/* <SidebarButton handleMenuClick={handleMenuClick} path={"/notifications"} icon={faChartPie} nameSpan={"Graficas"} /> */}
            </ul>
        </nav>
    );
};

export default Nav;