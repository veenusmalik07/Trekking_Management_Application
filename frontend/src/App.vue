<template>
  <router-view />
  <NotificationBell />
</template>

<script>
import NotificationBell from "@/components/NotificationBell.vue";

export default {
  name: "App",
  components: { NotificationBell }
}
</script>

<style>
</style>
