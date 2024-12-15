import { useState, useEffect } from "react";
import BaseContent from "../BaseContent/BaseContent";

import { apiFetch, apiDelete } from "@utils/api.js";

const PlantContent = () => {
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
      const URL = `/plants/${id}/`;
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
        console.log("Error al eliminar las plantas");
      }
    }

    useEffect(() => {
        const getData = async () => {
            const URL = "/plants/";
            const data = await apiFetch(URL);
            const titles = [
              { id: `item-1`, title: "ID"},
              { id: `item-2`, title: "Nombre cientifico"},
              { id: `item-3`, title: "Temperatura ideal"},
              { id: `item-4`, title: "Tipo Id"},
              { id: `item-5`, title: "identificación de riego requerida"},
              { id: `item-6`, title: "identificación de luz requerida"},
            ];
            const plants = data.map(plant => (
              {
                id: { value: plant.id, className: "item-id" },
                scientific_name: { value: plant.scientific_name, className: "item-field-md" },
                ideal_temperature: { value: plant.ideal_temperature, className: "item-field-md" },
                type_id: { value: plant.type_id, className: "item-field-md" },
                required_irrigation_id: { value: plant.required_irrigation_id, className: "item-field-md" },
                required_light_id: { value: plant.required_light_id, className: "item-field-md" },
                type: { 
                  value: plant.type,
                  className: "item-field-md",
                  hasBadge: true,
                  badgeStyle: function () {
                    return this.value ? "bg-primary" : "bg-secondary";
                  },
                },
                active: {
                  value: plant.active,
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
                  value: plant.is_logged_in,
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
            setDataArray(plants);
        }
        getData();
    }, []); 

    return (
        <BaseContent
          title={"Plantas"}
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

export default PlantContent;