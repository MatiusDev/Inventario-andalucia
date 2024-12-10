import "./BaseContent.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import {
  faEye,
  faPenToSquare,
  faTrash,
} from "@fortawesome/free-solid-svg-icons";

const ContentTableData = ({ title, dataArray }) => {
  console.log(dataArray);

  let titles = [];
  if (dataArray.length > 0) {
    const reference = dataArray[0];
    titles = Object.keys(reference);
    console.log(titles);
  }

  return (
    <table id="example" className="table table-striped">
          {/* <caption>{title}</caption> */}
          <thead>
            <tr>
              { titles.length > 0 
                  ? titles.map((title, id) => <th key={id}>{title}</th>)
                  : "No hay datos"}
            </tr>
          </thead>
          <tbody>
            {
              dataArray.length > 0
                ? dataArray.map(user => (
                  <tr>
                    <td key={user.ID}>{user.ID}</td>
                    <td key={user.ID}>{user.NombreUsuario}</td>
                    <td key={user.ID}>{user.NombreCompleto}</td>
                    <td key={user.ID}>{user.CorreoElectronico}</td>
                    <td key={user.ID}>{user.TipoDeUsuario}</td>
                    <td key={user.ID}>{user.Estado}</td>
                    <td key={user.ID}>{user.EstaLogueado}</td>
                    <td key={user.ID}>{user.FechaCreacion}</td>
                    <td key={user.ID}>{user.FechaActualizacion}</td>
                    <td key={user.ID}>{user.UltimaSesion}</td>
                  </tr>
                ))
                : "No hay datos"
            }
            
            {/* <tr>
              <td>Macetas S.A.</td>
              <td>Maceta de cerámica 20cm</td>
              <td>Accesorios</td>
              <td>Medellín</td>
              <td>150</td>
              <td>2023-09-15</td>
              <td>
                <div className="botones-acciones">
                  <a
                    className="btn btn-primary"
                    data-bs-toggle="modal"
                    data-bs-target="#"
                  >
                    <FontAwesomeIcon icon={faEye} />
                    <i className="fa-solid fa-eye"></i>
                  </a>
                  <a
                    className="btn btn-warning"
                    data-bs-toggle="modal"
                    data-bs-target="#"
                  >
                    <FontAwesomeIcon icon={faPenToSquare} />
                  </a>
                  <a
                    className="btn btn-danger"
                    data-bs-toggle="modal"
                    data-bs-target="#"
                  >
                    <FontAwesomeIcon icon={faTrash} />
                  </a>
                </div>
              </td>
            </tr>
            <tr>
              <td>Jardines Verde</td>
              <td>Planta de Aloe Vera</td>
              <td>Plantas</td>
              <td>Cali</td>
              <td>200</td>
              <td>2023-08-05</td>
              <td>
                <div className="botones-acciones">
                  <a
                    className="btn btn-primary"
                    data-bs-toggle="modal"
                    data-bs-target="#"
                  >
                    <FontAwesomeIcon icon={faEye} />
                    <i className="fa-solid fa-eye"></i>
                  </a>
                  <a
                    className="btn btn-warning"
                    data-bs-toggle="modal"
                    data-bs-target="#"
                  >
                    <FontAwesomeIcon icon={faPenToSquare} />
                  </a>
                  <a
                    className="btn btn-danger"
                    data-bs-toggle="modal"
                    data-bs-target="#"
                  >
                    <FontAwesomeIcon icon={faTrash} />
                  </a>
                </div>
              </td>
            </tr> */}
          </tbody>
    </table>
  )
};

const ContentTable = ({ title, dataArray, handleClick }) => {
  return (
    <>
      <div className="contenido">
        <ContentTableData title={title} dataArray={dataArray} />
      </div>

      <div className="acciones">
        <button className="btn-agregar" onClick={handleClick}>
          <i className="fas fa-plus"></i>
          Crear
        </button>
      </div>
    </>
  );
};

export default ContentTable;
