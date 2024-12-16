import { useContext, createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router";

import { apiFetch } from "@utils/api";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const navigate = useNavigate();
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

  useEffect(() => {
    if (authState.authenticated) return;

    const fetchUser = async () => {
      try {
        const URL_PATH = "/auth/profile";
        const response = await apiFetch(URL_PATH);
        if (response) {
          const data = response;
          const user = {
            id: data.id,
            type: data.type,
            username: data.username,
            fullName: data.full_name,
            email: data.email,
            permissions: data.permissions,
            active: data.active,
            authenticated: data.is_logged_in,
          };
          if (JSON.stringify(user) !== JSON.stringify(authState)) {
            setAuthState(user);
            navigate("/dashboard", { replace: true });
          }
        }
      } catch (error) {
        console.log(error);
      }
    };
    fetchUser();
  }, [authState.authenticated]);

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