<template>

<div class="staff-profile-page">

    <!-- ==========================================
            FIXED BACKGROUND
    ========================================== -->
    <div class="page-background"></div>

    <!-- ==========================================
        SIDEBAR
========================================== -->

<aside class="sidebar">

    <!-- Logo -->

    <div class="sidebar-logo">
        <i class="bi bi-tree-fill logo-icon"></i>
        <h2 class="logo-text">
            TREKMATE
        </h2>

    </div>

    <!-- Navigation -->

    <nav class="sidebar-menu">

        <router-link
            to="/staff-dashboard"
            class="menu-item"
        >
            <i class="bi bi-grid-1x2-fill"></i>
            <span>Dashboard</span>
        </router-link>

        <router-link
            to="/staff-treks"
            class="menu-item"
        >
            <i class="bi bi-signpost-2-fill"></i>
            <span>Treks</span>
        </router-link>

        <router-link
            to="/staff-participants"
            class="menu-item"
        >
            <i class="bi bi-person-circle"></i>
            <span>Participants</span>
        </router-link>

        <router-link
            to="/staff-profile"
            class="menu-item"
        >
            <i class="bi bi-people-fill"></i>
            <span>Profile</span>
        </router-link>

        <router-link
            to="/staff-summary"
            class="menu-item"
        >
            <i class="bi bi-bar-chart-fill"></i>
            <span>Summary</span>
        </router-link>

    </nav>

    <!-- Logout -->

    <div class="sidebar-footer">

        <router-link
            to="/login"
            class="menu-item"
        >
            <i class="bi bi-box-arrow-right"></i>
            <span>Logout</span>
        </router-link>

    </div>

</aside>

    <!-- ==========================================
            MAIN CONTENT
    ========================================== -->

    <main class="main-content">
        <div class="content-wrapper">

        <!-- Header -->
         <header class="page-header">

    <div class="header-left">

        <h1 class="page-title">
            Staff Management
        </h1>

        <p class="page-subtitle">
            Build a trusted team, assign responsibilities, and ensure every trek is led with confidence.
        </p>

    </div>

    <div class="header-right">

        <button class="create-btn" @click="$router.push('/admin-create-staff')">

            <i class="bi bi-plus-lg"></i>
            Create New Staff

        </button>

    </div>

</header>

<br><br><br>

<div>
<p class="staff-quote">
    "Behind every unforgettable expedition is a dedicated team turning every step into a safe adventure."
</p>
</div>

<br><br><br><br><br><br>

<!-- Basic Information -->
<section class="glass-card">
            <div class="section-title">
                <h3>
                    <i class="bi bi-geo-alt-fill"></i>
                    Basic Information</h3>
    <p>
        Enter the core details of your trekking expedition.
    </p>
</div>

<hr class="section-divider">

        <!-- BASIC INFORMATION BODY -->
         <div class="section-body">
            <!-- ==========================================
                            PERSONAL INFORMATION
                    ========================================== -->

                    <div class="profile-section">

                        <h3>

                            Personal Information

                        </h3>

                        <div class="info-grid">

                            <div class="info-item">

                                <label>Email</label>

                                <p>{{ staff.email }}</p>

                            </div>

                            <div class="info-item">

                                <label>Mobile Number</label>

                                <p>{{ staff.mobile_number }}</p>

                            </div>

                            <div class="info-item">

                                <label>Gender</label>

                                <p>{{ staff.gender }}</p>

                            </div>

                            <div class="info-item">

                                <label>Date of Birth</label>

                                <p>{{ staff.date_of_birth }}</p>

                            </div>

                            <div class="info-item">

                                <label>City</label>

                                <p>{{ staff.city }}</p>

                            </div>

                            <div class="info-item">

                                <label>State</label>

                                <p>{{ staff.state }}</p>

                            </div>

                        </div>

                    </div>
         </div>
</section>

<!-- Basic Information -->
<section class="glass-card">
            <div class="section-title">
                <h3>
                    <i class="bi bi-geo-alt-fill"></i>
                    Basic Information</h3>
    <p>
        Enter the core details of your trekking expedition.
    </p>
</div>

<hr class="section-divider">

        <!-- BASIC INFORMATION BODY -->
         <div class="section-body">
            <!-- ==========================================
                            PROFESSIONAL INFORMATION
                    ========================================== -->

                    <div class="profile-section">

                        <h3>

                            Professional Information

                        </h3>

                        <div class="info-grid">

                            <div class="info-item">

                                <label>Profession</label>

                                <p>{{ staff.profession }}</p>

                            </div>

                            <div class="info-item">

                                <label>Specialization</label>

                                <p>{{ staff.specialization }}</p>

                            </div>

                            <div class="info-item">

                                <label>Experience</label>

                                <p>{{ staff.experience_years }} Years</p>

                            </div>

                            <div class="info-item">

                                <label>Joining Date</label>

                                <p>{{ staff.joining_date }}</p>

                            </div>

                            <div class="info-item">

                                <label>Languages</label>

                                <p>{{ staff.languages_known }}</p>

                            </div>

                            <div class="info-item">

                                <label>Certifications</label>

                                <p>{{ staff.certifications }}</p>

                            </div>

                        </div>

                    </div>

         </div>
</section>

<!-- Basic Information -->
<section class="glass-card">
            <div class="section-title">
                <h3>
                    <i class="bi bi-geo-alt-fill"></i>
                    Basic Information</h3>
    <p>
        Enter the core details of your trekking expedition.
    </p>
</div>

<hr class="section-divider">

        <!-- BASIC INFORMATION BODY -->
         <div class="section-body">
            <!-- ==========================================
                            BIO
                    ========================================== -->

                    <div class="profile-section">

                        <h3>

                            About Me

                        </h3>

                        <p class="bio">

                            {{ staff.bio }}

                        </p>

                    </div>
         </div>
</section>

<!-- Basic Information -->
<section class="glass-card">
            <div class="section-title">
                <h3>
                    <i class="bi bi-geo-alt-fill"></i>
                    Basic Information</h3>
    <p>
        Enter the core details of your trekking expedition.
    </p>
</div>

<hr class="section-divider">

        <!-- BASIC INFORMATION BODY -->
         <div class="section-body">
            <!-- ==========================================
                            EMERGENCY CONTACT
                    ========================================== -->

                    <div class="profile-section">

                        <h3>

                            Emergency Contact

                        </h3>

                        <div class="info-grid">

                            <div class="info-item">

                                <label>Contact Person</label>

                                <p>

                                    {{ staff.emergency_contact_name }}

                                </p>

                            </div>

                            <div class="info-item">

                                <label>Phone Number</label>

                                <p>

                                    {{ staff.emergency_contact_number }}

                                </p>

                            </div>

                            <div class="info-item full-width">

                                <label>Address</label>

                                <p>

                                    {{ staff.address }}

                                </p>

                            </div>

                        </div>

                    </div>
         </div>
</section>

</div>







        <!-- Pagination -->
    </main>

</div>

</template>

<style scoped>
/*==================================================
GLOBAL
==================================================*/

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

.staff-profile-page{
    min-height:100vh;
    display:flex;
    position:relative;
    overflow:hidden;
}

.page-background{

    position:fixed;

    inset:0;

    background:
        linear-gradient(
            rgba(255,255,255,.72),
            rgba(255,255,255,.78)
        ),
        url("@/assets/images/staff-bg.jpg");

    background-size:cover;

    background-position:center;

    background-attachment:fixed;

    z-index:-2;

}


/*==================================================
SIDEBAR
==================================================*/

.sidebar{

    width:260px;

    height:100vh;

    background:#670626;

    position:fixed;

    left:0;

    top:0;

    display:flex;

    flex-direction:column;

    justify-content:space-between;

    padding:35px 22px;

    box-shadow:
    10px 0 40px rgba(0,0,0,.18);

}


/* ==========================================
   LOGO
========================================== */
.sidebar-logo{

    display:flex;

    align-items:center;

    gap:18px;

    margin:30px 0 55px 0;

    position:relative;

    padding-bottom:30px;

}



.logo-icon{

    color:white;

    font-size:1.8rem;

    flex-shrink:0;

}

.logo-text{

    color:white;

    font-size:1.8rem;

    letter-spacing:2.5px;

    margin:0;

    white-space:nowrap;

    font-weight:700;

}



/*==================================================
MENU
==================================================*/

.sidebar-menu{

    display:flex;

    flex-direction:column;

    gap:12px;

    flex:1;
    background:#670626;
    font-family:"Your Premium Heading Font", serif;
    letter-spacing: 1.5px;

}

.menu-item{

    display:flex;

    align-items:center;

    gap:18px;

    padding:15px 18px;

    border-radius:18px;

    color:white;

    text-decoration:none;

    transition:.35s ease;

    font-size:1.15rem;

    font-weight:500;

    position:relative;

}

.menu-item i{

    font-size:1.25rem;

    width:28px;

    text-align:center;

}



/*==================================================
HOVER
==================================================*/
.menu-item:hover{
    background:#c5e4a1;

backdrop-filter:blur(18px);

border:1px solid rgba(255,255,255,.35);
    color:white;
    transform:translateX(4px);
}

.menu-item:hover i{

    color:white;

}


/*==================================================
ACTIVE
==================================================*/

.menu-item.active{

    background:rgba(255,255,255,.10);

}

.menu-item.active::before{

    content:"";

    position:absolute;

    left:-22px;

    top:12px;

    width:5px;

    height:34px;

    background:#BAD797;

    border-radius:10px;

}


/*==================================================
FOOTER
==================================================*/

.sidebar-footer{

    padding-top:25px;

    border-top:1px solid rgba(255,255,255,.12);

}


/*==================================================
MAIN CONTENT
==================================================*/

.main-content{

    flex:1;
    margin-left:240px;
    padding:35px;

}

/* ==========================================
   HEADER
========================================== */

.page-header{

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:26px 36px;

    margin-bottom:35px;

    border-radius:26px;

    background:rgba(218, 240, 190, 0.65);

    backdrop-filter:blur(16px);

    border:1px solid rgba(255,255,255,.25);

    box-shadow:0 10px 35px rgba(0,0,0,.08);

}

.page-title{

    font-family:"Your Premium Heading Font", serif;

    font-size:3rem;

    color:#670626;

    margin:0;

    letter-spacing:2px;
    font-weight: 500;

}

.page-subtitle{
    font-family:"Your Premium Heading Font", serif;
    letter-spacing: 1px;
    margin-top:10px;

    color:#4d4d4d;

    font-size:1rem;

    opacity:.8;

}

.trek-quote{

    font-family:"BrotherSignature", cursive;

    font-size:3.2rem;

    color:#670626;

    font-weight:400;

    line-height:1.3;

    letter-spacing:1.4px;

    opacity:.92;

    margin-top:18px;
    text-align: center;


}

/* ==========================================================
GLASS CARD
========================================================== */
.section-title{
    font-family:"Your Premium Heading Font", serif;
    color:#670626;
    font-size:2.5rem;

    margin:0;

    letter-spacing:1px;
    font-weight: 500;

}


.glass-card{

    background:rgba(255,255,255,0.22);

    backdrop-filter:blur(22px);

    -webkit-backdrop-filter:blur(22px);

    border:1px solid rgba(255,255,255,.35);

    border-top:5px solid #BAD797;

    border-radius:30px;

    padding:28px 40px;

    margin-bottom:40px;

    box-shadow:
        0 20px 45px rgba(0,0,0,.08);

    transition:.35s ease;

}

.glass-card:hover{

    transform:translateY(-4px);

    box-shadow:
        0 28px 60px rgba(0,0,0,.12);

}

.glass-card .col-md-6{
    margin-bottom:20px;
}

/* ==========================================================
SECTION HEADER
========================================================== */

.section-title{

    margin-bottom:15px;

}

.section-title h3{

    display:flex;

    align-items:center;

    gap:12px;

    font-size:2rem;

    color:#670626;

    margin-bottom:8px;

    font-weight:700;

}

.section-title i{

    color:#670626;

    font-size:1.6rem;

}

.section-title p{

    color:#666;

    font-size:1rem;

    margin:0;

}

/* ==========================================================
SECTION DIVIDER
========================================================== */

.section-divider{

    border:none;

    border-top:1px solid rgba(103,6,38,.15);

    margin:18px 0 24px;

}


/* ==========================================================
SECTION BODY
========================================================== */

.section-body{

    width:100%;

}


</style>

<script>

import axios from "axios"

export default{

    name:"StaffProfile",

    data(){

        return{

            staff:{}

        }

    },

    mounted(){

        this.fetchProfile()

    },

    methods:{

        async fetchProfile(){

            try{

                const user = JSON.parse(

                    localStorage.getItem("user")

                )

                const response = await axios.get(

                    `http://127.0.0.1:5000/api/staff/profile/${user.id}`

                )

                this.staff = response.data.data

            }

            catch(error){

                console.log(error)

            }

        }

    }

}

</script>