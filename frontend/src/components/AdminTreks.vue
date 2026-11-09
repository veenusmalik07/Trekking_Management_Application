<template>

<div class="admin-treks-page">

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
            Treks Management
        </h1>

        <p class="page-subtitle">
            Manage, organize and monitor all trekking expeditions.
        </p>

    </div>

    <div class="header-right">

        <button class="create-btn" @click="$router.push('/admin-create-trek')">

            <i class="bi bi-plus-lg"></i>
            Create New Trek

        </button>

    </div>

</header>

<br><br><br>

<div>
<p class="trek-quote">
    "Every great adventure begins with careful planning."
</p>
</div>

<br><br><br><br><br><br>

        <!-- Statistics -->

<section class="stats-section">

    <!-- Total Treks -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-signpost-2-fill"></i>
        </div>

        <div class="stat-number">
            {{ treks.length }}
        </div>

        <div class="stat-title">
            Total Treks
        </div>

        <div class="stat-subtitle">
            Registered
        </div>

    </div>

    <!-- Upcoming Treks -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-calendar-event-fill"></i>
        </div>

        <div class="stat-number">
                {{
                    treks.filter(
                        t=>t.status=="Upcoming"
                    ).length
                }}
        </div>

        <div class="stat-title">
            Upcoming
        </div>

        <div class="stat-subtitle">
            Awaiting start
        </div>

    </div>

    <!-- CLOSED TREKS -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-journal-check"></i>
        </div>

        <div class="stat-number">
                {{
                    treks.filter(
                        t=>t.status=="Completed"
                    ).length
                }}
        </div>

        <div class="stat-title">
            Closed
        </div>

        <div class="stat-subtitle">
            Completed
        </div>

    </div>

    <!-- Ongoing Slots -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-people-fill"></i>
        </div>

        <div class="stat-number">
                {{
                    treks.filter(
                        t=>t.status=="Ongoing"
                    ).length
                }}
        </div>

        <div class="stat-title">
            Ongoing Slots
        </div>

        <div class="stat-subtitle">
            Currently active
        </div>

    </div>

</section>

<br><br><br><br>

<!-- ====================================================
                TOP PERFORMING TREKS
==================================================== -->

<section class="top-treks-section">

    <div class="section-header">

        <div>

            <h2 class="section-title">

                Top Performing Treks

            </h2>

            <p class="section-subtitle">

                Discover the highest booked trekking adventures.

            </p>

        </div>


    </div>

    <div class="top-treks-slider">

        <div
            class="top-trek-card"
            v-for="trek in popularTreks"
            :key="trek.id"
        >

            <!-- Cover Image -->

            <img
                :src="trek.cover_image"
                class="trek-image"
            >

            <!-- Overlay -->

            <div class="trek-overlay">

                <span class="booking-chip">

                    ★ {{ trek.booking_count }} Bookings

                </span>

            </div>

            <!-- Body -->

            <div class="trek-body">

                <h4>

                    {{ trek.trek_name }}

                </h4>

                <p>

                    <i class="bi bi-geo-alt-fill"></i>

                    {{ trek.location }}

                </p>

                <div class="trek-details">

                    <span>

                        ₹ {{ trek.price }}

                    </span>

                    <span>

                        {{ trek.duration }} Days

                    </span>

                </div>

                <div class="trek-details">

                    <span>

                        {{ trek.difficulty }}

                    </span>

                    <span>

                        {{ trek.available_slots }}/{{ trek.capacity }}

                    </span>

                </div>

                <div class="trek-actions">

                    <button @click="$router.push(`/admin-view-trek/${trek.id}`)">

                        <i class="bi bi-eye"></i>

                    </button>

                    <button @click="$router.push(`/admin-edit-trek/${trek.id}`)">

                        <i class="bi bi-pencil"></i>

                    </button>

                    <button @click="deleteTrek(trek.id)">

                        <i class="bi bi-trash"></i>

                    </button>

                </div>

            </div>

        </div>

    </div>

</section>

<br><br><br>

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
            placeholder="Search by trek name or location..."
        >

    </div>

    <div class="filter-group">

        <select v-model="difficultyFilter">

            <option value="">All Difficulty</option>

            <option value="Easy">Easy</option>

            <option value="Moderate">Moderate</option>

            <option value="Hard">Hard</option>

        </select>

        <select v-model="statusFilter">

            <option value="">All Status</option>

            <option value="Upcoming">Upcoming</option>

            <option value="Ongoing">Ongoing</option>

            <option value="Completed">Completed</option>
            <option value="Cancelled">Cancelled</option>

        </select>

    </div>

    <div class="result-count">

        {{ filteredTreks.length }}

        <span>Treks Found</span>

    </div>

</section>


        <!-- Table -->
         <!-- =====================================================
TREKS TABLE
===================================================== -->

<section class="trek-table-section">

    <div class="table-header">

        <span>

            Trek Management

        </span>
        <p class="section-subtitle">
    Complete overview of all trekking expeditions and their current status.
</p>
        

    </div>

    <div class="table-wrapper">

        <table class="trek-table">

            <thead>

                <tr>

                    <th>Cover</th>

                    <th>Trek</th>

                    <th>State</th>

                    <th>Difficulty</th>

                    <th>Duration</th>

                    <th>Slots</th>

                    <th>Price</th>

                    <th>Status</th>

                    <th>Bookings</th>

                    <th>Actions</th>

                </tr>

            </thead>

            <tbody>

                <tr
                    v-for="trek in filteredTreks"
                    :key="trek.id"
                >

                    <!-- Cover -->

                    <td>

                        <img
                            :src="trek.cover_image"
                            class="table-cover"
                        >

                    </td>

                    <!-- Name -->

                    <td>

                        <div class="table-name">

                            {{ trek.trek_name }}

                        </div>

                    </td>

                    <!--STATE-->
                    <td>
                        <div>
                            {{ trek.state }}
                        </div>
                    </td>

                    <!-- Difficulty -->

                    <td>

                        <span
                            class="difficulty-pill"
                            :class="trek.difficulty.toLowerCase()"
                        >

                            {{ trek.difficulty }}

                        </span>

                    </td>

                    <!-- Duration -->

                    <td>

                        {{ trek.duration }} Days

                    </td>

                    <!-- Slots -->

                    <td>

                        {{ trek.available_slots }}/{{ trek.capacity }}

                    </td>

                    <!-- Price -->

                    <td>

                        ₹{{ trek.price }}

                    </td>

                    <!-- Status -->

                    <td>

                        <span
                            class="status-pill"
                            :class="trek.status.toLowerCase()"
                        >

                            {{ trek.status }}

                        </span>

                    </td>

                    <!-- Bookings -->

                    <td>

                        {{ trek.booking_count }}

                    </td>

                    <!-- Actions -->

                    <td>

                        <div class="table-actions">

    <button class="view-btn" @click="$router.push(`/admin-view-trek/${trek.id}`)">

        <i class="bi bi-eye"></i>


    </button>

    <button class="edit-btn" @click="$router.push(`/admin-edit-trek/${trek.id}`)">

        <i class="bi bi-pencil"></i>

    </button>

    <button class="delete-btn"@click="deleteTrek(trek.id)">

        <i class="bi bi-trash"></i>

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

.admin-treks-page{
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

    overflow-x:auto;

}

.trek-table{

    width:90%;

    min-width:800px;

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
    width: 80%;
}

.view-btn{

    background:white;

    color:#670626;

}

.view-btn:hover{

    background:rgb(241, 242, 233);

    transform:translateY(-3px);

}

.edit-btn{

    background:rgb(6, 114, 6);

    color:white;

}

.edit-btn:hover{

    background:#1c3f01;

    transform:translateY(-3px);

}

.delete-btn{

    background:#ea0b0b;

    color:white;

}

.delete-btn:hover{

    background:#5c0202;

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


</style>

<script>

import axios from "axios"

export default{

    name:"AdminTreks",

    data(){

        return{
            treks:[],
            search: "",
            difficultyFilter: "",
            statusFilter: ""


        }

    },

    mounted(){

        this.fetchTreks()

    },

    methods:{

        // ==========================================
        // FETCH TREKS
        // ==========================================

        async fetchTreks(){

    try{

        const response = await axios.get(
            "http://127.0.0.1:5000/api/admin/treks"
        )

        console.log("Response:", response.data)

        this.treks = response.data.data

        console.log("Treks Array:", this.treks)

        console.log("Treks Length:", this.treks.length)

    }

    catch(error){

        console.log(error)

    }

},
viewTrek(id) {
        this.$router.push(`/admin-view-trek/${id}`);
    },

    editTrek(id) {
        this.$router.push(`/admin-edit-trek/${id}`);
    },
     async deleteTrek(id) {

        if (!confirm("Are you sure you want to delete this trek?")) {
            return;
        }

        try {

            const token = localStorage.getItem("access_token");

            await axios.delete(
                `http://127.0.0.1:5000/api/admin/delete-trek/${id}`,
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            );
            alert("✅ Trek deleted successfully!");
            this.fetchTreks();   // Reload the table

        }

        catch (error) {

            console.error(error);
            alert(error.response?.data?.message || "Unable to delete this trek. Please try again.");

        }

    }

    },



    computed:{

        filteredTreks() {

        return this.treks.filter(trek => {

            const matchesSearch =
    !this.search ||
    trek.trek_name.toLowerCase().includes(this.search.toLowerCase()) ||
    trek.state.toLowerCase().includes(this.search.toLowerCase());

const matchesDifficulty =
    !this.difficultyFilter ||
    trek.difficulty === this.difficultyFilter;

const matchesStatus =
    !this.statusFilter ||
    trek.status === this.statusFilter;

            return matchesSearch && matchesDifficulty && matchesStatus;

        });

    },



    popularTreks(){

        return [...this.treks]

            .sort((a,b)=>b.booking_count-a.booking_count)

            .slice(0,3)

    },



    maxBookings(){

        if(this.treks.length===0){

            return 0

        }

        return Math.max(

            ...this.treks.map(

                trek=>trek.booking_count

            )

        )

    }

    }

}

</script>
