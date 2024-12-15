import { useState, useEffect } from "react";
import BaseContent from "../BaseContent/BaseContent";

import { apiFetch, apiDelete } from "@utils/api.js";

const InputContent = () => {
    const [dataArray, setDataArray] = useState([]);
    const [titles, setTitles] = useState([]);

    const handleCreate = () => {
      console.log("Sisas", dataArray);
    };

    const handleView = (id) => {
      console.log("Ver", id);
    };

    const handleEdit = (id) => {
      console.log("Editar", id);
    };

    const handleDelete = async (id) => {
      const URL = `/inputs/${id}/`;
      const response = await apiDelete(URL);
      if (response.status === "success") {
        const dataMapped = dataArray.map(({item}) => {
          if (item.id.value === id) {
            item.active.value = false;
            return item;
          }
          return item;
        });
        setDataArray(dataMapped);
      } else {
        console.log("Error al eliminar los insumos");
      }
    }

    useEffect(() => {
        const getData = async () => {
            const URL = "/inputs/";
            const data = await apiFetch(URL);
            const titles = [
              { id: `item-1`, title: "ID"},
              { id: `item-2`, title: "Nombre"},
              { id: `item-3`, title: "cantidad"},
              { id: `item-4`, title: "Unidad"},
              { id: `item-5`, title: "Precio"},
              { id: `item-6`, title: "Ubicación"},
            ];
            const inputs = data.map(input => (
              {
                id: { value: input.id, className: "item-id" },
                name: { value: input.scientific_name, className: "item-field-md" },
                quantity: { value: input.ideal_temperature, className: "item-field-md" },
                unit: { value: input.type_id, className: "item-field-md" },
                price: { value: input.required_irrigation_id, className: "item-field-md" },
                location: { value: input.required_light_id, className: "item-field-md" },
                type: { 
                  value: input.type,
                  className: "item-field-md",
                  hasBadge: true,
                  badgeStyle: function () {
                    return this.value ? "bg-primary" : "bg-secondary";
                  },
                },
                active: {
                  value: input.active,
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
                  value: input.is_logged_in,
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
            setTitles(titles);
            setDataArray(inputs);
        }
        getData();
    }, []); 

    return (
        <BaseContent
          title={"Insumos"}
          titles={titles}
          dataArray={dataArray} 
          handleClick={handleCreate}
          handleView={handleView}
          handleEdit={handleEdit}
          handleDelete={handleDelete}
          canDelete={false}
        />
    );
};

export default InputContent;