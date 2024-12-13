import { useState, useEffect } from "react";
import BaseContent from "../BaseContent/BaseContent";
import UserCreate from "../../Modals/UserCreate";

import { apiFetch, apiDelete } from "@utils/api.js";

// Titulos, el arreglo debe tener el mismo tamaño que el objeto que se recibe en la petición GET
const TITLES = [
  "ID",
  "Nombre completo",
  "Nombre de usuario",
  "Correo electrónico",
  "Tipo de usuario",
  "Estado",
  "Sesión"
];

const UserContent = () => {
    const [dataArray, setDataArray] = useState([]);

    const handleCreate = () => {
      console.log("Sisas");
    };

    const handleView = (id) => {
      console.log("Ver", id);
    };

    const handleEdit = (id) => {
      console.log("Editar", id);
    };

    const handleDelete = async (id) => {
      const URL = `/users/${id}/`;
      const response = await apiDelete(URL);
      if (response.status === "success") {
        const dataMapped = dataArray.map(item => {
          const { id, active } = item;
          if (id.value === id) {
            active.value = false;
            return item;
          }
          return item;
        });
        setDataArray(dataMapped);
      } else {
        console.log("Error al eliminar el usuario");
      }
    }

    useEffect(() => {
        const getData = async () => {
            const URL = "/users/";
            const data = await apiFetch(URL);
            const users = data.map(user => (
              {
                id: { value: user.id, className: "item-id" },
                fullName: { value: user.full_name, className: "item-field-md" },
                username: { value: user.username, className: "item-field-md" },
                email: { value: user.email, className: "item-field-md" },
                type: { 
                  value: user.type,
                  className: "item-field-md",
                  hasBadge: true,
                  badgeStyle: function () {
                    return this.value ? "bg-primary" : "bg-secondary";
                  },
                },
                active: {
                  value: user.active,
                  strValue: function () {
                    return this.value ? "Activo" : "Inactivo";
                  },
                  className: "item-field-sm", 
                  hasBadge: true,
                  badgeStyle: function () {
                    return this.value ? "bg-success" : "bg-danger";
                  },
                },
                isLogged: { 
                  value: user.is_logged_in,
                  strValue: function () {
                    return this.value ? "Conectado" : "Desconectado";
                  },
                  className: "item-field-sm", 
                  hasBadge: true,
                  badgeStyle: function () {
                    return this.value ? "bg-success" : "bg-danger";
                  },
                },
              }
            ));
            setDataArray(users);
        }
        getData();
    }, []); 

    return (
      <>
        <BaseContent
          title={"Usuarios"}
          titles={TITLES}
          dataArray={dataArray} 
          handleCreate={handleCreate}
          handleView={handleView}
          handleEdit={handleEdit}
          handleDelete={handleDelete}
          canDelete={false}
        />
        <UserCreate />
      </>
    );
};

export default UserContent;