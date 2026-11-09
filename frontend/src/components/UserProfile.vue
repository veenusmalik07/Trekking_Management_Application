<template>

    <!-- USER NAVBAR -->
    <nav class="user-navbar">
        <!-- Logo -->
        <div class="navbar-logo" @click="$router.push('/user-dashboard')">
            <i class="bi bi-tree-fill"></i>
            <span> TREKMATE </span>
        </div>

        <!-- Navigation -->
        <div class="navbar-links">
            <router-link to="/user-dashboard" class="nav-link"> Dashboard </router-link>
            <router-link to="/user-browse-treks" class="nav-link"> Browse Treks </router-link>
            <router-link to="/user-my-bookings" class="nav-link"> My Bookings </router-link>
            <router-link to="/user-profile" class="nav-link active-link"> Profile </router-link>
        </div>

        <!-- Right -->
        <div class="navbar-right">
            <button class="logout-btn" @click="$router.push('/')">
                <i class="bi bi-box-arrow-right me-2"></i>
                Logout
            </button>
        </div>
    </nav>
    <!-- NAVBAR ENDS -->

    <div class="profile-page">
        
        <!-- Left Side -->
        <div class="profile-image-section">
            <img src="@/assets/images/user-bg.jpg"
                alt="Profile Background"
                class="profile-bg"
            >
            
            <div class="image-text">
                <span>MY PROFILE</span>
                <h1>Adventure Begins With You</h1>
                <p>
                    Keep your profile updated so every trekking experience
                    becomes safer, smoother and more memorable.
                </p>
            </div>
        </div>
        <!--LEFT SIDE ENDS-->
        
        <!-- Right Side -->
        <div class="profile-content">
            <div class="profile-card">
                <div class="profile-header">
                    
                    <div class="profile-picture-wrapper">
                        <img :src="profileImage" class="profile-picture">
                        <label v-if="editing" class="change-photo">
                            <i class="bi bi-camera-fill"></i>
                            <input type="file" hidden @change="selectProfilePicture">
                        </label>
                    </div>

    <!-- PROFILE PICTURE WRAPPER ENDS -->

    <div class="profile-heading">

        <h2>{{ user.full_name }}</h2>

        <p>{{ user.email }}</p>

    </div>

</div>
<!-- PROFILE HEADER ENDS -->

<!-- =======================================================
                    PERSONAL INFORMATION
======================================================= -->

<div class="section-title">

    <h3>Personal Information</h3>

</div>

<div class="profile-form">

    <div class="form-group">

        <label>Full Name</label>

        <input
            v-if="editing"
            v-model="user.full_name"
            type="text"
        >

        <div
            v-else
            class="profile-value"
        >
            {{ user.full_name }}
        </div>

    </div>

    <div class="form-group">

        <label>Email Address</label>

        <div class="profile-value readonly">

            {{ user.email }}

        </div>

    </div>

    <div class="form-group">

        <label>Mobile Number</label>

        <input
            v-if="editing"
            v-model="user.mobile_number"
            type="text"
        >

        <div
            v-else
            class="profile-value"
        >
            {{ user.mobile_number }}
        </div>

    </div>

    <div class="form-group">

        <label>Date of Birth</label>

        <div class="profile-value readonly">

            {{ user.date_of_birth }}

        </div>

    </div>

    <div class="form-group">

        <label>Gender</label>

        <div class="profile-value readonly">

            {{ user.gender }}

        </div>

    </div>

    <div class="form-group">

        <label>City</label>

        <input
            v-if="editing"
            v-model="user.city"
            type="text"
        >

        <div
            v-else
            class="profile-value"
        >
            {{ user.city }}
        </div>

    </div>

    <div class="form-group">

        <label>State</label>

        <input
            v-if="editing"
            v-model="user.state"
            type="text"
        >

        <div
            v-else
            class="profile-value"
        >
            {{ user.state }}
        </div>

    </div>

    <div class="form-group">

        <label>Emergency Contact Name</label>

        <input
            v-if="editing"
            v-model="user.emergency_contact_name"
            type="text"
        >

        <div
            v-else
            class="profile-value"
        >
            {{ user.emergency_contact_name }}
        </div>

    </div>

    <div class="form-group">

        <label>Emergency Contact Number</label>

        <input
            v-if="editing"
            v-model="user.emergency_contact_number"
            type="text"
        >

        <div
            v-else
            class="profile-value"
        >
            {{ user.emergency_contact_number }}
        </div>

    </div>

</div>
<!-- PROFILE FORM ENDS -->

<!-- =======================================================
                    ACTION BUTTONS
======================================================= -->

<div class="profile-actions">

    <button
        v-if="!editing"
        class="edit-btn"
        @click="editing = true"
    >

        <i class="bi bi-pencil-square me-2"></i>

        Edit Profile

    </button>

    <template v-else>

        <button
            class="cancel-btn"
            @click="cancelEdit"
        >

            <i class="bi bi-x-circle me-2"></i>

            Cancel

        </button>

        <button
            class="save-btn"
            @click="saveProfile"
        >

            <i class="bi bi-check-circle me-2"></i>

            Save Changes

        </button>

    </template>

</div>
<!-- PROFILE ACTIONS ENDS -->

</div>
<!-- PROFILE CARD ENDS -->

</div>
<!--PROFILE CONTENT ENDS-->

</div>
<!-- PROFILE PAGE ENDS -->

</template>

<style scoped>

:root {
  --primary: #0a3323; /* Dark Green */
  --secondary: #839958; /* Moss Green */
  --cream: #f7f4d5; /* Beige */
  --accent: #d3968c; /* Rosy Brown */
  --dark: #105666; /* Midnight Green */
  --white: #ffffff;
}

/*==================================================
USER NAVBAR
==================================================*/
.user-navbar{
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:88px;
  padding:0 70px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  background:rgba(247,244,213,.95);   /* Cream */
  backdrop-filter:blur(18px);
  box-shadow:0 6px 30px rgba(0,0,0,.08);
  z-index:9999;
}

.navbar-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  color: white;
}

.navbar-logo i {
  font-size: 1.8rem;
  color:#0A3323;
}

.navbar-logo span {
  font-size: 2rem;
  color:#0A3323;
  font-weight: 700;
  letter-spacing: 2px;
}

.navbar-links {
  display: flex;
  gap: 18px;
}

.nav-link {
  text-decoration: none;
  color: #4d4d4d;
  padding: 12px 22px;
  border-radius: 16px;
  font-weight: 600;
  transition: 0.3s;
}
.nav-link:hover {
  background: rgba(255, 255, 255, 0.55);
  color: #670626;
}

.active-link{
    background:#839958;
    color:white !important;
}
.active-link:hover {
  background: rgba(255, 255, 255, 0.55);
  color: #670626;
}


.logout-btn {
  font-weight: 600;
  padding: 12px 24px;
  border: none;
  border-radius: 16px;
  transition: 0.3s;
  background:#D3968C;
  background:#0A3323;
  color:white;
}
.logout-btn:hover {
  background:#D3968C;
  color: white;
}

/*======================================================
                    PROFILE PAGE
======================================================*/

.profile-page{

    display:flex;

    min-height:100vh;

    background:#edf4ef;

}

/*======================================================
                    LEFT SECTION
======================================================*/

.profile-image-section{

    width:50%;

    height:100vh;

    position:sticky;

    top:0;

    overflow:hidden;

}

.profile-bg{

    width:100%;

    height:100%;

    object-fit:cover;

    object-position:center;

}

.image-overlay{

    position:absolute;

    inset:0;

    background:linear-gradient(
        rgba(7,35,24,.15),
        rgba(7,35,24,.45)
    );

}

.image-text{

    position:absolute;

    left:60px;

    bottom:70px;

    color:#fff;

    z-index:2;

    max-width:75%;

}

.image-text span{

    display:inline-block;

    letter-spacing:4px;

    font-size:.9rem;

    font-weight:700;

    color:#F5E7A6;

    margin-bottom:18px;

}

.image-text h1{

    font-size:3.2rem;

    font-weight:800;

    line-height:1.15;

    margin-bottom:20px;

}

.image-text p{

    font-size:1.05rem;

    line-height:1.8;

    color:rgba(255,255,255,.9);

}

/*== RIGHT SECTION ==*/

.profile-content{
    width:50%;
    padding:5px;
    overflow-y:auto;
    display:flex;
    justify-content:center;
    align-items:flex-start;
    margin-top: 70px;
}

.profile-card{
    position: relative;
    overflow: hidden;
    width:100%;
    max-width:800px;
    padding:45px;
    border-radius:28px;
    box-shadow:0 20px 45px rgba(0,0,0,.08);
    z-index:1;
    background:
        linear-gradient(
            rgba(255,255,255,.35),
            rgba(255,255,255,.35)
        ),
        url("@/assets/images/user-bg.jpg");
}


.profile-card::after{
    content:"";
    position:absolute;
    inset:0;
    backdrop-filter:blur(2px);
    background:rgba(255,255,255,.18);
    z-index:-1;
}

/*======================================================
                    PROFILE HEADER
======================================================*/

.profile-header{

    display:flex;

    align-items:center;

    gap:30px;

    margin-bottom:45px;

}

.profile-picture-wrapper{

    position:relative;

    width:140px;

    height:140px;

}

.profile-picture{

    width:140px;

    height:140px;

    border-radius:50%;

    object-fit:cover;

    border:5px solid white;

    box-shadow:0 12px 30px rgba(0,0,0,.12);

}

.change-photo{

    position:absolute;

    bottom:6px;

    right:6px;

    width:42px;

    height:42px;

    border-radius:50%;

    background:#87A651;

    color:white;

    display:flex;

    align-items:center;

    justify-content:center;

    cursor:pointer;

    transition:.3s;

}

.change-photo:hover{

    transform:scale(1.08);

}

.profile-heading h2{

    margin-bottom:8px;

    color:#0A3323;

    font-size:2rem;

    font-weight:800;

}

.profile-heading p{

    color:#6c757d;

    font-size:1rem;

}

/*======================================================
                    SECTION TITLE
======================================================*/

.section-title{

    margin-bottom:30px;

}

.section-title h3{

    font-size:1.45rem;

    color:#0A3323;

    font-weight:700;

}

/*======================================================
                    FORM
======================================================*/

.profile-form{

    display:grid;

    grid-template-columns:repeat(2,1fr);

    gap:28px;

}

.form-group{

    display:flex;

    flex-direction:column;
    color: #0A3323;

}

.form-group label{

    margin-bottom:10px;

    color:#0A3323;

    font-size:.92rem;

    font-weight:600;

}

.form-group input{

    height:56px;

    border:1px solid #d8d8d8;

    border-radius:14px;

    padding:0 18px;

    font-size:1rem;

    outline:none;

    transition:.3s;
    background:rgba(247,244,213,.95);
    color: #0A3323;

}

.form-group input:focus{

    border-color:#87A651;

    box-shadow:0 0 0 4px rgba(135,166,81,.15);

}

.profile-value{

    min-height:56px;

    background:#f7f7f7;

    border-radius:14px;

    display:flex;

    align-items:center;

    padding:0 18px;

    color:#083321;

    font-weight:500;

}

.readonly{

    background:#eef2ed;

    color:#7d7d7d;

}

/*======================================================
                    BUTTONS
======================================================*/

.profile-actions{

    margin-top:45px;

    display:flex;

    justify-content:flex-end;

    gap:18px;

}

.profile-actions button{

    border:none;

    border-radius:14px;

    padding:14px 28px;

    font-size:1rem;

    font-weight:600;

    transition:.3s;

}

.edit-btn{

    background:#87A651;

    color:white;

}

.edit-btn:hover{

    background:#0A3323;

}

.save-btn{

    background:#87A651;

    color:white;

}

.save-btn:hover{

    background:#0A3323;

}

.cancel-btn{

    background:#ececec;

    color:#444;

}

.cancel-btn:hover{

    background:#d9d9d9;

}

/*======================================================
                    RESPONSIVE
======================================================*/

@media(max-width:992px){

.profile-page{

    flex-direction:column;

}

.profile-image-section{

    width:100%;

    height:350px;

    position:relative;

}

.profile-content{

    width:100%;

    padding:30px;

}

.profile-form{

    grid-template-columns:1fr;

}

.profile-header{

    flex-direction:column;

    text-align:center;

}

.profile-actions{

    justify-content:center;

}

}

</style>

<script>
import axios from 'axios'

export default {
  name: 'UserBrowseTreks',
  data() {

    return {

        user: {},

        editing:false,

        selectedImage:null,
        originalUser: {}

    }

},
    mounted(){

    this.fetchProfile();

},

methods: {
    selectProfilePicture(event){

    const file = event.target.files[0];

    if(!file){

        return;

    }

    this.selectedImage=file;

    this.user.profile_picture = URL.createObjectURL(file);

},

async fetchProfile(){

    try{

        const response = await axios.get(

            "http://127.0.0.1:5000/api/user/profile",

            {

                headers:{

                    Authorization:`Bearer ${localStorage.getItem("access_token")}`

                }

            }

        );

        this.user = response.data.data;
        this.originalUser = JSON.parse(JSON.stringify(this.user));

    }

    catch(error){

        console.error(error);

    }

},

cancelEdit(){

    this.user = JSON.parse(JSON.stringify(this.originalUser));

    this.selectedImage = null;

    this.editing = false;

},

async saveProfile(){

    try{

        const formData = new FormData();

        formData.append(

            "full_name",

            this.user.full_name

        );

        formData.append(

            "mobile_number",

            this.user.mobile_number

        );

        formData.append(

            "city",

            this.user.city

        );

        formData.append(

            "state",

            this.user.state

        );

        formData.append(

            "emergency_contact_name",

            this.user.emergency_contact_name

        );

        formData.append(

            "emergency_contact_number",

            this.user.emergency_contact_number

        );

        if(this.selectedImage){

            formData.append(

                "profile_picture",

                this.selectedImage

            );

        }

        await axios.put(

            "http://127.0.0.1:5000/api/user/profile",

            formData,

            {

                headers:{

                    Authorization:`Bearer ${localStorage.getItem("access_token")}`

                }

            }

        );

        await this.fetchProfile();

        this.editing=false;

        alert("Profile Updated Successfully.");

    }

    catch(error){

        console.error(error);

    }

}
},

computed:{

    profileImage(){

        if(

            this.user.profile_picture?.startsWith("blob:")

        ){

            return this.user.profile_picture;

        }

        if(

            !this.user.profile_picture ||

            this.user.profile_picture==="default_profile.png"

        ){

            return "http://127.0.0.1:5000/static/profile_uploads/default_profile.png";

        }

        return `http://127.0.0.1:5000/static/profile_uploads/${this.user.profile_picture}`;

    }

}

}
</script>
