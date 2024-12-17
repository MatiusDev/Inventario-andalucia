import { useContext, createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router";

import { getProfile } from "@auth/services/auth.service";

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
    if (authState && authState.authenticated) return;

    const fetchUser = async () => {
      try {
        const data = await getProfile();
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
      } catch (error) {
        // console.log("here in error", error);
        return;
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