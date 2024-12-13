import { useContext, createContext, useState } from "react";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [authState, setAuthState] = useState({
    name: null,
    email: null,
    authenticated: false,
  });

  const changeAuthState = (newState) => {
    setAuthState(newState);
  }

  return (
    <AuthContext.Provider value={{ authState, changeAuthState }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
}