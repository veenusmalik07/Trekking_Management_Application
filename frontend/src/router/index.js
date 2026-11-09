import { createRouter, createWebHistory } from 'vue-router'

import AdminDashboard from '@/components/AdminDashboard.vue'
import AdminTreks from '@/components/AdminTreks.vue'
import AdminCreateTrek from '@/components/AdminCreateTrek.vue'
import AdminViewTrek from '@/components/AdminViewTrek.vue'
import AdminEditTrek from '@/components/AdminEditTrek.vue'
import AdminUsers from "@/components/AdminUsers.vue"
import AdminViewUser from "@/components/AdminViewUser.vue"
import AdminStaff from "@/components/AdminStaff.vue"
import AdminCreateStaff from '@/components/AdminCreateStaff.vue'
import AdminViewStaff from "@/components/AdminViewStaff.vue"
import AdminEditStaff from "@/components/AdminEditStaff.vue"
import AdminAssignStaff from '@/components/AdminAssignStaff.vue'
import AdminBookings from '@/components/AdminBookings.vue'
import AdminViewBooking from '@/components/AdminViewBooking.vue'
import AdminSummary from '@/components/AdminSummary.vue'

import LandingView from '../views/LandingView.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import TermsView from '@/views/TermsView.vue'

import UserDashboard from '@/components/UserDashboard.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserBrowseTreks from "@/components/UserBrowseTreks.vue"
import UserViewTrek from "@/components/UserViewTrek.vue"
import UserMyBookings from '@/components/UserMyBookings.vue'
import UserBookTrek from '@/components/UserBookTrek.vue'
import UserHistory from '@/components/UserHistory.vue'
import UserSummary from '@/components/UserSummary.vue'

import StaffDashboard from "@/components/StaffDashboard.vue";
import StaffTreks from "@/components/StaffTreks.vue";
import StaffParticipants from "@/components/StaffParticipants.vue";
import StaffSummary from "@/components/StaffSummary.vue";
import StaffProfile from "@/components/StaffProfile.vue";
import StaffViewTrek from "@/components/StaffViewTrek.vue";


const routes = [
  {
    path: '/',
    component: LandingView
  },
  
  {
    path: "/login",
    component: Login 
  },

  {
    path: "/register",
    component: Register
  },

  {
    path: '/terms',
    name: 'terms',
    component: TermsView
  },

  /* ======ADMIN======= */
  {
    path: "/admin-dashboard",
    component: AdminDashboard
  },

{
    path: "/admin-treks",
    component: AdminTreks
},

{
    path: "/admin-create-trek",
    component: AdminCreateTrek
},

{
    path: "/admin-view-trek/:id",
    component: AdminViewTrek
},

{
    path: "/admin-edit-trek/:id",
    component: AdminEditTrek
},

{
    path: "/admin-users",
    component: AdminUsers
},

{
  path: "/admin-view-user/:id",
  component: AdminViewUser
},

{
  path: "/admin-staff",
  component: AdminStaff
},

{
  path: "/admin-create-staff",
  component: AdminCreateStaff
},

{
    path:"/admin-view-staff/:id",
    component:AdminViewStaff
},

{
    path:"/admin-edit-staff/:id",
    component:AdminEditStaff
},

{
    path: "/admin-assign-staff/:id",
    component: AdminAssignStaff
},

{
  path: "/admin-bookings",
  component: AdminBookings
},

{
    path: "/admin/view-booking/:id",
    component: AdminViewBooking,
},

{
  path: "/admin-summary",
  component: AdminSummary
},

 /* ======USER======= */

  {
    path: '/user-dashboard',
    name: 'UserDashboard',
    component: UserDashboard
  },

  {
    path: '/user-profile',
    name: 'UserProfile',
    component: UserProfile
  },

  {
    path: "/user-browse-treks",
    name: "UserBrowseTreks",
    component: UserBrowseTreks
},

{
    path: "/user-view-trek/:id",
    name: "UserViewTrek",
    component: UserViewTrek
},

  {
    path: '/user-my-bookings',
    name: 'UserMyBookings',
    component: UserMyBookings
  },

  {
  path: "/user-book-trek/:id",
  name: "UserBookTrek",
  component: UserBookTrek
},

  {
    path: "/user-history",
    component: UserHistory
  },

  {
    path: "/user-summary",
    component: UserSummary
  },



   /* ======STAFF======= */

  {
    path: "/staff-dashboard",
    name: "StaffDashboard",
    component: StaffDashboard
},
{
    path: "/staff-treks",
    name: "StaffTreks",
    component: StaffTreks
},
{
    path: "/staff-view-trek/:id",
    name: "StaffViewTrek",
    component: StaffViewTrek
},
{
    path: "/staff-participants",
    name: "StaffParticipants",
    component: StaffParticipants
},
{
    path: "/staff-summary",
    name: "StaffSummary",
    component: StaffSummary
},
{
    path: "/staff-profile",
    name: "StaffProfile",
    component: StaffProfile
},

  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
