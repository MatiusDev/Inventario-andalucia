import { useEffect, useState } from 'react';

import styles from './App.module.css';

import Login from '@/auth/components/Login.jsx';


import { apiFetch } from '@utils/api.js';

function App() {
  const [count, setCount] = useState(0);
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const URL = '/products/';
        const data = await apiFetch(URL);
        setData(data);
      } catch (error) {
        setError(error.message);
      }
    }
    fetchData();
  }, []);

  return (
    <>
      {/* <div className={styles.container}>
        <h1>Vite + React</h1>
        <div className={styles.card}>
          <button onClick={() => setCount((count) => count + 1)}>
            count is {count}
          </button>
        </div>
        <p className={styles.readTheDocs}>
          Click on the Vite and React logos to learn more
        </p>
      </div> */}
      <div className={styles.container_login}>
        <Login />
      </div>
    </>
  )
};

export default App;
