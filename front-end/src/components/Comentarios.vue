<template>
  <div class="wrapper4">
    <h1 class="text-center">Comentarios</h1>
    <div class="form-group">
      <div class="input-field"> 
        
        <input class="cliente" type="text" v-model="comentarios.idCliente" placeholder="Id del cliente" required>
      </div>
    </div>
    <div class="form-group">
      <div class="text-area"> 
        

        <textarea class="text" v-model="comentarios.comentario" placeholder="comentarios" required>
        </textarea>
      </div>
    </div> 

    <div class="group2">
      <button type="button" class="btn btn-enviar text-center" v-on:click="AddingComentar">enviar</button>
      <button type="button" class="btn btn-enviar text-center" v-on:click="loadComents">Ver comentarios</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "comentarios",
  data: function(){
    return {
      comentarios: {
        idCliente: "",
        comentario: "",
        
      },
    };
  },
  methods: {
    AddingComentar: function() {
      axios
        .post(
          `https://computer-shop-mintic2022.herokuapp.com/comentarios/`,
          this.comentarios,
          { headers: {} }
        )
        .then((coments) => {
          let addComentario = {
            idCliente: this.comentarios.idCliente,
            comentario: this.comentarios.comentario,
           
          };
          this.$emit("addedComentario", addComentario);
          alert("Registro exitoso");

          console.log(coments);
          this.clearForm();
        })
        .catch((error) => {
          console.log(error);
          alert("Error  de ingreso.");
        });
    },

    clearForm: function() {
      this.idCliente = '';
      this.comentario = '';
     
    },

    loadComents: function() {
      this.$router.push({ name: "readComentarios" });
    },
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
form-group{
    padding-top:20px ;
    margin: 20px;
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
.text{
    width: 80%;
}
input{
    size: 10%;
}

</style>