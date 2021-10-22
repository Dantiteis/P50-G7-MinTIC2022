import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';
 
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import RegistroVentas from './components/RegistroVentas.vue'
import Productos from "./components/Productos.vue";
import readProductos from "./components/readProductos";
import rudProducto from "./components/rudProducto";
 
 
const routes = [{
        path: '/',
        name: 'root',
        component: App
    },
    {
        path: '/user/logIn',
        name: "logIn",
        component: LogIn
    },
    {
        path: '/user/signUp',
        name: "signUp",
        component: SignUp
    },
    {
        path: '/user/home',
        name: "home",
        component: Home
    },
    {
        path: '/user/registro_ventas',
        name: "registroVentas",
        component: RegistroVentas
    },
    {
        path: "/user/producto/",
        name: "producto",
        component: Productos,
      },
    
      {
        path: "/user/producto/",
        name: "readProducts",
        component: readProductos,
      },
    
      {
        path: "/user/producto/detalle",
        name: "rudProducto",
        component: rudProducto,
      },
];
 
const router = createRouter({
    history: createWebHistory(),
    routes,
});
 
export default router;