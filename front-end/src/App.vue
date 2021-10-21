<template>
<div id="app" class="app">
<header>
  <nav class="navbar navbar-expand-lg navbar-dark">
    <div class="container">
      <router-link to="/" class="navbar-brand">Tienda Computadores</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <div class="navbar-nav me-auto mb-2 mb-lg-0">
          <router-link to="/" class="nav-item nav-link">Inicio</router-link>
          <router-link to="/" class="nav-item nav-link">Productos</router-link>
          <router-link to="/" class="nav-item nav-link">Agregar productos</router-link>
          <router-link to="/" class="nav-item nav-link">Proveedores</router-link>
        </div>
        <div class="navbar-nav ml-auto">
          <router-link to="/user/logIn" class="nav-item nav-link">Iniciar sesión</router-link>
        </div>
      </div>
    </div>
  </nav>
</header>

<footer class="footer">
      <div class="container">
        <h2 class="text-center">Grupo 7 - P50</h2>
      </div>
    </footer>
</div>
</template>

<script>
export default {
  name: 'App',

  data: function(){
      return{
        is_auth: false
      }
  },

  components: {
  },

  methods:{
    verifyAuth: function() {
      this.is_auth = localStorage.getItem("isAuth") || false;
		
			if (this.is_auth == false)
        this.$router.push({ name: "logIn" });
      else
        this.$router.push({ name: "home" });
    },

    loadLogIn: function(){
      this.$router.push({name: "logIn"})
    },

    loadSignUp: function(){
      this.$router.push({name: "signUp"})
    },

    completedLogIn: function(data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },


    completedSignUp: function(data) {
			alert("Registro Exitoso");
			this.completedLogIn(data);
    },
    loadHome: function() {
      this.$router.push({ name: "home" });
    },

    loadAccount: function () {
			this.$router.push({ name: "account" });
		},

    logOut: function () {
			localStorage.clear();
			alert("Sesión Cerrada");
			this.verifyAuth();
		},

  },

  created: function(){
    this.verifyAuth()
  }

}
</script>






<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:ital,wght@0,700;1,300&display=swap');

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  background: #F5F5F5;
  height: 100vh;
  font-family: 'Open Sans Condensed', sans-serif;
}

.navbar{
  width: 100%;
  margin-bottom: 30px;
  font-size: 20px;
  background: #05021f;
}
.navbar-brand{
  font-size: 25px;
}
 
  .footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: auto !important;
    background-color: #090622;
}

.footer h2{
  color: #fff;
  font-size: 30px;
  }
</style>
