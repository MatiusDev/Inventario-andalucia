const BASE_URL = import.meta.env.VITE_BASE_URL; //http://localhost:8000/api

export async function apiFetch(endpoint, options = {}) {
  const URL = `${BASE_URL}${endpoint}`;
  const fetchOptions = {
    ...options,
    headers: {
      'Content-Type': 'application/json'
    },
    credentials: 'include',
  }
  const response = await fetch(URL, fetchOptions);

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  return await response.json();
}

// ${BASE_URL} => http://localhost:8000/api
// ${endpoint} => /auth/login/
// const URL => http://localhost:8000/api/auth/login/
export async function apiPost(endpoint, data) {
  const URL = `${BASE_URL}${endpoint}`;
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    credentials: 'include',
    body: JSON.stringify(data), //Data = { username: "matiusdev", password: "12345" }
    // "{ "username": "matiusdev", "password": "12345" }"
  };
  const response = await fetch(URL, options); 
  console.log(response);
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  const json_response = await response.json();
  console.log(json_response);
  return json_response;
}