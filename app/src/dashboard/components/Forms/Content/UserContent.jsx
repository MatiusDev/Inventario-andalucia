import { useState, useEffect } from "react";
import BaseContent from "../BaseContent/BaseContent";
import { apiFetch } from "@utils/api.js";

const response = {
    data: [
      {
        username: "matiusdev",
        full_name: "string",
        email: "string",
        id: 1,
        type: "Administrador",
        permissions: [
          "READ",
          "EDIT",
          "DELETE"
        ],
        active: true,
        is_logged_in: true,
        created_at: "2024-12-09T19:46:28",
        updated_at: "2024-12-09T19:46:28",
        last_session: "2024-12-10T03:08:18"
      },
      {
        username: "prueba1",
        full_name: "Pruebas",
        email: "string1@pruebas.com",
        id: 2,
        type: "Usuario",
        permissions: [
          "READ"
        ],
        active: true,
        is_logged_in: false,
        created_at: "2024-12-10T03:07:43",
        updated_at: "2024-12-10T03:07:43",
        last_session: "2024-12-10T03:07:43"
      },
      {
        username: "prueba2",
        full_name: "Pruebas",
        email: "string2@pruebas.com",
        id: 3,
        type: "Usuario",
        permissions: [
          "READ"
        ],
        active: true,
        is_logged_in: false,
        created_at: "2024-12-10T03:07:51",
        updated_at: "2024-12-10T03:07:51",
        last_session: "2024-12-10T03:07:51"
      },
      {
        username: "prueba3",
        full_name: "Pruebas",
        email: "string3@pruebas.com",
        id: 4,
        type: "Usuario",
        permissions: [
          "READ"
        ],
        active: true,
        is_logged_in: false,
        created_at: "2024-12-10T03:07:56",
        updated_at: "2024-12-10T03:07:56",
        last_session: "2024-12-10T03:07:56"
      },
      {
        username: "prueba4",
        full_name: "Pruebas",
        email: "string4@pruebas.com",
        id: 5,
        type: "Usuario",
        permissions: [
          "READ"
        ],
        active: true,
        is_logged_in: false,
        created_at: "2024-12-10T03:08:01",
        updated_at: "2024-12-10T03:08:01",
        last_session: "2024-12-10T03:08:01"
      }
    ],
    status: "success"
  }
  
const UserContent = () => {
    const [dataArray, setDataArray] = useState([]);

    const handleClick = () => {
      console.log("Sisas");
    };

    useEffect(() => {
        // const getData = async () => {
        //     const URL = "/users/";
        //     const data = await apiFetch(URL);
        //     setDataArray(data);
        // }
        // getData();
        // setDataArray(response.data);
        const data = response.data;
        const data_filtered = data.map((user) => {
            return {
                ID: user.id,
                NombreUsuario: user.username,
                NombreCompleto: user.full_name,
                CorreoElectronico: user.email,
                TipoDeUsuario: user.type,
                Estado: user.active,
                EstaLogueado: user.is_logged_in,
                FechaCreacion: user.created_at,
                FechaActualizacion: user.updated_at,
                UltimaSesion: user.last_session
            }
        } );
        setDataArray(data_filtered);
    }, []);

    return (
        <BaseContent
          title={"Usuarios"}
          dataArray={dataArray} 
          handleClick={handleClick} 
        />
    );
};

export default UserContent;