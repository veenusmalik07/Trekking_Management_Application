<template>

<div class="admin-staff-page">

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
            to="/admin-dashboard"
            class="menu-item"
        >
            <i class="bi bi-grid-1x2-fill"></i>
            <span>Dashboard</span>
        </router-link>

        <router-link
            to="/admin-treks"
            class="menu-item"
        >
            <i class="bi bi-signpost-2-fill"></i>
            <span>Treks</span>
        </router-link>

        <router-link
            to="/admin-users"
            class="menu-item"
        >
            <i class="bi bi-people-fill"></i>
            <span>Users</span>
        </router-link>

        <router-link
            to="/admin-staff"
            class="menu-item"
        >
            <i class="bi bi-person-workspace"></i>
            <span>Staff</span>
        </router-link>

        <router-link
            to="/admin-bookings"
            class="menu-item"
        >
            <i class="bi bi-journal-check"></i>
            <span>Bookings</span>
        </router-link>

        <router-link
            to="/admin-summary"
            class="menu-item"
        >
            <i class="bi bi-bar-chart-fill"></i>
            <span>Summary</span>
        </router-link>

    </nav>

    <!-- Logout -->

    <div class="sidebar-footer">

        <router-link
            to="/"
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

        <!-- Statistics -->

<section class="stats-section">

    <!-- Total staff -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-people-fill"></i>
        </div>

        <div class="stat-number">
            {{ staff.length }}
        </div>

        <div class="stat-title">
            Total Staff
        </div>

        <div class="stat-subtitle">
            Registered
        </div>

    </div>

    <!-- active staff -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-check-circle-fill"></i>
        </div>

        <div class="stat-number">
                {{ staff.filter(s => s.account_status=="Active").length }}
        </div>

        <div class="stat-title">
            Active Staff
        </div>

        <div class="stat-subtitle">
            Currently working
        </div>

    </div>

    <!-- inactive staff -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-check-circle-fill"></i>
        </div>

        <div class="stat-number">
                {{ staff.filter(s => s.account_status=="InActive").length }}
        </div>

        <div class="stat-title">
            InActive Staff
        </div>

        <div class="stat-subtitle">
            Currently not working
        </div>

    </div>

    <!-- absent -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-calendar-x-fill"></i>
        </div>

        <div class="stat-number">
                {{ staff.filter(s => s.availability == "On Leave").length }}
        </div>

        <div class="stat-title">
            On Leave
        </div>

        <div class="stat-subtitle">
            Temporarily Unavailable
        </div>

    </div>

    <!-- guides -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-person-walking"></i>
        </div>

        <div class="stat-number">
                {{ staff.filter(s=>s.profession=="Trek Guide").length }}
        </div>

        <div class="stat-title">
            Trek Guide
        </div>

        <div class="stat-subtitle">
            Guides
        </div>

    </div>

    <!-- trek leader -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-person-walking"></i>
        </div>

        <div class="stat-number">
                {{ staff.filter(s=>s.profession=="Trek Leader").length }}
        </div>

        <div class="stat-title">
            Trek Leader
        </div>

        <div class="stat-subtitle">
            Leaders
        </div>

    </div>

    <!-- coordinator -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-person-walking"></i>
        </div>

        <div class="stat-number">
                {{ staff.filter(s=>s.profession=="Coordinator").length }}
        </div>

        <div class="stat-title">
            Coordinator
        </div>

        <div class="stat-subtitle">
            Coordinates
        </div>

    </div>

    <!-- Photographer -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-person-walking"></i>
        </div>

        <div class="stat-number">
                {{ staff.filter(s=>s.profession=="Photographer").length }}
        </div>

        <div class="stat-title">
            Photographer
        </div>

        <div class="stat-subtitle">
            Photos
        </div>

    </div>

    <!-- medic -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-person-walking"></i>
        </div>

        <div class="stat-number">
                {{ staff.filter(s=>s.profession=="Medic").length }}
        </div>

        <div class="stat-title">
            Medical Expert
        </div>

        <div class="stat-subtitle">
            Medic
        </div>

    </div>

    <!-- rescue expert -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-person-walking"></i>
        </div>

        <div class="stat-number">
                {{ staff.filter(s=>s.profession=="Rescue Expert").length }}
        </div>

        <div class="stat-title">
            Rescue Expert
        </div>

        <div class="stat-subtitle">
            Rescues
        </div>

    </div>

</section>

<br><br><br><br>


        <!-- Search -->
         <!-- ==========================================================
SEARCH & FILTER SECTION
========================================================== -->

<section class="filter-section">

    <div class="search-box">

        <i class="bi bi-search"></i>

        <input
            type="text"
            v-model="search"
            placeholder="Search member..."
        >

    </div>

    <div class="filter-group">

        <select v-model="professionFilter">

            <option value="">Profession</option>

                        <option>Trek Guide</option>

                        <option>Medic</option>

                        <option>Photographer</option>

                        <option>Coordinator</option>

        </select>

        <select v-model="statusFilter">

            <option value="">Status</option>

                        <option>Active</option>

                        <option>On Leave</option>

                        <option>Inactive</option>

        </select>

    </div>

    <div class="result-count">

        {{ filteredStaff.length }}

        <span>Staff Found</span>

    </div>

</section>


        <!-- Table -->
         <!-- =====================================================
TREKS TABLE
===================================================== -->

<section class="trek-table-section">

    <div class="table-header">

        <span>
            Staff Directory
        </span>
        <p class="section-subtitle">
    Complete overview of all registered staff members and their assignments.
</p>
        

    </div>

    <div class="table-wrapper">

        <table class="trek-table">

            <thead>

                <tr>
                    <th>Email</th>
                        <th>Profession</th>
                        <th>Experience</th>
                        <th>Status</th>
                        <th>Availability</th>
                        <th>Assigned Treks</th>
                        <th>Actions</th>
                </tr>

            </thead>

            <tbody>

                <tr
                        v-for="member in filteredStaff"
                        :key="member.id"
                    >

                        <!-- EMAIL -->

                        <td>

                            {{ member.email }}

                        </td>

                        <!-- profession -->

                        <td>

                            {{ member.profession }}

                        </td>

                        <!-- EXPERIENCE -->

                        <td>

                            {{ member.experience_years }} Years

                        </td>

                        <!-- STATUS -->
                        <td>
                            <span class="status-badge"
                                :class="member.account_status=='Active'
                                ? 'status-active'
                                : member.account_status=='Blocked'
                                ? 'status-inactive'
                                : 'bg-secondary'"
                            >
                                {{ member.account_status }}
                            </span>
                        </td>

                        <!-- availability -->
                        <td>
                            <strong>
                                {{ member.availability }}

                            </strong>
                        </td>
                        

                        <!-- ASSIGNED TREKS -->

                        <td>

                            {{ member.assigned_treks }}

                        </td>

                    <!-- Actions -->

                    <td>

                        <div class="table-actions">

    <button class="view-btn" @click="$router.push('/admin-view-staff/'+member.id)">

        <i class="bi bi-eye"></i>
    </button>

</div>

                    </td>

                </tr>

            </tbody>

        </table>

    </div>

</section>

        <!-- Pagination -->
    </div>
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

.admin-staff-page{
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
        url("@/assets/images/admin-bg.jpg");

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

.create-btn{

    display:flex;

    align-items:center;

    gap:10px;

    padding:14px 28px;

    border:none;

    border-radius:18px;

    background:#670626;

    color:#fff;

    font-weight:600;

    transition:.3s ease;

    box-shadow:0 10px 25px rgba(103,6,38,.18);

    cursor:pointer;

}

.create-btn:hover{

    transform:translateY(-2px);
    background: white;
    color:#7b0a31;
    border-color: #7b0a31;
}

.create-btn i{

    font-size:1.1rem;

}

.staff-quote{

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

/*==================================================
STATISTICS
==================================================*/

.stats-section{

    display:grid;

    grid-template-columns:repeat(4,1fr);

    gap:24px;

    margin-bottom:40px;

}

.stat-card{

    position:relative;

    overflow:hidden;

    padding:28px;

    border-radius:24px;

    background:rgba(255,255,255,.16);

    backdrop-filter:blur(18px);

    -webkit-backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,.28);

    box-shadow:0 12px 35px rgba(0,0,0,.08);

    transition:.35s ease;
    display:flex;

    flex-direction:column;

    justify-content:center;

    align-items:center;

    text-align:center;

}


.stat-card::before{

    content:"";

    position:absolute;

    top:0;

    left:0;

    width:100%;

    height:4px;

    background:#BAD797;

}

.stat-card:hover{

    transform:translateY(-6px);

    box-shadow:0 18px 45px rgba(0,0,0,.15);

}

.stat-icon{

    font-size:2rem;

    color:#670626;

    margin-bottom:18px;

}

.stat-number{
    font-size:3rem;
    font-weight:700;
    color:#670626;
    margin-bottom:8px;
    line-height: 1;
}

.stat-number .h3{
    font-size:3.2rem;
    font-weight:700;
    color:#670626;
    margin-bottom:14px;
    line-height: 1;
}

.stat-title{

    font-size:1.15rem;

    font-weight:600;

    color:#2d2d2d;

    margin-bottom:8px;
    font-family:"Your Premium Heading Font", serif;
    letter-spacing: 1.1px;

}

.stat-subtitle{

    font-size:.92rem;

    color:#666;

}

/*==================================================
TOP TREKS
==================================================*/

.top-treks-section{

    margin-bottom:45px;

}

.section-header{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:25px;

}

.section-title{
    font-family:"Your Premium Heading Font", serif;
    color:#670626;
    font-size:2.5rem;

    margin:0;

    letter-spacing:1px;
    font-weight: 500;

}

.section-subtitle{
    font-family:"Your Premium Heading Font", serif;

    color:#666;
    letter-spacing: 1px;

    margin-top:6px;

    margin-bottom:0;

    font-size:.95rem;

}


/*==================================================
SLIDER
==================================================*/

.top-treks-slider{

    display:flex;

    gap:24px;

    overflow-x:auto;

    scroll-behavior:smooth;

    padding-bottom:10px;

}

.top-treks-slider::-webkit-scrollbar{

    display:none;

}

/*==================================================
CARD
==================================================*/
.top-trek-card{

    width:340px;

    max-width:340px;

    overflow:hidden;

    border-radius:28px;

    background:rgba(255,255,255,.18);

    backdrop-filter:blur(20px);

    -webkit-backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,.25);

    box-shadow:0 20px 40px rgba(0,0,0,.12);

    transition:.35s;

    position:relative;

    padding:10px;

}

.top-trek-card:hover{

    transform:translateY(-8px);

    box-shadow:0 28px 55px rgba(0,0,0,.16);

}

/*==================================================
IMAGE
==================================================*/
.trek-image{

    width:100%;

    height:240px;

    display:block;

    object-fit:cover;

    border-radius:28px 28px 0 0;

}

/*==================================================
OVERLAY
==================================================*/

.trek-overlay{

    position:absolute;

    top:18px;

    right:18px;

}

.booking-chip{

    padding:10px 18px;

    border-radius:40px;

    background:rgba(255,255,255,.18);

    backdrop-filter:blur(20px);

    color:white;

    font-weight:600;
    font-size:.85rem;

    border:1px solid rgba(255,255,255,.25);

}

/*==================================================
BODY
==================================================*/

.trek-body{
    padding:24px 26px 28px;
}


.trek-body h4{

    font-size:1.45rem;

    color:#670626;

    margin-bottom:12px;

    font-weight:700;

}


.trek-body p{

    color:#555;

    margin-bottom:18px;

    display:flex;

    align-items:center;

    gap:8px;

}

.trek-details{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:14px;

    font-weight:600;

    color:#444;

}

/*==================================================
BUTTONS
==================================================*/

.trek-actions{

    display:flex;

    justify-content:space-between;

    margin-top:28px;

}
 
.trek-actions button{

    width:56px;

    height:56px;

    border:none;

    border-radius:16px;

    background:#b0d483;

    color:white;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:1.15rem;

    transition:.35s;

    cursor:pointer;

    box-shadow:0 10px 25px rgba(103,6,38,.25);

}

.trek-actions button:hover{

    background:white;

    color:#71904c;

    transform:translateY(-4px);

}

/*==================================================
FILTER SECTION
==================================================*/

.filter-section{

    margin:50px 0;

    display:flex;

    align-items:center;

    justify-content:space-between;

    gap:25px;

    padding:22px 28px;

    border-radius:26px;

    background:rgba(255,255,255,.18);

    backdrop-filter:blur(20px);

    -webkit-backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,.25);

}

.search-box{

    flex:1;

    display:flex;

    align-items:center;

    gap:15px;

    padding:16px 22px;

    border-radius:18px;

    background:rgba(255,255,255,.22);

    transition:.35s ease;

}

.search-box:focus-within{

    background:white;
    color:black;

    box-shadow:0 10px 30px rgba(0,0,0,.08);

}


.search-box i{

    color:#670626;

    transition:.3s;
    font-size:1.2rem;

}

.search-box:focus-within i{

    color:#670626;

}

.search-box input{

    width:100%;

    border:none;

    outline:none;

    background:transparent;

    color:#666;

    font-size:1rem;

    transition:.3s;

}
.search-box input::placeholder{

    color:#777;

}
.search-box input:focus{

    color:#000;

}

.search-box input:focus::placeholder{

    color:#999;

}

.filter-group{

    display:flex;

    gap:15px;

}

.filter-group select{

    background:#670626;
    width:180px;

    color:white;

    border:none;
    outline:none;

    border-radius:16px;

    padding:15px 18px;

    font-weight:600;

    transition:.3s;

    cursor:pointer;

}
.filter-group select:hover{

    background:white;

    color:#670626;

}

.filter-group select:focus{

    background:white;

    color:#670626;

    box-shadow:0 8px 25px rgba(0,0,0,.08);

}

.result-count{

    width:120px;

    text-align:center;

    font-size:2rem;

    font-weight:700;

    color:#670626;

}

.result-count span{

    display:block;

    margin-top:4px;

    font-size:.9rem;

    font-weight:500;

    color:#555;

}

/*=========================================
TABLE HEADER
=========================================*/
.table-wrapper{

    width:100%;
    max-width:1400px;

    overflow-x:auto;

}

.trek-table{
     width:100%;
    border-collapse:separate;
    border-spacing:0 18px;

}

.table-name + small{

    color:#666;

    font-size:.85rem;

}

.trek-table thead{

    background:#b0d483;

}

.trek-table thead th{

    color:white;

    font-weight:700;

    font-size:1.2rem;

    letter-spacing:1px;

    padding:20px;

    border:none;

    text-align:center;
    font-family:"Your Premium Heading Font", serif;

}

.trek-table thead th:first-child{

    border-radius:20px 0 0 20px;

}

.trek-table thead th:last-child{

    border-radius:0 20px 20px 0;

}

.trek-table tbody td{

    padding:24px 18px;

    vertical-align:middle;

}

.trek-table th,
.trek-table td{

    text-align:center;

    vertical-align:middle;

}

.trek-table tbody tr{

    transition:.3s;

}

.trek-table tbody tr:hover{

    background:rgba(255,255,255,.18);

}

.table-cover{

    width:70px;

    height:70px;

    object-fit:cover;

    border-radius:16px;

    box-shadow:0 8px 20px rgba(0,0,0,.15);

}

.table-actions{

    display:flex;

    justify-content:center;

    gap:12px;

}


.table-actions button{

    width:42px;

    height:42px;

    border:none;

    border-radius:12px;

    display:flex;

    align-items:center;

    justify-content:center;

    cursor:pointer;

    transition:.3s ease;

    font-size:1rem;

    box-shadow:0 10px 20px rgba(0,0,0,.12);

}

.trek-table-section{
    width: 100%;
}

.trek-table-section .table-header{
    font-family:"Your Premium Heading Font", serif;
    color:#670626;
    font-size:2.6rem;
    margin:0;
    letter-spacing:1.2px;
    font-weight: 500;
    width: 100%;
}

.view-btn{

    background:white;

    color:#670626;

}

.view-btn:hover{

    background:rgb(241, 242, 233);

    transform:translateY(-3px);

}

.status-pill{

    padding:8px 18px;

    border-radius:30px;

    font-size:.85rem;

    font-weight:600;

}

.status-pill.upcoming{

    background:#badbe7;

    color:black;

}

.status-pill.completed{

    background:#ebf3bb;

    color:black;

}

.status-pill.ongoing{

    background:#b2ecd4;

    color:black;

}

.status-pill.cancelled{

    background:#ecd1d3;

    color:black;

}

.easy{
    padding:8px 18px;

    border-radius:30px;

    font-size:.85rem;

    font-weight:600;

    background:#f4cfd1;

    color:black;

}

.moderate{
    padding:8px 18px;

    border-radius:30px;

    font-size:.85rem;

    font-weight:600;

    background:#cfc9ea;

    color:black;

}

.hard{
    padding:8px 18px;

    border-radius:30px;

    font-size:.85rem;

    font-weight:600;

    background:#baecb1;

    color:black;

}

/*active and inactive staff */
.status-badge {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 0.9rem;
    font-weight: 700;
    color: #fff;
    min-width: 90px;
    text-align: center;
    letter-spacing: 0.5px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}

/* Active = Yellow */
.status-active {
    background: #fafa15;       /* Yellow */
    color: #222;
}

/* Inactive = Red */
.status-inactive {
    background: #ec1919;       /* Red */
    color: #fff;
}

.status-badge:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(0,0,0,0.2);
}

</style>

<script>

import axios from "axios"

export default{

    name:"AdminStaff",

    data(){

        return{

            staff:[],

            search:"",

            professionFilter:"",

            statusFilter:""
        }

    },

    mounted(){

        this.fetchStaff()

    },

    methods:{

        async fetchStaff(){
            console.log(this.staff)

            try{

                const response = await axios.get(

                    "http://127.0.0.1:5000/api/admin/staff"

                )

                this.staff = response.data.data

            }

            catch(error){

                console.log(error)

            }

        }

    },

    computed:{

        filteredStaff(){

            return this.staff.filter(member=>{

                const matchesSearch =
                    member.email.toLowerCase().includes(this.search.toLowerCase()) ||
                    member.profession.toLowerCase().includes(this.search.toLowerCase()) ||
                    member.account_status.toLowerCase().includes(this.search.toLowerCase())
                const matchesProfession =
                    this.professionFilter=="" ||
                    member.profession==this.professionFilter

                const matchesStatus =
                    this.statusFilter=="" ||
                    member.account_status==this.statusFilter

                return matchesSearch &&
                       matchesProfession &&
                       matchesStatus
                                })

        }

    }

}

</script>