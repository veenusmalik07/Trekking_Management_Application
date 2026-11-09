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
    
    <br /><br /> <br><br>
    
    <div class="content-bg">
        
        <!-- SUCCESS PAGE -->
        <div v-if="success"
            class="booking-success"
        >
            <div class="success-icon">
                <i class="bi bi-check-circle-fill"></i>
            </div>

            <h1>Booking Confirmed!</h1>

            <p>
                Congratulations! Your adventure has been successfully booked.
            </p>

            <div class="reference-box">
                Booking Reference
                <strong>{{ bookingReference }}</strong>
            </div>

            <div class="success-buttons">
                <button class="browse-btn"
                    @click="$router.push('/user-browse-treks')"
                >
                    Browse More Treks
                </button>

                <button class="booking-btn"
                    @click="$router.push('/user-my-bookings')"
                >
                    View My Bookings
                </button>
            </div>
        </div>
        <!-- SUCCESS PAGE ENDS -->
         
        <!-- NORMAL BOOKING PAGE -->
        <div v-else>
            <!-- Booking Hero -->
            <section class="booking-hero">
                <div class="hero-card">
                    <img v-if="trek.cover_image"
                        :src="trek.cover_image"
                        class="hero-image"
                    >
                    
                    <div class="hero-overlay">

            <button
                class="back-btn"
                @click="goBack"
            >
                <i class="bi bi-arrow-left"></i>
                Back
            </button>

            <div class="hero-content">

                <h1>{{ trek.trek_name }}</h1>

                <p>
                    <i class="bi bi-geo-alt-fill"></i>
                    {{ trek.location }}, {{ trek.state }}
                </p>

                <div class="hero-badges">

                    <span
                        class="difficulty"
                        :class="trek.difficulty?.toLowerCase()"
                    >
                        {{ trek.difficulty }}
                    </span>

                    <span class="status">
                        {{ trek.status }}
                    </span>

                </div>

            </div>

            <div class="price-badge">

                <small>Starting From</small>

                <h2>₹ {{ trek.price }}</h2>

            </div>

        </div>

    </div>

</section>

        <!-- Info Strip -->

        <section class="info-strip">

    <div class="info-item">

        <i class="bi bi-calendar-event"></i>

        <div>

            <small>Dates</small>

            <strong>

                {{ trek.start_date }}

                -

                {{ trek.end_date }}

            </strong>

        </div>

    </div>

    <div class="info-item">

        <i class="bi bi-clock-history"></i>

        <div>

            <small>Duration</small>

            <strong>{{ trek.duration }} Days</strong>

        </div>

    </div>

    <div class="info-item">

        <i class="bi bi-people-fill"></i>

        <div>

            <small>Available</small>

            <strong>

                {{ trek.available_slots }}

                /

                {{ trek.capacity }}

            </strong>

        </div>

    </div>

    <div class="info-item">

        <i class="bi bi-heart-pulse-fill"></i>

        <div>

            <small>Fitness</small>

            <strong>{{ trek.fitness_requirement }}</strong>

        </div>

    </div>

    <div class="info-item">

        <i class="bi bi-signpost-fill"></i>

        <div>

            <small>Meeting Point</small>

            <strong>{{ trek.meeting_point }}</strong>

        </div>

    </div>

</section>


        <!-- Participants -->

        <section class="participants-section">

    <div class="section-heading">

        <h2>Who's Joining?</h2>

        <p>

            Select the number of participants for this trek.

        </p>

    </div>

    <div class="participant-card">

        <button @click="decreasePeople">

            <i class="bi bi-dash-lg"></i>

        </button>

        <span>

            {{ booking.number_of_people }}

        </span>

        <button @click="increasePeople">

            <i class="bi bi-plus-lg"></i>

        </button>

    </div>

</section>
    

        <!-- Participant Details -->

        <!-- ==========================================
     PARTICIPANT DETAILS
========================================== -->

<section class="participant-details-section">

    <div class="section-heading">

        <h2>Participant Details</h2>

        <p>
            Enter the information for each participant joining the trek.
        </p>

    </div>

    <div
        v-for="(participant,index) in booking.participant_details"
        :key="index"
        class="participant-form"
    >

        <div class="participant-number">

            <i class="bi bi-person-circle"></i>

            Participant {{ index + 1 }}

        </div>

        <div class="row g-4">

            <div class="col-md-6">

                <label>Full Name</label>

                <input
                    v-model="participant.full_name"
                    type="text"
                    class="form-control"
                    placeholder="Enter Full Name"
                >

            </div>

            <div class="col-md-3">

                <label>Age</label>

                <input
                    v-model="participant.age"
                    type="number"
                    class="form-control"
                    placeholder="Age"
                >

            </div>

            <div class="col-md-3">

                <label>Gender</label>

                <select
                    v-model="participant.gender"
                    class="form-select"
                >

                    <option value="">Select</option>

                    <option>Male</option>

                    <option>Female</option>

                    <option>Other</option>

                </select>

            </div>

            <div class="col-md-6">

                <label>Mobile Number</label>

                <input
                    v-model="participant.mobile_number"
                    type="text"
                    class="form-control"
                    placeholder="Enter Mobile Number"
                >

            </div>

            <div class="col-md-6">

                <label>Emergency Contact</label>

                <input
                    v-model="participant.emergency_contact"
                    type="text"
                    class="form-control"
                    placeholder="Emergency Contact Number"
                >

            </div>

        </div>

    </div>

</section>

        <!-- Special Requests -->

        <!-- ==========================================
     SPECIAL REQUESTS
========================================== -->

<section class="special-request-section">

    <div class="section-heading">

        <h2>Special Requests</h2>

        <p>

            Let us know if you have any dietary preferences, medical conditions,
            transportation requirements, or anything else we should know.

        </p>

    </div>

    <div class="request-card">

        <textarea

            v-model="booking.special_requests"

            rows="6"

            class="form-control"

            placeholder="Example:
• Vegetarian Meals
• Asthma or Medical Conditions
• Pickup Required
• Any Other Requests..."

        ></textarea>

        <div class="request-note">

            <i class="bi bi-info-circle-fill"></i>

            This field is optional. Our trek coordinators will review your
            request before the trek begins.

        </div>

    </div>

</section>

        <!-- Booking Summary -->

<section class="booking-summary-section">

    <div class="summary-card">

        <div class="summary-header">

            <i class="bi bi-receipt-cutoff"></i>

            <h2>Booking Summary</h2>

        </div>

        <div class="summary-row">

            <span>Price Per Person</span>

            <strong>₹ {{ trek.price }}</strong>

        </div>

        <div class="summary-row">

            <span>Participants</span>

            <strong>{{ booking.number_of_people }}</strong>

        </div>

        <div class="summary-row">

            <span>Duration</span>

            <strong>{{ trek.duration }} Days</strong>

        </div>

        <div class="summary-row">

            <span>Difficulty</span>

            <strong>{{ trek.difficulty }}</strong>

        </div>

        <div class="summary-row">

            <span>Start Date</span>

            <strong>{{ trek.start_date }}</strong>

        </div>

        <div class="summary-row">

            <span>End Date</span>

            <strong>{{ trek.end_date }}</strong>

        </div>

        <hr>

        <div class="summary-total">

            <span>Total Amount</span>

            <h2>₹ {{ totalAmount }}</h2>

        </div>

         <!-- HANDLING ERRORS -->
<div
    v-if="errorMessage"
    class="booking-error"
>

    <div class="error-icon">

        <i class="bi bi-exclamation-circle-fill"></i>

    </div>

    <div>

        <h5>Booking Failed</h5>

        <p>{{ errorMessage }}</p>

    </div>

</div>


        <button
            class="confirm-booking-btn"
            @click="confirmBooking"
        >

            <i class="bi bi-check-circle-fill me-2"></i>

            Confirm Booking

        </button>

    </div>

</section>

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

/* ==========================================
   HERO SECTION
========================================== */

.booking-hero{
    margin-bottom:40px;
}

.hero-card{
    position:relative;
    border-radius:32px;
    overflow:hidden;
    min-height:520px;
    box-shadow:0 25px 60px rgba(0,0,0,.18);
    max-width: 1400px;
    margin-left: 50px;
}

.hero-image{
    width:100%;
    height:520px;
    object-fit:cover;
    display:block;
}

.hero-overlay{
    position:absolute;
    inset:0;
    background:linear-gradient(
        90deg,
        rgba(8,45,31,.82),
        rgba(8,45,31,.55),
        rgba(8,45,31,.25)
    );
    padding:45px;
    display:flex;
    justify-content:space-between;
    align-items:flex-end;
}

/* ==========================================
   BACK BUTTON
========================================== */

.back-btn{
    position:absolute;
    top:35px;
    left:35px;

    border:none;
    background:rgba(255,255,255,.18);
    backdrop-filter:blur(15px);

    color:#fff;
    padding:12px 24px;
    border-radius:50px;
    font-weight:600;

    transition:.3s;
}

.back-btn:hover{
    background:white;
    color:#0b3f2d;
}

/* ==========================================
   HERO CONTENT
========================================== */

.hero-content{
    max-width:700px;
    color:white;
}

.hero-content h1{
    font-size:3.2rem;
    font-weight:800;
    margin-bottom:15px;
}

.hero-content p{
    font-size:1.2rem;
    margin-bottom:28px;
    opacity:.92;
}

.hero-content i{
    margin-right:8px;
}

/* ==========================================
   BADGES
========================================== */

.hero-badges{
    display:flex;
    gap:15px;
    flex-wrap:wrap;
}

.hero-badges span{
    padding:10px 22px;
    border-radius:40px;
    font-weight:700;
    font-size:.95rem;
}

.difficulty.easy{
    background:#58b368;
    color:white;
}

.difficulty.moderate{
    background:#f2c94c;
    color:#173d2e;
}

.difficulty.hard{
    background:#d84a4a;
    color:white;
}

.status{
    background:rgba(255,255,255,.18);
    backdrop-filter:blur(15px);
    color:white;
}

/* ==========================================
   PRICE CARD
========================================== */

.price-badge{
    width:270px;
    background:rgba(255,255,255,.15);
    backdrop-filter:blur(18px);

    border-radius:28px;

    padding:35px;

    text-align:center;

    color:white;
}

.price-badge small{
    display:block;
    font-size:1rem;
    letter-spacing:1px;
    margin-bottom:18px;
    opacity:.9;
}

.price-badge h2{
    font-size:3rem;
    font-weight:800;
}

/* ==========================================
   INFO STRIP
========================================== */

.info-strip{

    background:rgba(255,255,255,.45);

    backdrop-filter:blur(18px);

    border-radius:26px;

    padding:30px;

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

    gap:25px;

    margin-bottom:50px;

    box-shadow:0 10px 30px rgba(0,0,0,.08);

}

.info-item{

    display:flex;

    align-items:center;

    gap:18px;

}

.info-item i{

    width:60px;
    height:60px;

    border-radius:18px;

    background:#88a35b;

    color:white;

    display:flex;
    justify-content:center;
    align-items:center;

    font-size:1.5rem;

}

.info-item small{

    display:block;

    color:#777;

    margin-bottom:5px;

}

.info-item strong{

    color:#123b2d;

    font-size:1.05rem;

}

/* ==========================================
   PARTICIPANTS SECTION
========================================== */

.participants-section{

    background:rgba(255,255,255,.42);

    backdrop-filter:blur(18px);

    border-radius:30px;

    padding:45px;

    margin-bottom:45px;

    box-shadow:0 15px 35px rgba(0,0,0,.08);

}

.section-heading{

    margin-bottom:30px;

}

.section-heading h2{

    font-size:2rem;

    color:#0b3f2d;

    font-weight:800;

}

.section-heading p{

    color:#666;

    font-size:1.05rem;

}

/* ==========================================
   COUNTER CARD
========================================== */

.participant-card{

    display:flex;

    justify-content:center;

    align-items:center;

    gap:40px;

}

.participant-card button{

    width:60px;

    height:60px;

    border:none;

    border-radius:50%;

    background:#88a35b;

    color:white;

    font-size:1.4rem;

    transition:.3s;

}

.participant-card button:hover{

    background:#0b3f2d;

    transform:scale(1.08);

}

.participant-card span{

    font-size:2.5rem;

    font-weight:800;

    color:#0b3f2d;

    min-width:70px;

    text-align:center;

}

/* ==========================================
   PARTICIPANT DETAILS
========================================== */

.participant-details-section{

    margin-bottom:50px;

}

.participant-form{

    background:rgba(255,255,255,.45);

    backdrop-filter:blur(18px);

    border-radius:28px;

    padding:35px;

    margin-bottom:30px;

    box-shadow:0 12px 30px rgba(0,0,0,.08);

}

.participant-number{

    display:inline-flex;

    align-items:center;

    gap:10px;

    background:#88a35b;

    color:white;

    padding:10px 22px;

    border-radius:30px;

    font-weight:700;

    margin-bottom:28px;

}

.participant-number i{

    font-size:1.2rem;

}

.participant-form label{

    font-weight:700;

    color:#123b2d;

    margin-bottom:8px;

}

.participant-form .form-control,
.participant-form .form-select{

    height:56px;

    border:none;

    border-radius:16px;

    background:white;

    box-shadow:0 4px 12px rgba(0,0,0,.05);

}

.participant-form .form-control:focus,
.participant-form .form-select:focus{

    border:2px solid #88a35b;

    box-shadow:none;

}

/* ==========================================
   SPECIAL REQUESTS
========================================== */
.special-request-section{
    margin-bottom:50px;
}

.request-card{
    background:rgba(255,255,255,.45);
    backdrop-filter:blur(18px);
    border-radius:28px;
    padding:35px;
    box-shadow:0 12px 30px rgba(0,0,0,.08);
}

.request-card textarea{
    min-height:180px;
    border:none;
    border-radius:18px;
    padding:18px;
    resize:none;
    font-size:16px;
    line-height:1.8;
    box-shadow:0 4px 12px rgba(0,0,0,.05);
}

.request-card textarea:focus{
    border:2px solid #88a35b;
    box-shadow:none;
}

.request-note{
    margin-top:18px;
    display:flex;
    align-items:flex-start;
    gap:10px;
    color:#555;
    font-size:.95rem;
}

.request-note i{
    color:#88a35b;
    font-size:1.1rem;
    margin-top:2px;
}

/*==========================================
BOOKING SUMMARY
==========================================*/

.booking-summary-section{

    margin-bottom:80px;

}

.summary-card{

    background:rgba(255,255,255,.48);

    backdrop-filter:blur(20px);

    border-radius:30px;

    padding:40px;

    box-shadow:0 20px 45px rgba(0,0,0,.08);
    max-width: 800px;
    margin-left:20px;

}

.summary-header{

    display:flex;

    align-items:center;

    gap:15px;

    margin-bottom:35px;

}

.summary-header i{

    width:55px;

    height:55px;

    border-radius:18px;

    background:#88a35b;

    color:white;

    display:flex;

    justify-content:center;

    align-items:center;

    font-size:1.4rem;

}

.summary-header h2{

    font-weight:800;

    color:#0A3323;

    margin:0;

}

.summary-row{

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:14px 0;

    font-size:17px;

}

.summary-row span{

    color:#666;

}

.summary-row strong{

    color:#0A3323;

}

.summary-total{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-top:25px;

}

.summary-total span{

    font-size:20px;

    font-weight:700;

    color:#0A3323;

}

.summary-total h2{

    font-size:2.6rem;

    color:#0A3323;

    font-weight:800;

}

.confirm-booking-btn{

    width:100%;

    margin-top:35px;

    border:none;

    border-radius:18px;

    padding:18px;

    background:#88a35b;

    color:white;

    font-weight:700;

    font-size:18px;

    transition:.35s;

}

.confirm-booking-btn:hover{

    background:#0A3323;

    transform:translateY(-3px);

}

/*==========================================
SUCCESS
==========================================*/

.booking-success{

    min-height:75vh;

    display:flex;

    flex-direction:column;

    justify-content:center;

    align-items:center;

    text-align:center;

}

.success-icon{

    width:120px;

    height:120px;

    border-radius:50%;

    background:#88a35b;

    display:flex;

    justify-content:center;

    align-items:center;

    color:white;

    font-size:4rem;

    margin-bottom:30px;

    animation:pop .5s ease;

}

.booking-success h1{

    font-size:3rem;

    font-weight:800;

    color:#0A3323;

}

.booking-success p{

    font-size:1.2rem;

    color:#666;

    max-width:650px;

    margin:20px auto 35px;

}

.reference-box{

    background:white;

    padding:25px 45px;

    border-radius:22px;

    box-shadow:0 15px 35px rgba(0,0,0,.08);

    font-size:18px;

}

.reference-box strong{

    display:block;

    margin-top:12px;

    font-size:2rem;

    color:#88a35b;

}

.success-buttons{

    display:flex;

    gap:20px;

    margin-top:40px;

}

.success-buttons button{

    padding:16px 34px;

    border:none;

    border-radius:18px;

    font-weight:700;

    transition:.3s;

}

.booking-btn{

    background:#88a35b;

    color:white;

}

.booking-btn:hover{

    background:#0A3323;

}

.browse-btn{

    background:white;

    color:#0A3323;

    box-shadow:0 8px 20px rgba(0,0,0,.08);

}

.browse-btn:hover{

    transform:translateY(-3px);

}

@keyframes pop{

    0%{

        transform:scale(.3);

        opacity:0;

    }

    100%{

        transform:scale(1);

        opacity:1;

    }

}

.booking-error{

    display:flex;

    align-items:center;

    gap:18px;

    background:#ffe8e8;

    border-left:6px solid #d63031;

    padding:20px;

    border-radius:18px;

    margin-bottom:30px;

    animation:fadeDown .35s ease;
    max-width: 800px;

}

.error-icon{

    width:60px;

    height:60px;

    border-radius:50%;

    background:#d63031;

    color:white;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:28px;

}

.booking-error h5{

    margin:0;

    color:#7a1010;

    font-weight:700;

}

.booking-error p{

    margin:5px 0 0;

    color:#5b5b5b;

}

@keyframes fadeDown{

    from{

        opacity:0;

        transform:translateY(-15px);

    }

    to{

        opacity:1;

        transform:translateY(0);

    }

}
</style>



<script>
import axios from "axios";

export default {

    name: "UserBookTrek",

    data() {
        return {
            trek: {},
            booking: {
                number_of_people: 0,
                participant_details: [],
                special_requests: ""
            },
            success: false,
            bookingReference: "",
            errorMessage: ""
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
                if (this.trek.available_slots === 0) {

    this.errorMessage = "This trek is fully booked. No slots are available.";

}
                this.errorMessage = "";

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
            this.$router.push(`/user-view-trek/${this.trek.id}`);
        },

        increasePeople() {
            if (this.booking.number_of_people < this.trek.available_slots) {
                this.booking.number_of_people++;
            }
        },

        decreasePeople() {
            if (this.booking.number_of_people >= 1) {
                this.booking.number_of_people--;
            }
        },

        async confirmBooking() {
            // Clear Error
            this.errorMessage = "";

            if (this.trek.available_slots === 0) {
                this.errorMessage = "This trek is fully booked.";
                return;
            }

            // Participants
            if (this.booking.number_of_people < 1) {
                this.errorMessage = "Please select at least one participant.";
                return;
            }

            // Participant Validation
            for (let index = 0; index < this.booking.participant_details.length; index++) {
                const participant = this.booking.participant_details[index];
                if (
                    !participant.full_name ||
                    !participant.age ||
                    !participant.gender ||
                    !participant.mobile_number
                ) {
                    this.errorMessage = `Participant ${index + 1}: Please complete all details.`;
                    return;
                }
                
                if (!/^[0-9]{10}$/.test(participant.mobile_number)) {
                    this.errorMessage = `Participant ${index + 1}: Invalid mobile number.`;
                    return;
                }

                if (
                    participant.age < this.trek.minimum_age ||
                    participant.age > this.trek.maximum_age
                ) {
                    this.errorMessage = `Participant ${index + 1}: Age must be between ${this.trek.minimum_age} and ${this.trek.maximum_age}.`;
                    return;
                }
            }

            try {
                const response = await axios.post(
                "http://127.0.0.1:5000/api/user/book-trek",
                    {
                        trek_id: this.trek.id,
                        number_of_people: this.booking.number_of_people,
                        participant_details: this.booking.participant_details,
                        special_requests: this.booking.special_requests,
                        total_amount: this.totalAmount
                    },
                    
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem("access_token")}`
                        }
                    }
                );
                this.bookingReference = response.data.booking_reference;
                this.success = true;
            }
            catch(error){
                this.errorMessage = error.response?.data?.message || "Booking Failed";
            }
        }
    },

    // WHEN NUMBER OF PARTICIPANTS CHANGES
    watch: {
        "booking.number_of_people"(value) {
            while (this.booking.participant_details.length < value) {
                this.booking.participant_details.push({
                    full_name: "",
                    age: "",
                    gender: "",
                    mobile_number: "",
                    emergency_contact: ""
                });
            }
            while (this.booking.participant_details.length > value) {
                this.booking.participant_details.pop();
            }
        }
    },

    computed: {
        totalAmount(){

        return this.trek.price * this.booking.number_of_people;

    }
    }

};
</script>

