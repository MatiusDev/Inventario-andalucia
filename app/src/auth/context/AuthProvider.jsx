import { useContext, createContext, useState } from "react";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [authState, setAuthState] = useState({
    username: "",
    fullName: "",
    email: "",
    id: 0,
    type: "",
    permissions: [],
    active: false,
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