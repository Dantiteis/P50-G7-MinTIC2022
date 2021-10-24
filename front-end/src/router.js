import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';
 
import LogIn from './components/LogIn.vue';
import SignUp from './components/SignUp.vue';
import Home from './components/Home.vue';
import RegistroVentas from './components/RegistroVentas.vue';
import Productos from "./components/Productos.vue";
import readProductos from "./components/readProductos";
import rudProducto from "./components/rudProducto";
import listaClientes from './components/listClientes';
import RegistroClientes from './components/registroClientes';
import Proveedores from './components/Proveedores.vue';
import readSales from './components/readSales';
import Account from './components/Account.vue';
import Comentarios   from "./components/Comentarios.vue";
import readComentarios from './components/readComentarios.vue';
 
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
    {
        path: '/user/addClientes',
        name: "registroClientes",
        component: RegistroClientes
    },
    {
        path: "/user/Ventas/",
        name: "readSales",
        component: readSales,
    },
    {
        path: '/user/listClientes',
        name: "listClientes",
        component: listaClientes
    },
    {
        path: '/user/account',
        name: "account",
        component: Account
    },
    {
        path:'/user/Proveedor' ,
        name: "Proveedor",
        component: Proveedores
    },
    {
        path:'/user/comentarios' ,
        name: "comentarios",
        component: Comentarios
    },
    {
        path:'/user/readComentarios' ,
        name: "readComentarios",
        component: readComentarios
    },
];
 
const router = createRouter({
    history: createWebHistory(),
    routes,
});
 
export default router;