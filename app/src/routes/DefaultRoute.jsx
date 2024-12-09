import { Navigate } from 'react-router';

import NotFound from '@/common/components/NotFound.jsx';

const DefaultRoute = ({ isAuthenticated }) => {
  return isAuthenticated ? <NotFound /> : <Navigate to="/" />;
};

export default DefaultRoute;