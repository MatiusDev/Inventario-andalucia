import "./ContentForm.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import { faEye,faPenToSquare,faTrash} from "@fortawesome/free-solid-svg-icons";

// import DataTable from 'datatables.net-react';

// import DT from 'datatables.net-dt';

const BaseForm = ({title}) => {
    return (
        <div class="body-form">
            <div class="head">
                <h2>{title}</h2>
            </div>
            <div class="content">
                <table id="example" class="table table-striped" >
                    <caption>
                        {title}
                    </caption>
                    <thead>
                        <tr>
                            <th>Proveedor</th>
                            <th>Producto suministrado</th>
                            <th>Categoría</th>
                            <th>Ubicación</th>
                            <th>Cantidad suministrada</th>
                            <th>Fecha de ingreso</th>
                            <th>Accioones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Plantas del Valle</td>
                            <td>Planta de Ficus</td>
                            <td>Plantas</td>
                            <td>Bogotá</td>
                            <td>120</td>
                            <td>2023-11-10</td>
                            <td>
                                <div class="botones-acciones">
                                    <a class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#">
                                        <FontAwesomeIcon icon={faEye}/>
                                        <i class="fa-solid fa-eye"></i>
                                    </a>
                                    <a class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#">
                                        <FontAwesomeIcon icon={faPenToSquare} />
                                    </a>
                                    <a class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#">
                                        <FontAwesomeIcon icon={faTrash} />
                                    </a>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="actions">
                <button class="btn-add">
                    <i class="fas fa-plus"></i>
                    Crear
                </button>
            </div>
        </div>
    );
};

export default BaseForm;