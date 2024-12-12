import { useState, useEffect } from "react";
import BaseContent from "../BaseContent/BaseContent";

const SupplierContent = () => {
    const [dataArray, setDataArray] = useState([]);

    const handleClick = () => {
      console.log("Sisas");
    };

    // useEffect(() => {
    //   console.log("Melo");
    // });

    return (
        <BaseContent
          title={"Proveedores"}
          dataArray={dataArray} 
          handleClick={handleClick} 
        />
    );
};

export default SupplierContent;