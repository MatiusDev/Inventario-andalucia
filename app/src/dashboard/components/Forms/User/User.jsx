import "./User.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import { faEye,faPenToSquare,faTrash} from "@fortawesome/free-solid-svg-icons";

// import DataTable from 'datatables.net-react';

// import DT from 'datatables.net-dt';

const User = () => {
    return (
        <div class="contenedor">
            <div class="cabecera">
                <h2>Proveedores</h2>
            </div>
            <div class="contenido">
                <table id="example" class="table table-striped" >
                    <caption>
                        Proveedores
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
                        <tr>
                            <td>Macetas S.A.</td>
                            <td>Maceta de cerámica 20cm</td>
                            <td>Accesorios</td>
                            <td>Medellín</td>
                            <td>150</td>
                            <td>2023-09-15</td>
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
                        <tr>
                            <td>Jardines Verde</td>
                            <td>Planta de Aloe Vera</td>
                            <td>Plantas</td>
                            <td>Cali</td>
                            <td>200</td>
                            <td>2023-08-05</td>
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

            <div class="acciones">
                <button class="btn-agregar">
                    <i class="fas fa-plus"></i>
                    Crear
                </button>
            </div>
        </div>
    );
};

export default User;