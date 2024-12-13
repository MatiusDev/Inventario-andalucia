import "./PanelUser.css"

import image from "@/assets/user.png";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import {faEllipsisVertical}from "@fortawesome/free-solid-svg-icons";

const PanelUser = () => {
    return (
        <div className="user">
            <img src={image} />
            <div className="info-user">
                <div className="name-rol">
                    <span className="name">juan daniel</span>
                    <span className="rol">admin</span>
                </div>
                <button className="menu-user" type="button" data-bs-toggle="modal" data-bs-target="#perfilUsuarios">
                    <FontAwesomeIcon className="iconEllipsis" icon={faEllipsisVertical} />
                </button>
            </div>
        </div>
    );
};

export default PanelUser;