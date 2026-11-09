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
            <router-link to="/user-browse-treks" class="nav-link active-link"> Browse Treks </router-link>
            <router-link to="/user-my-bookings" class="nav-link"> My Bookings </router-link>
            <router-link to="/user-profile" class="nav-link"> Profile </router-link>
        </div>
        
        <!-- Right -->
        <div class="navbar-right">
            <button class="logout-btn" @click="$router.push('/')">
                <i class="bi bi-box-arrow-right me-2"></i>
                Logout
            </button>
        </div>
    </nav>
    
    <br /><br />
    
    <div class="content-bg">
        <!-- TREK HEADER -->
        <section class="trek-header">
            <div class="container-fluid">
                <div class="header-top">
                    <div>
                        <h1 class="trek-title">
                            {{ trek.trek_name }}
                        </h1>
                        
                        <p class="trek-location">
                            <i class="bi bi-geo-alt-fill"></i>
                            {{ trek.location }}, {{ trek.state }}
                        </p>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- TREK COVER -->
        <section class="cover-section">
            <div class="container-fluid">
                <div class="cover-card">
                    <img :src="trek.cover_image"
                        :alt="trek.trek_name"
                    >
                    
                    <div class="cover-overlay">
                        <span class="cover-badge difficulty">
                            {{ trek.difficulty }}
                        </span>
                        
                        <span class="cover-badge status">
                            {{ trek.status }}
                        </span>
                        
                        <span class="cover-badge price">
                            ₹ {{ trek.price }}
                        </span>
                    </div>
                
                </div>
            </div>
        </section>
        
        <!-- TREK HIGHLIGHTS -->
        <section class="highlights-section">
            <div class="row g-4">

                <div class="col-lg-4 col-md-6">
                    <div class="highlight-card">
                        
                        <div class="highlight-icon">
                            <i class="bi bi-clock-history"></i>
                        </div>

                        <div>
                            <span class="highlight-label">
                                Duration
                            </span>
                            
                            <h5>
                                {{ trek.duration }} Days
                            </h5>
                        </div>
                    
                    </div>
                </div>
                
                <div class="col-lg-4 col-md-6">
                    <div class="highlight-card">
                        
                        <div class="highlight-icon">
                            <i class="bi bi-signpost-split-fill"></i>
                        </div>

                        <div>
                            <span class="highlight-label">
                                Trek Type
                            </span>
                            
                            <h5>
                                {{ trek.trek_type }}
                            </h5>
                        </div>
                    
                    </div>
                </div>

        <div class="col-lg-4 col-md-6">

            <div class="highlight-card">

                <div class="highlight-icon">

                    <i class="bi bi-person-workspace"></i>

                </div>

                <div>

                    <span class="highlight-label">

                        Organizer

                    </span>

                    <h5>

                        {{ trek.organizer }}

                    </h5>

                </div>

            </div>

        </div>

        <div class="col-lg-4 col-md-6">

            <div class="highlight-card">

                <div class="highlight-icon">

                    <i class="bi bi-people-fill"></i>

                </div>

                <div>

                    <span class="highlight-label">

                        Capacity

                    </span>

                    <h5>

                        {{ trek.capacity }} Participants

                    </h5>

                </div>

            </div>

        </div>

        <div class="col-lg-4 col-md-6">

            <div class="highlight-card">

                <div class="highlight-icon">

                    <i class="bi bi-person-check-fill"></i>

                </div>

                <div>

                    <span class="highlight-label">

                        Slots Left

                    </span>

                    <h5>

                        {{ trek.available_slots }}

                    </h5>

                </div>

            </div>

        </div>

        <div class="col-lg-4 col-md-6">

            <div class="highlight-card">

                <div class="highlight-icon">

                    <i class="bi bi-geo-alt-fill"></i>

                </div>

                <div>

                    <span class="highlight-label">

                        Meeting Point

                    </span>

                    <h5>

                        {{ trek.meeting_point }}

                    </h5>

                </div>

            </div>

        </div>

    </div>

</section>

<!-- ==========================================================
ABOUT TREK
========================================================== -->

<section class="about-section">

    <div class="about-card">

        <div class="section-title">

            <span>ABOUT THE TREK</span>

            <h2>
                Experience Nature Like Never Before
            </h2>

        </div>

        <p class="about-description">

            {{ trek.description }}

        </p>

    </div>

</section>

<!-- ==========================================================
TREK INFORMATION
========================================================== -->

<section class="info-section">

    <div class="section-title">

        <span>TREK INFORMATION</span>

        <h2>Know Your Adventure</h2>

    </div>

    <div class="row g-4">

        <!-- Location -->

        <div class="col-lg-4 col-md-6">

            <div class="info-card">

                <i class="bi bi-geo-alt-fill"></i>

                <h5>Location</h5>

                <p>{{ trek.location }}, {{ trek.state }}</p>

            </div>

        </div>

        <!-- Meeting Point -->

        <div class="col-lg-4 col-md-6">

            <div class="info-card">

                <i class="bi bi-signpost-fill"></i>

                <h5>Meeting Point</h5>

                <p>{{ trek.meeting_point }}</p>

            </div>

        </div>

        <!-- Organizer -->

        <div class="col-lg-4 col-md-6">

            <div class="info-card">

                <i class="bi bi-person-badge-fill"></i>

                <h5>Organizer</h5>

                <p>{{ trek.organizer }}</p>

            </div>

        </div>

        <!-- Start Date -->

        <div class="col-lg-4 col-md-6">

            <div class="info-card">

                <i class="bi bi-calendar-event-fill"></i>

                <h5>Start Date</h5>

                <p>{{ trek.start_date }}</p>

            </div>

        </div>

        <!-- End Date -->

        <div class="col-lg-4 col-md-6">

            <div class="info-card">

                <i class="bi bi-calendar-check-fill"></i>

                <h5>End Date</h5>

                <p>{{ trek.end_date }}</p>

            </div>

        </div>

        <!-- Emergency -->

        <div class="col-lg-4 col-md-6">

            <div class="info-card">

                <i class="bi bi-exclamation-triangle-fill"></i>

                <h5>Emergency Level</h5>

                <p>{{ trek.emergency_level }}</p>

            </div>

        </div>

    </div>

</section>

<!-- ==========================================================
TREK REQUIREMENTS
========================================================== -->

<section class="requirements-section">

    <div class="section-title">

        <span>TREK REQUIREMENTS</span>

        <h2>Prepare Before You Begin</h2>

    </div>

    <div class="row g-4">

        <!-- Fitness -->

        <div class="col-lg-3 col-md-6">

            <div class="requirement-card">

                <div class="requirement-icon">

                    <i class="bi bi-heart-pulse-fill"></i>

                </div>

                <h5>Fitness Level</h5>

                <p>

                    {{ trek.fitness_requirement }}

                </p>

            </div>

        </div>

        <!-- Age -->

        <div class="col-lg-3 col-md-6">

            <div class="requirement-card">

                <div class="requirement-icon">

                    <i class="bi bi-person-fill"></i>

                </div>

                <h5>Age Limit</h5>

                <p>

                    {{ trek.minimum_age }} - {{ trek.maximum_age }} Years

                </p>

            </div>

        </div>

        <!-- Equipment -->

        <div class="col-lg-3 col-md-6">

            <div class="requirement-card">

                <div class="requirement-icon">

                    <i class="bi bi-backpack4-fill"></i>

                </div>

                <h5>Equipment</h5>

                <p>

                    {{ trek.equipment_required }}

                </p>

            </div>

        </div>

        <!-- STAFF -->

        <div class="col-lg-3 col-md-6">
            <div class="requirement-card">
                
                <div class="requirement-icon">
                    <i class="bi bi-person-badge"></i>
                </div>

                            <h5>
                                {{ staff.full_name }}
                            </h5>
                            <p>
                                {{ staff.profession }}
                            </p>
                            <p>
                                {{ staff.role_in_trek }}
                            </p>
                            <p>
                                {{ staff.experience_years }} Years Experience
                            </p>
            </div>
        </div>
        <!-- STAFF ENDS -->

    </div>

</section>

<!-- ==========================================================
TREK GALLERY
========================================================== -->

<section class="gallery-section">

    <div class="section-title">

        <span>TREK GALLERY</span>

        <h2>Moments From The Journey</h2>

        <p>

            Explore breathtaking views and unforgettable memories captured along the trail.

        </p>

    </div>

    <div class="row g-4">

        <div
            class="col-lg-4 col-md-6"
            v-for="media in trek.gallery"
            :key="media.id"
        >

            <div class="gallery-card">

                <img
                    :src="media.media_url"
                    :alt="media.caption"
                >

                <div class="gallery-overlay">

                    <h6>

                        {{ media.caption }}

                    </h6>

                </div>

            </div>

        </div>

    </div>

</section>

<!-- ==========================================================
BOOK TREK
========================================================== -->

<section class="booking-section">

    <div class="booking-card">

        <div class="row align-items-center">

            <!-- Left -->

            <div class="col-lg-8">

                <span class="booking-tag">

                    READY FOR YOUR NEXT ADVENTURE?

                </span>

                <h2>

                    Reserve Your Trek Today

                </h2>

                <p>

                    Join fellow adventurers on an unforgettable journey through
                {{ trek.location }}, {{ trek.state }}.
                Secure your spot before registrations close and experience
                one of India's most memorable trekking adventures.

                </p>

                <div class="booking-info">

                    <div>

                        <i class="bi bi-calendar-event-fill"></i>

                        Registration closes before

                        <strong>{{ trek.start_date }}</strong>

                    </div>

                    <div>

                        <i class="bi bi-people-fill"></i>

                        Only

                        <strong>{{ trek.available_slots }}</strong>

                        of

                        <strong>{{ trek.capacity }}</strong>

                        spots remaining

                    </div>

                </div>

            </div>

            <!-- Right -->

            <div class="col-lg-4">

                <div class="price-box">

                    <span class="price-title">

                        Starting From

                    </span>

                    <h1>

                        ₹ {{ trek.price }}

                    </h1>

                    <button
    class="book-btn"
    :disabled="trek.available_slots === 0"
    @click="bookTrek"
>
    <i class="bi bi-bag-check-fill"></i>

    {{ trek.available_slots === 0 ? "Sold Out" : "Book This Trek" }}
</button>

                </div>

            </div>

        </div>

    </div>

</section>

<div>
    <button class="back-btn"
                            @click="$router.push('/user-browse-treks')"
                        >
                            <i class="bi bi-arrow-left me-2"></i>
                            Back to Treks
                        </button>
</div>

</div>
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

/*==================================================
CONTENT BACKGROUND
==================================================*/

.content-bg{
    position: relative;
    padding: 40px 0 120px;
    inset:0;
    background:
        linear-gradient(
            rgba(255,255,255,.58),
            rgba(255,255,255,.62)
        ),
        url("@/assets/images/user-bg.jpg");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
    z-index:0;
}

.content-bg::before{
    content: "";
    position: absolute;
    inset: 0;
    backdrop-filter: blur(2px);
    z-index: 0;
}

.content-bg > *{
    position: relative;
    z-index: 2;
}

/*==================================================
TREK HEADER
==================================================*/

.trek-header{

    padding:60px 7% 35px;

}

.header-top{

    display:flex;

    justify-content:space-between;

    align-items:flex-start;

    gap:30px;

}

.back-btn{

    background:white;

    border:none;

    border-radius:14px;

    padding:12px 22px;

    color:#0A3323;

    font-weight:700;

    box-shadow:0 10px 30px rgba(0,0,0,.08);

    transition:.35s;
    margin-left: 1200px;

}

.back-btn:hover{

    background:#0A3323;

    color:white;

    transform:translateY(-3px);

}

.trek-title{

    margin-top:28px;

    font-size:3.3rem;

    font-weight:800;

    color:#0A3323;

    line-height:1.1;

}

.trek-location{

    margin-top:12px;

    font-size:1.15rem;

    color:#555;

}

.trek-location i{

    color:#839958;

    margin-right:8px;

}

/*==================================================
TREK COVER
==================================================*/

.cover-section{

    padding:0 7% 60px;

}

.cover-card{

    position:relative;

    height:520px;

    border-radius:30px;

    overflow:hidden;

    box-shadow:0 25px 60px rgba(0,0,0,.18);

}

.cover-card img{

    width:100%;

    height:100%;

    object-fit:cover;

    transition:.5s;

}

.cover-card:hover img{

    transform:scale(1.05);

}

.cover-card::after{

    content:"";

    position:absolute;

    inset:0;

    background:linear-gradient(
        rgba(0,0,0,.10),
        rgba(0,0,0,.20),
        rgba(0,0,0,.55)
    );

}

.cover-overlay{

    position:absolute;

    left:35px;

    right:35px;

    bottom:30px;

    display:flex;

    gap:16px;

    z-index:2;

}

.cover-badge{

    padding:12px 24px;

    border-radius:50px;

    font-weight:700;

    backdrop-filter:blur(18px);

}

.difficulty{

    background:rgba(131,153,88,.92);

    color:white;

}

.status{

    background:rgba(255,255,255,.90);

    color:#0A3323;

}

.price{

    margin-left:auto;

    background:#0A3323;

    color:white;

}

/*==================================================
TREK HIGHLIGHTS
==================================================*/

.highlights-section{

    padding:0 7% 70px;

}

.highlight-card{

    display:flex;

    align-items:center;

    gap:20px;

    padding:28px;

    height:100%;

    background:rgba(255,255,255,.75);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,.55);

    border-radius:22px;

    transition:.35s;

    box-shadow:0 18px 45px rgba(0,0,0,.08);

}

.highlight-card:hover{

    transform:translateY(-8px);

    box-shadow:0 25px 55px rgba(10,51,35,.15);

}

.highlight-icon{

    width:72px;

    height:72px;

    border-radius:18px;

    background:#839958;

    color:white;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:28px;

    flex-shrink:0;

}

.highlight-label{

    display:block;

    color:#777;

    font-size:14px;

    margin-bottom:6px;

    text-transform:uppercase;

    letter-spacing:1px;

}

.highlight-card h5{

    margin:0;

    font-size:1.3rem;

    font-weight:700;

    color:#0A3323;

}

/*==================================================
ABOUT TREK
==================================================*/

.about-section{

    padding:0 7% 80px;

}

.about-card{

    background:rgba(255,255,255,.72);

    backdrop-filter:blur(18px);

    border-radius:28px;

    padding:55px;

    box-shadow:0 18px 45px rgba(0,0,0,.08);

}

.section-title span{

    color:#839958;

    font-weight:700;

    letter-spacing:4px;

    font-size:14px;

}

.section-title h2{

    margin-top:12px;

    margin-bottom:30px;

    font-size:2.5rem;

    color:#0A3323;

    font-weight:800;

}

.about-description{

    font-size:1.1rem;

    line-height:2.1;

    color:#555;

    text-align:justify;

    white-space:pre-line;

}

/*==================================================
TREK INFORMATION
==================================================*/

.info-section{

    padding:0 7% 80px;

}

.info-card{

    background:rgba(255,255,255,.78);

    backdrop-filter:blur(18px);

    border-radius:24px;

    padding:35px 30px;

    text-align:center;

    height:100%;

    transition:.35s;

    box-shadow:0 18px 40px rgba(0,0,0,.08);

}

.info-card:hover{

    transform:translateY(-8px);

    box-shadow:0 28px 60px rgba(10,51,35,.15);

}

.info-card i{

    font-size:2rem;

    color:#839958;

    margin-bottom:18px;

}

.info-card h5{

    color:#0A3323;

    font-weight:700;

    margin-bottom:10px;

}

.info-card p{

    color:#666;

    margin:0;

    line-height:1.7;

}

/*==================================================
TREK REQUIREMENTS
==================================================*/

.requirements-section{

    padding:0 7% 90px;

}

.requirement-card{

    background:rgba(255,255,255,.80);

    backdrop-filter:blur(18px);

    border-radius:24px;

    padding:35px 28px;

    height:100%;

    text-align:center;

    transition:.35s;

    box-shadow:0 18px 40px rgba(0,0,0,.08);

}

.requirement-card:hover{

    transform:translateY(-10px);

    box-shadow:0 30px 65px rgba(10,51,35,.15);

}

.requirement-icon{

    width:78px;

    height:78px;

    margin:auto;

    margin-bottom:22px;

    border-radius:20px;

    background:#839958;

    display:flex;

    align-items:center;

    justify-content:center;

}

.requirement-icon i{

    color:white;

    font-size:30px;

}

.requirement-card h5{

    color:#0A3323;

    font-weight:700;

    margin-bottom:15px;

}

.requirement-card p{

    color:#666;

    line-height:1.8;

    margin:0;

}


/*==================================================
TREK GALLERY
==================================================*/

.gallery-section{

    padding:0 7% 100px;

}

.gallery-section p{

    color:#666;

    margin-top:12px;

}

.gallery-card{

    position:relative;

    border-radius:24px;

    overflow:hidden;

    cursor:pointer;

    box-shadow:0 20px 45px rgba(0,0,0,.10);

}

.gallery-card img{

    width:100%;

    height:280px;

    object-fit:cover;

    transition:.55s;

}

.gallery-overlay{

    position:absolute;

    inset:0;

    display:flex;

    align-items:flex-end;

    padding:25px;

    background:linear-gradient(
        transparent,
        rgba(0,0,0,.75)
    );

    opacity:0;

    transition:.35s;

}

.gallery-overlay h6{

    color:white;

    font-size:18px;

    margin:0;

}

.gallery-card:hover img{

    transform:scale(1.08);

}

.gallery-card:hover .gallery-overlay{

    opacity:1;

}

/*==================================================
BOOK TREK
==================================================*/

.booking-section{

    padding:0 7% 120px;

}

.booking-card{

    background:linear-gradient(
        135deg,
        rgba(10,51,35,.95),
        rgba(26,83,64,.95)
    );

    color:white;

    border-radius:32px;

    padding:60px;

    overflow:hidden;

    position:relative;

    box-shadow:0 30px 70px rgba(10,51,35,.25);

}

.booking-card::before{

    content:"";

    position:absolute;

    top:-120px;

    right:-120px;

    width:300px;

    height:300px;

    border-radius:50%;

    background:rgba(255,255,255,.05);

}

.booking-tag{

    letter-spacing:4px;

    color:#D8E7B5;

    font-size:14px;

    font-weight:700;

}

.booking-card h2{

    margin:18px 0;

    font-size:3rem;

    font-weight:800;

}

.booking-card p{

    color:rgba(255,255,255,.85);

    line-height:2;

    margin-bottom:35px;

}

.booking-info{

    display:flex;

    flex-direction:column;

    gap:18px;

}

.booking-info div{

    font-size:17px;

}

.booking-info i{

    color:#D8E7B5;

    margin-right:10px;

}

.price-box{

    background:rgba(255,255,255,.10);

    backdrop-filter:blur(15px);

    border-radius:24px;

    padding:40px;

    text-align:center;

}

.price-title{

    color:#D8E7B5;

    letter-spacing:2px;

    font-size:14px;

}

.price-box h1{

    font-size:3.8rem;

    margin:20px 0;

    font-weight:800;

}

.book-btn{

    width:100%;

    border:none;

    border-radius:18px;

    padding:18px;

    background:#F7F4D5;

    color:#0A3323;

    font-weight:700;

    transition:.35s;

}

.book-btn:hover{

    background:white;

    transform:translateY(-4px);

}

.book-btn:disabled{

    background:#adb5bd;

    color:white;

    cursor:not-allowed;

    opacity:.75;

}
</style>

<script>
import axios from "axios";

export default {

    name: "UserViewTrek",

    data() {
        return {
            trek: {},
            staff: {}
        };
    },

    mounted() {
        this.fetchTrek();
    },

    methods: {

        async fetchTrek() {
            try {
                const response = await axios.get(
                    `http://127.0.0.1:5000/api/user/view-trek/${this.$route.params.id}`,
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem("access_token")}`
                        }
                    }
                );
                this.trek = response.data.data;
                this.staff = response.data.data.staff;
            }

            catch (error) {

                if (error.response?.data?.msg === "Token has expired") {

                    localStorage.removeItem("access_token");

                    this.$router.push("/login");

                    return;

                }

                console.error(error);

            }

        },

        goBack() {

            this.$router.push("/user-browse-treks");

        },

        viewTrek(id) {
            this.$router.push(`/user-view-trek/${id}`);
        },

        bookTrek() {

    if (this.trek.available_slots === 0) {

        this.errorMessage = "Sorry! This trek is fully booked.";

        return;

    }

    this.$router.push(`/user-book-trek/${this.trek.id}`);

}

    }

};
</script>
