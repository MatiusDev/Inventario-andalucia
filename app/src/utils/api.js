const BASE_URL = import.meta.env.VITE_BASE_URL;

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

export async function apiPost(endpoint, data) {
  const URL = `${BASE_URL}${endpoint}`;
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    credentials: 'include',
    body: JSON.stringify(data),
  };
  const response = await fetch(URL, options); 
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return await response.json();
}

export async function apiDelete(endpoint) {
  const URL = `${BASE_URL}${endpoint}`;
  const options = {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
    credentials: 'include'
  };
  const response = await fetch(URL, options);
  if (!response.ok) {
    throw new Error(response.statusText)
  }
  return await response.json();
}