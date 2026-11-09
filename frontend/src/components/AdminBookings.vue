<template>

<div class="admin-bookings-page">
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

    <!-- ===================================================== -->
    <!-- PAGE HEADER -->
    <!-- ===================================================== -->
     <!-- ===================================================== -->
<!-- PAGE HEADER -->
<!-- ===================================================== -->
 <main class="main-content">
        <div class="content-wrapper">

        <!-- Header -->
         <header class="page-header">

    <div class="header-left">

        <h1 class="page-title">
            Bookings Management
        </h1>

        <p class="page-subtitle">
            Oversee your trekking community with confidence and precision.
        </p>

    </div>


</header>
        <br><br><br>

<div>
<p class="trek-quote">
    "A well-managed booking isn't just a reservation—it's the first step toward an unforgettable expedition."
</p>
</div>

<br><br><br><br>

<!-- Statistics -->

<section class="stats-section">

    <!-- Total Users -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-people-fill"></i>
        </div>

        <div class="stat-number">
            {{ summary.total }}
        </div>

        <div class="stat-title">
            Total Bookings
        </div>

        <div class="stat-subtitle">
            Every Trek Journey Starts Here
        </div>

    </div>

    <!-- ACTIVE USERS -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-person-check-fill"></i>
        </div>

        <div class="stat-number">
                {{ summary.pending }}
        </div>

        <div class="stat-title">
            Pending Bookings
        </div>

        <div class="stat-subtitle">
            Waiting for Admin Review
        </div>

    </div>




    <!-- accepted bookings -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-person-x-fill"></i>
        </div>

        <div class="stat-number">
                {{ summary.accepted }}
        </div>

        <div class="stat-title">
            Accepted Bookings
        </div>

        <div class="stat-subtitle">
            Ready for the Adventure
        </div>

    </div>



    <!-- rejected bookings -->

    <div class="stat-card">

        <div class="stat-icon">
            <i class="bi bi-person-plus-fill"></i>
        </div>

        <div class="stat-number">
                {{ summary.rejected }}
        </div>

        <div class="stat-title">
            Rejected Bookings
        </div>

        <div class="stat-subtitle">
            Requests Not Approved
        </div>

    </div>

</section>

<br><br><br><br>

<!-- ===================================================== -->
<!-- SEARCH & FILTER -->
<!-- ===================================================== -->

<section class="filter-section">

    <!-- Search -->

    <div class="search-box">

        <i class="bi bi-search"></i>

        <input
            type="text"
            v-model="search"
            placeholder="Search ..."
        >

    </div>
    <div class="filter-group">

    <select v-model="bookingStatusFilter">

    <option value="">Booking Status</option>

    <option>Pending</option>

    <option>Accepted</option>

    <option>Rejected</option>


</select>

    </div>

    <!-- User Count -->

    <div class="trek-count">

        <h2>{{ filteredBookings.length }}</h2>

        <span>Bookings Found</span>

    </div>

</section>
<br>

<section class="trek-table-section">

    <div class="table-header">

        <span class="page-title">

    Manage Bookings

</span>

<p class="page-subtitle">

    Complete overview of all registered trekkers and their account status.

</p>
        

    </div>

    <div class="table-wrapper">

       <table class="trek-table">

    <thead>

        <tr>

            <th>Booking Ref</th>

            <th>User</th>

            <th>Trek</th>

            <th>People</th>

            <th>Total Amount</th>


            <th>Booking</th>

            <th>Booked On</th>

            <th>Actions</th>

        </tr>

    </thead>

    <tbody>

        <tr
            v-for="booking in filteredBookings"
            :key="booking.id"
        >

            <!-- Booking Reference -->

            <td>

                {{ booking.booking_reference }}

            </td>

            <!-- User -->

            <td>

                {{ booking.user_name }}

            </td>

            <!-- Trek -->

            <td>

                {{ booking.trek_name }}

            </td>

            <!-- Number of People -->

            <td>

                {{ booking.number_of_people }}

            </td>

            <!-- Amount -->

            <td>

                ₹{{ booking.total_amount }}

            </td>


            <!-- Booking Status -->

            <td>

                <span
    class="status-badge"
    :class="{
        accepted: booking.booking_status === 'Accepted',
        pending: booking.booking_status === 'Pending',
        rejected: booking.booking_status === 'Rejected'
    }"
>
    {{ booking.booking_status }}
</span>

            </td>

            <!-- Booking Date -->

            <td>

                {{ booking.booking_date }}

            </td>

            <!-- Actions -->

            <td>

                <div class="table-actions">

                    <button
    class="view-btn"
    @click="$router.push(`/admin/view-booking/${booking.id}`)"
>

                        <i class="bi bi-eye"></i>

                    </button>

                </div>

            </td>

        </tr>

    </tbody>

</table>
    </div>

</section>







        </div>

 </main>

</div>

</template>

<style scoped>
/*==================================================
GLOBAL
==================================================*/
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&display=swap');

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

.admin-bookings-page{
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
        url("@/assets/images/admin.jpg");

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
.sidebar-footer{

    padding-top:25px;

    border-top:1px solid rgba(255,255,255,.12);

}
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
.sidebar-logo{

    display:flex;

    align-items:center;

    gap:18px;

    margin:30px 0 55px 0;

    position:relative;

    padding-bottom:30px;

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
MAIN CONTENT
==================================================*/

.main-content{

    flex:1;

    margin-left:290px;

    padding:35px;

}


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

.back-btn{

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

.back-btn:hover{

    transform:translateY(-2px);
    background: white;
    color:#7b0a31;
    border-color: #7b0a31;
}

.back-btn i{

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



/*=====================================================

HEADER

=====================================================*/

.view-header{

display:flex;

justify-content:space-between;

align-items:center;

margin-bottom:35px;

}

.header-actions{

display:flex;

gap:15px;

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

/*=========================================
TABLE HEADER
=========================================*/
.table-wrapper{

    width:100%;
    max-width: 1400px;
    margin:0 auto;

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
    transform: translateX(6px);

}

.table-cover{

    width:70px;

    height:70px;

    object-fit:cover;

    border-radius:16px;

    box-shadow:0 8px 20px rgba(0,0,0,.15);

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

.table-actions{
    display:flex;
    justify-content:center;
    gap:12px;
}

.view-btn,
.block-btn,
.unblock-btn{
    width:48px;
    height:48px;
    border:none;
    border-radius:14px;
    display:flex;
    align-items:center;
    justify-content:center;
    color:#fff;
    font-size:1.15rem;
    transition:.3s;
}

.view-btn{
    background:#ffffff;
    color:#7b002c;
}

.view-btn:hover{
    background:#7b002c;
    color:#fff;
}

.block-btn{
    background:#dc3545;
}

.block-btn:hover{
    transform:translateY(-3px);
    box-shadow:0 10px 20px rgba(220,53,69,.35);
}

.unblock-btn{
    background:#198754;
}

.unblock-btn:hover{
    transform:translateY(-3px);
    box-shadow:0 10px 20px rgba(25,135,84,.35);
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


/* booking status */
.status-badge {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    text-align: center;
    min-width: 110px;
    transition: all 0.3s ease;
}

/* Accepted */
.status-badge.accepted {
    background: #d4edda;
    color: #1e7e34;
    border: 1px solid #8fd19e;
}

/* Pending */
.status-badge.pending {
    background: #fff3cd;
    color: #856404;
    border: 1px solid #ffe08a;
}

/* Rejected */
.status-badge.rejected {
    background: #f8d7da;
    color: #c82333;
    border: 1px solid #f5a3ab;
}
</style>

<script>

import axios from "axios"

export default{

    name:"AdminUsers",

    data(){

    return{

        bookings:[],

        summary:{},

        search:"",

        bookingStatusFilter:"",

        paymentStatusFilter:""

    }

},

    mounted(){

        this.fetchBookings()

    },

    methods:{

    async fetchBookings(){

        try{

            const response = await axios.get(

                "http://127.0.0.1:5000/api/admin/bookings"

            )

            this.bookings = response.data.data

            this.summary = response.data.summary

        }

        catch(error){

            console.log(error)

        }

    }

},

    computed:{

    filteredBookings(){

        return this.bookings.filter(booking=>{

            const matchesSearch =

                booking.booking_reference.toLowerCase().includes(

                    this.search.toLowerCase()

                ) ||

                booking.user_name.toLowerCase().includes(

                    this.search.toLowerCase()

                ) ||

                booking.trek_name.toLowerCase().includes(

                    this.search.toLowerCase()

                )

            const matchesBooking =

                this.bookingStatusFilter=="" ||

                booking.booking_status==this.bookingStatusFilter

            const matchesPayment =

                this.paymentStatusFilter=="" ||

                booking.payment_status==this.paymentStatusFilter

            return(

                matchesSearch &&

                matchesBooking &&

                matchesPayment

            )

        })

    }

}

}

</script>