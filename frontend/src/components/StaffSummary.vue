<template>
<div class="staff-summary-page">
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
            class="menu-item"
        >
            <i class="bi bi-person-circle"></i>
            <span>Participants</span>
        </router-link>

        <router-link
            to="/staff-summary"
            class="menu-item active"
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

<!-- Header -->
         <header class="page-header">

    <div class="header-left">

        <h1 class="page-title">
            Treks Management
        </h1>

        <p class="page-subtitle">
            Manage your assigned trekking expeditions and participants.
        </p>

    </div>

</header>

<br><br><br>

<div>
<p class="trek-quote">
    "Every expedition becomes memorable when every guide leads with confidence."
</p>
</div>

<br><br><br><br><br><br>
    <div class="row g-4 mt-4">

    <div class="col-md-3">

        <div class="summary-card green">

            <i class="bi bi-map-fill"></i>

            <h2>{{ summary.assigned_treks }}</h2>

            <p>Assigned Treks</p>

        </div>

    </div>

    <div class="col-md-3">

        <div class="summary-card blue">

            <i class="bi bi-people-fill"></i>

            <h2>{{ summary.total_participants }}</h2>

            <p>Total Participants</p>

        </div>

    </div>

    <div class="col-md-3">

        <div class="summary-card yellow">

            <i class="bi bi-calendar-event-fill"></i>

            <h2>{{ summary.upcoming_treks }}</h2>

            <p>Upcoming Treks</p>

        </div>

    </div>

    <div class="col-md-3">

        <div class="summary-card red">

            <i class="bi bi-check-circle-fill"></i>

            <h2>{{ summary.completed_treks }}</h2>

            <p>Completed Treks</p>

        </div>

    </div>

</div>

<br><br><br>

<div class="row mt-5">

    <div class="col-lg-6">

        <div class="glass-card">

            <h3>Trek Status</h3>

            <canvas id="statusChart"></canvas>

        </div>

    </div>

    <div class="col-lg-6">

        <div class="glass-card">

            <h3>Difficulty Distribution</h3>

            <canvas id="difficultyChart"></canvas>

        </div>

    </div>

</div>


<br><br><br>

<div class="glass-card mt-5">

<h3>

<i class="bi bi-person-check-fill me-2"></i>

Recent Participants

</h3>

<table class="table">

<thead>

<tr>

<th>Name</th>

<th>Trek</th>

<th>Booking Date</th>

</tr>

</thead>

<tbody>

<tr

v-for="user in recentParticipants"

:key="user.id"

>

<td>{{ user.name }}</td>

<td>{{ user.trek }}</td>

<td>{{ user.booking_date }}</td>

</tr>

</tbody>

</table>

</div>

<br><br><br>

</div>
</template>














<script>
import axios from "axios"
import Chart from "chart.js/auto"

export default {

    name: "StaffSummary",

    data() {
        return {

            summary: {},

            statusChart: {},

            difficultyChart: {},

            assignedTreks: [],

            recentParticipants: []

        }
    },

    async mounted() {

        await this.fetchSummary()

        this.$nextTick(() => {

            this.createStatusChart()
            this.createDifficultyChart()

        })

    },

    methods: {

        async fetchSummary() {

            const token = localStorage.getItem("access_token")

            const response = await axios.get(
                "http://127.0.0.1:5000/api/staff/summary",
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            )

            this.summary = response.data.data.summary

            this.statusChart = response.data.data.status_chart

            this.difficultyChart = response.data.data.difficulty_chart

            this.assignedTreks = response.data.data.assigned_trek_table

            this.recentParticipants = response.data.data.recent_participants

        },

        createStatusChart() {

            new Chart(
                document.getElementById("statusChart"),
                {
                    type: "pie",
                    data: {
                        labels: Object.keys(this.statusChart),
                        datasets: [
                            {
                                data: Object.values(this.statusChart)
                            }
                        ]
                    }
                }
            )

        },

        createDifficultyChart() {

            new Chart(
                document.getElementById("difficultyChart"),
                {
                    type: "doughnut",
                    data: {
                        labels: Object.keys(this.difficultyChart),
                        datasets: [
                            {
                                data: Object.values(this.difficultyChart)
                            }
                        ]
                    }
                }
            )

        }

    }

}
</script>

<style scoped>
.staff-summary-page{

    min-height:100vh;

    position:relative;

    padding-left:290px;

    padding-right:35px;

    padding-top:35px;

    padding-bottom:40px;

}

.page-background{

    position:fixed;

    inset:0;

    background:
        linear-gradient(
            rgba(255,255,255,.72),
            rgba(255,255,255,.78)
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

.summary-card{

padding:25px;

border-radius:24px;

backdrop-filter:blur(18px);

background:rgba(255,255,255,.18);

border:1px solid rgba(255,255,255,.25);

text-align:center;

height:180px;

display:flex;

flex-direction:column;

justify-content:center;

}

.summary-card i{

font-size:2rem;

margin-bottom:10px;

color:#73002d;

}

.summary-card h2{

font-size:2.2rem;

font-weight:700;

color:#73002d;

margin:0;

}

.summary-card p{

margin-top:8px;

font-size:1rem;

}

.green{

background:linear-gradient(135deg,#dff8e5,#edfdf3);

}

.blue{

background:linear-gradient(135deg,#e6f2ff,#f5fbff);

}

.yellow{

background:linear-gradient(135deg,#fff6d8,#fffdf2);

}

.red{

background:linear-gradient(135deg,#ffe6e6,#fff5f5);

}

.glass-card{

margin-top:25px;

padding:25px;

border-radius:25px;

background:rgba(255,255,255,.18);

backdrop-filter:blur(16px);

border:1px solid rgba(255,255,255,.25);

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

</style>