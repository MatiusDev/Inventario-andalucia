// css
import "./Sidebar.css";

// formulario
import Notification from "../Forms/Notification/Notification"
import User from "../Forms/User/User";

// componentes
import HeadIcon from "../HeadIcon/HeadIcon";
import Nav from "../Nav/Nav";
import Menu from "../Menu/Menu";
import Line from "../Line/Line";
import DarkMode from "../DarkMode/DarkMode";
import PanelUser from "../PanelUser/PanelUser";
import LogOut from "../LogOut/LogOut";

const Sidebar = () => {
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
                <User/>
            </main>
        </div>
    );
};

export default Sidebar;