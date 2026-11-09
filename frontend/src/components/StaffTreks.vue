<template>

<div class="staff-treks-page">

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
            class="menu-item active"
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
            Treks Management
        </h1>

        <p class="page-subtitle">
            Manage your assigned trekking expeditions and participants.
        </p>

    </div>

</header>

<br><br><br>

<div>
<p class="trek-quote">
    "Every expedition becomes memorable when every guide leads with confidence."
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
            {{ assignedTreks }}
        </div>

        <div class="stat-title">
            Assigned Treks
        </div>

        <div class="stat-subtitle">
            Currently under supervision
        </div>

    </div>

    <!-- Upcoming Treks -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-calendar-event-fill"></i>
        </div>

        <div class="stat-number">
                {{ upcomingTreks }}
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
                {{ completedTreks }}
        </div>

        <div class="stat-title">
            Completed
        </div>

        <div class="stat-subtitle">
            Successfully guided expeditions
        </div>

    </div>

    <!-- Ongoing Slots -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-people-fill"></i>
        </div>

        <div class="stat-number">
                {{ totalParticipants }}
        </div>

        <div class="stat-title">
            Participants
        </div>

        <div class="stat-subtitle">
            Trekkers under guidance
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

            Assigned Treks

        </span>
        <p class="section-subtitle">
            Complete overview of your assigned trekking expeditions.
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
                    <th>Role</th>

                    <th>Duration</th>

                    <th>Slots</th>

                    <th>Status</th>

                    <th>Participants</th>

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
                        {{ trek.assigned_role }}
                     </td>

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

    <button class="view-btn" @click="viewTrek(trek.id)">

        <i class="bi bi-eye"></i>


    </button>
    <br>
    <button
class="completed-btn"
@click="completeTrek(trek.assignment_id)"
>
    Complete Trek
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

.staff-treks-page{
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

    background:#43302E;

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
    background:#43302E;
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
    background:#43302E;

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

    background:#FFF1B5;

    backdrop-filter:blur(16px);

    border:1px solid rgba(255,255,255,.25);

    box-shadow:0 10px 35px rgba(0,0,0,.08);

}

.page-title{

    font-family:"Your Premium Heading Font", serif;

    font-size:3rem;

    color:#43302E;

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

    background:#43302E;

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

    color:#43302E;

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

    background:rgba(255,241,181,.35);

}

.stat-card:hover{

    transform:translateY(-6px);

    box-shadow:0 18px 45px rgba(0,0,0,.15);

}

.stat-icon{

    font-size:2rem;

    color:#43302E;

    margin-bottom:18px;

}

.stat-number{
    font-size:3rem;
    font-weight:700;
    color:#43302E;
    margin-bottom:8px;
    line-height: 1;
}

.stat-number .h3{
    font-size:3.2rem;
    font-weight:700;
    color:#43302E;
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
    color:#43302E;
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

    color:#43302E;

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

    color:rgba(255,241,181,.35);

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

    color:#43302E;

    transition:.3s;
    font-size:1.2rem;

}

.search-box:focus-within i{

    color:#43302E;

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

    background:#43302E;
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

    color:#43302E;

}

.filter-group select:focus{

    background:white;

    color:#43302E;

    box-shadow:0 8px 25px rgba(0,0,0,.08);

}

.result-count{

    width:120px;

    text-align:center;

    font-size:2rem;

    font-weight:700;

    color:#43302E;

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

    width:100%;

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
    color:#43302E;
    font-size:2.6rem;
    margin:0;
    letter-spacing:1.2px;
    font-weight: 500;
    width: 80%;
}

.view-btn{

    background:white;

    color:#43302E;
    width:50px;

}

.view-btn:hover{

    background:rgb(241, 242, 233);

    transform:translateY(-3px);

}

.completed-btn{
    background:#ebf3bb;

    color:black;
    width: 90px;
    padding:8px;
}
.completed-btn:hover{
    background:black;

    color:white;

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

    name:"StaffTreks",

    data(){

        return{

            treks:[],

            search:"",

            difficultyFilter:"",

            statusFilter:""

        }

    },

    mounted(){

        this.fetchTreks()

    },

    methods:{

        // ==========================================
        // FETCH ASSIGNED TREKS
        // ==========================================

        async fetchTreks(){

            try{

                const user = JSON.parse(
                    localStorage.getItem("user")
                )

                const response = await axios.get(

                    `http://127.0.0.1:5000/api/staff/treks/${user.id}`

                )

                this.treks = response.data.data

            }

            catch(error){

                console.log(error)

            }

        },

        // ==========================================
        // VIEW TREK
        // ==========================================

        viewTrek(id){

            this.$router.push(

                `/staff-view-trek/${id}`

            )

        },

        // ==========================================
        // VIEW PARTICIPANTS
        // ==========================================

        viewParticipants(id){

            this.$router.push(

                `/staff-participants/${id}`

            )

        },

        async completeTrek(assignmentId) {

    if (!confirm("Mark this trek as completed?")) return

    try {

        const token = localStorage.getItem("access_token")

        const response = await axios.put(

            `http://127.0.0.1:5000/api/staff/complete-trek/${assignmentId}`,

            {},

            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }

        )

        alert(response.data.message)

        this.fetchTreks()

    }

    catch(error){

        alert(error.response.data.message)

    }

}

    },

    

    computed:{

        // ==========================================
        // FILTERED TREKS
        // ==========================================

        filteredTreks(){

            return this.treks.filter(trek=>{

                const matchesSearch =

                    trek.trek_name.toLowerCase().includes(

                        this.search.toLowerCase()

                    ) ||

                    trek.location.toLowerCase().includes(

                        this.search.toLowerCase()

                    )

                const matchesDifficulty =

                    this.difficultyFilter=="" ||

                    trek.difficulty==this.difficultyFilter

                const matchesStatus =

                    this.statusFilter=="" ||

                    trek.status==this.statusFilter

                return(

                    matchesSearch &&

                    matchesDifficulty &&

                    matchesStatus

                )

            })

        },

        // ==========================================
        // SUMMARY CARDS
        // ==========================================

        assignedTreks(){

            return this.treks.length

        },

        upcomingTreks(){

            return this.treks.filter(

                trek=>trek.status=="Upcoming"

            ).length

        },

        completedTreks(){

            return this.treks.filter(

                trek=>trek.status=="Completed"

            ).length

        },

        totalParticipants(){

            return this.treks.reduce(

                (total,trek)=>

                total+trek.booking_count,

                0

            )

        }

    }

}

</script>
