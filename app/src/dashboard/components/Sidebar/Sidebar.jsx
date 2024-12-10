// css
import "./Sidebar.css";

// formulario
import Notification from "../Forms/Notification/Notification"
import BaseForm from "../Forms/ContentForm/ContentForm";

import { useEffect, useState } from "react";

// componentes
import HeadIcon from "../HeadIcon/HeadIcon";
import Nav from "../Nav/Nav";
import Menu from "../Menu/Menu";
import Line from "../Line/Line";
import DarkMode from "../DarkMode/DarkMode";
import PanelUser from "../PanelUser/PanelUser";
import LogOut from "../LogOut/LogOut";
import Welcome from "../Welcome/Welcome";

const Sidebar = () => {
    const [OptNav, setOptNav] = useState("");

    const handleClick = (route) => {
        setOptNav(route);
    };

    const menuComponents = {
        notifications: <Notification />,
        // users: <User />,
    }
    return (
        <div>
            <Menu />
            <div className="sidebar">
                <HeadIcon />
                <Nav />
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
                {menuComponents[OptNav] || <BaseForm />}
            </main>
        </div>
    );
};

export default Sidebar;