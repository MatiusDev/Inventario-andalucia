import { apiFetch, apiDelete } from "@utils/api.js";

const ROOT_URL = '/products';

const getProducts = async () => {
  const URL = `${ROOT_URL}/`;
  const response = await apiFetch(URL);

  if (response.status !== "success") {
    throw new Error("Error al obtener los productos");
  }
  const { data } = response;
  return data;
};


const deleteProduct = async (id) => {
  const URL = `${ROOT_URL}/${id}/`;
  const response = await apiDelete(URL);
  if (response.status !== "success") {
    throw new Error("Error al eliminar el producto");
  }
};

export { getProducts, deleteProduct };