import { useEffect, useState } from 'react';
import { BrowserRouter } from 'react-router';

import './App.css';

import AppRoutes from '../routes/AppRoutes';

import { apiFetch } from '@utils/api.js';

// import Auth from '@/auth/components/Auth/Auth';

import BarraLateral from '@/dashboard/components/BarraLateral/BarraLateral';


function App() {
  // const [count, setCount] = useState(0);
  const [data, setData] = useState(null);
  // const [error, setError] = useState("");

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
      <div className="app-container">
        <BrowserRouter>
          <AppRoutes />
        </BrowserRouter>
      </div>
    </>
  )
};

export default App;