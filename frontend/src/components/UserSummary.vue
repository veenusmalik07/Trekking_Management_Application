<template>

<div class="dashboard-wrapper">

    <!-- ================= SIDEBAR ================= -->

    <aside class="sidebar">

      <div class="logo-section">
        <i class="bi bi-tree-fill"></i>
        <h3>TrekMate</h3>
      </div>

      <ul class="sidebar-menu">

        <li class="active">
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

    <!-- ================= MAIN ================= -->

    <div class="main-content">

        <!-- ================= HERO ================= -->

        <section class="summary-header">

            <h1>

                My Trekking Journey

            </h1>

            <p>

                Track your adventures, achievements and trekking progress.

            </p>

        </section>

        <!-- ================= STATS ================= -->

        <section class="stats-grid">

            <div class="stat-card">

                <i class="bi bi-map-fill"></i>

                <h2>{{ summary.totalTreks }}</h2>

                <p>Total Treks</p>

            </div>

            <div class="stat-card">

                <i class="bi bi-geo-alt-fill"></i>

                <h2>{{ summary.placesVisited }}</h2>

                <p>Places Visited</p>

            </div>

            <div class="stat-card">

                <i class="bi bi-currency-rupee"></i>

                <h2>₹ {{ summary.totalSpent }}</h2>

                <p>Total Spent</p>

            </div>

            <div class="stat-card">

                <i class="bi bi-star-fill"></i>

                <h2>{{ summary.completedTreks }}</h2>

                <p>Completed Treks</p>

            </div>

        </section>

        <!-- ================= CHARTS ================= -->

        <section class="charts-grid">

            <div class="chart-card">

                <h2>

                    Booking Status

                </h2>

                <canvas

                    ref="bookingChart"

                    height="280"

                ></canvas>

            </div>

            <div class="chart-card">

                <h2>

                    Monthly Bookings

                </h2>

                <canvas

                    ref="monthlyChart"

                    height="280"

                ></canvas>

            </div>

        </section>

        <section class="chart-card">

            <h2>

                Difficulty Distribution

            </h2>

            <canvas

                ref="difficultyChart"

                height="280"

            ></canvas>

        </section>

                <!-- ================= NEXT TREK + ACTIVITIES ================= -->

        <section class="bottom-grid">

            <!-- NEXT TREK -->

            <div class="next-trek-card">

                <h2>

                    <i class="bi bi-backpack2-fill"></i>

                    Upcoming Trek

                </h2>

                <div class="next-trek-content">

                    <img

                        :src="nextTrek.cover_image"

                        :alt="nextTrek.trek_name"

                    >

                    <div>

                        <h3>

                            {{ nextTrek.trek_name }}

                        </h3>

                        <p>

                            <i class="bi bi-geo-alt-fill"></i>

                            {{ nextTrek.location }}

                        </p>

                        <p>

                            <i class="bi bi-calendar-event-fill"></i>

                            {{ nextTrek.start_date }}

                        </p>

                        <p>

                            <i class="bi bi-clock-fill"></i>

                            {{ nextTrek.reporting_time }}

                        </p>

                    </div>

                </div>

            </div>

            <!-- RECENT ACTIVITY -->

            <div class="activity-section">

                <h2>

                    <i class="bi bi-clock-history"></i>

                    Recent Activities

                </h2>

                <div

                    class="activity-card"

                    v-for="activity in activities"

                    :key="activity.id"

                >

                    <i class="bi bi-check-circle-fill"></i>

                    <div>

                        <h4>

                            {{ activity.title }}

                        </h4>

                        <p>

                            {{ activity.date }}

                        </p>

                    </div>

                </div>

            </div>

        </section>

        <!-- ================= ACHIEVEMENTS ================= -->

        <section class="badge-section">

            <h2>

                <i class="bi bi-trophy-fill"></i>

                Achievement Badges

            </h2>

            <div class="badge-grid">

                <div

                    class="badge-card"

                    v-for="badge in badges"

                    :key="badge.id"

                >

                    <i :class="badge.icon"></i>

                    <h4>

                        {{ badge.title }}

                    </h4>

                    <p>

                        {{ badge.description }}

                    </p>

                </div>

            </div>

        </section>

        <!-- ================= PLACES VISITED ================= -->

        <section class="places-section">

            <h2>

                <i class="bi bi-pin-map-fill"></i>

                Places Explored

            </h2>

            <div class="places-grid">

                <div

                    class="place-card"

                    v-for="place in placesVisited"

                    :key="place"

                >

                    <i class="bi bi-geo-fill"></i>

                    {{ place }}

                </div>

            </div>

        </section>

    </div>

</div>

</template>



<script>

import axios from "axios";
import Chart from "chart.js/auto";

export default{

    name:"UserSummary",

    data(){

        return{

            loading:true,

            bookingChart:null,

            monthlyChart:null,

            difficultyChart:null,

            summary:{

                totalTreks:0,

                placesVisited:0,

                totalSpent:0,

                completedTreks:0

            },

            bookingData:{

                Pending:0,

                Accepted:0,

                Completed:0,

                Cancelled:0

            },

            monthlyData:[],

            difficultyData:{

                Easy:0,

                Moderate:0,

                Difficult:0

            },

            nextTrek:{},

            activities:[],

            badges:[],

            placesVisited:[]

        }

    },

    async mounted(){

        await this.fetchSummary();

    },

    methods:{

        async fetchSummary(){

            try{

                const token=localStorage.getItem("token");

                const response=await axios.get(

                    "http://127.0.0.1:5000/api/user/summary",

                    {

                        headers:{

                            Authorization:`Bearer ${token}`

                        }

                    }

                );

                this.summary=response.data.summary;

                this.bookingData=response.data.bookingChart;

                this.monthlyData=response.data.monthlyChart;

                this.difficultyData=response.data.difficultyChart;

                this.nextTrek=response.data.nextTrek;

                this.activities=response.data.activities;

                this.badges=response.data.badges;

                this.placesVisited=response.data.placesVisited;

                this.$nextTick(()=>{

                    this.renderBookingChart();

                    this.renderMonthlyChart();

                    this.renderDifficultyChart();

                });

            }

            catch(error){

                console.log(error);

            }

            finally{

                this.loading=false;

            }

        },

        renderBookingChart(){

            if(this.bookingChart){

                this.bookingChart.destroy();

            }

            const ctx=this.$refs.bookingChart.getContext("2d");

            this.bookingChart=new Chart(ctx,{

                type:"pie",

                data:{

                    labels:[

                        "Pending",

                        "Accepted",

                        "Completed",

                        "Cancelled"

                    ],

                    datasets:[

                        {

                            data:[

                                this.bookingData.Pending,

                                this.bookingData.Accepted,

                                this.bookingData.Completed,

                                this.bookingData.Cancelled

                            ],

                            backgroundColor:[

                                "#FFC107",

                                "#0DCAF0",

                                "#198754",

                                "#DC3545"

                            ],

                            borderWidth:2,

                            borderColor:"#fff"

                        }

                    ]

                },

                options:{

                    responsive:true,

                    maintainAspectRatio:false,

                    plugins:{

                        legend:{

                            position:"bottom"

                        }

                    }

                }

            });

        },

        renderMonthlyChart(){

            if(this.monthlyChart){

                this.monthlyChart.destroy();

            }

            const ctx=this.$refs.monthlyChart.getContext("2d");

            this.monthlyChart=new Chart(ctx,{

                type:"bar",

                data:{

                    labels:this.monthlyData.map(

                        item=>item.month

                    ),

                    datasets:[

                        {

                            label:"Bookings",

                            data:this.monthlyData.map(

                                item=>item.count

                            ),

                            backgroundColor:"#2D6A4F",

                            borderRadius:10,

                            borderSkipped:false

                        }

                    ]

                },

                options:{

                    responsive:true,

                    maintainAspectRatio:false,

                    plugins:{

                        legend:{

                            display:false

                        }

                    },

                    scales:{

                        y:{

                            beginAtZero:true,

                            ticks:{

                                stepSize:1

                            }

                        }

                    }

                }

            });

        },

        renderDifficultyChart(){

            if(this.difficultyChart){

                this.difficultyChart.destroy();

            }

            const ctx=this.$refs.difficultyChart.getContext("2d");

            this.difficultyChart=new Chart(ctx,{

                type:"doughnut",

                data:{

                    labels:[

                        "Easy",

                        "Moderate",

                        "Difficult"

                    ],

                    datasets:[

                        {

                            data:[

                                this.difficultyData.Easy,

                                this.difficultyData.Moderate,

                                this.difficultyData.Difficult

                            ],

                            backgroundColor:[

                                "#4CAF50",

                                "#FFC107",

                                "#DC3545"

                            ],

                            borderColor:"#fff",

                            borderWidth:3

                        }

                    ]

                },

                options:{

                    responsive:true,

                    maintainAspectRatio:false,

                    cutout:"65%",

                    plugins:{

                        legend:{

                            position:"bottom"

                        }

                    }

                }

            });

        },

        logout(){

            localStorage.removeItem("token");

            this.$router.push("/user-login");

        }

    }

}

</script>