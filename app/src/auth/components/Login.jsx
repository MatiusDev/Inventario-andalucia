import styles from "./Login.module.css";

const {
  container_form,
  information,
  info_childs,
  form_information,
  form_information_childs,
  button_container,
  button: styleButton,
  check: styleCheck,
  enlaces_autenticacion,
  button_login,
} = styles;

const Login = () => {
  return (
    <>
      <div className={container_form}>
        <div className={information}>
          <div className={info_childs}>
            <img src="" alt="" />
            <h2>Vivero Andalucia</h2>
          </div>
        </div>
        <div className={form_information}>
          <div className={form_information_childs}>
            <h2>Inicia Sesión</h2>
            <form id="loginForm">
              <div className={button_container}>
                <div className={styleButton}>
                  <span className={styles.icon}></span>
                  <i className={[styles.faSolid, styles.faUser]}></i>
                  <input type="text" placeholder="Usuario" />
                </div>
                <div className={styleButton}>
                  <span className={styles.icon}></span>
                  <i className={[styles.faSolid, styles.faLock]}></i>
                  <input type="password" placeholder="Contraseña" />
                </div>
                <div className={styleCheck}>
                  <input type="checkbox" id="remember-me" />
                  <label for="remember-me">Recordarme</label>
                </div>
                <div>
                  <span className={styles.icon}></span>
                  <button className={button_login} type="submit">
                    Iniciar Sesión
                  </button>
                </div>
                <div className={enlaces_autenticacion}>
                  <a href="">Recuperar Contraseña</a>
                  <a href="">Registrarse</a>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default Login;
