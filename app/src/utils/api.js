const BASE_URL = import.meta.env.VITE_BASE_URL;
console.log(BASE_URL);

export async function apiFetch(endpoint, options = {}) {
  const URL = `${BASE_URL}${endpoint}`;
  console.log(URL);
  const response = await fetch(URL, options);

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  return await response.json();
}