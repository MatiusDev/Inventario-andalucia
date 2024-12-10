import { useEffect, useState } from 'react';
import { BrowserRouter } from 'react-router';

import './App.css';

import AppRoutes from '@routes/AppRoutes';

import { apiFetch } from '@utils/api.js';

function App() {
  // const [count, setCount] = useState(0);
  const [data, setData] = useState(null);
  // const [error, setError] = useState("");

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