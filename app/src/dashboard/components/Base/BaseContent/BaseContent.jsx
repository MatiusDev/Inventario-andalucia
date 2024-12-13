import "./BaseContent.css"

import ContentTable from "./ContentTable";

const BaseContent = ({ titles, title, dataArray, handleCreate, handleView, handleEdit, handleDelete, canDelete }) => {
    return (
        <div className="contenedor">
            <div className="cabecera">
                <h2>{title}</h2>
            </div>
            <div className="contenido">
                <ContentTable
                    dataArray={dataArray}
                    titles={titles}
                    handleView={handleView}
                    handleEdit={handleEdit}
                    handleDelete={handleDelete}
                    canDelete={canDelete}
                />
            </div>

            <div className="acciones">
                <button 
                    className="btn-agregar"
                    onClick={handleCreate}
                >
                <i className="fas fa-plus"></i>
                Crear
                </button>
            </div>
        </div>
    );
};

export default BaseContent;