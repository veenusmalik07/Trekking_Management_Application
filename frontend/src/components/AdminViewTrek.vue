<template>

<div class="admin-view-trek">
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
            to="/admin-Summary"
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
            View Trek
        </h1>

        <p class="page-subtitle">
            Explore every detail of your trekking expedition before making changes.
        </p>

    </div>

    <div class="header-right">

        <button
        class="back-btn"
        @click="$router.push('/admin-treks')"
    >
        <i class="bi bi-arrow-left"></i>
        Back
    </button>

    <!-- Edit Button -->
    <router-link
        :to="'/admin-edit-trek/' + trek.id"
        class="edit-btn"
    >
        <i class="bi bi-pencil-square me-2"></i>
        Edit Trek
    </router-link>



    </div>

</header>

<br><br><br><br>




    <!-- ===================================================== -->
    <!-- HERO SECTION -->
    <!-- Cover Image + Trek Name + Badges + Quick Stats -->
    <!-- ===================================================== -->



    <!-- ===================================================== -->
    <!-- BASIC INFORMATION -->
    <!-- Trek Type, Organizer, Location, Meeting Point -->
    <!-- ===================================================== -->
<!-- TREK OVERVIEW -->
<!-- ===================================================== -->

<section class="glass-card mb-5">

    <div class="row g-0 align-items-center">

        <!-- Cover Image -->

        <div class="col-lg-5">

            <img
                :src="trek.cover_image || 'https://placehold.co/900x700?text=No+Image'"
                class="overview-image"
            >

        </div>

        <!-- Trek Details -->

        <div class="col-lg-7">

            <div class="overview-content">

                <!-- Trek Name -->

                <h2 class="overview-title">

                    {{ trek.trek_name }}

                </h2>

                <p class="overview-location">

                    <i class="bi bi-geo-alt-fill me-2"></i>

                    {{ trek.location }}, {{ trek.state }}

                </p>

                <!-- Badges -->

                <div class="d-flex flex-wrap gap-3 mb-4">

                    <span
                        class="difficulty-pill"
                        :class="{
                            easy: trek.difficulty=='Easy',
                            moderate: trek.difficulty=='Moderate',
                            difficult: trek.difficulty=='Difficult'
                        }"
                    >

                        <i class="bi bi-bar-chart-fill me-2"></i>

                        {{ trek.difficulty }}

                    </span>

                    <span
                        class="status-pill"
                    >

                        <i class="bi bi-flag-fill me-2"></i>

                        {{ trek.status }}

                    </span>

                </div>

                <hr class="section-divider">

                <!-- Quick Stats -->

                <div class="row gx-4 gy-4">

                    <div class="col-6">

                        <div class="quick-info">

                            <i class="bi bi-cash-stack"></i>

                            <div>

                                <small>Price</small>

                                <h5>₹{{ trek.price }}</h5>

                            </div>

                        </div>

                    </div>

                    <div class="col-6">

                        <div class="quick-info">

                            <i class="bi bi-people-fill"></i>

                            <div>

                                <small>Capacity</small>

                                <h5>{{ trek.capacity }} Trekkers</h5>

                            </div>

                        </div>

                    </div>

                    <div class="col-6">

                        <div class="quick-info">

                            <i class="bi bi-calendar-event-fill"></i>

                            <div>

                                <small>Duration</small>

                                <h5>{{ trek.duration }} Days</h5>

                            </div>

                        </div>

                    </div>

                    <div class="col-6">

                        <div class="quick-info">

                            <i class="bi bi-building"></i>

                            <div>

                                <small>Organizer</small>

                                <h5>{{ trek.organizer }}</h5>

                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>

<br><br><br><br>

<!-- ===================================================== -->
<!-- BASIC INFORMATION -->
<!-- ===================================================== -->

<section class="glass-card mb-5">

    <div class="section-title">

        <h3>
            <i class="bi bi-calendar-event me-2"></i>
            Trek Schedule
        </h3>

        <p>
            Important dates and current trek status.
        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gx-4 gy-4">

            <div class="col-md-6">

                <div class="info-card">

                    <span>
                        <i class="bi bi-calendar-check-fill me-2"></i>
                        Start Date
                    </span>

                    <h5>
                        {{ formatDate(trek.start_date) }}
                    </h5>

                </div>

            </div>

            <div class="col-md-6">

                <div class="info-card">

                    <span>
                        <i class="bi bi-calendar-x-fill me-2"></i>
                        End Date
                    </span>

                    <h5>
                        {{ formatDate(trek.end_date) }}
                    </h5>

                </div>

            </div>

            <div class="row gx-4 gy-4">

            <div class="col-md-6">

                <div class="info-card">

                    <span>
                        <i class="bi bi-calendar-check-fill me-2"></i>
                        Registration Deadline
                    </span>

                    <h5>
                        {{ formatDate(trek.registration_deadline) }}
                    </h5>

                </div>

            </div>

            <div class="col-md-6">

                <div class="info-card">

                    <span>
                        <i class="bi bi-flag-fill me-2"></i>
                        Status
                    </span>

                    <h5>
                        {{ trek.status }}
                    </h5>

                </div>

            </div>

        </div>

    </div>
    </div>

</section>

<br><br><br><br>

    <!-- ===================================================== -->
    <!-- ELIGIBILITY -->
    <!-- Age Limit + Fitness Requirement -->
    <!-- ===================================================== -->
     <!-- ===================================================== -->
<!-- ELIGIBILITY & REQUIREMENTS -->
<!-- ===================================================== -->

<section class="glass-card mb-5">

    <!-- ============================================== -->
    <!-- SECTION HEADER -->
    <!-- ============================================== -->

    <div class="section-title">

        <h3>

            <i class="bi bi-shield-check me-2"></i>

            Eligibility & Requirements

        </h3>

        <p>

            Ensure participants meet the required age and fitness criteria before joining the trek.

        </p>

    </div>

    <hr class="section-divider">

    <!-- ============================================== -->
    <!-- ELIGIBILITY CARDS -->
    <!-- ============================================== -->

    <div class="row gx-4 gy-4">

    <!-- Minimum Age -->
    <div class="col-md-6">

        <div class="info-card">

            <span>
                <i class="bi bi-person-fill me-2"></i>
                Minimum Age
            </span>

            <h5 class="logo-script">
                {{ trek.minimum_age }} Years
            </h5>

        </div>

    </div>

    <!-- Maximum Age -->
    <div class="col-md-6">

        <div class="info-card">

            <span>
                <i class="bi bi-person-check-fill me-2"></i>
                Maximum Age
            </span>

            <h5 class="logo-script">
                {{ trek.maximum_age }} Years
            </h5>

        </div>

    </div>

    <!-- Fitness -->
    <div class="col-md-6">

        <div class="info-card">

            <span>
                <i class="bi bi-heart-pulse-fill me-2"></i>
                Fitness Requirement
            </span>

            <h5 class="logo-script">
                {{ trek.fitness_requirement }}
            </h5>

        </div>

    </div>

</div>

</section>
<br><br><br><br>

<!-- ===================================================== -->
<!-- TREK GALLERY -->
<!-- ===================================================== -->

<section class="glass-card mb-5">

    <!-- ============================================== -->
    <!-- SECTION HEADER -->
    <!-- ============================================== -->

    <div class="section-title">

        <h3 class="logo-script">

            <i class="bi bi-images me-2"></i>

            Trek Gallery

        </h3>

        <p>

            Explore memorable moments captured during this trekking expedition.

        </p>

    </div>

    <hr class="section-divider">

    <!-- ============================================== -->
    <!-- GALLERY -->
    <!-- ============================================== -->

    <div v-if="gallery.length" class="gallery-grid">

        <div
            class="gallery-card"
            v-for="image in gallery"
            :key="image.id"
        >

            <img
                :src="image.media_url"
                class="gallery-image"
            >

        </div>

    </div>

    <!-- ============================================== -->
    <!-- EMPTY GALLERY -->
    <!-- ============================================== -->

    <div
        v-else
        class="gallery-grid"
    >

        <div
            class="gallery-card placeholder-card"
            v-for="n in 6"
            :key="n"
        >

            <div class="placeholder-content">

                <i class="bi bi-image"></i>

                <h5>Gallery Image</h5>

                <p>Coming Soon</p>

            </div>

        </div>

    </div>

</section>

<br><br><br><br>

<!-- ===================================================== -->
<!-- EQUIPMENT & DESCRIPTION -->
<!-- ===================================================== -->

<section class="glass-card mb-5">

    <div class="section-title">

        <h3>

            <i class="bi bi-backpack2-fill me-2"></i>

            Equipment & Description

        </h3>

        <p>

            Essential gear, preparation guidelines, and complete trek overview.

        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gx-4 gy-4">

            <!-- Equipment -->

            <div class="col-12">

                <div class="info-card large-card">

                    <span>

                        <i class="bi bi-tools me-2"></i>

                        Equipment Required

                    </span>

                    <div class="info-description">

                        {{ trek.equipment_required }}

                    </div>

                </div>

            </div>

            <!-- Description -->

            <div class="col-12">

                <div class="info-card large-card">

                    <span>

                        <i class="bi bi-card-text me-2"></i>

                        Trek Description

                    </span>

                    <div class="info-description">

                        {{ trek.description }}

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>
<br><br><br><br>

<!-- ===================================================== -->
<!-- ASSIGNED TREK STAFF -->
<!-- ===================================================== -->

<section class="glass-card mb-5">

    <div class="section-title">
        <h3>
            <i class="bi bi-people-fill me-2"></i>
            Assigned Trek Staff
        </h3>

        <p>
            Staff members responsible for managing and guiding this trekking expedition.
        </p>
    </div>

    <hr class="section-divider">

    <div
        class="staff-grid"
        v-if="staff.length"
    >

        <div
            class="staff-card"
            v-for="member in staff"
            :key="member.id"
        >

            <div class="staff-avatar">

                {{ member.name.charAt(0) }}

            </div>

            <div class="staff-content">

                <h5>

                    {{ member.name }}

                </h5>

                <p>

                    <i class="bi bi-envelope-fill me-2"></i>

                    {{ member.email }}

                </p>

                <p>

                    <i class="bi bi-telephone-fill me-2"></i>

                    {{ member.mobile }}

                </p>

                <div class="staff-tags">

                    <span class="staff-badge">

                        {{ member.profession }}

                    </span>

                    <span class="staff-badge">

                        {{ member.specialization }}

                    </span>

                </div>

            </div>

        </div>

    </div>

    <div
        class="empty-gallery"
        v-else
    >

        <i class="bi bi-person-x-fill"></i>

        <h4>No Staff Assigned</h4>

        <p>

            No trekking staff have been assigned to this trek yet.

        </p>

    </div>

</section>

<br><br><br><br>

<!-- ===================================================== -->
<!-- RECENT BOOKINGS -->
<!-- ===================================================== -->

<section class="glass-card mb-5">

    <div class="section-title">

        <h3>

            <i class="bi bi-journal-check me-2"></i>

            Recent Bookings

        </h3>

        <p>

            View the latest participant bookings and payment details for this trek.

        </p>

    </div>

    <hr class="section-divider">

    <div
        class="table-responsive"
        v-if="bookings.length"
    >

        <table class="booking-table">

            <thead>

                <tr>

                    <th>Booking ID</th>

                    <th>Participant</th>

                    <th>People</th>

                    <th>Amount</th>

                    <th>Payment</th>

                    <th>Status</th>

                    <th>Date</th>

                </tr>

            </thead>

            <tbody>

                <tr
                    v-for="booking in bookings"
                    :key="booking.booking_reference"
                >

                    <td>

                        {{ booking.booking_reference }}

                    </td>

                    <td>

                        {{ booking.user_name }}

                    </td>

                    <td>

                        {{ booking.people }}

                    </td>

                    <td>

                        ₹{{ booking.amount }}

                    </td>

                    <td>

                        <span
                            class="payment-badge"
                            :class="booking.payment_status.toLowerCase()"
                        >

                            {{ booking.payment_status }}

                        </span>

                    </td>

                    <td>

                        <span
                            class="status-badge"
                            :class="booking.booking_status.toLowerCase()"
                        >

                            {{ booking.booking_status }}

                        </span>

                    </td>

                    <td>

                        {{ booking.booking_date }}

                    </td>

                </tr>

            </tbody>

        </table>

    </div>

    <div
        class="empty-gallery"
        v-else
    >

        <i class="bi bi-journal-x"></i>

        <h4>No Bookings Yet</h4>

        <p>

            This trek has not received any participant bookings.

        </p>

    </div>

</section>





        </div>

        <br><br><br><br><br>

<div>
<p class="trek-quote">
    "Great treks aren't just climbed they're carefully crafted."
</p>
</div>

<br><br><br><br><br>
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

.admin-view-trek{
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

/*=====================================================

HERO

=====================================================*/

.hero-card{

display:flex;

gap:35px;

padding:35px;

border-radius:30px;

background:rgba(255,255,255,.28);

backdrop-filter:blur(20px);

border:1px solid rgba(255,255,255,.4);

margin-bottom:35px;

}

.hero-image{

width:420px;

height:300px;

overflow:hidden;

border-radius:25px;

flex-shrink:0;

}

.hero-image img{

width:100%;

height:100%;

object-fit:cover;

}

.hero-content{

flex:1;

display:flex;

flex-direction:column;

justify-content:center;

}

.hero-content h1{

font-size:2.7rem;

color:#670626;

font-weight:700;

margin-bottom:10px;

}

.location{

font-size:1.1rem;

color:#666;

margin-bottom:25px;

}

.hero-badges{

display:flex;

gap:12px;

margin-bottom:30px;

}

.hero-badges span{

padding:10px 20px;

border-radius:30px;

font-weight:600;

}

.status-badge{

background:#a2c2d3;

}

.difficulty-badge{

background:#edc3c3;

}

.emergency-badge{

background:#cdc49e;

}

.hero-stats{

display:grid;

grid-template-columns:repeat(4,1fr);

margin-bottom:25px;

}

.hero-stats h3{

margin:0;

font-size:2rem;

color:#670626;

}

.hero-stats span{

color:#777;

font-size:.9rem;

}

.organizer{

font-size:1rem;

color:#444;

}
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

    padding:12px 26px;

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

    font-size:1rem;

}

.edit-btn{

    display:flex;

    align-items:center;

    gap:10px;

    padding:12px 26px;

    border:none;

    border-radius:18px;

    color:#670626;

    background:#fff;

    font-weight:600;

    transition:.3s ease;

    box-shadow:0 10px 25px rgba(103,6,38,.18);

    cursor:pointer;
    margin-top: 10px;

}

.edit-btn:hover{

    transform:translateY(-2px);
    color: white;
    background:#7b0a31;
    border-color: white;
}

.edit-btn i{

    font-size:1rem;

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



/* ===================================================== */
/* INFORMATION CARDS */
/* ===================================================== */

/*==================================================
TREK OVERVIEW
==================================================*/

/*=========================================
/*=========================================
OVERVIEW IMAGE
=========================================*/

.overview-image{

    width:100%;

    height:440px;          /* Was around 520px */

    object-fit:cover;

    border-radius:28px;

    padding:15px;          /* Adds space around image */

    background:#fff;

    box-sizing:border-box;

}

.overview-image:hover{

    transform:scale(1.08);

}

/*=========================================
OVERVIEW
=========================================*/

.overview-content{

    padding:20px 35px;

}

.overview-title{

    font-family:"Your Premium Heading Font", serif;

    color:#670626;

    font-size:2.8rem;      /* Smaller */

    margin-bottom:10px;

}

.overview-location{

    color:#666;

    font-size:1rem;

    margin-bottom:20px;

}

.overview-location i{

    color:#670626;

}

/*=========================================
BADGES
=========================================*/

.difficulty-pill,
.status-pill{

    display:inline-flex;

    align-items:center;

    gap:10px;

    padding:14px 28px;

    border-radius:40px;

    font-weight:700;

    font-size:1rem;

}

.easy{

    background:#B0D483;

    color:#670626;

}

.moderate{

    background:#FFD77A;

    color:#670626;

}

.difficult{

    background:#dc3545;

    color:white;

}

.status-pill{

    background:#670626;

    color:white;

}

/*=========================================
QUICK INFO
=========================================*/

.quick-info{

    background:rgba(255,255,255,.18);

    backdrop-filter:blur(16px);

    border:1px solid rgba(255,255,255,.35);

    border-top:4px solid #B0D483;

    border-radius:24px;

    padding:18px;

    display:flex;

    align-items:center;

    gap:10px;

    min-height:100px;

    transition:.35s;
    margin:8px;

}


.quick-info:hover{

    transform:translateY(-6px);

    box-shadow:0 18px 35px rgba(0,0,0,.12);

}

.quick-info i{

    background:#670626;

    color:white;

    border-radius:20px;

    display:flex;

    align-items:center;

    justify-content:center;
    flex-shrink:0;
    width:54px;

    height:40px;

    font-size:0.8rem;

}


.quick-info small{

    display:block;

    color:#666;

    font-size:0.9rem;

    margin-bottom:6px;

}

.quick-info h5{
    font-family:'Cormorant Garamond', serif;

    margin:0;

    color:#670626;

    font-size:1.3rem;

    font-weight:500;

}

.section-body{
    margin:8px;
}

/*=========================================
SECTION TITLE
=========================================*/

.section-title{

    margin-bottom:30px;

}

.section-title h3{

    color:#670626;

    font-size:2.6rem;

    font-family:"Your Premium Heading Font", serif;

}

.section-title p{

    color:#666;

    font-size:1.05rem;

}

/*=========================================
SECTION DIVIDER
=========================================*/

.section-divider{

    border:none;

    border-top:2px solid rgba(176,212,131,.45);

    margin:30px 0;

}

/*=========================================
INFO CARDS
=========================================*/

.info-card{

    background:rgba(255,255,255,.18);

    backdrop-filter:blur(16px);

    border:1px solid rgba(255,255,255,.35);

    border-top:4px solid #B0D483;

    border-radius:24px;

    padding:28px;

    min-height:150px;

    transition:.35s;
    width:500px;
    margin-top:14px;

}

.info-card:hover{

    transform:translateY(-6px);

    box-shadow:0 18px 35px rgba(0,0,0,.12);

}

.info-card span{

    display:flex;

    align-items:center;

    color:black;

    font-size:0.9rem;

    font-weight:600;

    margin-bottom:22px;

}

.info-card span i{

    color:black;

    font-size:1.2rem;

}

.info-card h5{
    font-family:'Cormorant Garamond', serif;
    color:#670626;

    font-size:2rem;

    font-weight:500;

    line-height:1.1;

}

/* ===================================================== */
/* GALLERY */
/* ===================================================== */
/*=====================================
TREK GALLERY
=====================================*/

.gallery-grid{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(350px,1fr));

    gap:35px;

    margin-top:35px;

}

.gallery-card{

    height:280px;

    border-radius:24px;

    overflow:hidden;

    cursor:pointer;

    position:relative;

    background:#fff;

    box-shadow:0 12px 30px rgba(0,0,0,.15);

    transition:all .4s ease;

}

.gallery-image{

    width:100%;
    height:100%;

    object-fit:cover;

    transition:transform .5s ease;

}

/* Hover Effect */

.gallery-card:hover{

    transform:translateY(-10px);

    box-shadow:0 22px 45px rgba(0,0,0,.28);

}

.gallery-card:hover .gallery-image{

    transform:scale(1.08);

}

/* Overlay */

.gallery-card::after{

    content:"";

    position:absolute;

    inset:0;

    background:linear-gradient(
        to top,
        rgba(0,0,0,.35),
        transparent 45%
    );

    opacity:0;

    transition:.35s;

}

.gallery-card:hover::after{

    opacity:1;

}


/* ==========================================
   LARGE INFO CARDS
==========================================*/

.large-card{

    min-height:220px;

    display:flex;

    flex-direction:column;

    justify-content:flex-start;
    width: 1050px;

}

.info-description{

    margin-top:20px;

    color:#2d2d2d;

    font-size:17px;

    line-height:1.9;

    text-align:justify;

    white-space:pre-line;

    font-family:"Poppins",sans-serif;

}

/*bookings */
/*=========================================
BOOKING TABLE
=========================================*/

.booking-table{

    width:100%;

    border-collapse:separate;

    border-spacing:0 15px;

}

.booking-table thead th{

    background:#B0D483;

    color:#670626;

    padding:18px;

    text-align:center;

    font-weight:700;

    font-size:1rem;

}

.booking-table thead th:first-child{

    border-radius:18px 0 0 18px;

}

.booking-table thead th:last-child{

    border-radius:0 18px 18px 0;

}

.booking-table tbody tr{

    background:white;

    transition:.35s;

    box-shadow:0 8px 20px rgba(0,0,0,.08);

}

.booking-table tbody tr:hover{

    transform:translateY(-4px);

}

.booking-table td{

    padding:18px;

    text-align:center;

}

/*=========================================
BADGES
=========================================*/

.payment-badge,
.status-badge{

    padding:8px 16px;

    border-radius:30px;

    color:white;

    font-size:.85rem;

    font-weight:600;

}

.payment-badge.paid{

    background:#198754;

}

.payment-badge.pending{

    background:#ffc107;

    color:#222;

}

.payment-badge.failed{

    background:#dc3545;

}

.status-badge.confirmed{

    background:#0d6efd;

}

.status-badge.cancelled{

    background:#dc3545;

}

.status-badge.completed{

    background:#198754;

}

/* ===========================
   STAFF SECTION
=========================== */

.staff-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
    gap:25px;
    margin-top:25px;
}

.staff-card{
    display:flex;
    align-items:flex-start;
    gap:20px;

    padding:25px;
    border-radius:22px;

    background:rgba(255,255,255,.18);
    backdrop-filter:blur(16px);
    -webkit-backdrop-filter:blur(16px);

    border:1px solid rgba(255,255,255,.35);

    box-shadow:
        0 10px 30px rgba(0,0,0,.08);

    transition:.35s ease;
}

.staff-card:hover{
    transform:translateY(-8px);
    box-shadow:
        0 18px 40px rgba(0,0,0,.15);
}

/* ===========================
   Avatar
=========================== */

.staff-avatar{
    width:75px;
    height:75px;

    min-width:75px;

    border-radius:50%;

    display:flex;
    align-items:center;
    justify-content:center;

    background:linear-gradient(135deg,#8fc866,#6da742);

    color:#fff;
    font-size:2rem;
    font-weight:700;

    box-shadow:0 10px 20px rgba(143,200,102,.35);
}

/* ===========================
   Content
=========================== */

.staff-content{
    flex:1;
}

.staff-content h5{
    margin-bottom:10px;

    color:#6b002b;

    font-size:1.4rem;
    font-weight:700;
}

.staff-content p{
    margin-bottom:8px;

    display:flex;
    align-items:center;

    color:#444;

    font-size:.97rem;
}

.staff-content i{
    width:24px;
    color:#7b0c33;
}

/* ===========================
   Tags
=========================== */

.staff-tags{
    display:flex;
    flex-wrap:wrap;
    gap:10px;

    margin-top:14px;
}

.staff-badge{
    padding:6px 14px;

    border-radius:30px;

    background:#eef8df;

    color:#5f8128;

    font-size:.82rem;
    font-weight:600;

    border:1px solid #d3ebb1;
}

/* ===========================
   Footer
=========================== */

.staff-footer{
    margin-top:18px;
    padding-top:15px;

    border-top:1px dashed rgba(0,0,0,.15);
}

.staff-footer strong{
    color:#7b0c33;
}

.staff-footer span{
    color:#333;
    font-weight:500;
}
</style>

<script>

import axios from "axios"

export default{

name:"AdminViewTrek",

data(){

return{

trek:{},

gallery:[],


staff:[],

bookings:[],

summary:{}

}

},

mounted(){

this.fetchTrek()

},

methods:{

// =====================================================
// FETCH SINGLE TREK
// =====================================================

async fetchTrek(){

    try{

        const id=this.$route.params.id

        const response=await axios.get(
            "http://127.0.0.1:5000/api/admin/treks/"+id
        )

        this.trek=response.data.data.trek

        this.gallery=response.data.data.gallery

        this.staff=response.data.data.staff

        this.bookings=response.data.data.recent_bookings

        this.summary=response.data.data.summary

    }

    catch(error){

        console.log(error)

    }

},
// =====================================================
// FORMAT DATE
// =====================================================

formatDate(date){

if(!date) return "-"

return new Date(date).toLocaleDateString("en-IN",{

day:"2-digit",

month:"short",

year:"numeric"

})

},

// =====================================================
// DELETE TREK
// =====================================================

async deleteTrek(){

const confirmDelete=confirm(

"Are you sure you want to delete this trek?"

)

if(!confirmDelete) return

try{

await axios.delete(

"http://127.0.0.1:5000/api/admin/treks/"+this.trek.id

)

alert("Trek deleted successfully.")

this.$router.push("/admin-treks")

}

catch(error){

alert(

error.response?.data?.message ||

"Unable to delete trek."

)

}

},

}

}

</script>