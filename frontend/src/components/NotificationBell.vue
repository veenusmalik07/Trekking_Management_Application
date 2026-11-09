<template>
  <div v-if="hasToken" class="notification-menu">
    <button
      class="notification-toggle"
      type="button"
      aria-label="Open notifications"
      @click="toggleNotifications"
    >
      <i class="bi bi-bell-fill"></i>
      <span v-if="unreadCount" class="notification-count">{{ unreadCount > 99 ? '99+' : unreadCount }}</span>
    </button>

    <section v-if="isOpen" class="notification-panel">
      <header class="notification-header">
        <div>
          <h2>Notifications</h2>
          <p>{{ unreadCount ? `${unreadCount} unread` : 'You are all caught up' }}</p>
        </div>
        <button v-if="unreadCount" class="read-all" type="button" @click="markAllAsRead">
          Mark all read
        </button>
      </header>

      <div v-if="loading" class="notification-state">Loading notifications...</div>
      <div v-else-if="!notifications.length" class="notification-state">No notifications yet.</div>

      <div v-else class="notification-list">
        <button
          v-for="notification in notifications"
          :key="notification.id"
          :class="['notification-item', { unread: !notification.is_read }]"
          type="button"
          @click="markAsRead(notification)"
        >
          <i :class="notificationIcon(notification.notification_type)"></i>
          <span class="notification-content">
            <strong>{{ notification.title }}</strong>
            <span>{{ notification.message }}</span>
            <small>{{ notification.created_at }}</small>
          </span>
          <span v-if="!notification.is_read" class="unread-dot"></span>
        </button>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000/api";

export default {
  name: "NotificationBell",

  data() {
    return {
      hasToken: false,
      isOpen: false,
      loading: false,
      unreadCount: 0,
      notifications: [],
      refreshTimer: null,
    };
  },

  watch: {
    "$route.fullPath": {
      immediate: true,
      handler() {
        this.refreshUnreadCount();
      },
    },
  },

  mounted() {
    this.refreshTimer = window.setInterval(this.refreshUnreadCount, 30000);
  },

  beforeUnmount() {
    window.clearInterval(this.refreshTimer);
  },

  methods: {
    authConfig() {
      const token = localStorage.getItem("access_token");
      return { headers: { Authorization: `Bearer ${token}` } };
    },

    async refreshUnreadCount() {
      const token = localStorage.getItem("access_token");
      this.hasToken = Boolean(token);
      if (!token) {
        this.isOpen = false;
        this.unreadCount = 0;
        this.notifications = [];
        return;
      }

      try {
        const response = await axios.get(`${API_BASE_URL}/notifications/unread-count`, this.authConfig());
        this.unreadCount = response.data.count;
      } catch (error) {
        if (error.response?.status === 401 || error.response?.status === 422) {
          this.hasToken = false;
          this.isOpen = false;
        }
      }
    },

    async toggleNotifications() {
      this.isOpen = !this.isOpen;
      if (this.isOpen) {
        await this.fetchNotifications();
      }
    },

    async fetchNotifications() {
      this.loading = true;
      try {
        const response = await axios.get(`${API_BASE_URL}/notifications`, this.authConfig());
        this.notifications = response.data.notifications;
        await this.refreshUnreadCount();
      } finally {
        this.loading = false;
      }
    },

    async markAsRead(notification) {
      if (notification.is_read) return;

      try {
        await axios.put(`${API_BASE_URL}/notifications/${notification.id}/read`, {}, this.authConfig());
        notification.is_read = true;
        this.unreadCount = Math.max(0, this.unreadCount - 1);
      } catch (error) {
        console.error("Unable to mark notification as read", error);
      }
    },

    async markAllAsRead() {
      try {
        await axios.put(`${API_BASE_URL}/notifications/read-all`, {}, this.authConfig());
        this.notifications.forEach((notification) => {
          notification.is_read = true;
        });
        this.unreadCount = 0;
      } catch (error) {
        console.error("Unable to mark notifications as read", error);
      }
    },

    notificationIcon(type) {
      const icons = {
        Booking: "bi bi-calendar-check-fill",
        Payment: "bi bi-credit-card-fill",
        Refund: "bi bi-cash-coin",
        Assignment: "bi bi-person-workspace",
        Completion: "bi bi-trophy-fill",
        Export: "bi bi-file-earmark-spreadsheet-fill",
      };
      return icons[type] || "bi bi-bell-fill";
    },
  },
};
</script>

<style scoped>
.notification-menu {
  position: fixed;
  top: 18px;
  right: 28px;
  z-index: 20000;
}

.notification-toggle {
  position: relative;
  width: 48px;
  height: 48px;
  border: 0;
  border-radius: 50%;
  background: #43302e;
  color: white;
  font-size: 1.15rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

.notification-count {
  position: absolute;
  top: -5px;
  right: -7px;
  min-width: 20px;
  height: 20px;
  padding: 0 5px;
  border-radius: 12px;
  background: #c62828;
  color: white;
  font-size: 0.7rem;
  font-weight: 700;
  line-height: 20px;
}

.notification-panel {
  position: absolute;
  top: 58px;
  right: 0;
  width: min(390px, calc(100vw - 30px));
  max-height: 520px;
  overflow: hidden;
  border: 1px solid #eadfce;
  border-radius: 18px;
  background: white;
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.22);
}

.notification-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 18px;
  border-bottom: 1px solid #f0e9df;
}

.notification-header h2 { margin: 0; color: #43302e; font-size: 1.1rem; }
.notification-header p { margin: 3px 0 0; color: #777; font-size: 0.8rem; }
.read-all { border: 0; background: transparent; color: #6d0031; font-size: 0.8rem; font-weight: 700; }
.notification-list { max-height: 420px; overflow-y: auto; }
.notification-state { padding: 30px 18px; color: #777; text-align: center; }

.notification-item {
  display: flex;
  width: 100%;
  gap: 12px;
  padding: 15px 18px;
  border: 0;
  border-bottom: 1px solid #f5f1eb;
  background: white;
  color: #43302e;
  text-align: left;
}

.notification-item:hover, .notification-item.unread { background: #fff8e8; }
.notification-item > i { padding-top: 3px; color: #6d0031; font-size: 1.05rem; }
.notification-content { display: grid; flex: 1; gap: 3px; }
.notification-content strong { font-size: 0.9rem; }
.notification-content span { color: #666; font-size: 0.82rem; line-height: 1.35; }
.notification-content small { color: #999; font-size: 0.72rem; }
.unread-dot { width: 8px; height: 8px; margin-top: 7px; border-radius: 50%; background: #c62828; }

@media (max-width: 768px) {
  .notification-menu { top: 12px; right: 14px; }
}
</style>
