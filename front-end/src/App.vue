<template>
  <div id="app" class="app">
    <header>
      <nav class="navbar fixed-top navbar-expand-lg navbar-dark ">
        <div class="container">
          <a class="navbar-brand" href="#">Tienda Computadores</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarText">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">  
                <a class="nav-link active" aria-current="page" v-if="is_auth"  v-on:click="loadHome">Inicio</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" v-if="is_auth" @click="loadCliente">Clientes</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" v-on:click="Product">Agregar productos</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Proveedores</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" v-on:click="loadRV">Registro de Ventas</a>
              </li>
            </ul>
            <ul class="navbar-nav ml-auto">
              <li class="nav-item">
                <a class="nav-link" v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" v-if="!is_auth" @click="loadSignUp">Registrarse</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" v-if="is_auth" @click="logOut">Cerrar Sesión</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
    
    <div class="main-component">
      <router-view  
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
      >
      </router-view>
    </div>
    
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
    loadRV: function() {
      this.$router.push({ name: "registroVentas" });
    },
     Product: function() {
      this.$router.push({ name: "producto" });
    },
    loadCliente: function(){
      this.$router.push({name: "registroClientes"})
    },
    loadProducts: function() {
      this.$router.push({ name: "readProducts" });
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
  
  .navbar{
  width: 100%;
  margin-bottom: 30px;
  font-size: 17px;
  background: #05021f;
}

.navbar-brand{
  font-size: 23px;
}
  .main-component{
    height: 75vh;
    margin: 0%;
    padding: 0%;
    background: #FDFEFE;
  }
 
  .footer {
    position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   background-color: #05021f;
   color: white;
   text-align: center;
}
.footer h2{
  color: #fff;
  font-size: 30px;
  }
</style>