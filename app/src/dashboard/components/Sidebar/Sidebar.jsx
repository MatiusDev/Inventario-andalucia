// css
import "./Sidebar.css";

import { useState } from "react";

// componentes
import HeadIcon from "../HeadIcon/HeadIcon";
import Nav from "../Nav/Nav";
import Menu from "../Menu/Menu";
import Line from "../Line/Line";
import DarkMode from "../DarkMode/DarkMode";
import PanelUser from "../PanelUser/PanelUser";
import LogOut from "../LogOut/LogOut";

// formulario
// import Notification from "../Base/Notification/Notification"
import UserContent from "../Base/Content/UserContent";
import SupplierContent from "../Base/Content/SupplierContent";
import ProductContent from "../Base/Content/ProductContent";
import OrderContent from "../Base/Content/OrderContent";

const menuNavOptions = {
    "/users": <UserContent />,
    "/suppliers": <SupplierContent />,
    "/products": <ProductContent />,
    "/orders": <OrderContent />,
    // "/tools": <ProductContent />,
    // "/plants": <ProductContent />,
    // "/supplies": <ProductContent />,
    // "/customers
    // "/notifications": <Notification />,
}

const Sidebar = () => {
    const [navOption, setNavOption] = useState("/users");

    const handleMenuClick = (option) => {
        setNavOption(option);
    }

    return (
        <div>
            <Menu />
            <div className="sidebar">
                <HeadIcon />
                <Nav handleMenuClick={handleMenuClick} />
                <div>
                    <Line />
                    <DarkMode />
                    <PanelUser />
                    <div>
                        <LogOut />
                    </div>
                </div>
            </div>
            <main>
                {menuNavOptions[navOption]}
            </main>
        </div>
    );
};

export default Sidebar;