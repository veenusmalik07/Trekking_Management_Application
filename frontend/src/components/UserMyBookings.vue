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
      <router-link to="/user-my-bookings" class="nav-link active-link"> My Bookings </router-link>
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


  <!-- =======================================================
                        HERO SECTION
======================================================= -->

  <section class="bookings-hero">
    <div class="hero-overlay">
      <div class="hero-content">
        <small> MY TREKKING JOURNEY </small>

        <h1>My Bookings</h1>

        <p>
          Every adventure you've planned, every mountain you've conquered, and every unforgettable
          memory begins here.
        </p>
      </div>
    </div>
  </section>
   <div class="content-page">

  <!-- =======================================================
                    BOOKING STATISTICS
======================================================= -->
<br><br>

<section class="booking-stats">

    <!-- Row 1 -->

    <div class="row g-4 mb-4">

        <div class="col-lg-3 col-md-6">

            <div class="stat-card">

                <div class="stat-icon">
                    <i class="bi bi-backpack4-fill"></i>
                </div>

                <h2>{{ stats.total }}</h2>

                <p>Total Bookings</p>

            </div>

        </div>

        <div class="col-lg-3 col-md-6">

            <div class="stat-card">

                <div class="stat-icon">
                    <i class="bi bi-hourglass-split"></i>
                </div>

                <h2>{{ stats.pending }}</h2>

                <p>Pending Bookings</p>

            </div>

        </div>

        <div class="col-lg-3 col-md-6">

            <div class="stat-card">

                <div class="stat-icon">
                    <i class="bi bi-check2-circle"></i>
                </div>

                <h2>{{ stats.accepted }}</h2>

                <p>Accepted Bookings</p>

            </div>

        </div>

        <div class="col-lg-3 col-md-6">

            <div class="stat-card">

                <div class="stat-icon">
                    <i class="bi bi-x-octagon-fill"></i>
                </div>

                <h2>{{ stats.rejected }}</h2>

                <p>Rejected Bookings</p>

            </div>

        </div>

    </div>

    <!-- Row 2 -->

    <div class="row g-4">

        <div class="col-lg-4 col-md-6">

            <div class="stat-card">

                <div class="stat-icon">
                    <i class="bi bi-calendar2-event-fill"></i>
                </div>

                <h2>{{ stats.upcoming }}</h2>

                <p>Upcoming Treks</p>

            </div>

        </div>

        <div class="col-lg-4 col-md-6">

            <div class="stat-card">

                <div class="stat-icon">
                    <i class="bi bi-flag-fill"></i>
                </div>

                <h2>{{ stats.completed }}</h2>

                <p>Completed Treks</p>

            </div>

        </div>

        <div class="col-lg-4 col-md-12">

            <div class="stat-card">

                <div class="stat-icon">
                    <i class="bi bi-slash-circle-fill"></i>
                </div>

                <h2>{{ stats.cancelled }}</h2>

                <p>Cancelled Bookings</p>

            </div>

        </div>

    </div>

</section>

  <br><br>

  <!-- =======================================================
                SEARCH & FILTER
======================================================= -->

<section class="booking-filter-section">

    <div class="filter-card">

        <div class="row align-items-center g-4">

            <div class="col-lg-6">

                <div class="search-box">

                    <i class="bi bi-search"></i>

                    <input
                        type="text"
                        placeholder="Search by trek name..."
                        v-model="search"
                    >

                </div>

            </div>

            <div class="col-lg-6">

                <select
                    class="status-select"
                    v-model="selectedStatus"
                >

                    <option value="All">All Bookings</option>

                    <option value="Accepted">Accepted</option>

                    <option value="Cancelled">Cancelled</option>

                    <option value="Rejected">Rejected</option>

                    <option value="Pending">Pending</option>
                    <option value="Completed">Completed</option>
                    <option value="Upcoming">Upcoming</option>

                </select>

            </div>

        </div>

    </div>

</section>

<!-- =======================================================
                    MY BOOKINGS
======================================================= -->

<section class="bookings-list">

    <div
        class="booking-card"
        v-for="booking in filteredBookings"
        :key="booking.id"
    >

        <!-- Trek Cover -->

        <div class="booking-image">

            <img
                :src="booking.cover_image"
                alt=""
            >

            <span
                class="difficulty-badge"
                :class="booking.difficulty.toLowerCase()"
            >

                {{ booking.difficulty }}

            </span>

        </div>

        <!-- Booking Details -->

        <div class="booking-details">

            <div class="booking-header">

                <div>

                    <h2>

                        {{ booking.trek_name }}

                    </h2>

                    <p>

                        <i class="bi bi-geo-alt-fill"></i>

                        {{ booking.location }},
                        {{ booking.state }}

                    </p>

                </div>

                <span
                    class="status-badge"
                    :class="booking.booking_status.toLowerCase()"
                >

                    {{ booking.booking_status }}

                </span>

            </div>

            <div class="booking-grid">

                <div>

                    <small>Booking ID</small>

                    <h6>

                        {{ booking.booking_reference }}

                    </h6>

                </div>

                <div>

                    <small>Booking Date</small>

                    <h6>

                        {{ booking.booking_date }}

                    </h6>

                </div>

                <div>

                    <small>Participants</small>

                    <h6>

                        {{ booking.number_of_people }}

                    </h6>

                </div>

                <div>

                    <small>Total Paid</small>

                    <h6>

                        ₹ {{ booking.total_amount }}

                    </h6>

                </div>

                <div>

                    <small>Start Date</small>

                    <h6>

                        {{ booking.start_date }}

                    </h6>

                </div>

                <div>

                    <small>End Date</small>

                    <h6>

                        {{ booking.end_date }}

                    </h6>

                </div>

            </div>

            <div class="booking-actions">

                <button
                    class="view-btn"
                    @click="viewTrek(booking.trek_id)"
                >

                    View Trek

                </button>

                <button
    v-if="booking.booking_status=='Accepted'"
    class="cancel-btn"
    @click="cancelBooking(booking.id)"
>
    Cancel Booking
</button>

            </div>

        </div>

    </div>

</section>

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
.user-navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 88px;
  padding: 0 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(247, 244, 213, 0.95); /* Cream */
  backdrop-filter: blur(18px);
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.08);
  z-index: 9999;
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
  color: #0a3323;
}

.navbar-logo span {
  font-size: 2rem;
  color: #0a3323;
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

.active-link {
  background: #839958;
  color: white !important;
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
  background: #d3968c;
  background: #0a3323;
  color: white;
}
.logout-btn:hover {
  background: #d3968c;
  color: white;
}

/* =======================================================
                    HERO SECTION
======================================================= */

.bookings-hero {
    background: url('/src/assets/images/user-bg.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  position: relative;
  height: 100vh;
  min-height: 900px;
  margin-top: -90px;
  padding-top: 120px;
  overflow: hidden;
  display: flex;
  align-items: center;
}

.hero-overlay {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  padding: 60px;
  background: linear-gradient(
    90deg,
    rgba(6,48,35,.55),
    rgba(6,48,35,.25),
    rgba(6,48,35,.05)
  );
}

.hero-content {
  max-width: 620px;
  color: white;
}

.hero-content small {
  display: inline-block;

  margin-bottom: 18px;

  letter-spacing: 4px;

  font-size: 0.9rem;

  font-weight: 700;

  color: #eaf2c8;
}

.hero-content h1 {
  font-size: 4rem;

  font-weight: 800;

  margin-bottom: 18px;
}

.hero-content p {
  font-size: 1.15rem;

  line-height: 1.8;

  color: rgba(255, 255, 255, 0.92);
}

.content-page{
    position: relative;
    padding: 40px 0 120px;
    inset:0;
    background:
        linear-gradient(
            rgba(255,255,255,.24),
            rgba(255,255,255,.35)
        ),
        url("@/assets/images/staff-bg.jpg");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
    z-index:0;
}

.content-page::before{
    content: "";
    position: absolute;
    inset: 0;
    backdrop-filter: blur(2px);
    z-index: 0;
}

.content-page > *{
    position: relative;
    z-index: 2;
}

/* =======================================================
                BOOKING STATS
======================================================= */

.booking-stats {
  margin-bottom: 55px;
}

.stat-card {
  background: rgba(255, 255, 255, 0.18);

  backdrop-filter: blur(20px);

  border: 1px solid rgba(255, 255, 255, 0.25);

  border-radius: 24px;

  padding: 35px;

  text-align: center;

  transition: 0.35s;

  height: 100%;
  max-width: 300px;
  margin-left: 18px;
}

.stat-card:hover {
  transform: translateY(-8px);

  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.12);
}

.stat-icon {
  width: 75px;

  height: 75px;

  margin: auto;

  border-radius: 22px;

  background: #8da35b;

  color: white;

  display: flex;

  align-items: center;

  justify-content: center;

  font-size: 2rem;

  margin-bottom: 20px;
}

.stat-card h2 {
  font-size: 2.8rem;

  font-weight: 800;

  color: #063023;

  margin-bottom: 8px;
}

.stat-card p {
  margin: 0;

  font-size: 1.05rem;

  color: #666;
}

/* =======================================================
                SEARCH FILTER
======================================================= */

.booking-filter-section{

    margin-bottom:45px;

}

.filter-card{

    background:rgba(255,255,255,.18);

    backdrop-filter:blur(18px);

    border-radius:24px;

    padding:28px;
    max-width: 1400px;
    margin-left: 40px;

}

.search-box{

    position:relative;
}

.search-box i{

    position:absolute;

    left:20px;

    top:50%;

    transform:translateY(-50%);

    color:#8DA35B;

    font-size:1.2rem;

}

.search-box input{

    width:100%;

    height:58px;

    border:none;

    outline:none;

    border-radius:16px;

    padding-left:55px;

    background:white;

    font-size:1rem;

}

.status-select{

    width:100%;

    height:58px;

    border:none;

    outline:none;

    border-radius:16px;

    padding:0 18px;

    background:white;

    font-size:1rem;

    color:#063023;

    font-weight:600;

}

/* =======================================================
                    BOOKING CARD
======================================================= */

.bookings-list{

    display:flex;

    flex-direction:column;

    gap:100px;


}

.booking-card{

    display:flex;

    background:rgba(255,255,255,.18);

    backdrop-filter:blur(18px);

    border-radius:28px;

    overflow:hidden;

    transition:.35s;
    max-width: 1400px;
    margin-left: 40px;

}

.booking-card:hover{

    transform:translateY(-6px);

    box-shadow:0 18px 45px rgba(0,0,0,.15);

}

.booking-image{

    width:340px;

    position:relative;

    flex-shrink:0;

}

.booking-image img{

    width:100%;

    height:100%;

    object-fit:cover;

}

.booking-details{

    flex:1;

    padding:35px;

}

.booking-header{

    display:flex;

    justify-content:space-between;

    align-items:flex-start;

    margin-bottom:30px;

}

.booking-header h2{

    font-size:2rem;

    color:#063023;

    font-weight:800;

}

.booking-header p{

    color:#666;

    margin-top:8px;

}

.booking-grid{

    display:grid;

    grid-template-columns:repeat(3,1fr);

    gap:25px;

    margin-bottom:35px;

}

.booking-grid small{

    color:#777;

}

.booking-grid h6{

    margin-top:8px;

    font-size:1rem;

    color:#063023;

    font-weight:700;

}

.booking-actions{

    display:flex;

    gap:18px;

}

</style>

<script>
import axios from 'axios'

export default {
  name: 'UserProfile',

  data() {
    return {
      bookings: [],
      stats: {
        total: 0,
        upcoming: 0,
        completed: 0,
        cancelled: 0
      },
      search: "",
      selectedStatus: "All"
    }
  },

    mounted(){

    this.fetchBookings();

},

  methods: {
    async fetchBookings(){

    try{

        const response = await axios.get(

            "http://127.0.0.1:5000/api/user/my-bookings",

            {

                headers:{

                    Authorization:`Bearer ${localStorage.getItem("access_token")}`

                }

            }

        );

        this.bookings = response.data.data.bookings;

        this.stats = response.data.data.stats;

    }

    catch(error){

        console.error(error);

    }

},

viewTrek(id){

    this.$router.push(`/user-view-trek/${id}`);

},

async cancelBooking(id){

     console.log("Cancel clicked", id);

    const confirmCancel = confirm(
        "Are you sure you want to cancel this booking?"
    );

    if(!confirmCancel){

        return;

    }

    try{

        await axios.put(
    `http://127.0.0.1:5000/api/user/cancel-booking/${id}`,
    {},
    {
        headers: {
            Authorization: `Bearer ${localStorage.getItem("access_token")}`
        }
    }
);

        this.fetchBookings();

    }

    catch(error){

        alert(

            error.response?.data?.message ||

            "Unable to cancel booking."

        );

    }

}

  },

  computed: {
    filteredBookings() {

    return this.bookings.filter(booking => {

        const matchesSearch =
            booking.trek_name.toLowerCase().includes(this.search.toLowerCase());

        const matchesStatus =
            this.selectedStatus === "All" ||
            booking.booking_status === this.selectedStatus;

        return matchesSearch && matchesStatus;

    });

}
  }
}
</script>
