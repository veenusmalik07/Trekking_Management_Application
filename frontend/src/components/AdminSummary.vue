<template>
  <div class="admin-summary-page">
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
            <h1 class="page-title">Admin Summary</h1>

            <p class="page-subtitle">
              Your central command for organizing treks, supervising staff, and delivering
              exceptional outdoor experiences.
            </p>
          </div>
        </header>

        <br /><br /><br />

        <div>
          <p class="trek-quote">
            "The mountains reward preparation. Every well-managed detail creates a safer and more
            memorable journey."
          </p>
        </div>

        <br /><br /><br />
        <section class="stats-section">
          <div class="stat-card">
            <div class="stat-icon">
              <i class="bi bi-people-fill"></i>
            </div>

            <div class="stat-number">
              {{ summary.total_users }}
            </div>

            <div class="stat-title">Total Users</div>

            <div class="stat-subtitle">Registered Trekkers</div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">
              <i class="bi bi-person-workspace"></i>
            </div>

            <div class="stat-number">
              {{ summary.total_staff }}
            </div>

            <div class="stat-title">Total Staff</div>

            <div class="stat-subtitle">Trek Team</div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">
              <i class="bi bi-signpost-2-fill"></i>
            </div>

            <div class="stat-number">
              {{ summary.total_treks }}
            </div>

            <div class="stat-title">Total Treks</div>

            <div class="stat-subtitle">Active Expeditions</div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">
              <i class="bi bi-journal-check"></i>
            </div>

            <div class="stat-number">
              {{ summary.total_bookings }}
            </div>

            <div class="stat-title">Total Bookings</div>

            <div class="stat-subtitle">Reservations Made</div>
          </div>
        </section>

        <br /><br /><br />

        <section class="glass-card mt-5">
          <div class="section-title">
            <h3 class="section-title">
              <i class="bi bi-people-fill me-2"></i>
              Staff Assignment Summary
            </h3>
          </div>

          <hr class="section-divider" />

          <div class="table-responsive">
            <table class="table summary-table">
              <thead>
                <tr>
                  <th>Name</th>

                  <th>Profession</th>

                  <th>Assigned Treks</th>

                  <th>Availability</th>
                </tr>
              </thead>

              <tbody>
                <tr v-for="staff in staffTable" :key="staff.id">
                  <td>{{ staff.name }}</td>

                  <td>{{ staff.profession }}</td>

                  <td>{{ staff.assigned_treks }}</td>

                  <td>{{ staff.availability }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <br /><br /><br />

        <section class="glass-card mt-5">
          <div class="section-title">
            <h3 class="section-title">
              <i class="bi bi-person-lines-fill me-2"></i>
              User Booking Summary
            </h3>
          </div>

          <hr class="section-divider" />

          <div class="table-responsive">
            <table class="table summary-table">
              <thead>
                <tr>
                  <th>User</th>

                  <th>Total Bookings</th>

                  <th>Accepted</th>

                  <th>Pending</th>

                  <th>Rejected</th>

                  <th>Total Spent</th>
                </tr>
              </thead>

              <tbody>
                <tr v-for="user in userBookingTable" :key="user.id">
                  <td>{{ user.full_name }}</td>

                  <td>{{ user.total_bookings }}</td>

                  <td>{{ user.accepted }}</td>

                  <td>{{ user.pending }}</td>

                  <td>{{ user.rejected }}</td>

                  <td>₹{{ user.total_spent }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
        <br /><br /><br />

        <!-- ====================================================
                BOOKING STATUS
==================================================== -->

        <section class="top-treks-section">
          <div class="section-header">
            <div>
              <h2 class="section-title">Booking Status</h2>

              <p class="section-subtitle">Current booking distribution across all reservations.</p>
            </div>
          </div>

          <div class="chart-card">
            <canvas id="bookingChart"></canvas>
          </div>
        </section>

        <br /><br /><br />

        <!-- ====================================================
                TREK STATUS
==================================================== -->

        <section class="top-treks-section">
          <div class="section-header">
            <div>
              <h2 class="section-title">Trek Status</h2>

              <p class="section-subtitle">
                Current availability and progress of trekking expeditions.
              </p>
            </div>
          </div>

          <div class="chart-card">
            <canvas id="trekChart"></canvas>
          </div>
        </section>

        <br /><br /><br />

        <!-- ====================================================
            DIFFICULTY DISTRIBUTION
==================================================== -->

        <section class="top-treks-section">
          <div class="section-header">
            <div>
              <h2 class="section-title">Difficulty Distribution</h2>

              <p class="section-subtitle">Explore how treks are distributed by difficulty level.</p>
            </div>
          </div>

          <div class="chart-card">
            <canvas id="difficultyChart"></canvas>
          </div>
        </section>

        <br /><br /><br />

        <!-- ====================================================
            STAFF DISTRIBUTION
==================================================== -->

        <section class="top-treks-section">
          <div class="section-header">
            <div>
              <h2 class="section-title">Staff Profession Distribution</h2>

              <p class="section-subtitle">Overview of registered staff members by profession.</p>
            </div>
          </div>

          <div class="chart-card">
            <canvas id="staffChart"></canvas>
          </div>
        </section>

        <br /><br /><br />

        <section class="glass-card mt-5">
          <div class="section-title">
            <h3 class="section-title">
              <i class="bi bi-map me-2"></i>
              Trek Capacity Overview
            </h3>

            <p class="section-subtitle">View booking occupancy and trek availability.</p>
          </div>

          <hr class="section-divider" />

          <div class="table-responsive">
            <table class="table summary-table">
              <thead>
                <tr>
                  <th>Trek</th>

                  <th>Booked</th>

                  <th>Capacity</th>

                  <th>Available</th>

                  <th>Status</th>
                </tr>
              </thead>

              <tbody>
                <tr v-for="trek in trekTable" :key="trek.id">
                  <td>{{ trek.trek_name }}</td>

                  <td>{{ trek.booked }}</td>

                  <td>{{ trek.capacity }}</td>

                  <td>{{ trek.available }}</td>

                  <td>
                    <span class="status-badge" :class="trek.status.toLowerCase()">
                      {{ trek.status }}
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <br /><br /><br />

        <section class="chart-card mt-5">
          <div class="chart-header">
            <h3>
              <i class="bi bi-currency-rupee"></i>
              Revenue Trend
            </h3>

            <p>Revenue generated over the last six months.</p>
          </div>

          <canvas id="revenueChart"></canvas>
        </section>

        <br /><br /><br />

        <div class="summary-section mt-5">
          <div class="section-title">
            <i class="bi bi-fire me-2"></i>

            Most Popular Treks
          </div>

          <div class="popular-grid">
            <div class="popular-card" v-for="trek in mostPopularTreks" :key="trek.id">
              <img :src="trek.cover_image" class="popular-image" />

              <div class="popular-content">
                <h5>{{ trek.trek_name }}</h5>

                <p>
                  <i class="bi bi-geo-alt-fill"></i>

                  {{ trek.location }}
                </p>

                <div class="popular-footer">
                  <span> ⭐ {{ trek.booking_count }} Bookings </span>

                  <span> ₹{{ trek.price }} </span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <br /><br /><br />

        <!-- Pagination -->
      </div>
    </main>
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

/*==================================================
STATISTICS
==================================================*/

.stats-section {
  display: grid;

  grid-template-columns: repeat(4, 1fr);

  gap: 24px;

  margin-bottom: 40px;
}

.stat-card {
  position: relative;

  overflow: hidden;

  padding: 28px;

  border-radius: 24px;

  background: rgba(255, 255, 255, 0.16);

  backdrop-filter: blur(18px);

  -webkit-backdrop-filter: blur(18px);

  border: 1px solid rgba(255, 255, 255, 0.28);

  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.08);

  transition: 0.35s ease;
  display: flex;

  flex-direction: column;

  justify-content: center;

  align-items: center;

  text-align: center;
}

.stat-card::before {
  content: '';

  position: absolute;

  top: 0;

  left: 0;

  width: 100%;

  height: 4px;

  background: #bad797;
}

.stat-card:hover {
  transform: translateY(-6px);

  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.15);
}

.stat-icon {
  font-size: 2rem;

  color: #670626;

  margin-bottom: 18px;
}

.stat-number {
  font-size: 3rem;
  font-weight: 700;
  color: #670626;
  margin-bottom: 8px;
  line-height: 1;
}

.stat-number .h3 {
  font-size: 3.2rem;
  font-weight: 700;
  color: #670626;
  margin-bottom: 14px;
  line-height: 1;
}

.stat-title {
  font-size: 1.15rem;

  font-weight: 600;

  color: #2d2d2d;

  margin-bottom: 8px;
  font-family: 'Your Premium Heading Font', serif;
  letter-spacing: 1.1px;
}

.stat-subtitle {
  font-size: 0.92rem;

  color: #666;
}

/*==================================================
TOP TREKS
==================================================*/

.top-treks-section {
  margin-bottom: 45px;
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

/*==================================================
SLIDER
==================================================*/

.top-treks-slider {
  display: flex;

  gap: 24px;

  overflow-x: auto;

  scroll-behavior: smooth;

  padding-bottom: 10px;
}

.top-treks-slider::-webkit-scrollbar {
  display: none;
}

/*==================================================
CARD
==================================================*/
.top-trek-card {
  width: 340px;

  max-width: 340px;

  overflow: hidden;

  border-radius: 28px;

  background: rgba(255, 255, 255, 0.18);

  backdrop-filter: blur(20px);

  -webkit-backdrop-filter: blur(20px);

  border: 1px solid rgba(255, 255, 255, 0.25);

  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);

  transition: 0.35s;

  position: relative;

  padding: 10px;
}

.top-trek-card:hover {
  transform: translateY(-8px);

  box-shadow: 0 28px 55px rgba(0, 0, 0, 0.16);
}

/*==================================================
IMAGE
==================================================*/
.trek-image {
  width: 100%;

  height: 240px;

  display: block;

  object-fit: cover;

  border-radius: 28px 28px 0 0;
}

/*==================================================
OVERLAY
==================================================*/

.trek-overlay {
  position: absolute;

  top: 18px;

  right: 18px;
}

.booking-chip {
  padding: 10px 18px;

  border-radius: 40px;

  background: rgba(255, 255, 255, 0.18);

  backdrop-filter: blur(20px);

  color: white;

  font-weight: 600;
  font-size: 0.85rem;

  border: 1px solid rgba(255, 255, 255, 0.25);
}

/*==================================================
BODY
==================================================*/

.trek-body {
  padding: 24px 26px 28px;
}

.trek-body h4 {
  font-size: 1.45rem;

  color: #670626;

  margin-bottom: 12px;

  font-weight: 700;
}

.trek-body p {
  color: #555;

  margin-bottom: 18px;

  display: flex;

  align-items: center;

  gap: 8px;
}

.trek-details {
  display: flex;

  justify-content: space-between;

  align-items: center;

  margin-bottom: 14px;

  font-weight: 600;

  color: #444;
}

/*==================================================
BUTTONS
==================================================*/

.trek-actions {
  display: flex;

  justify-content: space-between;

  margin-top: 28px;
}

.trek-actions button {
  width: 56px;

  height: 56px;

  border: none;

  border-radius: 16px;

  background: #b0d483;

  color: white;

  display: flex;

  align-items: center;

  justify-content: center;

  font-size: 1.15rem;

  transition: 0.35s;

  cursor: pointer;

  box-shadow: 0 10px 25px rgba(103, 6, 38, 0.25);
}

.trek-actions button:hover {
  background: white;

  color: #71904c;

  transform: translateY(-4px);
}

/*==================================================
FILTER SECTION
==================================================*/

.filter-section {
  margin: 50px 0;

  display: flex;

  align-items: center;

  justify-content: space-between;

  gap: 25px;

  padding: 22px 28px;

  border-radius: 26px;

  background: rgba(255, 255, 255, 0.18);

  backdrop-filter: blur(20px);

  -webkit-backdrop-filter: blur(20px);

  border: 1px solid rgba(255, 255, 255, 0.25);
}

.search-box {
  flex: 1;

  display: flex;

  align-items: center;

  gap: 15px;

  padding: 16px 22px;

  border-radius: 18px;

  background: rgba(255, 255, 255, 0.22);

  transition: 0.35s ease;
}

.search-box:focus-within {
  background: white;
  color: black;

  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
}

.search-box i {
  color: #670626;

  transition: 0.3s;
  font-size: 1.2rem;
}

.search-box:focus-within i {
  color: #670626;
}

.search-box input {
  width: 100%;

  border: none;

  outline: none;

  background: transparent;

  color: #666;

  font-size: 1rem;

  transition: 0.3s;
}
.search-box input::placeholder {
  color: #777;
}
.search-box input:focus {
  color: #000;
}

.search-box input:focus::placeholder {
  color: #999;
}

.filter-group {
  display: flex;

  gap: 15px;
}

.filter-group select {
  background: #670626;
  width: 180px;

  color: white;

  border: none;
  outline: none;

  border-radius: 16px;

  padding: 15px 18px;

  font-weight: 600;

  transition: 0.3s;

  cursor: pointer;
}
.filter-group select:hover {
  background: white;

  color: #670626;
}

.filter-group select:focus {
  background: white;

  color: #670626;

  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
}

.result-count {
  width: 120px;

  text-align: center;

  font-size: 2rem;

  font-weight: 700;

  color: #670626;
}

.result-count span {
  display: block;

  margin-top: 4px;

  font-size: 0.9rem;

  font-weight: 500;

  color: #555;
}

/*=========================================
TABLE HEADER
=========================================*/
.table-wrapper {
  width: 100%;

  overflow-x: auto;
}

.trek-table {
  width: 90%;

  min-width: 800px;

  border-collapse: separate;

  border-spacing: 0 18px;
}

.table-name + small {
  color: #666;

  font-size: 0.85rem;
}

.trek-table thead {
  background: #b0d483;
}

.trek-table thead th {
  color: white;

  font-weight: 700;

  font-size: 1.2rem;

  letter-spacing: 1px;

  padding: 20px;

  border: none;

  text-align: center;
  font-family: 'Your Premium Heading Font', serif;
}

.trek-table thead th:first-child {
  border-radius: 20px 0 0 20px;
}

.trek-table thead th:last-child {
  border-radius: 0 20px 20px 0;
}

.trek-table tbody td {
  padding: 24px 18px;

  vertical-align: middle;
}

.trek-table th,
.trek-table td {
  text-align: center;

  vertical-align: middle;
}

.trek-table tbody tr {
  transition: 0.3s;
}

.trek-table tbody tr:hover {
  background: rgba(255, 255, 255, 0.18);
}

.table-cover {
  width: 70px;

  height: 70px;

  object-fit: cover;

  border-radius: 16px;

  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.table-actions {
  display: flex;

  justify-content: center;

  gap: 12px;
}

.table-actions button {
  width: 42px;

  height: 42px;

  border: none;

  border-radius: 12px;

  display: flex;

  align-items: center;

  justify-content: center;

  cursor: pointer;

  transition: 0.3s ease;

  font-size: 1rem;

  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
}

.trek-table-section {
  width: 100%;
}

.trek-table-section .table-header {
  font-family: 'Your Premium Heading Font', serif;
  color: #670626;
  font-size: 2.6rem;
  margin: 0;
  letter-spacing: 1.2px;
  font-weight: 500;
  width: 80%;
}

.view-btn {
  background: white;

  color: #670626;
}

.view-btn:hover {
  background: rgb(241, 242, 233);

  transform: translateY(-3px);
}

.edit-btn {
  background: rgb(6, 114, 6);

  color: white;
}

.edit-btn:hover {
  background: #1c3f01;

  transform: translateY(-3px);
}

.delete-btn {
  background: #ea0b0b;

  color: white;
}

.delete-btn:hover {
  background: #5c0202;

  transform: translateY(-3px);
}

.status-pill {
  padding: 8px 18px;

  border-radius: 30px;

  font-size: 0.85rem;

  font-weight: 600;
}

.status-pill.upcoming {
  background: #badbe7;

  color: black;
}

.status-pill.completed {
  background: #ebf3bb;

  color: black;
}

.status-pill.ongoing {
  background: #b2ecd4;

  color: black;
}

.status-pill.cancelled {
  background: #ecd1d3;

  color: black;
}

.easy {
  padding: 8px 18px;

  border-radius: 30px;

  font-size: 0.85rem;

  font-weight: 600;

  background: #f4cfd1;

  color: black;
}

.moderate {
  padding: 8px 18px;

  border-radius: 30px;

  font-size: 0.85rem;

  font-weight: 600;

  background: #cfc9ea;

  color: black;
}

.hard {
  padding: 8px 18px;

  border-radius: 30px;

  font-size: 0.85rem;

  font-weight: 600;

  background: #baecb1;

  color: black;
}

/*==================================================
CHART CARD
==================================================*/

.chart-card {
  width: 100%;

  padding: 35px;

  border-radius: 28px;

  background: rgba(255, 255, 255, 0.18);

  backdrop-filter: blur(20px);

  -webkit-backdrop-filter: blur(20px);

  border: 1px solid rgba(255, 255, 255, 0.25);

  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.08);
}

.chart-card canvas {
  width: 100% !important;

  height: 420px !important;
}

.summary-table {
  margin-top: 20px;
}

.summary-table thead {
  background: #b8d98a;
}

.summary-table th {
  color: #6b002b;

  font-weight: 700;

  text-align: center;

  padding: 16px;
}

.summary-table td {
  text-align: center;

  padding: 16px;

  vertical-align: middle;
}

.summary-table tbody tr {
  transition: 0.3s;
}

.summary-table tbody tr:hover {
  background: rgba(184, 217, 138, 0.18);
}

.popular-grid {
  display: grid;

  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));

  gap: 25px;

  margin-top: 25px;
}

.popular-card {
  background: rgba(255, 255, 255, 0.18);

  backdrop-filter: blur(16px);

  border: 1px solid rgba(255, 255, 255, 0.3);

  border-radius: 24px;

  overflow: hidden;

  transition: 0.35s;
}

.popular-card:hover {
  transform: translateY(-8px);

  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.popular-image {
  width: 100%;

  height: 510px;

  object-fit: cover;
}

.popular-content {
  padding: 20px;
}

.popular-content h5 {
  font-weight: 700;

  color: #6d002d;

  margin-bottom: 8px;
}

.popular-content p {
  color: #555;

  margin-bottom: 18px;
}

.popular-footer {
  display: flex;

  justify-content: space-between;

  font-weight: 600;

  color: #7b002c;
}
</style>

<script>
import axios from 'axios'
import Chart from 'chart.js/auto'

export default {
  name: 'AdminSummary',

  data() {
    return {
      summary: {},

      bookingChart: {},

      trekChart: {},

      difficultyChart: {},

      staffChart: {},

      topTreks: [],

      topStaff: [],

      recentBookings: [],

      recentUsers: [],

      trekTable: [],

      staffTable: [],

      userBookingTable: [],
      revenueChart: {},
      mostPopularTreks: [],
    }
  },

  mounted() {
    this.fetchSummary()
  },

  methods: {
    async fetchSummary() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/admin/summary')

        this.summary = response.data.data.summary

        this.bookingChart = response.data.data.booking_chart

        this.trekChart = response.data.data.trek_chart

        this.difficultyChart = response.data.data.difficulty_chart

        this.staffChart = response.data.data.staff_chart

        this.topTreks = response.data.data.top_treks

        this.topStaff = response.data.data.top_staff

        this.recentBookings = response.data.data.recent_bookings

        this.recentUsers = response.data.data.recent_users

        this.trekTable = response.data.data.trek_table

        this.staffTable = response.data.data.staff_table

        this.userBookingTable = response.data.data.user_booking_table
        this.revenueChart = response.data.data.revenue_chart
        this.mostPopularTreks = response.data.data.most_popular_treks

        this.$nextTick(() => {
          this.drawBookingChart()

          this.drawTrekChart()

          this.drawDifficultyChart()

          this.drawStaffChart()
          this.createRevenueChart()
        })
      } catch (error) {
        console.log(error)
      }
    },

    drawBookingChart() {
      new Chart(
        document.getElementById('bookingChart'),

        {
          type: 'pie',

          data: {
            labels: Object.keys(this.bookingChart),

            datasets: [
              {
                data: Object.values(this.bookingChart),

                backgroundColor: ['#F4C95D', '#7AC74F', '#577590', '#F94144'],
              },
            ],
          },

          options: {
            responsive: true,

            maintainAspectRatio: false,
          },
        },
      )
    },

    drawTrekChart() {
      new Chart(
        document.getElementById('trekChart'),

        {
          type: 'bar',

          data: {
            labels: Object.keys(this.trekChart),

            datasets: [
              {
                label: 'Treks',

                data: Object.values(this.trekChart),

                backgroundColor: '#BAD797',

                borderRadius: 12,
              },
            ],
          },

          options: {
            responsive: true,

            maintainAspectRatio: false,

            plugins: {
              legend: {
                display: false,
              },
            },
          },
        },
      )
    },

    drawDifficultyChart() {
      new Chart(
        document.getElementById('difficultyChart'),

        {
          type: 'doughnut',

          data: {
            labels: Object.keys(this.difficultyChart),

            datasets: [
              {
                data: Object.values(this.difficultyChart),

                backgroundColor: ['#8EC5FC', '#BAD797', '#F4C95D', '#F94144'],
              },
            ],
          },

          options: {
            responsive: true,

            maintainAspectRatio: false,
          },
        },
      )
    },

    drawStaffChart() {
      new Chart(
        document.getElementById('staffChart'),

        {
          type: 'bar',

          data: {
            labels: Object.keys(this.staffChart),

            datasets: [
              {
                label: 'Staff',

                data: Object.values(this.staffChart),

                backgroundColor: '#670626',

                borderRadius: 12,
              },
            ],
          },

          options: {
            indexAxis: 'y',

            responsive: true,

            maintainAspectRatio: false,

            plugins: {
              legend: {
                display: false,
              },
            },
          },
        },
      )
    },

    createRevenueChart() {
      const ctx = document.getElementById('revenueChart')

      if (!ctx) return

      new Chart(ctx, {
        type: 'line',

        data: {
          labels: this.revenueChart.map((item) => item.month),

          datasets: [
            {
              label: 'Revenue',

              data: this.revenueChart.map((item) => item.revenue),

              borderColor: '#7b002c',

              backgroundColor: 'rgba(123,0,44,.15)',

              fill: true,

              tension: 0.4,

              borderWidth: 3,

              pointRadius: 5,
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
        },
      })
    },
  },

  computed: {
    filteredTreks() {
      return this.treks.filter((trek) => {
        const matchesSearch =
          !this.search ||
          trek.trek_name.toLowerCase().includes(this.search.toLowerCase()) ||
          trek.state.toLowerCase().includes(this.search.toLowerCase())

        const matchesDifficulty =
          !this.difficultyFilter || trek.difficulty === this.difficultyFilter

        const matchesStatus = !this.statusFilter || trek.status === this.statusFilter

        return matchesSearch && matchesDifficulty && matchesStatus
      })
    },

    popularTreks() {
      return [...this.treks]

        .sort((a, b) => b.booking_count - a.booking_count)

        .slice(0, 3)
    },

    maxBookings() {
      if (this.treks.length === 0) {
        return 0
      }

      return Math.max(...this.treks.map((trek) => trek.booking_count))
    },
  },
}
</script>
