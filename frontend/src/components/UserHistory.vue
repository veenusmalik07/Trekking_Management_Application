<template>

<div class="dashboard-wrapper">

    <!-- Sidebar -->

    <aside class="sidebar">

      <div class="logo-section">
        <i class="bi bi-tree-fill"></i>
        <h3>TrekMate</h3>
      </div>

      <ul class="sidebar-menu">

        <li>
          <router-link to="/user-dashboard">
            <i class="bi bi-house-door-fill"></i>
            <span>Dashboard</span>
          </router-link>
        </li>

        <li>
          <router-link to="/user-browse-treks">
            <i class="bi bi-compass-fill"></i>
            <span>Browse Treks</span>
          </router-link>
        </li>

        <li>
          <router-link to="/user-my-bookings">
            <i class="bi bi-calendar-check-fill"></i>
            <span>My Bookings</span>
          </router-link>
        </li>

        <li>
          <router-link to="/user-history">
            <i class="bi bi-clock-history"></i>
            <span>User History</span>
          </router-link>
        </li>

        <li>
          <router-link to="/user-profile">
            <i class="bi bi-person-fill"></i>
            <span>Profile</span>
          </router-link>
        </li>

        <li>
          <router-link to="/user-summary">
            <i class="bi bi-bar-chart-fill"></i>
            <span>Summary</span>
          </router-link>
        </li>

      </ul>

      <div class="logout-btn">
        <button class="btn btn-success w-100">
          <i class="bi bi-box-arrow-right"></i>
          Logout
        </button>
      </div>

    </aside>

    <div class="main-content">

        <!-- HEADER -->

        <section class="history-header">

            <h1>

                Trek History

            </h1>

            <p>

                View your completed and cancelled trekking history.

            </p>

        </section>

        <!-- STATISTICS -->

        <section class="stats-grid">

            <div class="stat-card">

                <i class="bi bi-check-circle-fill"></i>

                <h2>{{ statistics.completed }}</h2>

                <p>Completed Treks</p>

            </div>

            <div class="stat-card">

                <i class="bi bi-x-circle-fill"></i>

                <h2>{{ statistics.cancelled }}</h2>

                <p>Cancelled Treks</p>

            </div>

        </section>

        <!-- CHART -->

        <section class="chart-card">

            <h2>

                Trek History Overview

            </h2>

            <canvas

                ref="historyChart"

                height="280"

            ></canvas>

        </section>

        <!-- TABS -->

        <section class="history-tabs">

            <button

                :class="{active:selectedTab==='Completed'}"

                @click="selectedTab='Completed'"

            >

                Completed ({{ completedTreks.length }})

            </button>

            <button

                :class="{active:selectedTab==='Cancelled'}"

                @click="selectedTab='Cancelled'"

            >

                Cancelled ({{ cancelledTreks.length }})

            </button>

        </section>

        <!-- Cards will come next -->

    </div>

    <!-- HISTORY CARDS -->

<section class="history-container">

    <div

        v-for="trek in displayedTreks"

        :key="trek.id"

        class="history-card"

    >

        <!-- Image -->

        <div class="history-image">

            <img

                :src="trek.cover_image"

                :alt="trek.trek_name"

            >

            <span

                :class="[

                    'status-badge',

                    trek.booking_status.toLowerCase()

                ]"

            >

                {{ trek.booking_status }}

            </span>

        </div>

        <!-- Details -->

        <div class="history-content">

            <h2>

                {{ trek.trek_name }}

            </h2>

            <div class="history-info">

                <p>

                    <i class="bi bi-upc-scan"></i>

                    {{ trek.booking_reference }}

                </p>

                <p>

                    <i class="bi bi-geo-alt-fill"></i>

                    {{ trek.location }}

                </p>

                <p>

                    <i class="bi bi-calendar-event-fill"></i>

                    {{ trek.start_date }}

                </p>

                <p>

                    <i class="bi bi-currency-rupee"></i>

                    ₹ {{ trek.amount }}

                </p>

            </div>

            <div class="history-buttons">

                <button

                    class="details-btn"

                    @click="viewDetails(trek)"

                >

                    View Details

                </button>

            </div>

        </div>

    </div>

</section>

</div>

</template>


<script>

import axios from "axios";
import Chart from "chart.js/auto";

export default{

    name:"TrekHistory",

    data(){

        return{

            loading:true,

            historyChart:null,

            selectedTab:"Completed",

            statistics:{

                completed:0,

                cancelled:0

            },

            completedTreks:[],

            cancelledTreks:[]

        }

    },

    computed:{

        displayedTreks(){

            if(this.selectedTab==="Completed"){

                return this.completedTreks;

            }

            return this.cancelledTreks;

        }

    },

    async mounted(){

        await this.fetchHistory();

    },

    methods:{

        async fetchHistory(){

            try{

                const token=localStorage.getItem("token");

                const response=await axios.get(

                    "http://127.0.0.1:5000/api/user/trek-history",

                    {

                        headers:{

                            Authorization:`Bearer ${token}`

                        }

                    }

                );

                this.statistics=response.data.statistics;

                this.completedTreks=response.data.completedTreks;

                this.cancelledTreks=response.data.cancelledTreks;

                this.$nextTick(()=>{

                    this.renderHistoryChart();

                });

            }

            catch(error){

                console.error("Unable to fetch trek history",error);

            }

            finally{

                this.loading=false;

            }

        },

        renderHistoryChart(){

            if(this.historyChart){

                this.historyChart.destroy();

            }

            const ctx=this.$refs.historyChart.getContext("2d");

            this.historyChart=new Chart(ctx,{

                type:"doughnut",

                data:{

                    labels:[

                        "Completed",

                        "Cancelled"

                    ],

                    datasets:[

                        {

                            data:[

                                this.statistics.completed,

                                this.statistics.cancelled

                            ],

                            backgroundColor:[

                                "#198754",

                                "#DC3545"

                            ],

                            borderColor:"#ffffff",

                            borderWidth:3,

                            hoverOffset:15

                        }

                    ]

                },

                options:{

                    responsive:true,

                    maintainAspectRatio:false,

                    cutout:"65%",

                    plugins:{

                        legend:{

                            position:"bottom",

                            labels:{

                                usePointStyle:true,

                                pointStyle:"circle",

                                padding:20,

                                font:{

                                    size:14

                                }

                            }

                        }

                    }

                }

            });

        },

        viewDetails(trek){

            this.$router.push(

                `/trek-history/${trek.id}`

            );

        }

    }

}

</script>










