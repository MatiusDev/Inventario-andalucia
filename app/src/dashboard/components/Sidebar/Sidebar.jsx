// css
import "./Sidebar.css";

// componentes
import HeadIcon from "../HeadIcon/HeadIcon";
import Nav from "../Nav/Nav";
import Line from "../Line/Line";
import DarkMode from "../DarkMode/DarkMode";
import PanelUser from "../PanelUser/PanelUser";
import LogOut from "../LogOut/LogOut";

const Sidebar = ({ handleMenuClick, handleLogout }) => {
  return (
    <div className="sidebar">
      <HeadIcon />
      <Nav handleMenuClick={handleMenuClick} />
      <div>
        <Line />
        <DarkMode />
        <PanelUser />
        <div>
          <LogOut handleLogout={handleLogout} />
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
