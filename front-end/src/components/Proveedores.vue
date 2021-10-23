<template>
  <div class="wrapper4" >
    <h1 class="text-center">Formulario Registro Proveedores</h1>
    <!--<form v-on:submit.prevent="addProveedores" >-->
      <div class="form-group">
        <div class="input-field">
          <input type=number placeholder="ID del proveedor"  v-model="proveedor.id" required>
        </div>
      </div>
      <div class="form-group">
        <div class="input-field">
          <input type="text"  placeholder="Razón social" v-model="proveedor.razon_social" required>
        </div>
      </div>
      <div class="form-group">
        <div class="input-field">
          <input type="text" placeholder="E-mail" v-model="proveedor.correo_e" required>
        </div>
      </div>
      <div class="form-group">
        <div class="input-field">
          <input type="text" placeholder="telefono" v-model="proveedor.numero_telefono" required>
        </div>
      </div>
      <div class="form-group">
        <div class="input-field">
          <input type="text" placeholder="direccion" v-model="proveedor.direccion" required>
        </div>
      </div>
      <div class="group2">
        <button class="btn btn-enviar text-center" v-on:click="addingProveedores" type="button"> Agregar proveedor </button>
        <button class="btn btn-enviar text-center"  v-on:click="getproveedor" type="button"> Ver Proveedores  </button>
        <button class="btn btn-enviar text-center" v-on:click="updateproveedor"    type="button" >  Editar proveedor</button>
        <button class="btn btn-enviar text-center"  v-on:click="deleteproveedor" type="button"> Eliminar   </button>
      </div>
    <!--</form>-->
  </div>   

</template>

<script>
import axios from 'axios';


export default {
    name:"proveedor",
    data: function() {
        return { proveedor:{
            
            id: Number(),
            razon_social:"",
            correo_e:"",
            numero_telefono:"",
            direccion:""

        },
     };        
    },

methods:{
    addingProveedores: function(){
axios.post(
    'https://computer-shop-mintic2022.herokuapp.com/proveedores/',
    this.proveedor,
    { Headers:{} }
    ).then((result) => {
        let addProveedores={

            id:this.proveedor.id,
            razon_social:this.proveedor.razon_social,
            correo_e:this.proveedor.correo_e,
            numero_telefono:this.proveedor.numero_telefono,
            direccion:this.proveedor.direccion,

    };
                this.$emit("addedProveedores", addProveedores);
                alert("El proveedor fue registrado de manera exitosa");

                console.log(result);
                this.clearForm();
                           
            })
            .catch((error) => {
                console.log(error)
                alert("Error en el registro."); 
 });
},
    
    updateproveedor() {
      let idproveedor = this.proveedor.id;
      if (idproveedor != null) {
      }
      axios
        .put(
          `https://computer-shop-mintic2022.herokuapp.com/proveedores/${idproveedor}`,
          this.proveedor
        )
        .then((result) => {
          let editproveedor = {

            id:this.proveedor.id,
            razon_social:this.proveedor.razon_social,
            correo_e:this.proveedor.correo_e,
            numero_telefono:this.proveedor.numero_telefono,
            direccion:this.proveedor.direccion,

          };
          this.$emit("editproveedor", editproveedor);
          console.log(result);
        })
        .catch((error) => {
          console.log(error);
          alert("No se puede actualizar el registro");
        });
    },

    deleteproveedor() {
      let idproveedor = this.proveedor.id;
      
      axios
        .delete(
          `https://computer-shop-mintic2022.herokuapp.com/proveedores/${idproveedor}`,
          this.proveedor
        )
        .then((result) => {
          this.proveedor = result;
          console.log(result);
          alert("El registro fue eliminado de manera exitosa");
        })
        .catch((error) => {
          console.log(error.result);
          alert("El registro no pudo ser eliminado");
        });
},
getproveedor() {
      let idproveedor = this.proveedor.id;
      axios
        .get(
          `https://computer-shop-mintic2022.herokuapp.com/proveedores/${idproveedor}`
        )

        .then((proveedor) => {
          this.proveedor = proveedor.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Error  al momento de leer el registro");
        });
        
    
},

        clearForm: function() {
            id:this.proveedor.id;
            razon_social:this.proveedor.razon_social;
            correo_e:this.proveedor.correo_e;
            numero_telefono:this.proveedor.numero_telefono;
            direccion:this.proveedor.direccion;
      
    }

    }








}

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Hind:wght@300&family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Kaushan+Script&family=Poppins&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');
.wrapper4 {
  font-family:'Hind', sans-serif;
  max-width: 700px;
  border-radius: 10px;
  height: auto;
  margin: auto !important;
  margin-top: 80px !important;
  padding: 30px 40px;
  border: 3px solid #05021f;
}

label{
  font-size: 20px;
  padding: 0px 2px;
  font-family: 'Poppins', sans-serif
}
.group2{
  width: 600px;
    margin-left: 50%;
    border-radius: 20px;
    transform: translateX(-50%);
    flex-direction: row;
    display: flex;
    margin-top: 15px;
    margin-bottom: -10px !important;
  justify-content: center;
}

</style>