import { BrowserRouter } from 'react-router';

import './App.css';

import AppRoutes from '@routes/AppRoutes';

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