import { useState, useEffect } from "react";
import BaseContent from "../BaseContent/BaseContent";

import { apiFetch, apiDelete } from "@utils/api.js";

const TITLES = [
  "ID",
  "Nombre completo",
  "Nombre de usuario",
  "Correo electrónico",
  "Tipo de usuario",
  "Estado",
  "Sesión",
];

const ProductContent = () => {
    const [dataArray, setDataArray] = useState([]);

    const handleClick = () => {
      console.log("Sisas", dataArray);
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
          if (item.id.value === id) {
            item.active.value = false;
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
        <BaseContent
          title={"Productos"}
          titles={TITLES}
          dataArray={dataArray} 
          handleClick={handleClick}
          handleView={handleView}
          handleEdit={handleEdit}
          handleDelete={handleDelete}
          canDelete={false}
        />
    );
};

export default ProductContent;