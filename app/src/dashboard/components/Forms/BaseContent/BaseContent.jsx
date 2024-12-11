import "./BaseContent.css"

import ContentTable from "./ContentTable";

const BaseContent = ({ title, dataArray, handleClick }) => {
    return (
        <div className="contenedor">
            <div className="cabecera">
                <h2>{title}</h2>
            </div>
            <ContentTable title={title} dataArray={dataArray} handleClick={handleClick} />
        </div>
    );
};

export default BaseContent;