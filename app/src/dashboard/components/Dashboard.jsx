import "./Sidebar/Sidebar.css";
import "./Dashboard.css";

import { useState } from "react";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faX } from "@fortawesome/free-solid-svg-icons";

import Sidebar from "./Sidebar/Sidebar";

// Opciones de menu
// import Notification from "../Base/Notification/Notification"
import Welcome from "./Welcome/Welcome";
import UserContent from "./Base/Content/UserContent";
import SupplierContent from "./Base/Content/SupplierContent";
import ProductContent from "./Base/Content/ProductContent";
import OrderContent from "./Base/Content/OrderContent";

import { useNavigate } from "react-router";

import { apiPost } from "@utils/api";

const menuNavOptions = {
  "/welcome": <Welcome />,
  "/users": <UserContent />,
  "/suppliers": <SupplierContent />,
  "/products": <ProductContent />,
  "/orders": <OrderContent />,
  // "/tools": <ProductContent />,
  // "/plants": <ProductContent />,
  // "/supplies": <ProductContent />,
  // "/customers:
  // "/notifications": <Notification />,
}

const Dashboard = () => {
    const [navOption, setNavOption] = useState("/welcome");
    const navigate = useNavigate();

    const handleMenuClick = (option) => {
        setNavOption(option);
    }

    const handleLogout = async () => {
      const URL = '/auth/logout';
      const response = await apiPost(URL);
      
      if (response) {
        navigate('/', { replace: true });
      }
    }

    return (
      <div className="dashboard">
        <div className="menu">
            <FontAwesomeIcon className="icon" icon={faBars} />
            <FontAwesomeIcon className="icon" icon={faX} />
        </div>
        <Sidebar handleMenuClick={handleMenuClick} handleLogout={handleLogout} />
        <main>
          {menuNavOptions[navOption]}
        </main>
      </div>
    );
};

export default Dashboard;