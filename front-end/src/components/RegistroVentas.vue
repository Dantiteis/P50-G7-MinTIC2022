<template>
    <div class="wrapper2">
                    <h1 class="login text-center">Registro de Venta</h1>
                    <form>
                        <div class="form-group">
                          <label for="exampleInputEmail1">Nombre del cliente</label>
                          <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="ingrese el id del cliente">
                          <small id="emailHelp" class="form-text text-muted">nombre sin rellenar</small>
                        </div>
                        <div class="form-group">
                          <label for="exampleInputPassword1">Nombre del producto</label>
                          <input type="text" class="form-control" id="exampleInputPassword1" placeholder="ingrese el id del producto">
                        </div>
                        <div class="form-group">
                            <label for="exampleInputPassword1">Cantidad</label>
                            <input type="number" class="form-control" id="exampleInputPassword1" placeholder="ingrese la cantidad">
                        </div>
                        <div class="form-group">
                            <label for="exampleInputPassword1">fecha</label>
                            <input type="date" class="form-control" id="exampleInputPassword1" placeholder="ingrese el Producto">
                        </div>
                        <!--<div class="form-check">
                          <input type="checkbox" class="form-check-input" id="exampleCheck1">
                          <label class="form-check-label" for="exampleCheck1">Check me out</label>
                        </div>-->
                        <button type="submit" class="btn btn-block text-center">Registrar Venta</button>
                      </form>
        </div>
</template>

<script>

export default {
    name: "RegistroVentas",
    data: function(){
        return {
            username: localStorage.getItem('username') || "none"
        }
    },
    methods: {
        processShopRegister: function(){
            axios.post(
                "https://computer-shop-mintic2022.herokuapp.com/registro_ventas", 
                this.registro_ventas,  
                {headers: {}}
                )
                .then((result) => {
                    let dataLogIn = {
                        username: this.registro_ventas.idCliente,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    
                    this.$emit('completedLogIn', dataLogIn)
                })
                .catch((error) => {
                    
                    if (error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas.");
                    
                });
        }
    }
}

</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Hind:wght@300&family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Kaushan+Script&family=Poppins&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');

.wrapper2 {
  font-family:'Hind', sans-serif;
  max-width: 700px;
  border-radius: 10px;
  margin: auto !important;
  margin-top: 80px !important;
  padding: 30px 40px;
  border: 3px solid #05021f;
}

.input-field{
  border-radius: 5px;
  padding: 8px;
  display: flex;
  align-items: center;
  cursor: pointer;
  margin-bottom: 20px;
  color: #05021f;
  font-size: 17px;
  background: #F5F5F5;
  border: 1px solid #05021f;
}

.input-field:hover {
      color: #7E91C0;
      font-size: 17px;
      border: 1px solid #7E91C0	
  }

  input {

    border: none;
    outline: none;
    box-shadow: none;
    width: 100%;
    padding: 0px 2px;
    background: #F5F5F5;
    font-size: 20px;
    font-family: 'Poppins', sans-serif
}

.btn.btn-block {
  width: auto;
  margin-top: 10px;
  margin-left: 50%;
  transform: translateX(-50%);
  flex-direction: column;
  display: flex;
  justify-content: center;
  border-radius: 20px;
  background-color: #05021f;
  color: #fff;
  font-size: 20px;
}

  .btn.btn-block:hover {
      background-color: #7E91C0;
  }
     
.login{
  color: #05021f;
  text-align: center;
  font-size: 45px !important;
  font-family: 'Anton', sans-serif;
}
</style>