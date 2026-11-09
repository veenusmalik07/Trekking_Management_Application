<template>

<div class="admin-view-user-page">

    <!-- Fixed Mountain Background -->
    <div class="page-background"></div>

    <!-- Sidebar -->
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


    <!-- Main Content -->

    <main class="main-content">

        <!-- Header -->

<section class="page-header">
    <div>
        <p class="page-title">
            Profile of {{ user.full_name }}
        </p>

        <p class="page-subtitle">
            Complete overview of the registered trek participant.
        </p>
    </div>

    <div class="header-right">
        <button class="back-btn" @click="$router.push('/admin-users')">
            <i class="bi bi-arrow-left"></i>
            Back
        </button>
    </div>
</section>

<br><br><br>

<div>
<p class="trek-quote">
"Every journey begins with a single booking."
</p>
</div>

<br><br><br><br><br>


        <!-- Basic Information -->
<section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-person-fill"></i>

            Basic Information

        </h3>

        <p>

            View the personal details of the registered trek participant.

        </p>

    </div>

    <hr class="section-divider">

    <!-- BASIC INFORMATION BODY -->

    <div class="section-body">

        <div class="row gy-3 gx-4">

            <!-- Full Name -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Full Name

                </label>

                <input
                    class="form-control"
                    :value="user.full_name"
                    readonly
                >

            </div>

            <!-- Email -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Email

                </label>

                <input
                    class="form-control"
                    :value="user.email"
                    readonly
                >

            </div>

            <!-- Mobile Number -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Mobile Number

                </label>

                <input
                    class="form-control"
                    :value="user.mobile_number"
                    readonly
                >

            </div>

            <!-- Gender -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Gender

                </label>

                <input
                    class="form-control"
                    :value="user.gender"
                    readonly
                >

            </div>

            <!-- Date of Birth -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Date of Birth

                </label>

                <input
                    class="form-control"
                    :value="formatDate(user.date_of_birth)"
                    readonly
                >

            </div>

        </div>

    </div>

</section>

<br><br>

         <br><br>

        <!-- Account Information -->
<section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-person-vcard-fill"></i>

            Account Information

        </h3>

        <p>

            View the user's registration details and account status.

        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gy-3 gx-4">

            <!-- City -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    City

                </label>

                <input
                    class="form-control"
                    :value="user.city"
                    readonly
                >

            </div>

            <!-- State -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    State

                </label>

                <input
                    class="form-control"
                    :value="user.state"
                    readonly
                >

            </div>

            <!-- Account Status -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Account Status

                </label>

                <input
                    class="form-control"
                    :value="user.status"
                    readonly
                >

            </div>

            <!-- Member Since -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Member Since

                </label>

                <input
                    class="form-control"
                    :value="formatDate(user.created_at)"
                    readonly
                >

            </div>

            <!-- Last Login -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Last Login

                </label>

                <input
                    class="form-control"
                    :value="formatDate(user.last_login)"
                    readonly
                >

            </div>

            <!-- Profile Picture -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Profile Picture

                </label>

                <div class="cover-preview">

                    <img v-if="user.profile_picture"
                        :src="`http://127.0.0.1:5000/static/profile_uploads/${user.profile_picture}`"
                        class="preview-image"
                    />

                    <div
                        v-else
                        class="preview-placeholder"
                    >

                        <i class="bi bi-person-circle"></i>

                        <p>

                            No Profile Picture

                        </p>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>


        <br><br>

        <!-- Emergency Contact -->
<section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-telephone-fill"></i>

            Emergency Contact

        </h3>

        <p>

            Emergency contact information provided during registration.

        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gy-3 gx-4">

            <!-- Emergency Contact Name -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Emergency Contact Name

                </label>

                <input
                    class="form-control"
                    :value="user.emergency_contact_name"
                    readonly
                >

            </div>

            <!-- Emergency Contact Number -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Emergency Contact Number

                </label>

                <input
                    class="form-control"
                    :value="user.emergency_contact_number"
                    readonly
                >

            </div>

        </div>

    </div>

</section>


<br><br>

<!-- Trekking Statistics -->

<section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-bar-chart-fill"></i>

            Trekking Statistics

        </h3>

        <p>

            Summary of the user's trekking activities and booking history.

        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gy-3 gx-4">

            <!-- Total Bookings -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Total Bookings

                </label>

                <input
                    class="form-control"
                    :value="summary.total_bookings"
                    readonly
                >

            </div>

            <!-- Upcoming Treks -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Upcoming Treks

                </label>

                <input
                    class="form-control"
                    :value="summary.upcoming_treks"
                    readonly
                >

            </div>

            <!-- Completed Treks -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Completed Treks

                </label>

                <input
                    class="form-control"
                    :value="summary.completed_treks"
                    readonly
                >

            </div>

            <!-- Cancelled Bookings -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Cancelled Bookings

                </label>

                <input
                    class="form-control"
                    :value="summary.cancelled_bookings"
                    readonly
                >

            </div>

            <!-- Total Amount Spent -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Total Amount Spent

                </label>

                <input
                    class="form-control"
                    :value="'₹ ' + summary.total_spent"
                    readonly
                >

            </div>

        </div>

    </div>

</section>

<br><br>

<!-- Recent Bookings -->

<section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-journal-check"></i>

            Recent Bookings

        </h3>

        <p>

            Latest trekking reservations made by this participant.

        </p>

    </div>

    <hr class="section-divider">

    <table class="trek-table">

        <thead>

            <tr>

                <th>Booking Ref</th>

                <th>Trek</th>

                <th>Booking Date</th>

                <th>Amount</th>

                <th>Payment</th>

                <th>Status</th>

            </tr>

        </thead>

        <tbody>

            <tr

                v-for="booking in bookings"

                :key="booking.id"

            >

                <!-- Booking Reference -->

                <td>

                    {{ booking.booking_reference }}

                </td>

                <!-- Trek Name -->

                <td>

                    {{ booking.trek_name }}

                </td>

                <!-- Booking Date -->

                <td>

                    {{ booking.booking_date }}

                </td>

                <!-- Amount -->

                <td>

                    ₹ {{ booking.amount }}

                </td>

                <!-- Payment -->

                <td>

                    <span

                        class="status-badge"

                        :class="{

                            paid:booking.payment_status=='Paid',

                            pending:booking.payment_status=='Pending',

                            refunded:booking.payment_status=='Refunded'

                        }"

                    >

                        {{ booking.payment_status }}

                    </span>

                </td>

                <!-- Booking Status -->

                <td>

                    <span

                        class="status-badge"

                        :class="{

                            accepted:booking.booking_status=='Accepted',

                            pending:booking.booking_status=='Pending',

                            cancelled:booking.booking_status=='Cancelled',

                            rejected:booking.booking_status=='Rejected'

                        }"

                    >

                        {{ booking.booking_status }}

                    </span>

                </td>

            </tr>

            <!-- No Bookings -->

            <tr

                v-if="bookings.length==0"

            >

                <td

                    colspan="6"

                    class="text-center py-4"

                >

                    No bookings found.

                </td>

            </tr>

        </tbody>

    </table>

</section>

<br><br>

<br><br>



        

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

.admin-view-user-page{
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

    margin-left:290px;

    padding:35px;

}

/*==================================================
MAIN CONTENT
==================================================*/

.main-content{

    flex:1;

    margin-left:290px;

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

/* ==========================================================
LABELS
========================================================== */

.form-label{

    color:#670626;

    font-size:17px;

    font-weight:600;

    margin-bottom:10px;
    font-family:"Your Premium Heading Font", serif;
    letter-spacing: 1.2px;

}

/* ==========================================================
INPUTS
========================================================== */

.form-control,
.form-select{

    height:58px;

    border:none;

    border-radius:22px;

    background:rgba(255,255,255,.78);

    padding:0 20px;

    font-size:15px;

    color:#333;

    transition:.3s;

    box-shadow:none;
    width:95%;

}

/* ==========================================================
TEXTAREA
========================================================== */

textarea.form-control{

    height:auto;

    padding:18px;

    resize:none;

}

/* ==========================================================
PLACEHOLDER
========================================================== */

.form-control::placeholder{

    color:#999;

}

/* ==========================================================
FOCUS
========================================================== */

.form-control:focus,
.form-select:focus{

    background:white;

    border:none;

    outline:none;

    box-shadow:

        0 0 0 4px rgba(186,215,151,.35),

        0 8px 25px rgba(0,0,0,.08);

}

/* ==========================================================
SELECT
========================================================== */

.form-select{

    cursor:pointer;

}

/* ==========================================================
ROW SPACING
========================================================== */

.row gy-3 gx-4{

    --bs-gutter-y:1.8rem;

}

/* ==========================================================
INPUT HOVER
========================================================== */

.form-control:hover,
.form-select:hover{

    background:white;

}

/* ==========================================================
RESPONSIVE
========================================================== */

@media(max-width:768px){

    .glass-card{

        padding:25px;

    }

}

.cover-preview{

    width:100%;

    min-height:300px;

    max-height:420px;

    background:#fff;

    border:2px dashed rgba(103,6,38,.18);

    border-radius:22px;

    display:flex;

    justify-content:center;

    align-items:center;

    padding:15px;

    overflow:hidden;

}

.preview-image{

    max-width:100%;

    max-height:380px;

    width:auto;

    height:auto;

    border-radius:16px;

    object-fit:contain;

    transition:.3s;

}

.preview-placeholder{

    display:flex;

    flex-direction:column;

    align-items:center;

    color:#888;

}

.preview-placeholder i{

    font-size:3rem;

    color:#670626;

    margin-bottom:10px;

}

.preview-placeholder p{

    margin:0;

}

.gallery-preview{

    display:flex;

    gap:18px;

    flex-wrap:wrap;

    margin-top:18px;

}

.gallery-card{

    width:180px;

    height:130px;

    border-radius:18px;

    overflow:hidden;

    background:#fff;

    box-shadow:0 10px 25px rgba(0,0,0,.08);

    transition:.3s;

}

.gallery-card:hover{

    transform:translateY(-6px);

}

.gallery-image{

    width:100%;

    height:100%;

    object-fit:cover;

}

/* ==========================================
ACTION BUTTONS
========================================== */

.action-section{

    display:flex;

    justify-content:flex-end;

    gap:18px;

    margin:45px 0;

}

.reset-btn{

    border:none;

    background:#b7d57a;

    color:white;

    padding:14px 34px;

    border-radius:50px;

    font-weight:600;

    box-shadow:0 10px 30px rgba(0,0,0,.08);

    transition:.3s;

}

.reset-btn:hover{

    background:#ececec;
    color:black;

    transform:translateY(-3px);

}

.create-btn{

    border:none;

    background:#670626;

    color:white;

    padding:14px 40px;

    border-radius:50px;

    font-weight:600;

    box-shadow:0 12px 35px rgba(103,6,38,.25);

    transition:.3s;

}

.create-btn:hover{

    background:white;

    color:black;

    transform:translateY(-3px);

}

/* ==========================================================
RECENT BOOKINGS TABLE
========================================================== */

.trek-table{

    width:100%;

    border-collapse:separate;

    border-spacing:0 14px;

    margin-top:10px;

}

.trek-table thead th{

    color:#670626;

    font-size:16px;

    font-weight:700;

    font-family:"Your Premium Heading Font", serif;

    letter-spacing:1px;

    padding:14px 18px;

    border:none;

}

.trek-table tbody tr{

    background:rgba(255,255,255,.72);

    backdrop-filter:blur(12px);

    transition:.3s ease;

    border-radius:18px;

    box-shadow:0 8px 20px rgba(0,0,0,.05);

}

.trek-table tbody tr:hover{

    transform:translateY(-2px);

    box-shadow:0 12px 28px rgba(0,0,0,.10);

}

.trek-table td{

    padding:18px;

    vertical-align:middle;

    color:#444;

    border:none;

}

.trek-table tbody tr td:first-child{

    border-radius:18px 0 0 18px;

}

.trek-table tbody tr td:last-child{

    border-radius:0 18px 18px 0;

}

/* ==========================================================
STATUS BADGES
========================================================== */

.status-badge{

    display:inline-block;

    padding:7px 16px;

    border-radius:50px;

    font-size:13px;

    font-weight:600;

    letter-spacing:.5px;

}

/* Booking Status */

.accepted{

    background:#BAD797;

    color:#29522b;

}

.rejected{

    background:#9ed8ff;

    color:#0d4f73;

}

.cancelled{

    background:#f6c4c9;

    color:#8b1f2d;

}

.pending{

    background:#ffe9a8;

    color:#8a6d00;

}

/* Payment Status */

.paid{

    background:#d5f4d1;

    color:#1d6b2b;

}

.refunded{

    background:#d8d8d8;

    color:#444;

}

/* ==========================================================
EMPTY TABLE MESSAGE
========================================================== */

.trek-table .text-center{

    color:#777;

    font-size:15px;

    font-style:italic;

}
</style>

<script>

import axios from "axios"

export default{

    name:"AdminDashboard",

    data(){

    return{

        user:{},

        bookings:[],

        summary:{}

    }

},

    mounted(){

        this.fetchUser()

    },

    methods:{

        async fetchUser(){

    try{

        const id = this.$route.params.id

        const response = await axios.get(

            "http://127.0.0.1:5000/api/admin/user/" + id

        )

        this.user = response.data.data.user

        this.summary = response.data.data.summary

        this.bookings = response.data.data.bookings

    }

    catch(error){

        console.log(error)

    }

},

formatDate(date){

    if(!date) return "-"

    return new Date(date).toLocaleDateString(

        "en-IN",

        {

            day:"2-digit",

            month:"short",

            year:"numeric"

        }

    )

}

    }

}

</script>