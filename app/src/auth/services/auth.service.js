import { apiFetch, apiPost, apiDelete } from "@utils/api.js";

const ROOT_URL = '/auth';

const login = async (userData) => {
  const URL = `${ROOT_URL}/login`;
  const response = await apiPost(URL, userData);
  if (response.status !== "success") {
    throw new Error("Error al iniciar sesión");
  }
  const { message } = response;
  return message;
};

const getProfile = async () => {
  const URL = `${ROOT_URL}/profile`;
  const response = await apiFetch(URL);
  if (response.status !== "success") {
    throw new Error("Error al obtener la información del perfil");
  }
  const { data } = response;
  return data;
}


const logout = async (id) => {
  const URL = `${ROOT_URL}/${id}/`;
  const response = await apiDelete(URL);
  if (response.status !== "success") {
    throw new Error("Error al eliminar el producto");
  }
};

export { login, logout, getProfile };