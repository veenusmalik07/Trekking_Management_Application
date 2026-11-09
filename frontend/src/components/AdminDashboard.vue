<template>
  <div class="admin-dashboard-page">
    <!-- FIXED BACKGROUND -->
    <div class="page-background"></div>

    <!-- SIDEBAR-->
    <aside class="sidebar">
      <!-- Logo -->
      <div class="sidebar-logo">
        <i class="bi bi-tree-fill logo-icon"></i>
        <h2 class="logo-text">TREKMATE</h2>
      </div>

      <!-- Navigation -->

      <nav class="sidebar-menu">
        <router-link to="/admin-dashboard" class="menu-item">
          <i class="bi bi-grid-1x2-fill"></i>
          <span>Dashboard</span>
        </router-link>

        <router-link to="/admin-treks" class="menu-item">
          <i class="bi bi-signpost-2-fill"></i>
          <span>Treks</span>
        </router-link>

        <router-link to="/admin-users" class="menu-item">
          <i class="bi bi-people-fill"></i>
          <span>Users</span>
        </router-link>

        <router-link to="/admin-staff" class="menu-item">
          <i class="bi bi-person-workspace"></i>
          <span>Staff</span>
        </router-link>

        <router-link to="/admin-bookings" class="menu-item">
          <i class="bi bi-journal-check"></i>
          <span>Bookings</span>
        </router-link>

        <router-link to="/admin-summary" class="menu-item">
          <i class="bi bi-bar-chart-fill"></i>
          <span>Summary</span>
        </router-link>
      </nav>

      <!-- Logout -->

      <div class="sidebar-footer">
        <router-link to="/" class="menu-item">
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
          <div class="header">
            <h1 class="page-title">Admin Dashboard</h1>

            <p class="page-subtitle">Monitor every expedition, empower every team, and deliver unforgettable adventures.</p>
          </div>
        </header>

        <br /><br />

      

        <br /><br /><br><br>

        <div class="row g-4 mt-4">

    <!-- Total Revenue -->
    <div class="col-lg-6 col-md-6">

        <div class="summary-card revenue-card">

            <div class="card-icon">
                <i class="bi bi-cash-stack"></i>
            </div>

            <div class="card-content">

                <h6>Total Revenue</h6>

                <h2>₹{{ summary.total_revenue }}</h2>

                <p>Revenue from accepted bookings</p>

            </div>

        </div>

    </div>


    <!-- Monthly Revenue -->
    <div class="col-lg-6 col-md-6">

        <div class="summary-card monthly-card">

            <div class="card-icon">
                <i class="bi bi-calendar2-week"></i>
            </div>

            <div class="card-content">

                <h6>Monthly Revenue</h6>

                <h2>₹{{ summary.monthly_revenue }}</h2>

                <p>Current Month</p>

            </div>

        </div>

    </div>


    <!-- Total Users -->
    <div class="col-lg-6 col-md-6">

        <div class="summary-card users-card">

            <div class="card-icon">
                <i class="bi bi-people-fill"></i>
            </div>

            <div class="card-content">

                <h6>Total Users</h6>

                <h2>{{ summary.total_users }}</h2>

                <p>Registered Trekkers</p>

            </div>

        </div>

    </div>


    <!-- Total Bookings -->
    <div class="col-lg-6 col-md-6">

        <div class="summary-card bookings-card">

            <div class="card-icon">
                <i class="bi bi-journal-check"></i>
            </div>

            <div class="card-content">

                <h6>Total Bookings</h6>

                <h2>{{ summary.total_bookings }}</h2>

                <p>Reservations</p>

            </div>

        </div>

    </div>

</div>

<br><br>

        <section class="charts-section">
          <div class="row">
            <!-- Booking Chart -->

            <div class="col-lg-6">
              <div class="glass-card">
                <div class="section-title">
                  <h3 class="section-title">
                    <i class="bi bi-pie-chart-fill"></i>

                    Booking Status
                  </h3>

                  <p class="section-subtitle">Current booking distribution.</p>
                </div>

                <canvas id="bookingChart"></canvas>
              </div>
            </div>

            <!-- Trek Chart -->

            <div class="col-lg-6">
              <div class="glass-card">
                <div class="section-title">
                  <h3 class="section-title">
                    <i class="bi bi-bar-chart-fill"></i>

                    Trek Status
                  </h3>

                  <p class="section-subtitle">Current trek availability.</p>
                </div>

                <canvas id="trekChart"></canvas>
              </div>
            </div>
          </div>
        </section>

        <br /><br />
        <div class="row gy-4 mt-4">

    <!-- Recent Bookings -->
    <div class="col-12">

        <div class="dashboard-table-card">


            <div class="table-header">

                <h4>
                    <i class="bi bi-journal-check me-2"></i>
                    Recent Bookings
                </h4>

                <router-link
                    to="/admin-bookings"
                    class="view-link"
                >
                    View All →
                </router-link>

            </div>

            <table class="table dashboard-table">

                <thead>

                    <tr>

                        <th>Ref</th>

                        <th>User</th>

                        <th>Status</th>

                    </tr>

                </thead>

                <tbody>

                    <tr
                        v-for="booking in recentBookings"
                        :key="booking.id"
                    >

                        <td>

                            {{ booking.booking_reference }}

                        </td>

                        <td>

                            {{ booking.user_name }}

                        </td>

                        <td>

                            <span
                                class="status-pill"
                                :class="booking.booking_status.toLowerCase()"
                            >

                                {{ booking.booking_status }}

                            </span>

                        </td>

                    </tr>

                </tbody>

            </table>
            </div>
        </div>


    <!-- Upcoming Treks -->
    <div class="col-12">

        <div class="dashboard-table-card">


            <div class="table-header">

                <h4>

                    <i class="bi bi-signpost-split-fill me-2"></i>

                    Upcoming Treks

                </h4>

                <router-link
                    to="/admin-treks"
                    class="view-link"
                >
                    Manage →
                </router-link>

            </div>

            <table class="table dashboard-table">

                <thead>

                    <tr>

                        <th>Trek</th>

                        <th>Date</th>

                        <th>Slots</th>

                    </tr>

                </thead>

                <tbody>

                    <tr
                        v-for="trek in upcomingTreks"
                        :key="trek.id"
                    >

                        <td>

                            {{ trek.trek_name }}

                        </td>

                        <td>

                            {{ trek.start_date }}

                        </td>

                        <td>

                            {{ trek.available_slots }}/{{ trek.capacity }}

                        </td>

                    </tr>

                </tbody>

            </table>

        </div>

    </div>

</div>
<br><br>
<div>
      <p class="trek-quote">"Great expeditions aren't built by chance—they're built through preparation, 
      teamwork, and leadership."</p>
      </div>
  


        

        <!-- Pagination -->
      </div>
    </main>
    <br><br>

    <br><br>
    
      <br><br>
  </div>
</template>

<style scoped>
/*==================================================
GLOBAL
==================================================*/

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.admin-summary-page {
  min-height: 100vh;
  display: flex;
  position: relative;
  overflow: hidden;
}

.page-background {
  position: fixed;

  inset: 0;

  background:
    linear-gradient(rgba(255, 255, 255, 0.72), rgba(255, 255, 255, 0.78)),
    url('@/assets/images/admin-bg.jpg');

  background-size: cover;

  background-position: center;

  background-attachment: fixed;

  z-index: -2;
}

/*==================================================
SIDEBAR
==================================================*/

.sidebar {
  width: 260px;

  height: 100vh;

  background: #670626;

  position: fixed;

  left: 0;

  top: 0;

  display: flex;

  flex-direction: column;

  justify-content: space-between;

  padding: 35px 22px;

  box-shadow: 10px 0 40px rgba(0, 0, 0, 0.18);
}

/* ==========================================
   LOGO
========================================== */
.sidebar-logo {
  display: flex;

  align-items: center;

  gap: 18px;

  margin: 30px 0 55px 0;

  position: relative;

  padding-bottom: 30px;
}

.logo-icon {
  color: white;

  font-size: 1.8rem;

  flex-shrink: 0;
}

.logo-text {
  color: white;

  font-size: 1.8rem;

  letter-spacing: 2.5px;

  margin: 0;

  white-space: nowrap;

  font-weight: 700;
}

/*==================================================
MENU
==================================================*/

.sidebar-menu {
  display: flex;

  flex-direction: column;

  gap: 12px;

  flex: 1;
  background: #670626;
  font-family: 'Your Premium Heading Font', serif;
  letter-spacing: 1.5px;
}

.menu-item {
  display: flex;

  align-items: center;

  gap: 18px;

  padding: 15px 18px;

  border-radius: 18px;

  color: white;

  text-decoration: none;

  transition: 0.35s ease;

  font-size: 1.15rem;

  font-weight: 500;

  position: relative;
}

.menu-item i {
  font-size: 1.25rem;

  width: 28px;

  text-align: center;
}

/*==================================================
HOVER
==================================================*/
.menu-item:hover {
  background: #c5e4a1;

  backdrop-filter: blur(18px);

  border: 1px solid rgba(255, 255, 255, 0.35);
  color: white;
  transform: translateX(4px);
}

.menu-item:hover i {
  color: white;
}

/*==================================================
ACTIVE
==================================================*/

.menu-item.active {
  background: rgba(255, 255, 255, 0.1);
}

.menu-item.active::before {
  content: '';

  position: absolute;

  left: -22px;

  top: 12px;

  width: 5px;

  height: 34px;

  background: #bad797;

  border-radius: 10px;
}

/*==================================================
FOOTER
==================================================*/

.sidebar-footer {
  padding-top: 25px;

  border-top: 1px solid rgba(255, 255, 255, 0.12);
}

/*==================================================
MAIN CONTENT
==================================================*/

.main-content {
  flex: 1;
  margin-left: 240px;
  padding: 35px;
}

/* ==========================================
   HEADER
========================================== */

.page-header {
  display: flex;

  justify-content: space-between;

  align-items: center;

  padding: 26px 36px;

  margin-bottom: 35px;

  border-radius: 26px;

  background: rgba(218, 240, 190, 0.65);

  backdrop-filter: blur(16px);

  border: 1px solid rgba(255, 255, 255, 0.25);

  box-shadow: 0 10px 35px rgba(0, 0, 0, 0.08);
}

.page-title {
  font-family: 'Your Premium Heading Font', serif;

  font-size: 3rem;

  color: #670626;

  margin: 0;

  letter-spacing: 2px;
  font-weight: 500;
}

.page-subtitle {
  font-family: 'Your Premium Heading Font', serif;
  letter-spacing: 1px;
  margin-top: 10px;

  color: #4d4d4d;

  font-size: 1rem;

  opacity: 0.8;
}

.create-btn {
  display: flex;

  align-items: center;

  gap: 10px;

  padding: 14px 28px;

  border: none;

  border-radius: 18px;

  background: #670626;

  color: #fff;

  font-weight: 600;

  transition: 0.3s ease;

  box-shadow: 0 10px 25px rgba(103, 6, 38, 0.18);

  cursor: pointer;
}

.create-btn:hover {
  transform: translateY(-2px);
  background: white;
  color: #7b0a31;
  border-color: #7b0a31;
}

.create-btn i {
  font-size: 1.1rem;
}

.trek-quote {
  font-family: 'BrotherSignature', cursive;

  font-size: 3.2rem;

  color: #670626;

  font-weight: 400;

  line-height: 1.3;

  letter-spacing: 1.4px;

  opacity: 0.92;

  margin-top: 18px;
  text-align: center;

}

.section-header {
  display: flex;

  justify-content: space-between;

  align-items: center;

  margin-bottom: 25px;
}

.section-title {
  font-family: 'Your Premium Heading Font', serif;
  color: #670626;
  font-size: 2.5rem;

  margin: 0;

  letter-spacing: 1px;
  font-weight: 500;
}

.section-subtitle {
  font-family: 'Your Premium Heading Font', serif;

  color: #666;
  letter-spacing: 1px;

  margin-top: 6px;

  margin-bottom: 0;

  font-size: 0.95rem;
}

.charts-section {
  margin: 45px 0;
}

.charts-section .glass-card {
  padding: 25px;

  height: 100%;
}

canvas {
  max-height: 340px;
}

.dashboard-table-card{
    background: rgba(255,255,255,.18);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,.3);
    border-radius: 28px;
    padding: 14px 18px;
    box-shadow: 0 15px 35px rgba(0,0,0,.08);

    max-width: 1100px;   /* adjust to your liking */
    margin-bottom: 50px;
    margin-left: 40px;
}

.dashboard-table tbody tr{
    transition: .25s;
}

.dashboard-table tbody tr:hover{
    background: rgba(173, 208, 122, .08);
}

.table-header{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:18px;

}

.table-header h4{

    color:#6b002b;

    font-size:1.5rem;

    margin:0;

}

.view-link{

    text-decoration:none;

    color:#7da84e;

    font-weight:600;

    transition:.3s;

}

.view-link:hover{

    color:#5d7f37;

}

.dashboard-table{

    margin-bottom:0;

}

.dashboard-table thead{

    background:#b7d98b;

}

.dashboard-table th{

    color:#6b002b;

    font-weight:700;

    text-align:center;

    padding:14px;

    border:none;

}

.dashboard-table td{

    text-align:center;

    vertical-align:middle;

    padding:16px;

}

.dashboard-table tbody tr{

    transition:.3s;

}

.dashboard-table tbody tr:hover{

    background:rgba(183,217,139,.15);

}

.status-pill{

    display:inline-block;

    padding:6px 14px;

    border-radius:30px;

    font-size:.8rem;

    font-weight:600;

}

.status-pill.accepted{

    background:#d4edda;

    color:#2d7d32;

}

.status-pill.pending{

    background:#fff3cd;

    color:#9a6a00;

}

.status-pill.rejected{

    background:#f8d7da;

    color:#b3261e;

}

.summary-card{

    display:flex;

    align-items:center;

    gap:35px;

    padding:20px 18px;

    min-height:10px;

    border-radius:30px;

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,.3);

    box-shadow:0 18px 40px rgba(0,0,0,.08);

    transition:.35s ease;
    max-width: 550px;
    margin-bottom: 20px;
    margin-left: 25px;

}

.summary-card:hover{

    transform:translateY(-8px);

    box-shadow:0 22px 45px rgba(0,0,0,.12);

}

.card-icon{

    width:100px;

    height:100px;

    border-radius:26px;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:2.8rem;

    background:rgba(255,255,255,.35);

    color:#73002b;

    flex-shrink:0;

}

.card-content{

    display:flex;

    flex-direction:column;

    justify-content:center;

}

.card-content h6{

    font-size:1.45rem;

    margin-bottom:14px;

    color:black;

    font-weight:600;

}

.card-content h2{

    font-size:3rem;

    margin-bottom:14px;

    color:#73002b;

    font-weight:700;

}

.card-content p{

    margin:0;

    font-size:1.25rem;

    color:#666;

}
.row.g-4{

    --bs-gutter-x:2.5rem;

    --bs-gutter-y:2.5rem;

}

.card-content p{

    color:#666;

    margin:0;

    font-size:.95rem;

}

.revenue-card{

    background:rgba(216,245,216,.35);

}

.monthly-card{

    background:rgba(255,242,214,.35);

}

.users-card{

    background:rgba(221,236,255,.35);

}

.bookings-card{

    background:rgba(255,226,235,.35);

}
</style>

<script>
import axios from 'axios'
import Chart from 'chart.js/auto'

export default {
  name: 'AdminDashboard',

  data() {
  return{

    summary:{},

    bookingChart:{},

    trekChart:{},

    recentBookings:[],

    upcomingTreks:[]

}
  },

  mounted() {
    this.fetchDashboard()
  },

  methods: {
    // ==========================================
    // FETCH DASHBOARD
    // ==========================================

    async fetchDashboard() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/admin/dashboard')

        console.log(response.data)


        this.summary = response.data.data.summary

this.bookingChart = response.data.data.booking_chart

this.trekChart = response.data.data.trek_chart

this.recentBookings = response.data.data.recent_bookings

this.upcomingTreks = response.data.data.upcoming_treks

        this.$nextTick(() => {
          this.drawBookingChart()

          this.drawTrekChart()
        })
      } catch (error) {
        console.log('Dashboard Error :', error)
      }
    },

    // ==========================================
    // FORMAT DATE
    // ==========================================

    formatDate(date) {
      if (!date) return '-'

      return new Date(date).toLocaleDateString(
        'en-IN',

        {
          day: '2-digit',

          month: 'short',

          year: 'numeric',
        },
      )
    },
    drawBookingChart() {
      const ctx = document.getElementById('bookingChart')

      if (this.bookingChartInstance) {
        this.bookingChartInstance.destroy()
      }

      this.bookingChartInstance = new Chart(ctx, {
        type: 'pie',

        data: {
          labels: Object.keys(this.bookingChart),

          datasets: [
            {
              data: Object.values(this.bookingChart),

              backgroundColor: ['#F6C344', '#7FB77E', '#C65D7B', '#6AAED6'],
            },
          ],
        },

        options: {
          responsive: true,

          plugins: {
            legend: {
              position: 'bottom',
            },
          },
        },
      })
    },

    drawTrekChart() {
      const ctx = document.getElementById('trekChart')

      if (this.trekChartInstance) {
        this.trekChartInstance.destroy()
      }

      this.trekChartInstance = new Chart(ctx, {
        type: 'bar',

        data: {
          labels: Object.keys(this.trekChart),

          datasets: [
            {
              label: 'Treks',

              data: Object.values(this.trekChart),

              backgroundColor: '#670626',

              borderRadius: 12,
            },
          ],
        },

        options: {
          responsive: true,

          plugins: {
            legend: {
              display: false,
            },
          },

          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      })
    },
  },
}
</script>
