import { Navigate, Outlet } from 'react-router';

const AuthRoute = ({ isAuthenticated }) => {
  return isAuthenticated ? <Outlet /> : <Navigate to="/" />;
};

export default AuthRoute;