import { useEffect, useState } from 'react';
import { BrowserRouter } from 'react-router';

import './App.css';

import AppRoutes from '@routes/AppRoutes';
import { AuthProvider } from '@auth/context/AuthProvider';

const App = () => {
  return (
    <div className="app-container">
      <BrowserRouter>
        {/* <AuthProvider> */}
        <AppRoutes />
        {/* </AuthProvider> */}
      </BrowserRouter>
    </div>
  )
};

export default App;