<template>

<div class="admin-view-booking-page">
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

<div class="admin-view-booking">

    <!-- Header -->
         <header class="page-header">

    <div class="header-left">

        <h1 class="page-title">
            Booking Details
        </h1>

        <p class="page-subtitle">
             View complete booking information.
        </p>

    </div>

    <div class="header-right">
        <button
            class="back-btn"
            @click="$router.push('/admin-bookings')"
        >
            <i class="bi bi-arrow-left"></i>

            Go Back 
        </button>

    </div>

</header>

    <!-- Booking Card -->

    <div class="glass-card">

        <h3 class="section-title">

            <i class="bi bi-receipt"></i>

            Booking Information

        </h3>

        <div class="info-grid">

            <div>

                <label>Booking Reference</label>

                <span>{{ booking.booking_reference }}</span>

            </div>

            <div>

                <label>Status</label>

                <span>{{ booking.booking_status }}</span>

            </div>

            <div>

                <label>Payment</label>

                <span>{{ booking.payment_status }}</span>

            </div>

            <div>

                <label>Total Amount</label>

                <span>₹{{ booking.total_amount }}</span>

            </div>

            <div>

                <label>Participants</label>

                <span>{{ booking.number_of_people }}</span>

            </div>

            <div>

                <label>Booking Date</label>

                <span>{{ booking.booking_date }}</span>

            </div>

        </div>

    </div>

    <!-- User -->

    <div class="glass-card">

        <h3 class="section-title">

            <i class="bi bi-person-circle"></i>

            User Information

        </h3>

        <div class="info-grid">

            <div>

                <label>Name</label>

                <span>{{ user.full_name }}</span>

            </div>

            <div>

                <label>Email</label>

                <span>{{ user.email }}</span>

            </div>

            <div>

                <label>Mobile</label>

                <span>{{ user.mobile_number }}</span>

            </div>

            <div>

                <label>City</label>

                <span>{{ user.city }}</span>

            </div>

            <div>

                <label>State</label>

                <span>{{ user.state }}</span>

            </div>

            <div>

                <label>Emergency Contact</label>

                <span>{{ user.emergency_contact_name }}</span>

            </div>

        </div>

    </div>

    <!-- Trek -->

    <div class="glass-card">

        <h3 class="section-title">

            <i class="bi bi-signpost-split"></i>

            Trek Information

        </h3>

        <div class="info-grid">

            <div>

                <label>Trek</label>

                <span>{{ trek.trek_name }}</span>

            </div>

            <div>

                <label>Location</label>

                <span>{{ trek.location }}</span>

            </div>

            <div>

                <label>Difficulty</label>

                <span>{{ trek.difficulty }}</span>

            </div>

            <div>

                <label>Dates</label>

                <span>{{ trek.start_date }} - {{ trek.end_date }}</span>

            </div>

            <div>

                <label>Assigned Staff</label>

                <span>{{ trek.staff_name }}</span>

            </div>

        </div>

    </div>

    <!-- Participants -->

    <div class="glass-card">

        <h3 class="section-title">

            <i class="bi bi-people-fill"></i>

            Participants

        </h3>

        <div
            class="participant-card"
            v-for="(participant,index) in participants"
            :key="index"
        >

            <h5>

                Participant {{ index+1 }}

            </h5>

            <div class="info-grid">

                <div>

                    <label>Name</label>

                    <span>{{ participant.full_name }}</span>

                </div>

                <div>

                    <label>Age</label>

                    <span>{{ participant.age }}</span>

                </div>

                <div>

                    <label>Gender</label>

                    <span>{{ participant.gender }}</span>

                </div>

                <div>

                    <label>Mobile</label>

                    <span>{{ participant.mobile_number }}</span>

                </div>

                <div>

                    <label>Emergency Contact</label>

                    <span>{{ participant.emergency_contact }}</span>

                </div>

            </div>

        </div>

    </div>

    <!--ACTION BUTTON-->
    <div class="glass-card">
        <div class="action_button">
            <div v-if="booking.booking_status === 'Pending'">
    <button
        class="accepted"
        @click="updateBookingStatus(booking.id, 'Accepted')"
    >
        Accept
    </button>

    <button
        class="rejected"
        @click="updateBookingStatus(booking.id, 'Rejected')"
    >
        Reject
    </button>
</div>
        </div>

    </div>

</div>
    

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

.admin-view-booking{

    margin-left:260px;

    width:calc(100% - 260px);

    min-height:100vh;

    padding:50px;

    background:
        linear-gradient(rgba(168, 169, 168, 0.2),rgba(183, 184, 183, 0.2)),
        url("@/assets/images/admin-bg.jpg");

    background-size:cover;
    background-position:center;
    background-attachment:fixed;

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

/*==================================================
ADMIN VIEW BOOKING
==================================================*/

.admin-view-booking{

    min-height:100vh;


}



/*==================================================
GLASS CARD
==================================================*/

.glass-card{

    background:rgba(255,255,255,.18);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,.25);

    border-radius:24px;

    padding:35px;

    margin-bottom:150px;

    box-shadow:0 20px 45px rgba(0,0,0,.15);

}

.glass-card h3 i{

    color:#670626;

    font-size:1.4rem;

}

.section-title{
    font-family:"Your Premium Heading Font", serif;
    color:#670626;
    font-size:2rem;

    margin:0;
    margin-bottom: 30px;
    letter-spacing:1px;
    font-weight: 600;

}

/*==================================================
GRID
==================================================*/

.info-grid{

    display:grid;

    grid-template-columns:repeat(2,1fr);

    gap:28px;

}

.info-grid div{

    display:flex;

    flex-direction:column;

}

/*==================================================
LABELS
==================================================*/

.info-grid label{

    color:#708b3b;

    margin-bottom:8px;

    font-weight:600;

    font-size:.95rem;

    letter-spacing:.6px;

}

/*==================================================
VALUES
==================================================*/

.info-grid span{

    background:rgba(255,255,255,.82);

    padding:14px 18px;

    border-radius:14px;

    font-weight:600;

    color:black;

    min-height:55px;

    display:flex;

    align-items:center;

}

/*==================================================
PARTICIPANTS
==================================================*/

.participant-card{

    background:rgba(255,255,255,.12);

    border:1px solid rgba(255,255,255,.2);

    border-radius:18px;

    padding:25px;

    margin-top:25px;

}

.participant-card h5{

    color:#670626;

    font-weight:700;

    margin-bottom:22px;

}

/*==================================================
STATUS BADGES
==================================================*/

.status{

    display:inline-flex;

    align-items:center;

    justify-content:center;

    padding:8px 18px;

    border-radius:999px;

    color:white;

    font-weight:700;

    font-size:.9rem;

}


.pending{
    padding: 15px;
    background:#f4b942;
}

/* ACTION BUTTONS */
.accepted{
    padding: 15px;
    background:#3CB371;
    border-radius: 25px;
    color: white;
    width: 140px;
    margin-left: 350px;
}
.accepted:hover{
    transform:translateY(-3px);
    background: #2c6f2f;
}


.rejected{
    padding: 15px;
    background:#D9534F;
    border-radius: 25px;
    width: 140px;
    color: white;
    margin-left: 100px;
}
.rejected:hover{
    transform:translateY(-3px);
    background: #d21009;
}

/*==================================================
ACTION BUTTONS
==================================================*/

.action-buttons{

    display:flex;

    justify-content:flex-end;

    gap:18px;

    margin-top:40px;

}

.approve-btn,
.reject-btn,
.complete-btn,
.cancel-btn{

    border:none;

    padding:14px 28px;

    border-radius:14px;

    color:white;

    font-weight:700;

    transition:.3s;

}

.approve-btn{

    background:#4CAF50;

}

.complete-btn{

    background:#0A3323;

}

.reject-btn{

    background:#C0392B;

}

.cancel-btn{

    background:#6c757d;

}

.approve-btn:hover,
.complete-btn:hover,
.reject-btn:hover,
.cancel-btn:hover{

    transform:translateY(-3px);

    box-shadow:0 10px 25px rgba(0,0,0,.2);

}

/*==================================================
RESPONSIVE
==================================================*/

@media(max-width:992px){

    .admin-view-booking{

        padding:110px 25px 60px;

    }

    .info-grid{

        grid-template-columns:1fr;

    }

    .page-header h1{

        font-size:2.3rem;

    }


}
</style>


<script>

import axios from "axios";

export default{

data(){

return{

booking:{},

user:{},

trek:{},

participants:[]

}

},

async mounted(){

this.fetchBooking();

},

methods:{
    async fetchBooking(){

    try{

        console.log("Route ID :", this.$route.params.id);

        console.log(localStorage.getItem("access_token"));

        const response = await axios.get(
            `http://127.0.0.1:5000/api/admin/booking/${this.$route.params.id}`,
            {
                headers:{
                    Authorization:`Bearer ${localStorage.getItem("access_token")}`
                }
            }
        );

        console.log("API Response :", response.data);

        this.booking=response.data.data.booking;
        this.user=response.data.data.user;
        this.trek=response.data.data.trek;
        this.participants=response.data.data.participants;

        console.log(this.participants);

    }

    catch(error){

        console.log(error.response);

    }

},

async updateBookingStatus(bookingId, status) {
    try {
        const response = await axios.put(
            `http://127.0.0.1:5000/api/admin/bookings/${bookingId}/status`,
            {
                status: status
            }
        )

        alert(response.data.message)

        // Update UI without refreshing
        this.booking.status = status;

    } catch (error) {
        console.error(error)

        alert(
            error.response?.data?.message ||
            "Failed to update booking status."
        )
    }
}

}



}

</script>