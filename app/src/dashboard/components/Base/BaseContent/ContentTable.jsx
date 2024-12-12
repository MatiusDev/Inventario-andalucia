import { useState } from "react";

import BaseButton from './BaseButton';
import BaseButtonToggle from './BaseButtonToggle';

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons"

const ContentTableData = ({ dataArray, titles, handleView, handleEdit, handleDelete, canDelete }) => {
  const [searchTerm, setSearchTerm] = useState(''); 

  const getFieldData = (item) => {
    if (!item.hasBadge && typeof item.value != 'boolean'
      && item.value) {
      return item.value;
    } else if (item.hasBadge && typeof item.value != 'boolean') {
      return (
        <span 
          className={`badge ${item.badgeStyle()}`}>
          {item.value}
        </span>
      )
    } else if (item.hasBadge && typeof item.value == 'boolean') {
      return (
        <span
          className={`badge ${item.badgeStyle()}`}>
          {item.strValue()}
        </span>
      )
    } else {
      return 'No hay datos';
    }
  }

  const filteredUsers = dataArray.filter(item =>
    Object.values(item).some(sItem =>
      sItem.value.toString().toLowerCase().includes(searchTerm.toLowerCase())
    )
  );

  return (
    <>
      <div className="container-fluid">
        <div className="card">
          <div className="card-header bg-white">
            <div className="row align-items-center">
              <div className="col">
                <div className="input-group">
                  {/* <FontAwesomeIcon icon={faMagnifyingGlass} className="input-group-text" /> */}
                  <input
                    type="search"
                    className="form-control search-input"
                    placeholder="Buscar un registro..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                  />
                </div>
              </div>
            </div>
          </div>
          <div className="card-body p-0" style={{ maxHeight: '500px', overflowY: 'auto' }}>
            <div className="table-responsive">
              <table className="table table-hover table-striped mb-0" style={{ minWidth: '800px' }}>
                <thead className="table-light">
                  <tr>
                    { titles &&
                      titles.map((title, idx) => (
                        <th key={titles.length+idx} className="text-center">
                          {title.title}
                        </th>
                      ))
                    }
                    <th className="text-center">Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredUsers.map((item) => {
                      return (
                        <tr key={item.id.value} className="text-center bold">
                          <th 
                            scope="row" 
                            className={item.id.className}
                          >{item.id.value}</th>
                          {Object.values(item).slice(1).map((sItem, idx) => {
                            return (
                              <td key={idx} className={sItem.className}>
                                { getFieldData(sItem) }
                              </td>
                            )
                          })}
                          <th>
                            {canDelete ?
                              <BaseButton
                                id={item.id.value}
                                handleView={handleView}
                                handleEdit={handleEdit}
                                handleDelete={handleDelete}
                              />
                              :
                              <BaseButtonToggle
                                id={item.id.value}
                                active={item.active.value}
                                handleView={handleView}
                                handleEdit={handleEdit}
                                handleDelete={handleDelete}
                              />
                             }
                          </th>
                        </tr>
                      )
                    })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default ContentTableData;