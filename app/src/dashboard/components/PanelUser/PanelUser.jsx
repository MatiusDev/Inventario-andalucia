import "./PanelUser.css"

import image from "@/assets/user.png";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import {faEllipsisVertical}from "@fortawesome/free-solid-svg-icons";

import { useAuth } from '@auth/context/AuthProvider';


const PanelUser = () => {
    const { authState } = useAuth();
    const { fullName, type } = authState;
    return (
        <div className="user">
            <img src={image} />
            <div className="info-user">
                <div className="name-rol">
                    <span className="name">{fullName}</span>
                    <span className="rol">{type}</span>
                </div>
                <button className="menu-user" type="button" data-bs-toggle="modal" data-bs-target="#perfilUsuarios">
                    <FontAwesomeIcon className="iconEllipsis" icon={faEllipsisVertical} />
                </button>
            </div>
        </div>
    );
};

export default PanelUser;