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
            <router-link to="/user-dashboard" class="nav-link active-link"> Dashboard </router-link>
            <router-link to="/user-browse-treks" class="nav-link"> Browse Treks </router-link>
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
    <!-- NAVBAR ENDS -->
     
    <!-- HERO SECTION -->
    <section class="hero-section">
        <div class="hero-overlay">
            <div class="hero-content">
                <h1 class="hero-title">
                    Discover India's Most Beautiful Treks
                </h1>
            </div>
        </div>
    </section>
    <!-- HERO SECTION ENDS -->
     
    <!-- CONTENT -->
    <div class="content-bg">
        
        <!-- Stats -->
        <section class="dashboard-section">
            <div class="section-heading">
                Your Adventure At A Glance
            </div>

            <p class="section-subheading">
                Track your trekking journey, upcoming adventures and achievements.
            </p>
            
            <div class="stats-grid">
                <div class="glass-card stat-card">
                    <div class="stat-icon">
                        <i class="bi bi-backpack2-fill"></i>
                    </div>
                    <h2>{{ dashboard.total }}</h2>
                    <span>Total Bookings</span>
                </div>
                
                <div class="glass-card stat-card">
                    <div class="stat-icon">
                        <i class="bi bi-calendar-event-fill"></i>
                    </div>
                    <h2>{{ dashboard.pending }}</h2>
                    <span>Pending Bookings</span>
                </div>
                
                <div class="glass-card stat-card">
                    <div class="stat-icon">
                        <i class="bi bi-check-circle-fill"></i>
                    </div>
                    <h2>{{ dashboard.accepted }}</h2>
                    <span>Accepted Bookings</span>
                </div>
                
                <div class="glass-card stat-card">
                    <div class="stat-icon">
                        <i class="bi bi-x-circle-fill"></i>
                    </div>
                    <h2>{{ dashboard.rejected }}</h2>
                    <span>Rejected Bookings</span>
                </div>
            </div>
        </section>
        <!-- STATS SECTION ENDS -->

        <section class="dashboard-section">
            <div class="glass-card export-card">
                <div>
                    <h2>Export Booking History</h2>
                    <p>Get a CSV of all your trek bookings by email.</p>
                </div>
                <button class="primary-btn" :disabled="exportPending" @click="requestBookingExport">
                    <i class="bi bi-file-earmark-spreadsheet me-2"></i>
                    {{ exportPending ? 'Preparing CSV...' : 'Export CSV' }}
                </button>
            </div>
            <p v-if="exportMessage" class="export-message">{{ exportMessage }}</p>
        </section>

        <!-- Upcoming Trek -->
        <section class="dashboard-section">
            <h2 class="section-heading">
                Your Next Adventure
            </h2>
            
            <p class="section-subheading">
                Here's your next booked trekking experience.
            </p>
            
            <div class="glass-card upcoming-card" v-if="nextTrek">
                <img :src="nextTrek.cover_image" class="upcoming-image">
                
                <div class="upcoming-content">
                    <span class="upcoming-tag">
                        Upcoming Trek
                    </span>
                    
                    <h2>
                        {{ nextTrek.trek_name }}
                    </h2>

                    <p>
                        <i class="bi bi-geo-alt-fill me-2"></i>
                        {{ nextTrek.location }}, {{ nextTrek.state }}
                    </p>
                    
                    <div class="upcoming-info">
                        <div>
                            <i class="bi bi-calendar-event"></i>
                            {{ nextTrek.start_date }}
                        </div>
                        <div>
                            <i class="bi bi-flag-fill"></i>
                            {{ nextTrek.difficulty }}
                        </div>
                        <div>
                            <i class="bi bi-people-fill"></i>
                            {{ nextTrek.number_of_people }} Participants
                        </div>
                    </div>
                    
                    <div class="upcoming-buttons">
                        <button class="primary-btn" @click="$router.push('/user-my-bookings')">
                            View Booking
                        </button>
                        <button class="secondary-btn" @click="$router.push('/user-browse-treks')">
                            Browse More Treks
                        </button>
                    </div>

                </div>
            </div>
        </section>
        <!-- UPCOMING TREK ENDS -->

        <!-- Featured Treks -->
        <section class="dashboard-section">
            <h2 class="section-heading">
                Recommended Treks
            </h2>
            <p class="section-subheading">
                Adventures handpicked for your next journey.
            </p>
            <div class="recommend-grid">
                <div class="recommend-card glass-card"
                    v-for="trek in recommendedTreks"
                    :key="trek.id"
                >
                    <img :src="trek.cover_image" class="recommend-image">
                    <div class="recommend-body">
                        <span class="difficulty">
                            {{ trek.difficulty }}
                        </span>
                        <h4>
                            {{ trek.trek_name }}
                        </h4>
                        <p>
                            <i class="bi bi-geo-alt-fill"></i>
                            {{ trek.location }}
                        </p>
                        <button class="recommend-btn"
                            @click="$router.push(`/user-view-trek/${trek.id}`)"
                        >
                            View Details
                        </button>
                    </div>
                </div>
            </div>
        </section>
        <!-- FEATURED TREKS ENDS -->

        <!-- EXPLORE BY CATEGORY -->
        <section class="dashboard-section">
            <h2 class="section-heading">
                Explore By Category
            </h2>
            <p class="section-subheading">
                Choose your favourite adventure style.
            </p>
            
            <div class="category-grid">
                <div class="category-card"
                    @click="goToCategory('Camping')"
                >
                    <i class="bi bi-fire"></i>
                    <h5>Camping</h5>
                </div>
                
                <div class="category-card"
                    @click="goToCategory('Mountain')"
                >
                    <i class="bi bi-image-alt"></i>
                    <h5>Mountain</h5>
                </div>
                
                <div class="category-card"
                    @click="goToCategory('Forest')"
                >
                    <i class="bi bi-tree-fill"></i>
                    <h5>Forest</h5>
                </div>

                <div
                    class="category-card"
                    @click="goToCategory('Snow')"
                >
                    <i class="bi bi-snow"></i>
                    <h5>Snow</h5>
                </div>

                <div class="category-card"
                    @click="goToCategory('Spiritual')"
                >
                    <i class="bi bi-stars"></i>
                    <h5>Spiritual</h5>
                </div>

                <div class="category-card"
                    @click="goToCategory('Adventure')"
                >
                    <i class="bi bi-compass-fill"></i>
                    <h5>Adventure</h5>
                </div>
            </div>
        </section>
        <!-- EXPLORE BY CATEGORY ENDS -->

        <!-- Quotes -->
        <section class="dashboard-section">
            <div class="quote-card">
                <h2>
                    "The mountains are calling, and I must go."
                </h2>
                <p>
                    — John Muir
                </p>
            </div>
        </section>
    
    <!-- RECENT ACTIVITY -->
    <section class="dashboard-section">
        <h2 class="section-heading">
            Recent Activity
        </h2>
        <p class="section-subheading">
            Stay updated with your latest actions.
        </p>
        <div class="activity-container">
            <div class="activity-card"
                v-for="activity in recentActivity"
                :key="activity.id"
            >
                <div class="activity-icon">
                    <i :class="activity.icon"></i>
                </div>
                <div class="activity-details">
                    <h4>
                        {{ activity.title }}
                    </h4>
                    <p>
                        {{ activity.description }}
                    </p>
                    <span>
                        {{ activity.time }}
                    </span>
                </div>
            </div>
        </div>
    </section>
    <!-- RECENT ACTIVITY ENDS -->

    </div>
    <!-- CONTENT ENDS -->

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

/* USER NAVBAR */
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

/* HERO */
.hero-section{
    position:relative;
    height:100vh;
    min-height:950px;
    margin-top:-90px;
    padding-top:120px;
    overflow:hidden;
    background:url("@/assets/images/user-bg.jpg");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
    display:flex;
    align-items:center;
}

.hero-section::before {
    content: '';
    position: absolute;
    inset: 0;
    background:linear-gradient(
        rgba(10,51,35,.28),
        rgba(10,51,35,.10),
        rgba(10,51,35,.30)
    );
    z-index: 1;
}

.hero-overlay{
    width:100%;
    height:100%;
    display:flex;
    align-items:center;
    justify-content:flex-start;
    padding:0 8%;
}

.hero-content{
    width:100%;
    margin-left:0;
    padding:0;
    position:relative;
    z-index:3;
    text-align:center;
    margin-top: 0px;
}

.hero-title{
    font-size:5.3rem;
    line-height:1;
    font-weight:800;
    color:rgb(176, 174, 174);
}

/* CONTENT SECTION */
.content-bg{
    position:relative;
    width:100%;
    min-height:100vh;
    padding:90px 7% 120px;
    background:url("@/assets/images/user-bg.jpg");
    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;
    overflow:hidden;
    z-index:1;
}

/* Dark Overlay */
.content-bg::before{
    content:"";
    position:absolute;
    inset:0;
    background:rgba(10,51,35,.45);
    backdrop-filter:blur(2px);
    z-index:0;
}

/* Everything inside stays above overlay */
.content-bg > *{
    position:relative;
    z-index:2;
}

/* Smooth spacing between sections */
.dashboard-section{
    margin-bottom:90px;
}

/* Section Headings */
.section-heading{
    color:#fff;
    font-size:2.6rem;
    font-weight:800;
    margin-bottom:12px;
}

.section-subheading{
    color:rgba(255,255,255,.82);
    font-size:1.05rem;
    margin-bottom:45px;
    max-width:700px;
}

/* Glass Cards */
.glass-card{
    background:rgba(255,255,255,.14);
    border:1px solid rgba(255,255,255,.18);
    backdrop-filter:blur(22px);
    border-radius:30px;
    box-shadow:0 20px 45px rgba(0,0,0,.18);
}


/* STATS */
.stats-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:35px;
}

.stat-card{
    padding:45px 30px;
    text-align:center;
    transition:.35s;
}

.stat-card:hover{
    transform:translateY(-10px);
    box-shadow:0 25px 45px rgba(0,0,0,.25);
}

.stat-icon{
    width:85px;
    height:85px;
    margin:auto;
    border-radius:22px;
    background:#839958;
    display:flex;
    justify-content:center;
    align-items:center;
    color:white;
    font-size:2rem;
    margin-bottom:25px;
}

.stat-card h2{
    color:white;
    font-size:3rem;
    font-weight:800;
    margin-bottom:8px;
}

.stat-card span{
    color:rgba(255,255,255,.88);
    font-size:1.05rem;
    letter-spacing:.5px;
}

.export-card{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:24px;
    padding:28px 32px;
}

.export-card h2{
    margin:0 0 8px;
    color:white;
    font-size:1.6rem;
}

.export-card p,
.export-message{
    margin:0;
    color:rgba(255,255,255,.88);
}

.export-message{
    margin-top:12px;
}

/* UPCOMING TREK */
.upcoming-card{
    display:flex;
    gap:40px;
    padding:35px;
    align-items:center;
}

.upcoming-image{
    width:380px;
    height:260px;
    object-fit:cover;
    border-radius:24px;
}

.upcoming-content{
    flex:1;
}

.upcoming-tag{
    display:inline-block;
    padding:8px 18px;
    background:#839958;
    color:white;
    border-radius:30px;
    font-weight:600;
    margin-bottom:20px;
}

.upcoming-content h2{
    color:white;
    font-size:2.5rem;
    font-weight:700;
    margin-bottom:18px;
}

.upcoming-content p{
    color:rgba(255,255,255,.9);
    font-size:1.1rem;
}

.upcoming-info{
    display:flex;
    gap:35px;
    margin:30px 0;
    color:white;
}

.upcoming-info div{
    display:flex;
    align-items:center;
    gap:10px;
}

.upcoming-buttons{
    display:flex;
    gap:18px;
}

.primary-btn{
    background:#839958;
    color:white;
    border:none;
    padding:14px 30px;
    border-radius:16px;
    font-weight:600;
}

.secondary-btn{
    background:white;
    color:#0A3323;
    border:none;
    padding:14px 30px;
    border-radius:16px;
    font-weight:600;
}

/* RECOMMENDED TREKS */
.recommend-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:30px;
}

.recommend-card{
    overflow:hidden;
    transition:.35s;
}

.recommend-card:hover{
    transform:translateY(-10px);
}

.recommend-image{
    width:100%;
    height:220px;
    object-fit:cover;
}

.recommend-body{
    padding:22px;
}

.recommend-body h4{
    color:white;
    font-size:1.4rem;
    margin:18px 0 12px;
}

.recommend-body p{
    color:rgba(255,255,255,.85);
}

.difficulty{
    background:#839958;
    color:white;
    padding:7px 15px;
    border-radius:20px;
    font-size:.9rem;
}

.recommend-btn{
    margin-top:22px;
    width:100%;
    border:none;
    border-radius:15px;
    padding:13px;
    background:#0A3323;
    color:white;
    font-weight:600;
    transition:.3s;
}

.recommend-btn:hover{
    background:#839958;
}

/* CATEGORY */
.category-grid{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:30px;
}

.category-card{
    background:rgba(255,255,255,.15);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,.18);
    border-radius:26px;
    padding:40px 20px;
    text-align:center;
    cursor:pointer;
    transition:.35s;
}

.category-card:hover{
    transform:translateY(-10px);
    background:rgba(131,153,88,.85);
}

.category-card i{
    font-size:3rem;
    color:white;
    margin-bottom:20px;
}

.category-card h5{
    color:white;
    font-size:1.2rem;
    font-weight:700;
}
.quote-card{
    padding:80px 40px;
    text-align:center;
    background:rgba(255,255,255,.12);
    backdrop-filter:blur(20px);
    border-radius:35px;
}

.quote-card h2{
    color:white;
    font-size:2.8rem;
    font-weight:700;
    font-style:italic;
    line-height:1.5;
}

.quote-card p{
    margin-top:25px;
    color:#F7F4D5;
    font-size:1.2rem;
}

/* RECENT ACTIVITY */
.activity-container{
    display:flex;
    flex-direction:column;
    gap:20px;
}

.activity-card{
    display:flex;
    align-items:center;
    gap:25px;
    padding:24px 30px;
    border-radius:22px;
    background:rgba(255,255,255,.12);
    backdrop-filter:blur(16px);
    border:1px solid rgba(255,255,255,.18);
    transition:.3s;
}

.activity-card:hover{
    transform:translateX(8px);
}

.activity-icon{
    width:70px;
    height:70px;
    border-radius:18px;
    background:#839958;
    display:flex;
    justify-content:center;
    align-items:center;
    color:white;
    font-size:1.6rem;
}

.activity-details{
    flex:1;
}

.activity-details h4{
    color:white;
    font-size:1.2rem;
    font-weight:700;
    margin-bottom:8px;
}

.activity-details p{
    color:rgba(255,255,255,.85);
    margin-bottom:6px;
}

.activity-details span{
    color:#F7F4D5;
    font-size:.9rem;
}

</style>

<script>
import axios from "axios";

export default {

    name: "UserDashboard",

    data() {

        return {

            dashboard: {

                total: 0,

                pending: 0,

                accepted: 0,

                rejected: 0

            },

            nextTrek: null,

            recommendedTreks: [],

            featuredTrek: null,

            recentActivity: [],

            exportPending: false,

            exportMessage: ""

        };

    },

    mounted() {

        this.fetchDashboard();

    },

    methods: {

        async fetchDashboard() {

            try {

                const response = await axios.get(

                    "http://127.0.0.1:5000/api/user/dashboard",

                    {

                        headers: {

                            Authorization: `Bearer ${localStorage.getItem("access_token")}`

                        }

                    }

                );

                const data = response.data.data;

                // -----------------------------
                // Dashboard Statistics
                // -----------------------------
                

                this.dashboard = data.stats;

                // -----------------------------
                // Next Upcoming Trek
                // -----------------------------

                this.nextTrek = data.next_trek;

                // Recommended Treks
                this.recommendedTreks = data.recommended;

                // Featured Trek
                this.featuredTrek = data.featured_trek;

                // -----------------------------
                // Recent Activity
                // -----------------------------

                this.recentActivity = data.recent_activity;

            }

            catch (error) {

                if (

                    error.response?.data?.msg === "Token has expired"

                ) {

                    localStorage.removeItem("access_token");

                    this.$router.push("/login");

                    return;

                }

                console.error(error);

            }

        },

        viewTrek(id) {

            this.$router.push(`/user-view-trek/${id}`);

        },

        browseTreks() {

            this.$router.push("/user-browse-treks");

        },

        myBookings() {

            this.$router.push("/user-my-bookings");

        },

        goToCategory(category) {

            this.$router.push({

                path: "/user-browse-treks",

                query: {

                    category

                }

            });

        },

        async requestBookingExport() {
            this.exportPending = true;
            this.exportMessage = "Starting your booking-history export...";

            try {
                const token = localStorage.getItem("access_token");
                const response = await axios.post(
                    "http://127.0.0.1:5000/api/user/export-bookings",
                    {},
                    { headers: { Authorization: `Bearer ${token}` } }
                );
                this.exportMessage = response.data.message;
                this.pollExportStatus(response.data.task_id, token);
            } catch (error) {
                this.exportPending = false;
                this.exportMessage = error.response?.data?.message || "Unable to start the export.";
            }
        },

        pollExportStatus(taskId, token) {
            const intervalId = window.setInterval(async () => {
                try {
                    const response = await axios.get(
                        `http://127.0.0.1:5000/api/user/export-bookings/${taskId}`,
                        { headers: { Authorization: `Bearer ${token}` } }
                    );
                    this.exportMessage = response.data.message;
                    if (response.data.completed) {
                        this.exportPending = false;
                        window.clearInterval(intervalId);
                    }
                } catch (error) {
                    this.exportPending = false;
                    this.exportMessage = error.response?.data?.message || "Booking-history export failed.";
                    window.clearInterval(intervalId);
                }
            }, 2000);
        },
        

    }

};
</script>
