<template>

<!-- REGISTRATION FORM -->
<div class="registration-page">
    <div class="register-container">

        <!-- LEFT PANEL -->
        <div class="left-panel">
            <div class="left-overlay">
                <div class="brand">
                    <i class="bi bi-tree-fill"></i>
                    <h1>TrekMate</h1>
                </div>

                <div class="hero-text">
                    <h2>
                        Adventure begins under the stars.
                    </h2>
                    <p>
                        Discover breathtaking treks, unforgettable camps,
                        and thousands of fellow explorers waiting for you.
                    </p>
                </div>
            </div>
        </div>

        <!--RIGHT PANEL-->
        <div class="right-panel">
            <!-- REGISTRATION CARD -->
    <div class="registration-card">
        <form @submit.prevent="handleRegister" class="register-form">
            <div v-if="!isLogin" class="wizard-progress">
                <div class="wizard-step" :class="{ active: currentStep >= 1 }">
                    <div class="step-circle">
                        1
                    </div>
                    <span> Account </span>
                </div>
                    
                <div class="wizard-line"></div>
                    <div class="wizard-step" :class="{ active: currentStep >= 2 }">
                        <div class="step-circle">
                            2
                        </div>
                        <span> Personal </span>
                    </div>
                    <div class="wizard-line"></div>
                    <div class="wizard-step" :class="{ active: currentStep >= 3 }">
                        <div class="step-circle">
                            3
                        </div>
                        <span> Emergency </span>
                    </div>
                </div>

                <!-- REGISTRATION STEPS -->
                <Transition name="slide" mode="out-in">
                    <div :key="currentStep">
                        <!-- STEP 1 -->
                        <div v-if="currentStep===1">
                            <h4> Account Information </h4>
                            
                            <!-- FULL NAME -->
                            <div class="mb-3">
                                <label> Full Name </label>
                                <input type="text"
                                    class="form-control"
                                    v-model="registerForm.full_name" 
                                    required
                                >
                                <small
                                    v-if="errors.full_name"
                                    class="text-danger"
                                >
                                    {{ errors.full_name }}
                                </small>
                            </div>
                            
                            <!-- EMAIL -->
                            <div class="mb-3">
                                <label> Email Address </label>
                                <input type="email"
                                    class="form-control"
                                    v-model="registerForm.email"
                                    required
                                >
                                <small
                                    v-if="errors.email"
                                    class="text-danger"
                                >
                                    {{ errors.email }}
                                </small>
                            </div>
                            
                            <!-- MOBILE -->
                            <div class="mb-3">
                                <label> Mobile Number </label>
                                <input type="tel" maxlength="10"
                                    class="form-control"
                                    v-model="registerForm.mobile_number"
                                    required
                                >
                                <small
                                    v-if="errors.mobile_number"
                                    class="text-danger"
                                >
                                    {{ errors.mobile_number }}
                                </small>
                            </div>
                            
                            <!-- PASSWORD -->
                            <div class="mb-3">
                                <label> Password </label>
                                <div class="input-group">
                                    <input :type="showPassword ? 'text' : 'password'"
                                        class="form-control"
                                        v-model="registerForm.password"
                                        required
                                    >
                                    <small
                                        v-if="errors.password"
                                        class="text-danger"
                                    >
                                        {{ errors.password }}
                                    </small>
                                    <button type="button"
                                        class="btn btn-outline-secondary"
                                        @click="togglePassword"
                                    >
                                        <i :class="showPassword
                                            ? 'bi bi-eye-slash-fill'
                                            : 'bi bi-eye-fill'"
                                        ></i>
                                    </button>
                                </div>
                            </div>
                            
                            <!-- CONFIRM PASSWORD -->
                            <div class="mb-4">
                                <label> Confirm Password </label>
                                <div class="input-group">
                                    <input :type="showConfirmPassword ? 'text' : 'password'"
                                        class="form-control"
                                        v-model="registerForm.confirm_password"
                                        required
                                    >
                                    <small
                                        v-if="errors.confirm_password"
                                        class="text-danger"
                                    >
                                        {{ errors.confirm_password }}
                                    </small>
                                    <button type="button"
                                        class="btn btn-outline-secondary"
                                        @click="toggleConfirmPassword"
                                    >
                                        <i :class="showConfirmPassword
                                            ? 'bi bi-eye-slash-fill'
                                            : 'bi bi-eye-fill'"
                                        ></i>
                                    </button>
                                </div>
                            </div>
                            
                            <!-- NEXT BUTTON -->
                            <button type="button"
                                class="btn btn-success w-100"
                                @click="nextStep"
                            >
                                Next →
                            </button>
                        </div>
                        <!-- STEP 1 ENDS -->

                        <!-- STEP 2 : PERSONAL INFORMATION -->
                        <div v-if="currentStep===2">
                            <h4> Personal Information </h4>
                            <p> Tell us a little about yourself. </p>
                            
                            <!-- DATE OF BIRTH -->
                            <div class="mb-3">
                                <label> Date of Birth </label>
                                <input type="date"
                                    class="form-control"
                                    v-model="registerForm.date_of_birth"
                                    required
                                >
                                <small
                                    v-if="errors.date_of_birth"
                                    class="text-danger"
                                >
                                    {{ errors.date_of_birth }}
                                </small>
                            </div>
                            
                            <!-- GENDER -->
                            <div class="mb-3">
                                <label> Gender </label>
                                <select class="form-select"
                                    v-model="registerForm.gender" 
                                    required
                                >
                                    <option disabled value=""> Select Gender </option>
                                    <option> Male </option>
                                    <option> Female </option>
                                    <option> Other </option>
                                </select>
                            </div>
                            
                            <!-- STATE -->
                            <div class="mb-3">
                                <label> State </label> 
                                <select class="form-select" 
                                    v-model="registerForm.state"
                                    required
                                >
                                    <option disabled value=""> Select State </option>
                                    <option>Andhra Pradesh</option>
                                    <option>Arunachal Pradesh</option>
                                    <option>Assam</option>
                                    <option>Bihar</option>
                                    <option>Chandigarh</option>
                                    <option>Chhattisgarh</option>
                                    <option>Delhi</option>
                                    <option>Goa</option>
                                    <option>Gujarat</option>
                                    <option>Haryana</option>
                                    <option>Himachal Pradesh</option>
                                    <option>Jharkhand</option>
                                    <option>Karnataka</option>
                                    <option>Kerala</option>
                                    <option>Madhya Pradesh</option>
                                    <option>Maharashtra</option>
                                    <option>Odisha</option>
                                    <option>Punjab</option>
                                    <option>Rajasthan</option>
                                    <option>Tamil Nadu</option>
                                    <option>Telangana</option>
                                    <option>Uttar Pradesh</option>
                                    <option>Uttarakhand</option>
                                    <option>West Bengal</option>
                                </select>
                            </div>
                            
                            <!-- CITY -->
                            <div class="mb-4">
                                <label> City </label>
                                <input type="text"
                                    class="form-control"
                                    v-model="registerForm.city"
                                    placeholder="Enter City"
                                    required
                                >
                                <small
                                    v-if="errors.city"
                                    class="text-danger"
                                >
                                    {{ errors.city }}
                                </small>
                            </div>

                            <!-- BUTTONS -->
                            <div class="d-flex justify-content-between"> 
                                <button type="button"
                                    class="btn btn-outline-secondary"
                                    @click="previousStep"
                                >
                                    ← Back
                                </button>
                                
                                <button type="button"
                                    class="btn btn-success"
                                    @click="nextStep"
                                >
                                    Next →
                                </button>
                            </div>
                        <!-- STEP-2 ENDS -->
                        </div>
                        
                        <!-- STEP 3 : EMERGENCY CONTACT -->
                        <div v-if="currentStep===3">
                            <h4> Emergency Contact </h4>
                            <p> Safety always comes first. </p>
                            
                            <!-- CONTACT NAME -->
                            <div class="mb-3">
                                <label> Emergency Contact Name </label>
                                <input type="text"
                                    class="form-control"
                                    v-model="registerForm.emergency_contact_name"
                                    required
                                >
                                <small
                                    v-if="errors.emergency_contact_name"
                                    class="text-danger"
                                >
                                    {{ errors.emergency_contact_name }}
                                </small>
                            </div>
                            
                            <!-- CONTACT NUMBER -->
                            <div class="mb-4">
                                <label> Emergency Contact Number </label>
                                <input type="tel" 
                                    maxlength="10"
                                    class="form-control"
                                    v-model="registerForm.emergency_contact_number"
                                    required
                                >
                                <small
                                    v-if="errors.emergency_contact_number"
                                    class="text-danger"
                                >
                                    {{ errors.emergency_contact_number }}
                                </small>
                            </div>
                            
                            <!-- BUTTONS -->
                            <div class="d-flex justify-content-between">
                                <button type="button"
                                    class="btn btn-outline-secondary"
                                    @click="previousStep"
                                >
                                    ← Back
                                </button>
                                
                                <button type="submit" 
                                    class="btn btn-success"
                                    :disabled="loading"
                                >
                                    {{ loading ? "Creating..." : "Create Account" }}
                                </button>

                                <!-- LOGIN BUTTON -->
                                 <div class="text-center mt-3">
                        <router-link to="/Login"
                            class="btn btn-primary mt-4"
                        >
                            Login
                        </router-link>
                    </div>
                            </div>
                        <!--STEP-3 ENDS-->
                        </div>

                    </div>
                </Transition>
            </form>
        </div>
        </div>

    </div>
</div>
</template>









<script>

import axios from "axios";

export default{

    name:"Login",

    data(){

        return{

            // LOGIN / REGISTER TOGGLE
            isLogin:true,

            // SELECTED ROLE
            selectedRole:"user",

            // PASSWORD VISIBILITY
            showPassword:false,
            showConfirmPassword: false,
            loading: false,

            // LOGIN FORM
            loginForm:{
                email:"",
                password:""
            },

            // REGISTER FORM
            registerForm:{
                full_name:"",
                email:"",
                mobile_number:"",
                password:"",
                confirm_password:"",
                date_of_birth:"",
                gender:"",
                city:"",
                state:"",
                emergency_contact_name:"",
                emergency_contact_number:""
            },

            // REGISTER WIZARD
            currentStep: 1,

            errors: {
                full_name: "",
                email: "",
                mobile_number: "",
                password: "",
                confirm_password: "",
                date_of_birth: "",
                gender: "",
                city: "",
                state: "",
                emergency_contact_name: "",
                emergency_contact_number: ""
            }

        }

    },

    // =====================================================
    // COMPUTED PROPERTIES
    // =====================================================
    
    computed: {

        passwordMatch(){
            if(this.registerForm.confirm_password===""){
                return "";
            }
            return this.registerForm.password===this.registerForm.confirm_password;
        },

        passwordStrength(){
            const password=this.registerForm.password;
            if(password.length===0){
                return "";
            }

            if(password.length<8){
                return "Weak";
            }

            let score=0;
            
            if(/[A-Z]/.test(password)) score++;
            if(/[a-z]/.test(password)) score++;
            if(/[0-9]/.test(password)) score++;
            if(/[^A-Za-z0-9]/.test(password)) score++;

            if(score<=2){
                return "Weak";
            }

            if(score===3){
                return "Medium";
            } 

            return "Strong";
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
        },

        // ==========================================
        // VALIDATE CURRENT STEP
        // ==========================================
        validateStep(){
            // Clear previous errors
            this.errors = {
                full_name: "",
                email: "",
                mobile_number: "",
                password: "",
                confirm_password: "",
                date_of_birth: "",
                gender: "",
                city: "",
                state: "",
                emergency_contact_name: "",
                emergency_contact_number: ""
            };
            
            let valid = true;
            // STEP 1
            if(this.currentStep === 1){
                // Full Name
                if(!this.registerForm.full_name.trim()){
                    this.errors.full_name = "Full Name is required.";
                    valid = false;
                }
                
                else if(!/^[A-Za-z ]{3,}$/.test(this.registerForm.full_name)){
                    this.errors.full_name = "Enter a valid full name.";
                    valid = false;
                }

                // Email
                if(!this.registerForm.email.trim()){
                    this.errors.email = "Email is required.";
                    valid = false;
                }

                else if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.registerForm.email)){
                    this.errors.email = "Enter a valid email.";
                    valid = false;
                }

                // Mobile
                if(!/^\d{10}$/.test(this.registerForm.mobile_number)){
                    this.errors.mobile_number = "Enter a valid 10-digit mobile number.";
                    valid = false;
                }

                // Password
                if(
                    !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$/
                    .test(this.registerForm.password)
                ){
                    this.errors.password =
                    "Password must contain uppercase, lowercase, number and special character.";
                    valid = false;
                }

                // Confirm Password
                if(this.registerForm.password !== this.registerForm.confirm_password){
                    this.errors.confirm_password =
                    "Passwords do not match.";
                    valid = false;
                }
            // STEP 1 ENDS
            }
            
            // STEP 2
            if(this.currentStep === 2){
                if(!this.registerForm.date_of_birth){
                    this.errors.date_of_birth =
                    "Please select your date of birth.";
                    valid = false;
                }
                
                if(!this.registerForm.gender){
                    this.errors.gender =
                    "Please select gender.";
                    valid = false;
                }
                
                if(!this.registerForm.city.trim()){
                    this.errors.city =
                    "City is required.";
                    valid = false;
                }
                
                if(!this.registerForm.state.trim()){
                    this.errors.state =
                    "State is required.";
                    valid = false;
                }
            }
            
            // STEP 3
            if(this.currentStep === 3){
                if(!this.registerForm.emergency_contact_name.trim()){
                    this.errors.emergency_contact_name =
                    "Emergency contact name is required.";
                    valid = false;
                }
                if(!/^\d{10}$/.test(this.registerForm.emergency_contact_number)){
                    this.errors.emergency_contact_number =
                    "Enter a valid emergency contact number.";
                    valid = false;
                }
            }
            return valid;
        // VALIDATE STEP() ENDS
        },

        // NEXT STEP
        nextStep(){
            if(!this.validateStep()){
                return;
            }
            this.currentStep++;
        // NEXT STEP ENDS
        },
        
        // PREVIOUS STEP
        previousStep(){
            if(this.currentStep>1){
                this.currentStep--;
            }
        },

        // REGISTER
        async handleRegister(){
            // PASSWORD MATCH VALIDATION
            if(this.registerForm.password !== this.registerForm.confirm_password){
                alert("Passwords do not match.");
                return;
            }
            
            this.loading = true;
            
            try{
                // API REQUEST
                const response = await axios.post(
                    "http://127.0.0.1:5000/api/register",
                    {
                        full_name: this.registerForm.full_name,
                        email: this.registerForm.email,
                        mobile_number: this.registerForm.mobile_number,
                        password: this.registerForm.password,
                        date_of_birth: this.registerForm.date_of_birth,
                        gender: this.registerForm.gender,
                        city: this.registerForm.city,
                        state: this.registerForm.state,
                        emergency_contact_name: this.registerForm.emergency_contact_name,
                        emergency_contact_number: this.registerForm.emergency_contact_number
                    }
                );

                // SUCCESS
                if(response.data.success){
                    alert(response.data.message);

                    // Back to Login
                    this.isLogin = true;
                    
                    // Clear Registration Form
                    this.registerForm={
                        full_name:"",
                        email:"",
                        mobile_number:"",
                        password:"",
                        confirm_password:"",
                        date_of_birth:"",
                        gender:"",
                        city:"",
                        state:"",
                        emergency_contact_name:"",
                        emergency_contact_number:""
                    };
                }
            // TRY BLOCK ENDS
            }
            
            catch(error){
                alert(
                    error.response?.data?.message ||
                    "Registration Failed"
                );
            }
            
            finally{
                this.loading=false;
            }

        // REGISTER ENDS
        },

    // METHODS ENDS
    }
}

</script>

<style scoped>

/* ==========================================================
   IMPORT FONT
========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* ===========================
   PAGE
=========================== */
.registration-page{

    width:100%;

    min-height:100vh;

    display:flex;

    justify-content:center;

    align-items:center;

    padding:0;

    margin:0;

    background:#edf2f7;

}

/* ===========================
   MAIN CONTAINER
=========================== */

.register-container{

    width:100%;

    max-width:1600px;

    min-height:100vh;

    display:grid;

    grid-template-columns:45% 55%;

    overflow:hidden;

    background:white;

}

.left-panel{
    height:100%;

    position:relative;

    background:

    linear-gradient(

        rgba(0,0,0,.25),

        rgba(0,0,0,.60)

    ),

    url("@/assets/images/registration-bg.jpg");

    background-size:cover;

    background-position:center;

}

.left-overlay{

    position:absolute;

    inset:0;

    display:flex;

    flex-direction:column;

    justify-content:space-between;

    padding:70px;

}

.brand{

    display:flex;

    align-items:center;

    gap:18px;

}

.brand i{

    font-size:42px;

    color:#6EE7B7;

}

.brand h1{

    font-family:"Cinzel",serif;

    color:white;

    font-size:3rem;

    font-weight:700;

}

.hero-text{

    color:white;

}

.hero-text h2{

    font-size:2.7rem;

    line-height:1.5;

    margin-bottom:25px;

    font-family:"Cinzel",serif;

}

.hero-text p{

    font-size:1.15rem;

    line-height:1.8;

    color:rgba(255,255,255,.85);

    max-width:420px;

}

.right-panel{

    display:flex;

    justify-content:center;

    align-items:center;

    padding:40px;

}
.registration-card{

    width:100%;

    max-width:700px;

    background:white;

    border-radius:20px;

    padding:35px;

    box-shadow:0 15px 40px rgba(0,0,0,.08);

}

.register-form{

    width:100%;

}

.register-form h4{

    font-size:2.4rem;

    font-weight:700;

    margin-bottom:8px;

}

.register-form p{

    color:#777;

    margin-bottom:35px;

}
.mb-3{

    margin-bottom:22px !important;

}

.register-form label{

    display:block;

    margin-bottom:8px;

    font-size:.95rem;

    font-weight:600;

    color:#404040;

}

.register-form .form-control{

    height:56px;

    border-radius:14px;

    border:1px solid #dddddd;

    padding:0 18px;

    font-size:16px;

    transition:.3s;

    box-shadow:none;

}

.register-form .form-control:hover{

    border-color:#7b4fff;

}

.register-form .form-control:focus{

    border-color:#7b4fff;

    box-shadow:0 0 0 4px rgba(123,79,255,.15);

}

.password-wrapper{

    position:relative;

}

.password-wrapper button{

    position:absolute;

    right:15px;

    top:50%;

    transform:translateY(-50%);

    border:none;

    background:none;

    color:#666;

    font-size:20px;

    cursor:pointer;

}

.text-danger{

    font-size:.85rem;

    margin-top:5px;

}

.next-btn{

    width:100%;

    height:56px;

    border:none;

    border-radius:15px;

    margin-top:20px;

    background:linear-gradient(
        135deg,
        #3ba55d,
        #237847
    );

    color:white;

    font-size:18px;

    font-weight:600;

    transition:.35s;

}

.next-btn:hover{

    transform:translateY(-3px);

    box-shadow:
        0 15px 30px rgba(35,120,71,.30);

}

.progress-container{

    display:flex;

    gap:12px;

    margin-bottom:35px;

}

.progress-step{

    flex:1;

    height:6px;

    background:#dddddd;

    border-radius:20px;

}

.progress-step.active{

    background:linear-gradient(
        90deg,
        #6b5cff,
        #915eff
    );

}

.slide-enter-active,
.slide-leave-active{

    transition:.45s ease;

}

.slide-enter-from{

    opacity:0;

    transform:translateX(50px);

}

.slide-leave-to{

    opacity:0;

    transform:translateX(-50px);

}
.left-panel,
.right-panel{

    height:100%;

}

</style>