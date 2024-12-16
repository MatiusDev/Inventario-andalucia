import { Routes, Route, Navigate } from "react-router";

import AuthRoute from "./AuthRoutes.jsx";
import DefaultRoute from "./DefaultRoute.jsx";

import Auth from '@/auth/components/Auth/Auth.jsx';
import { useAuth } from "@auth/context/AuthProvider.jsx";
import Dashboard from '@/dashboard/components/Dashboard.jsx';

const AppRoutes = () => {
  const { authState } = useAuth();

  return (
    <Routes>
      <Route index element={<Auth />} />

      <Route path="dashboard" element={<AuthRoute isAuthenticated={authState.authenticated} />}>
        <Route index element={<Dashboard />} />
      </Route>

      <Route path="*" element={<DefaultRoute isAuthenticated={authState.authenticated} />} />
    </Routes>
  );
};

export default AppRoutes;