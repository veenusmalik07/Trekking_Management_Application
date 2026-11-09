<template>

    <!-- LOGIN PAGE -->
    <div class="login-page">

        <!-- FULL SCREEN BACKGROUND -->
        <div class="background-wrapper">
            <img class="background-image" 
                src="@/assets/images/hero.jpg" 
                alt="Camping Background"
            >
        </div>
        

        <!-- LOGIN CARD -->
        <div class="login-card">

            <!-- LOGO -->
            <div class="logo-section">
                <p>Welcome To</p>
                <h1>TrekMate</h1>
            </div>

            <!-- LOGIN AS -->
            <div class="mb-3">
                <label class="form-label"> Select Your Role </label>
                
                <select class="form-select" v-model="selectedRole">
                    <option value="user"> User </option>
                    <option value="staff"> Staff </option>
                    <option value="admin"> Admin </option>
                </select>
            </div>

            <!-- LOGIN FORM -->
            <form v-if="isLogin" @submit.prevent="handleLogin">
                
                <!-- Email -->
                <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" 
                        class="form-control" 
                        v-model="loginForm.email" 
                        placeholder="Enter your email" 
                        required
                    >
                 </div>
                 
                <!-- Password -->
                <div class="mb-3"> 
                    <label class="form-label">Password</label>
                    
                    <div class="input-group">
                        <input :type="showPassword ? 
                            'text' : 'password'" 
                            class="form-control" 
                            v-model="loginForm.password" 
                            placeholder="Enter password"
                            required
                        >
                        
                        <button type="button"
                            class="btn btn-outline-secondary"
                            @click="showPassword=!showPassword"
                        >
                        
                            <i :class="showPassword
                                ? 'bi bi-eye-slash-fill'
                                : 'bi bi-eye-fill'"
                            ></i>
                        </button>
                    </div>
                </div>

                <!-- Terms & Conditions -->
                <div class="form-check mt-3">
                    <input class="form-check-input"
                        type="checkbox"
                        id="terms"
                        v-model="acceptTerms"
                    >
                    <label class="form-check-label" for="terms">
                        I agree to the
                        <router-link to="/terms">
                            Terms & Conditions
                        </router-link>
                    </label>
                </div>
                
                <div class="mt-4">
                    <!-- LOGIN BUTTON -->
                    <button type="submit"
                        class="login-btn"
                        :disabled="!acceptTerms"
                    >
                    Login
                    </button>

                    <!-- Register Link -->
                    <div class="text-center mt-3">
                        <span> New to TrekMate? </span>
                        <router-link to="/Register"
                            class="mt-4"
                        >
                            Create an account
                        </router-link>
                    </div>
                </div>

            </form>
            <!-- LOGIN FORM ENDS -->
            
        <!-- LOGIN CARD ENDS -->
        </div>

    <!-- LOGIN PAGE ENDS -->
    </div>

</template>









<style scoped>

/* ==========================================================
   IMPORT FONT
========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');


/* ==========================================================
   GLOBAL
========================================================== */

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}




/* ==========================================================
   PAGE
========================================================== */

.login-page{

    width:100%;

    height:100vh;

    position:relative;

    overflow:hidden;

}


/* ==========================================================
BACKGROUND
========================================================== */

.background-wrapper{
    position: fixed;
    inset: 0;
    overflow: hidden;
    z-index: -2;
    background:#08111f;
}

.background-image{
    position: absolute;
    top: 50%;
    left: -120px;
    height: 100vh;
    width: auto;
    transform: translateY(-50%);
}


/* ==========================================================
   CONTENT
========================================================== */

.content-wrapper{

    position:relative;

    z-index:5;

    width:100%;

    height:100vh;

    display:flex;

    justify-content:center;

    align-items:center;

}


/* ==========================================================
   LOGIN CARD
========================================================== */

.login-card{
    position:absolute;
    top:50%;
    left:70%;
    transform:translate(-50%,-50%);
    width:650px;
    height:auto;
    min-height:auto;
    max-height:90vh;
    overflow-y:auto;
    padding:50px 50px;
    border-radius:30px;
    background: rgba(10, 20, 40, 0.18);
    backdrop-filter:blur(2px);
    -webkit-backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,.12);
    box-shadow:inset 0 1px 1px rgba(255,255,255,.15), 0 20px 60px rgba(0,0,0,.35);
    color:white;
    z-index:100;
    display:flex;
    flex-direction: column;

    transition:
    transform .45s ease,
    background .45s ease,
    border .45s ease,
    box-shadow .45s ease,
    backdrop-filter .45s ease;
}

/* ==========================================================
   LOGIN CARD HOVER
========================================================== */

.login-btn{
    margin-top: 10px;
    margin-bottom:5px;
    width:200px;
    padding:10px;
    color:white;
background:#23965b;
 cursor:pointer;
 border-radius: 14px;
margin-left: 180px;
    transition:all .3s ease;

    box-shadow:0 8px 20px rgba(35,150,91,.35);
}

.login-btn:hover{

    background:#1d7d4d;

    transform:translateY(-2px);

    box-shadow:0 14px 30px rgba(35,150,91,.45);

}

.login-btn:active{

    transform:scale(.98);

}

.login-btn:disabled{
    background:#6c757d;
    color:white;
    cursor:not-allowed;
    opacity:.75;
    box-shadow:none;
}

.login-card:hover{

    transform: translate(-50%, -50%) scale(1.015);
    backdrop-filter: blur(48px);
    -webkit-backdrop-filter: blur(28px);
    border: 1px solid white;
    transition: all .45s ease;

}

/* ==========================================================
   LOGO
========================================================== */

.logo-section{
    text-align:center;
    margin-bottom:40px;
    align-items: center;
}

.logo-section h1{
    font-size:52px;
    color:white;
    font-weight:800;
    margin-left: 0px;
    font-size: 3.5rem;
}

.logo-section p{
    font-size: 1.2rem;
}



/* ==========================================================
   FORM
========================================================== */

.form-control{
    background: rgba(255,255,255,.08) !important;
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 14px;
    color: white;
    font-size: 17px;
    backdrop-filter: blur(15px);
    transition: all .3s ease;
    box-shadow: none;
    padding:12px 16px;
    height:60px;
    padding:16px 22px;

}

.form-control:focus{
    border-color:#f4f7f6;
    color: white;
    box-shadow:
    0 0 0 3px rgba(66,211,146,.15);
    background:rgba(255,255,255,.12);
}

.form-control::placeholder{
    color:rgba(255,255,255,.45);
}

.form-label{
    color: white;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 8px;
}

.form-select{
    background: rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.12);
    border-radius:14px;
    color:white;
    height:52px;
    font-size:17px;
    transition:.3s;
    padding: 15px;
}

.form-select:focus{
    background: rgba(255,255,255,.12);
    border-color: rgba(255,255,255,.35);
    color:white;
    box-shadow:
        0 0 0 3px rgba(76,175,80,.15);
}

.form-select option{
    background: white;
    color:black;
}

.mb-3{
    margin-bottom: 18px !important;
}

.mb-4{
    margin-bottom: 25px !important;
}

/*PASSWORD TOGGLE*/
.password-toggle{
    width:56px;
    border-radius:0 14px 14px 0;
    background:rgba(255,255,255,.05);
    border:1px solid rgba(255,255,255,.12);
    border-left:none;
    color:#aeb6c2;
    transition:.3s;
}

.password-toggle:hover{
    color:white;
    background:rgba(255,255,255,.12);
}

.password-toggle i{
    font-size:18px;
}

/*ERROR MESSAGES*/
.text-danger{
    display: block;
    margin-top: 6px;
    margin-left: 6px;
    color: #ff8a8a !important;
    font-size: 0.82rem;
    font-weight: 500;
}

.form-check{
    display:flex;
    align-items:center;
    gap:10px;
    margin-top:20px !important;
    margin-left:30px;
    margin-bottom:30px;
}

.form-check-input{
    margin-top:0 !important;
    width:20px;
    height:20px;
    cursor:pointer;
}

.form-check-label{
    margin-bottom:0;
    color:#fff;
    font-size:18px;
    line-height:1;
}

.form-check-label a{
    color:#2d8cff;
    text-decoration:underline;
}

</style>









<script>

import axios from "axios";

export default{

    name:"Login",

    data(){
        return{

            // LOGIN TOGGLE
            isLogin:true,

            // SELECTED ROLE
            selectedRole:"user",

            // PASSWORD VISIBILITY
            showPassword:false,
            loading: false,
            acceptTerms: false,

            // LOGIN FORM
            loginForm:{
                email:"",
                password:""
            }
        }
    },

    // COMPUTED PROPERTIES    
    computed: {

        passwordMatch(){
            if(this.registerForm.confirm_password===""){
                return "";
            }
            return this.registerForm.password===this.registerForm.confirm_password;
        }

    // COMPUTED PROPERTY ENDS
    },

    // METHODS
    methods:{

        // TOGGLE LOGIN / REGISTER
        showRegister(){
            this.isLogin=false;
            this.currentStep= 1;
        },

        showLogin(){
            this.isLogin=true;
            this.currentStep= 1;
        },

        // TOGGLE PASSWORD
        togglePassword(){
            this.showPassword=!this.showPassword;
        },

        toggleConfirmPassword(){
            this.showConfirmPassword=!this.showConfirmPassword;
        },
        
        // LOGIN
        async handleLogin(){
            this.loading = true;
            if(!this.acceptTerms){

        alert("Please agree to the Terms & Conditions before logging in.");

        return;
            }
            this.loading = true;
            
            try{
                // PREPARE REQUEST DATA
                const payload = {
                    email: this.loginForm.email,
                    password: this.loginForm.password,
                    role: this.selectedRole
                };

                // API REQUEST
                const response = await axios.post(
                    "http://127.0.0.1:5000/api/login",
                    payload
                );

                // LOGIN SUCCESS
                if(response.data.success){
                    localStorage.setItem(
                        "access_token",
                        response.data.data.access_token
                    );
                    
                    localStorage.setItem(
                        "role",
                        response.data.data.role
                    );
                    
                    localStorage.setItem(
                        "user",
                        JSON.stringify(response.data.data)
                    );

                    // REDIRECT BASED ON ROLE
                    switch(response.data.data.role){
                        case "admin":
                            this.$router.push("/admin-dashboard");
                            break;
                            
                        case "staff":
                            this.$router.push("/staff-dashboard");
                            break;
                        
                        default:
                            this.$router.push("/user-dashboard");
                    }
                }
            // TRY BLOCK ENDS
            }
            
            catch(error){
                alert(
                    error.response?.data?.message ||
                    "Login Failed"
                );
            }
            
            finally{
                this.loading = false;
            }
        // LOGIN ENDS
        }

    // METHODS ENDS
    }

}

</script>

