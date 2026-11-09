<template>
  <div class="staff-view-trek">
    <aside class="sidebar">
      <div class="sidebar-logo"><i class="bi bi-tree-fill logo-icon"></i><h2 class="logo-text">TREKMATE</h2></div>
      <nav class="sidebar-menu">
        <router-link to="/staff-dashboard" class="menu-item"><i class="bi bi-grid-1x2-fill"></i><span>Dashboard</span></router-link>
        <router-link to="/staff-treks" class="menu-item active"><i class="bi bi-signpost-2-fill"></i><span>Treks</span></router-link>
        <router-link to="/staff-participants" class="menu-item"><i class="bi bi-person-circle"></i><span>Participants</span></router-link>
        <router-link to="/staff-summary" class="menu-item"><i class="bi bi-bar-chart-fill"></i><span>Summary</span></router-link>
      </nav>
      <div class="sidebar-footer"><router-link to="/login" class="menu-item"><i class="bi bi-box-arrow-right"></i><span>Logout</span></router-link></div>
    </aside>

    <main class="main-content">
      <header class="page-header">
        <div><h1>View Trek</h1><p>Review your assigned trek and update its completion status when it finishes.</p></div>
        <button class="back-btn" @click="$router.push('/staff-treks')"><i class="bi bi-arrow-left"></i> Back</button>
      </header>

      <p v-if="error" class="alert alert-danger">{{ error }}</p>
      <div v-else-if="loading" class="loading">Loading trek details…</div>

      <template v-else>
        <section class="hero-card">
          <img :src="trek.cover_image || 'https://placehold.co/900x700?text=No+Image'" :alt="trek.trek_name">
          <div class="hero-details">
            <div class="badge-row"><span class="badge difficulty">{{ trek.difficulty }}</span><span class="badge status">{{ trek.status }}</span></div>
            <h2>{{ trek.trek_name }}</h2>
            <p><i class="bi bi-geo-alt-fill"></i> {{ trek.location }}, {{ trek.state }}</p>
            <div class="stats"><span><strong>{{ trek.duration }}</strong> Days</span><span><strong>{{ trek.available_slots }}/{{ trek.capacity }}</strong> Slots</span><span><strong>{{ assignment.role || 'Staff' }}</strong> Role</span></div>
          </div>
        </section>

        <section class="card completion-card">
          <div><h3><i class="bi bi-check2-circle"></i> Completion status</h3><p>Current assignment status: <strong>{{ assignment.status }}</strong></p></div>
          <button v-if="assignment.status !== 'Completed'" class="complete-btn" :disabled="updating" @click="completeTrek">
            <i class="bi bi-check-circle-fill"></i> {{ updating ? 'Updating…' : 'Mark Trek Completed' }}
          </button>
          <span v-else class="completed-label"><i class="bi bi-check-circle-fill"></i> Trek completed</span>
        </section>

        <section class="card"><h3>Trek schedule</h3><div class="detail-grid"><Detail label="Start date" :value="formatDate(trek.start_date)" /><Detail label="End date" :value="formatDate(trek.end_date)" /><Detail label="Registration deadline" :value="formatDate(trek.registration_deadline)" /><Detail label="Meeting point" :value="trek.meeting_point" /></div></section>
        <section class="card"><h3>Requirements</h3><div class="detail-grid"><Detail label="Age range" :value="`${trek.minimum_age || '-'} – ${trek.maximum_age || '-'} years`" /><Detail label="Fitness requirement" :value="trek.fitness_requirement" /><Detail label="Equipment required" :value="trek.equipment_required" wide /></div></section>
        <section class="card"><h3>About this trek</h3><p class="description">{{ trek.description || 'No description available.' }}</p></section>
        <section v-if="gallery.length" class="card"><h3>Gallery</h3><div class="gallery"><img v-for="image in gallery" :key="image.id" :src="image.media_url" :alt="image.caption || trek.trek_name"></div></section>
      </template>
    </main>
  </div>
</template>

<script>
import axios from 'axios'
import { h } from 'vue'

export default {
  name: 'StaffViewTrek',
  data: () => ({ trek: {}, gallery: [], assignment: {}, loading: true, updating: false, error: '' }),
  mounted () { this.fetchTrek() },
  methods: {
    authHeaders () { return { Authorization: `Bearer ${localStorage.getItem('access_token')}` } },
    async fetchTrek () {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/staff/treks/${this.$route.params.id}/details`, { headers: this.authHeaders() })
        const data = response.data.data
        this.trek = data.trek
        this.gallery = data.gallery
        this.assignment = data.assignment
      } catch (error) {
        this.error = error.response?.data?.message || 'Unable to load trek details.'
      } finally { this.loading = false }
    },
    formatDate (date) {
      return date ? new Date(date).toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' }) : '-'
    },
    async completeTrek () {
      if (!confirm('Mark this trek as completed?')) return
      this.updating = true
      try {
        const response = await axios.put(`http://127.0.0.1:5000/api/staff/complete-trek/${this.assignment.id}`, {}, { headers: this.authHeaders() })
        alert(response.data.message)
        this.assignment.status = 'Completed'
        this.trek.status = 'Completed'
      } catch (error) {
        alert(error.response?.data?.message || 'Unable to update completion status.')
      } finally { this.updating = false }
    }
  },
  components: {
    Detail: {
      props: ['label', 'value', 'wide'],
      render () {
        return h('div', { class: ['detail', { wide: this.wide }] }, [
          h('span', this.label),
          h('strong', this.value || '-')
        ])
      }
    }
  }
}
</script>

<style scoped>
.staff-view-trek { min-height: 100vh; background: #f3f7f2; color: #1e3024; display: flex; }
.sidebar { width: 255px; min-height: 100vh; padding: 28px 18px; background: #123d2a; color: #fff; position: fixed; display: flex; flex-direction: column; }
.sidebar-logo { display: flex; align-items: center; gap: 10px; padding: 0 12px 35px; }.logo-icon { font-size: 1.6rem; }.logo-text { font-size: 1.25rem; margin: 0; }.sidebar-menu { display: grid; gap: 8px; }.menu-item { color: #dce9df; text-decoration: none; padding: 12px; border-radius: 10px; display: flex; align-items: center; gap: 12px; }.menu-item:hover, .menu-item.active { background: #2c6847; color: #fff; }.sidebar-footer { margin-top: auto; }
.main-content { margin-left: 255px; width: calc(100% - 255px); padding: 42px clamp(20px, 5vw, 70px); }.page-header { display: flex; justify-content: space-between; gap: 20px; align-items: center; margin-bottom: 30px; }.page-header h1 { margin: 0 0 8px; }.page-header p { margin: 0; color: #637267; }.back-btn, .complete-btn { border: 0; border-radius: 9px; padding: 11px 16px; font-weight: 700; cursor: pointer; }.back-btn { background: #e0e9e2; color: #234b32; }.hero-card, .card { background: #fff; border-radius: 16px; box-shadow: 0 8px 25px #153d2114; margin-bottom: 24px; overflow: hidden; }.hero-card { display: grid; grid-template-columns: minmax(260px, .85fr) 1.15fr; }.hero-card > img { width: 100%; height: 310px; object-fit: cover; }.hero-details { padding: 34px; }.hero-details h2 { margin: 18px 0 10px; }.hero-details p { color: #526957; }.badge-row { display: flex; gap: 8px; }.badge { border-radius: 999px; padding: 6px 11px; font-size: .85rem; font-weight: 700; }.difficulty { color: #8a5c00; background: #fff1cb; }.status { color: #176438; background: #d9f4df; }.stats { display: flex; flex-wrap: wrap; gap: 24px; margin-top: 28px; }.stats span { display: grid; gap: 3px; color: #657468; }.stats strong { color: #1f3826; }.card { padding: 28px; }.card h3 { margin: 0 0 20px; }.completion-card { display: flex; align-items: center; justify-content: space-between; gap: 18px; }.completion-card p { margin: 8px 0 0; color: #637267; }.complete-btn { color: #fff; background: #187243; white-space: nowrap; }.complete-btn:disabled { opacity: .6; cursor: wait; }.completed-label { color: #187243; font-weight: 700; }.detail-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; }.detail { padding: 16px; border-radius: 10px; background: #f4f8f4; display: grid; gap: 6px; }.detail span { color: #667569; font-size: .86rem; }.detail.wide { grid-column: 1 / -1; }.description { line-height: 1.75; white-space: pre-line; color: #485d4d; }.gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; }.gallery img { width: 100%; height: 150px; border-radius: 10px; object-fit: cover; }.loading { padding: 50px; text-align: center; color: #58705e; }
@media (max-width: 800px) { .sidebar { width: 70px; padding: 20px 10px; }.logo-text, .menu-item span { display: none; }.sidebar-logo { padding: 0 10px 25px; }.main-content { margin-left: 70px; width: calc(100% - 70px); }.hero-card { grid-template-columns: 1fr; }.hero-card > img { height: 230px; }.detail-grid { grid-template-columns: 1fr; }.completion-card { align-items: flex-start; flex-direction: column; } }
</style>
