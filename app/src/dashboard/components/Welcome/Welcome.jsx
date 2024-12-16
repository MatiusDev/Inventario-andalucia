import "./Welcome.css";

import { useAuth } from "@auth/context/AuthProvider";

import image from "@/assets/fondo3.jpg";

const Welcome = () => {
    const { authState } = useAuth();

    return(
        <div className="container">
            <h2>Bienvenido {authState.fullName}</h2>
            <hr />
        </div>
    );
}

export default Welcome;