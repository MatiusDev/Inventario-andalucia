import { Routes, Route } from "react-router";

import Login from '@/auth/components/Login.jsx';
import Inventory from '@/inventory/components/Inventory.jsx';
import AuthRoute from "./AuthRoutes";

const AppRoutes = () => {
  return (
    <Routes>
      <Route index element={<Login />} />

      <Route element={
          <AuthRoute isAuthenticated={true}>
            <Route path="/inventory" element={<Inventory />} />
            
          </AuthRoute>
        }
      />
    </Routes>
  );
};

export default AppRoutes;