import { useState, useEffect } from "react";
import BaseContent from "../BaseContent/BaseContent";

import { getProducts } from "@/product/services/product.service.js";

const TITLES = [
  "ID",
  "Nombre",
  "Tipo de producto",
  "Descripción",
  "Stock",
  "Stock minimo",
  "Precio",
  "Ubicación",
  "Estado",
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
      console.log("Eliminar");
    }

    useEffect(() => {
        const getData = async () => {
            const data = await getProducts();
            const products = data.map(product => (
              {
                id: { value: product.id, className: "item-id" },
                name: { value: product.name, className: "item-field-md" },
                type: { 
                  value: product.type,
                  className: "item-field-md",
                  hasBadge: true,
                  badgeStyle: function () {
                    return this.value === "Planta" 
                      ? "bg-success" : this.value === "Insumo" 
                      ? "bg-warning" : "bg-info";
                  },
                },
                description: { value: product.description, className: "item-field-md" },
                stock: { value: product.stock, className: "item-field-sm" },
                stockMinium: { value: product.stock_minimum, className: "item-field-sm" },
                price: { value: product.price, className: "item-field-sm" },
                location: { value: product.location, className: "item-field-md" },
                active: {
                  value: product.active,
                  strValue: function () {
                    return this.value ? "Activo" : "Inactivo";
                  },
                  className: "item-field-sm", 
                  hasBadge: true,
                  badgeStyle: function () {
                    return this.value ? "bg-success" : "bg-danger";
                  },
                },
              }
            ));
            setDataArray(products);
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