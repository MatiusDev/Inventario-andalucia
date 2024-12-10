import { useContext, useState } from "react";
import { Routes, Route } from "react-router";

import AuthRoute from "./AuthRoutes.jsx";
import DefaultRoute from "./DefaultRoute.jsx";

import Auth from '@/auth/components/Auth/Auth.jsx';
// import { AuthContext } from "./AuthProvider.jsx";
import Dashboard from '@/dashboard/components/Dashboard.jsx';

const AppRoutes = () => {
  // const { user } = useContext(AuthContext);
  const [isAuthenticated, setIsAuthenticated] = useState(true);

  // if (user) {
  //   setIsAuthenticated(true);
  // }

  return (
    <Routes>
      <Route index element={<Auth />} />

      <Route path="dashboard" element={<AuthRoute isAuthenticated={isAuthenticated} />}>
        <Route index element={<Dashboard />} />
        
      </Route>

      <Route path="*" element={<DefaultRoute isAuthenticated={isAuthenticated} />} />
    </Routes>
  );
};

export default AppRoutes;