import { Navigate, Outlet } from 'react-router';

const AuthRoute = ({ isAuthenticated }) => {
  return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
};

export default AuthRoute;