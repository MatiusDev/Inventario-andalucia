import { BrowserRouter } from "react-router";

import "./App.css";

import AppRoutes from "@routes/AppRoutes";
import { AuthProvider } from "@auth/context/AuthProvider.jsx";
import { ThemeProvider } from "@/dashboard/context/ThemeContext.jsx";

const App = () => {
  return (
    <div className="app-container">
      <BrowserRouter>
        <AuthProvider>
          <ThemeProvider>
            <AppRoutes />
          </ThemeProvider>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
};

export default App;
