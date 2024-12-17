import { apiFetch, apiDelete } from "@utils/api.js";

const ROOT_URL = '/users';

const getUsers = async () => {
  const URL = `${ROOT_URL}/`;
  const response = await apiFetch(URL);

  if (response.status !== "success") {
    throw new Error("Error al obtener los usuarios");
  }
  const { data } = response;
  return data;
};


const deleteUser = async (id) => {
  const URL = `${ROOT_URL}/${id}/`;
  const response = await apiDelete(URL);
  if (response.status !== "success") {
    throw new Error("Error al eliminar el usuario");
  }
};

export { getUsers, deleteUser };