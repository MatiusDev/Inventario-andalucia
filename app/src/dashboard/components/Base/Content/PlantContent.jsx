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
              { id: `item-2`, title: "Categoria"},
              { id: `item-3`, title: "Material"},
              { id: `item-4`, title: "Marca"},
              { id: `item-5`, title: "Tipo de mantenimiento"},
              { id: `item-6`, title: "Id producto"},
            ];
            const tools = data.map(tool => (
              {
                id: { value: tool.id, className: "item-id" },
                category: { value: tool.category, className: "item-field-md" },
                material: { value: tool.material, className: "item-field-md" },
                brand: { value: tool.brand, className: "item-field-md" },
                type_maintenance: { value: tool.type_maintenance, className: "item-field-md" },
                id_product: { value: tool.id_product, className: "item-field-md" },
                type: { 
                  value: tool.type,
                  className: "item-field-md",
                  hasBadge: true,
                  badgeStyle: function () {
                    return this.value ? "bg-primary" : "bg-secondary";
                  },
                },
                active: {
                  value: tool.active,
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
                  value: tool.is_logged_in,
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
            setDataArray(tools);
        }
        getData();
    }, []); 

    return (
        <BaseContent
          title={"Herramientas"}
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

export default ToolContent;