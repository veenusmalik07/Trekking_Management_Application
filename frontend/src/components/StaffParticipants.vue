<template>

<div class="staff-participant-page">

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
            class="menu-item"
        >
            <i class="bi bi-signpost-2-fill"></i>
            <span>Treks</span>
        </router-link>

        <router-link
            to="/staff-participants"
            class="menu-item active"
        >
            <i class="bi bi-people-fill"></i>
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
            Participants Management
        </h1>

        <p class="page-subtitle">
            View and manage participants registered for your assigned treks.
        </p>

    </div>

</header>

<br>

<div>
<p class="trek-quote">
    Every journey is built on preparation, teamwork, and the courage to take the first step. 
    As a trek leader, you guide every explorer from planning to the summit, ensuring each trail is safe, 
    organized, and unforgettable. Lead with confidence, inspire every adventure, 
    and turn every expedition into a story worth remembering.
    Behind every successful expedition is a leader who plans with purpose and guides with passion. 
    Organize your treks, support every participant, 
    and transform every journey into an unforgettable adventure where every step brings new memories and every summit tells a story.
</p>
</div>

<br><br><br><br><br><br>

        <!-- CARDS -->

<section class="cards-section">
    <div class="container-fluid">

    <div
        class="participant-card mb-5"
        v-for="trek in trekCards"
        :key="trek.id"
    >

        <div class="trek-header">

            <div class="trek-image-wrap">
                <img
                    v-if="trek.cover_image && !imageErrors[trek.id]"
                    :src="trek.cover_image"
                    :alt="trek.trek_name"
                    class="trek-image"
                    @error="markImageUnavailable(trek.id)"
                >
                <div v-else class="trek-image-placeholder" aria-label="No trek cover image">
                    <i class="bi bi-image"></i>
                </div>
            </div>

            <div class="trek-details">
                <span class="trek-label">Assigned trek</span>
                <h2>{{ trek.trek_name }}</h2>
                <p><i class="bi bi-geo-alt-fill"></i>{{ trek.location }}</p>
                <small><i class="bi bi-calendar3"></i>{{ trek.start_date }} – {{ trek.end_date }}</small>
            </div>

            <div class="participant-count">
                <i class="bi bi-people-fill"></i>
                <strong>{{ trek.participant_count }}</strong>
                <span>{{ trek.participant_count === 1 ? 'Participant' : 'Participants' }}</span>
            </div>

        </div>

        <div class="table-responsive">
        <table class="table participant-table mb-0">

            <thead>

                <tr>

                    <th>Name</th>

                    <th>Phone</th>

                    <th>Gender</th>

                    <th>Age</th>

                    <th>People</th>

                    <th>Booked On</th>

                </tr>

            </thead>

            <tbody>

                <tr

                    v-for="participant in trek.participants"

                    :key="participant.id"

                >

                    <td>{{ participant.full_name }}</td>

                    <td>{{ participant.phone }}</td>

                    <td>{{ participant.gender }}</td>

                    <td>{{ participant.age }}</td>

                    <td>{{ participant.people }}</td>

                    <td>{{ participant.booking_date }}</td>

                </tr>

            </tbody>

        </table>
        </div>

    </div>

</div>



</section>

<br><br><br><br>

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

.staff-participant-page {
  min-height: 100vh;
  display: flex;
  position: relative;
  /* remove overflow: hidden */
}


.page-background{

    position:fixed;

    inset:0;

    background:
        linear-gradient(
            rgba(255,255,255,.70),
            rgba(255,255,255,.70)
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
cardISTICS
==================================================*/

.cards-section{
    display:block;
    margin-bottom:40px;
}

.cards-section {
  margin-bottom: 40px;
}

.card{
    min-width: 500px;
    margin-left: 30px;
    position:relative;

    overflow:hidden;

    padding:28px 28px 28px 28px;

    border-radius:28px;

    background:rgba(255,255,255,.16);

    backdrop-filter:blur(18px);

    -webkit-backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,.28);

    box-shadow: #BAD797;

    transition:.35s ease;
    display:flex;

    flex-direction:column;

    justify-content:center;

    align-items:center;

    text-align:center;

}


.card::before{

    content:"";

    position:absolute;

    top:0;

    left:0;

    width:100%;

    height:6px;

    background:rgba(255,241,181,.35);
    box-shadow: #BAD797;

}

.card:hover{

    transform:translateY(-6px);

    box-shadow:0 18px 45px rgba(0,0,0,.15);

}

.card-icon{

    font-size:2rem;

    color:#43302E;

    margin-bottom:18px;

}

.card-number{
    font-size:3rem;
    font-weight:700;
    color:#43302E;
    margin-bottom:8px;
    line-height: 1;
}

.card-title{
    font-size:2.5rem;
    font-weight:600;
    color:#43302E;
    margin-bottom:15px;
    font-family:"Your Premium Heading Font", serif;
    letter-spacing: 1.1px;
}

.card-subtitle{
    font-size:.92rem;
    color:#666;
    margin-bottom: 15px;
}

.view-btn
{
    width:160px;
    height:48px;
    border:none;
    border-radius:14px;
    display:flex;
    align-items:center;
    justify-content:center;
    color:#43302E;
    font-size:1.15rem;
    transition:.3s;
    font-weight: 400px;
    background: #FFF1B5;
    margin-top: 15px;
}

.view-btn:hover{
    background:white;
    color:#43302E;
}

.participant-card{
    overflow:hidden;
    margin-bottom:32px;
    border:1px solid rgba(255,255,255,.72);
    border-radius:28px;
    background:rgba(255,255,255,.54);
    box-shadow:0 16px 40px rgba(67,48,46,.12);
    backdrop-filter:blur(16px);
}

.trek-header{
    display:flex;
    align-items:center;
    gap:24px;
    padding:26px 28px;
    border-bottom:1px solid rgba(67,48,46,.1);
    background:linear-gradient(115deg, rgba(255,241,181,.88), rgba(255,255,255,.42));
}

.trek-image-wrap{ flex:0 0 180px; height:124px; overflow:hidden; border-radius:18px; box-shadow:0 8px 20px rgba(67,48,46,.16); }
.trek-image{ display:block; width:100%; height:100%; object-fit:cover; }
.trek-image-placeholder{ display:grid; width:100%; height:100%; place-items:center; color:#fff; font-size:2.2rem; background:linear-gradient(135deg,#5a3e3a,#8e6a56); }
.trek-details{ min-width:0; }
.trek-label{ display:inline-block; margin-bottom:5px; color:#7a5244; font-size:.72rem; font-weight:700; letter-spacing:1.1px; text-transform:uppercase; }
.trek-details h2{ margin:0 0 7px; color:#342522; font-size:1.8rem; font-weight:700; }
.trek-details p,.trek-details small{ display:block; margin:4px 0; color:#654d46; }
.trek-details i{ margin-right:7px; color:#875745; }

.participant-count{ min-width:122px; margin-left:auto; padding:14px 16px; display:grid; grid-template-columns:auto 1fr; column-gap:9px; align-items:center; border-radius:16px; color:#6d0031; background:rgba(255,255,255,.66); }
.participant-count i{ grid-row:span 2; font-size:1.45rem; }
.participant-count strong{ font-size:1.45rem; line-height:1; }
.participant-count span{ font-size:.78rem; font-weight:600; }

.participant-table{ margin:0; background:rgba(255,255,255,.92); }
.participant-table thead th{ padding:15px 20px; border:0; color:#66473e; background:#fff8df; font-size:.78rem; letter-spacing:.55px; text-transform:uppercase; white-space:nowrap; }
.participant-table tbody td{ padding:17px 20px; color:#3e302c; vertical-align:middle; border-color:#f0e7df; }
.participant-table tbody tr:last-child td{ border-bottom:0; }

@media (max-width:768px){
    .main-content{ margin-left:0; padding:20px; }
    .sidebar{ display:none; }
    .trek-header{ align-items:flex-start; flex-wrap:wrap; padding:20px; }
    .trek-image-wrap{ flex-basis:100%; height:190px; }
    .participant-count{ margin-left:0; }
}
</style>

<script>

import axios from "axios"

export default {

    data() {
        return {
            trekCards: [],
            imageErrors: {}
        }
    },

    mounted() {
        this.fetchParticipants()
    },

    methods: {

        markImageUnavailable(trekId) {
            this.imageErrors[trekId] = true
        },

        async fetchParticipants() {

    const token = localStorage.getItem("access_token")

    console.log("TOKEN =", token)

    const response = await axios.get(
        "http://127.0.0.1:5000/api/staff/participants",
        {
            headers: {
                Authorization: "Bearer " + token
            }
        }
    )

    this.trekCards = response.data.data

}

    }

}


</script>
