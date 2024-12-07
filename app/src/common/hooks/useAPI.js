import { apiFetch, apiPost } from "@utils/api";

const useAPI = async (url, method, body = {}) => {
  
  let response = {};
  if (method == "POST") {
    return await apiPost(url, body);
  } else {
    response = await apiFetch(url);
  }


  return [response]
};

export default useAPI;