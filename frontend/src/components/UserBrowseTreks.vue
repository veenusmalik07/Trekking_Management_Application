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

  <br /><br /><br /><br /><br />

  <!-- HERO SECTION -->
  <section class="hero-section">
    <div class="hero-overlay">
      <div class="hero-content">
        <p class="hero-tag">EXPLORE • DISCOVER • TREK</p>

        <h1 class="hero-title">
          Find Your <br>
          Next Adventure
        </h1>

        <p class="hero-subtitle">
          Explore breathtaking trekking destinations across India and choose your perfect journey
          into nature.
        </p>

        <button class="explore-btn">
          <i class="bi bi-compass"></i>
          Start Exploring
        </button>
      </div>
    </div>
  </section>
  
  <div class="content-bg">
    
  <!-- WHY TREKMATE -->
  <section class="journey-section">
    <div class="container">
      <div class="row align-items-center g-5">

            <!-- Left Images -->
            <div class="col-lg-6">
                <div class="journey-grid">
                    <img src="@/assets/images/browse-trek-1.jpg" alt="">
                    <img src="@/assets/images/browse-trek-2.jpg" alt="">
                    <img src="@/assets/images/browse-trek-3.jpg" alt="">
                    <img src="@/assets/images/browse-trek-4.jpg" alt="">
                </div>
            </div>

            <!-- Right Content -->
            <div class="col-lg-6">
              <div class="journey-content">
                  <span class="journey-tag">
                    WHY TREKMATE
                  </span>
                  <h2>
                    Every Trail Begins With A Single Step.
                  </h2>
                  <p class="quote">
                    Mountains have a way of reminding us how small our worries really are.
                    Every trek is more than just reaching a destination—it's about embracing
                    the journey, discovering breathtaking landscapes, building confidence,
                    and creating memories that stay with you forever.
                  </p>
                  <p class="quote">
                    Whether you're chasing snowy summits, peaceful forests, or hidden valleys,
                    TrekMate connects you with safe, unforgettable adventures guided by
                    experienced organizers across India.
                  </p>
              </div>
            </div>
            </div>
        </div>
      </section>

  <!-- ==========================================================
SEARCH & FILTERS
========================================================== -->

  <section class="search-section">
    <div class="glass-search">
      <!-- Search -->

      <div class="search-box">
        <i class="bi bi-search"></i>

        <input
          type="text"
          class="form-control"
          placeholder="Search by trek, location or state..."
          v-model="search"
        />
      </div>

      <!-- Difficulty -->

      <select class="form-select filter-select" v-model="selectedDifficulty">
        <option value="All">All Difficulties</option>

        <option v-for="difficulty in difficulties" :key="difficulty" :value="difficulty">
          {{ difficulty }}
        </option>
      </select>

      <!-- State -->

      <select class="form-select filter-select" v-model="selectedState">
        <option value="All">All States</option>

        <option v-for="state in states" :key="state" :value="state">
          {{ state }}
        </option>
      </select>
    </div>
  </section>

  <div class="sort-container">

    <span class="sort-title">
        <i class="bi bi-funnel-fill"></i>
        Quick Sort
    </span>

    <button
        class="sort-chip"
        :class="{ active: sortBy==='newest' }"
        @click="sortBy='newest'"
    >
        Newest
    </button>

    <button
        class="sort-chip"
        :class="{ active: sortBy==='priceLow' }"
        @click="sortBy='priceLow'"
    >
        Price ↑
    </button>

    <button
        class="sort-chip"
        :class="{ active: sortBy==='priceHigh' }"
        @click="sortBy='priceHigh'"
    >
        Price ↓
    </button>

    <button
        class="sort-chip"
        :class="{ active: sortBy==='duration' }"
        @click="sortBy='duration'"
    >
        Duration
    </button>

    <button
        class="sort-chip"
        :class="{ active: sortBy==='difficulty' }"
        @click="sortBy='difficulty'"
    >
        Difficulty
    </button>

</div>

  <!--available treks-->

<section class="available-section">

    <div class="container-fluid">

        <div class="section-heading">

            <h2>

                Discover Treks

            </h2>

            <p>
              Discover scenic trails, challenge your limits, and find the perfect trek for your next unforgettable adventure.
            </p>

        </div>

        <div class="row g-4">

            <div
                class="col-lg-4 col-md-6"
                v-for="trek in filteredTreks"
                :key="trek.id"
            >

                <div class="trek-card">

                    <!-- Image -->

                    <div class="trek-image">

                        <img
                            :src="trek.cover_image"
                            :alt="trek.trek_name"
                        >

                        <span
    class="difficulty-badge"
    :class="{
        easy: trek.difficulty === 'Easy',
        moderate: trek.difficulty === 'Moderate',
        hard: trek.difficulty === 'Hard'
    }"
>
<i class="bi bi-lightning-charge-fill me-1"></i>
    {{ trek.difficulty }}
</span>

                        <span class="price-badge">

                            ₹ {{ trek.price }}

                        </span>

                    </div>

                    <!-- Body -->

                    <div class="trek-body">

                        <h4>

                            {{ trek.trek_name }}

                        </h4>

                        <p class="location">

                            <i class="bi bi-geo-alt-fill"></i>

                            {{ trek.location }}, {{ trek.state }}

                        </p>

                        <div class="trek-info">

                            <div>

                                <i class="bi bi-clock"></i>

                                {{ trek.duration }} Days

                            </div>

                            <div>

                                <i class="bi bi-people"></i>

                                {{ trek.available_slots }} / {{ trek.capacity }} Slots Left

                            </div>

                        </div>
                        <div class="booking-note">
    <i class="bi bi-calendar-check"></i>

    Book Before

    <strong>{{ trek.start_date }}</strong>
</div>

                        <button
                            class="view-btn"
                            @click="viewTrek(trek.id)"
                        >
                          View Details
                          <i class="bi bi-arrow-right ms-2"></i>
                        </button>

                    </div>

                </div>

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
HERO
==================================================*/
.hero-section{

    position:relative;

    height:100vh;

    min-height:850px;

    margin-top:-90px;

    padding-top:120px;

    overflow:hidden;

    background:url("@/assets/images/staff-bg.jpg");

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

  background: linear-gradient(
    rgba(10, 51, 35, 0.45),
    rgba(10, 51, 35, 0.15),
    rgba(10, 51, 35, 0.45)
  );
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

    width:42%;

    margin-left:0;

    padding:0;

    position:relative;

    z-index:5;

    text-align:left;
    margin-top: -60px;

}

.hero-tag{

    color:#0A3323;

    letter-spacing:6px;

    font-size:15px;

    margin-bottom:18px;

    font-weight:600;

}

.hero-title{

    font-size:5.3rem;

    line-height:1.05;

    font-weight:800;

    color:white;

}

.hero-subtitle{

    margin-top:28px;

    max-width:560px;

    font-size:1.25rem;

    line-height:1.9;

    color:rgba(255,255,255,.92);

}


.explore-btn{

    margin-top:38px;

    border:none;

    padding:18px 40px;

    border-radius:60px;

    font-size:18px;

    background:#F7F4D5;
color:#0A3323;
background:#839958;
color:white;
font-weight:700;

    transition:.35s;

}

.start-btn {
  background: #0a3323;

  color: white;

  transition: 0.35s;

  box-shadow: 0 15px 35px rgba(10, 51, 35, 0.35);
}

.start-btn:hover {
  transform: translateY(-5px);

  background: #839958;
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
WHY TREKMATE
==================================================*/

.journey-section{

    padding:120px 8%;

}

.journey-grid{

    display:grid;

    grid-template-columns:repeat(2,1fr);

    gap:20px;

}

.journey-grid img{

    width:100%;

    height:250px;

    object-fit:cover;

    border-radius:22px;

    transition:.45s;

    box-shadow:0 15px 35px rgba(0,0,0,.12);

}

.journey-grid img:hover{

    transform:translateY(-10px) scale(1.04);

    box-shadow:0 25px 50px rgba(0,0,0,.18);

}

.journey-content{

    padding-left:30px;

}

.journey-tag{

    display:inline-block;

    color:#839958;

    letter-spacing:4px;

    font-weight:700;

    margin-bottom:18px;

}

.journey-content h2{

    font-size:3rem;

    color:#0A3323;

    font-weight:800;

    margin-bottom:28px;

    line-height:1.2;

}

.journey-content .quote{
  font-family:"BrotherSignature", cursive;
    color:rgb(51, 50, 50);

    font-size:2rem;
  font-weight: 400;
  letter-spacing: 1.4px;
    line-height:1;

    margin-bottom:22px;

}


/*==================================================
SEARCH
==================================================*/
.search-section {
  width: 92%;
  margin:30px auto 35px;
  z-index: 20;
}

.glass-search{

    display:grid;

    grid-template-columns:2fr 1fr 1fr;

    gap:22px;

    padding:26px;

    border-radius:26px;

    background:rgba(131,153,88,.45);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,.2);

}


.search-box {
  position: relative;
}

.search-box i {
  position: absolute;

  left: 20px;

  top: 50%;

  transform: translateY(-50%);

  color: #670626;
}

.search-box input {
  padding-left: 55px;

  height: 58px;

  border-radius: 18px;

  border: none;
}

.filter-select {
  height: 58px;

  border-radius: 18px;

  border: none;
}

.sort-container{

    width:92%;

    margin:0 auto 40px;

    display:flex;

    align-items:center;

    flex-wrap:wrap;

    gap:14px;

}

.sort-title{

    font-size:18px;

    font-weight:700;

    color:#0A3323;

    margin-right:10px;

}

.sort-title i{

    color:#839958;

    margin-right:8px;

}

.sort-chip{

    padding:10px 22px;

    border-radius:50px;

    border:2px solid rgba(131,153,88,.35);

    background:rgba(255,255,255,.75);

    color:#0A3323;

    font-weight:600;

    transition:.3s;

    cursor:pointer;

    backdrop-filter:blur(10px);

}

.sort-chip:hover{

    background:#F7F4D5;

    transform:translateY(-2px);

    border-color:#839958;

}

.sort-chip.active{

    background:#839958;

    color:white;

    border-color:#839958;

    box-shadow:0 8px 20px rgba(131,153,88,.3);

}

/*==================================================
AVAILABLE TREKS
==================================================*/

.available-section{
  padding:10px 7% 70px;
}

.section-heading{
  margin-bottom:28px;
}

.section-tag{

    color:var(--secondary);

    letter-spacing:4px;

    font-weight:700;

}

.section-heading h2{

    color:var(--primary);

    font-size:2.5rem;

    font-weight:700;

}

.section-heading p{
  color:#666;
}

.trek-card::before{
    content:"";
    position:absolute;
    inset:0;
    border-radius:24px;
    pointer-events:none;
    transition:.4s;
}
.trek-card{
  background: rgba(255,255,255,.88);
  backdrop-filter: blur(14px);
  border: 1px solid rgba(255,255,255,.55);
  box-shadow: 0 20px 45px rgba(10,51,35,.12);
  border-radius:24px;
  overflow:hidden;
  transition:.35s;
  height:100%;
  transition: all .4s ease;
  transform: translateY(0);
  overflow: hidden;
  position: relative;
}
.trek-card::before{
    content:"";
    position:absolute;
    inset:0;
    border-radius:24px;
    border:2px solid transparent;
    transition:.35s;
}

.trek-card:hover::before{
    border-color:#839958;
}
.trek-card:hover{
    transform:translateY(-12px) scale(1.02);
    box-shadow:0 35px 70px rgba(10,51,35,.22);
}

.trek-image{
  position:relative;
  overflow:hidden; 
  height:250px;
}

.trek-image img{
  width:100%;
  height:100%;
  object-fit:cover;
  transition: transform .6s ease;
}

.trek-card:hover .trek-image img{
  transform:scale(1.08);
}

.easy{
    background:#7CB342;
    color:white;
}

.moderate{
    background:#F4B400;
    color:white;
}

.hard{
    background:#D94F4F;
    color:white;
}

.difficulty-badge{

    position:absolute;

    top:18px;

    left:18px;

    background:#0A3323;

    color:white;

    padding:6px 14px;

    border-radius:30px;

    font-size:13px;
    transition:.35s;
    box-shadow:0 5px 15px rgba(0,0,0,.15);

}
.trek-card:hover .difficulty-badge{
    transform:translateY(-5px) scale(1.06);
}

.price-badge{
  position:absolute;
  right:18px;
  top:18px;
  background:#F7F4D5;
  color:#0A3323;
  padding:6px 14px;
  border-radius:30px;
  font-weight:700;
  transition:.35s;
}
.trek-card:hover .price-badge{
  transform:scale(1.02);
}

.trek-body{

    padding:24px;

}

.trek-body h4{

    color:var(--primary);

    font-weight:700;

    margin-bottom:15px;

}

.location{

    color:#666;

}

.trek-info{

    display:flex;

    justify-content:space-between;

    margin:18px 0;

    color:#555;

}

.registration{

    background:#F7F4D5;

    padding:12px 15px;

    border-radius:14px;

    margin-bottom:20px;

    font-size:.95rem;

}

.view-btn{
    width:100%;
    display:flex;
    justify-content:center;
    align-items:center;
    gap:10px;
    background:#839958;
    color:white;
    border:none;
    border-radius:16px;
    padding:15px;
    font-weight:700;
    transition:.35s;
}
.trek-card:hover .view-btn{
    background:#0A3323;
    letter-spacing:.6px;
    transform:translateY(-2px);
}
.view-btn i{
    transition:.35s;
}
.trek-card:hover .view-btn i{
    transform:translateX(6px);
}

.booking-note{

    margin:18px 0;

    padding:12px 16px;

    background:#F7F4D5;

    border-left:5px solid #839958;

    border-radius:14px;

    color:#0A3323;

    font-weight:600;
    transition:.35s;

}

.trek-card:hover .booking-note{
    background:#F7F4D5;
    border-left-width:8px;
}

.booking-note i{

    color:#839958;

    margin-right:8px;

}

.booking-note strong{

    float:right;

    color:#0A3323;

}

</style>

<script>
import axios from 'axios'

export default {
  name: 'UserBrowseTreks',
  data() {
    return {
      treks: [],
      search: "",
      selectedDifficulty: "All",
      selectedState: "All",
      difficulties: [],
      states: [],
      sortBy: "newest"
    }
  },

  mounted() {
    this.fetchTreks()
  },

  methods: {
    async fetchTreks() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:5000/api/user/browse-treks",
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("access_token")}`
              }
            }
        );
        this.treks = response.data.data.treks;
        console.log(this.treks);
        this.states = response.data.data.filters.states;
        this.difficulties = response.data.data.filters.difficulties;
      }
      catch (error) {
        console.error(error);
      }
    },

    viewTrek(id) {
      this.$router.push(`/user-view-trek/${id}`);
    }
  },

  computed:{
    filteredTreks() {
    let treks = this.treks.filter(trek => {
        const matchesSearch =
            trek.trek_name.toLowerCase().includes(this.search.toLowerCase()) ||
            trek.location.toLowerCase().includes(this.search.toLowerCase()) ||
            trek.state.toLowerCase().includes(this.search.toLowerCase());

        const matchesDifficulty =
            this.selectedDifficulty === "All" ||
            trek.difficulty === this.selectedDifficulty;

        const matchesState =
            this.selectedState === "All" ||
            trek.state === this.selectedState;

        return matchesSearch && matchesDifficulty && matchesState;
    });

    switch (this.sortBy) {
      case "priceLow":
        treks.sort((a, b) => a.price - b.price);
        break;

      case "priceHigh":
          treks.sort((a, b) => b.price - a.price);
          break;

      case "duration":
          treks.sort((a, b) => a.duration - b.duration);
          break;

      case "difficulty":
        const difficultyOrder = {
          Easy: 1,
          Moderate: 2,
          Hard: 3
        };

        treks.sort(
          (a, b) =>
            difficultyOrder[a.difficulty] -
            difficultyOrder[b.difficulty]
        );
        break;

        case "newest":
          default:
            // Keep API order
            break;
    }
    return treks;
  }
}

}
</script>
