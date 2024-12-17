import { useState, useEffect } from "react";
import BaseContent from "../BaseContent/BaseContent";

// const TITLES = [
//   "ID",
//   "Nombre completo",
//   "Nombre de usuario",
//   "Correo electrónico",
//   "Tipo de usuario",
//   "Estado",
//   "Sesión",
// ];

const OrderContent = () => {
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
      console.log("Eliminar");
    }

    // useEffect(() => {
    // }, []); 

    return (
        <BaseContent
          title={"Ordenes"}
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

export default OrderContent;