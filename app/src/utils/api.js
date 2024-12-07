const BASE_URL = import.meta.env.VITE_BASE_URL; //http://localhost:8000/api



export async function apiFetch(endpoint, options = {}) {
  const URL = `${BASE_URL}${endpoint}`;
  const response = await fetch(URL, options);

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  return await response.json();
}

export async function apiPost(endpoint, data) {
  //http://localhost:8000/api/auth/login/
  const URL = `${BASE_URL}${endpoint}`;
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data), //Data = { username: "matiusdev", password: "12345" }
    // "{ "username": "matiusdev", "password": "12345" }"
  };
  const response = await fetch(URL, options); 
  return await response.json();
}