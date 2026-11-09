<template>

<div class="admin-create-trek-page">

    <!-- Fixed Mountain Background -->
    <div class="page-background"></div>

    <!-- Sidebar -->
    <aside class="sidebar">
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
            to="/admin-dashboard"
            class="menu-item"
        >
            <i class="bi bi-grid-1x2-fill"></i>
            <span>Dashboard</span>
        </router-link>

        <router-link
            to="/admin-treks"
            class="menu-item"
        >
            <i class="bi bi-signpost-2-fill"></i>
            <span>Treks</span>
        </router-link>

        <router-link
            to="/admin-users"
            class="menu-item"
        >
            <i class="bi bi-people-fill"></i>
            <span>Users</span>
        </router-link>

        <router-link
            to="/admin-staff"
            class="menu-item"
        >
            <i class="bi bi-person-workspace"></i>
            <span>Staff</span>
        </router-link>

        <router-link
            to="/admin-bookings"
            class="menu-item"
        >
            <i class="bi bi-journal-check"></i>
            <span>Bookings</span>
        </router-link>

        <router-link
            to="/admin-summary"
            class="menu-item"
        >
            <i class="bi bi-bar-chart-fill"></i>
            <span>Summary</span>
        </router-link>

    </nav>

    <!-- Logout -->

    <div class="sidebar-footer">

        <router-link
            to="/"
            class="menu-item"
        >
            <i class="bi bi-box-arrow-right"></i>
            <span>Logout</span>
        </router-link>

    </div>

</aside>

    </aside>

    <!-- Main Content -->

    <main class="main-content">

        <!-- Header -->

<section class="page-header">
    <div>
        <p class="page-title">
            Create New Trek
        </p>

        <p class="page-subtitle">
            Craft unforgettable adventures for every explorer.
        </p>
    </div>

    <div class="header-right">
        <button class="back-btn" @click="$router.push('/admin-treks')">
            <i class="bi bi-arrow-left"></i>
            Back
        </button>
    </div>
</section>

<br><br><br>

<div>
<p class="trek-quote">
    "Behind every successful trek lies thoughtful planning."
</p>
</div>

<br><br><br><br><br>


        <!-- Basic Information -->
         <section class="glass-card">
            <div class="section-title">
                <h3>
                    <i class="bi bi-geo-alt-fill"></i>
                    Basic Information</h3>

    <p>

        Enter the core details of your trekking expedition.

    </p>

</div>



<hr class="section-divider">



        <!-- BASIC INFORMATION BODY -->
         <div class="section-body">
            <div class="row gy-3 gx-4">
                <!-- Trek Name -->

                <div class="col-md-6">

                    <label class="form-label fw-semibold">

                        Trek Name

                    </label>

                    <input
                        type="text"
                        class="form-control"
                        v-model="form.trek_name"
                        placeholder="Enter trek name"
                    >

                </div>

                <!-- Trek Type -->

                <div class="col-md-6">

                    <label class="form-label fw-semibold">

                        Trek Type

                    </label>

                    <select
                        class="form-select"
                        v-model="form.trek_type"
                    >

                        <option value="">Select Trek Type</option>

                        <option>Camping</option>

                        <option>Snow Trek</option>

                        <option>Forest Trek</option>

                        <option>Adventure Trek</option>

                        <option>High Altitude Trek</option>

                        <option>Weekend Trek</option>

                    </select>

                </div>

                <!-- Organizer -->

                <div class="col-md-6">

                    <label class="form-label fw-semibold">

                        Organizer

                    </label>

                    <input
                        type="text"
                        class="form-control"
                        v-model="form.organizer"
                        placeholder="Organizer Name"
                    >

                </div>

                <!-- Location -->

                <div class="col-md-6">

                    <label class="form-label fw-semibold">

                        Location

                    </label>

                    <input
                        type="text"
                        class="form-control"
                        v-model="form.location"
                        placeholder="Location"
                    >

                </div>

                <!-- Meeting Point -->

                <div class="col-md-6">

                    <label class="form-label fw-semibold">

                        Meeting Point

                    </label>

                    <input
                        type="text"
                        class="form-control"
                        v-model="form.meeting_point"
                        placeholder="Meeting Point"
                    >

                </div>

                <!-- State -->

                <div class="col-md-6">

                    <label class="form-label fw-semibold">

                        State

                    </label>

                    <input
                        type="text"
                        class="form-control"
                        v-model="form.state"
                        placeholder="State"
                    >

                </div>
            </div>
         </div>
         </section>

         <br><br>

        <!-- TREK DETAILS -->
         <section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-signpost-split-fill"></i>

            Trek Details

        </h3>

        <p>

            Configure the adventure, capacity and pricing.

        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gy-3 gx-4">
            <!-- Difficulty -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Difficulty

                </label>

                <select
                    class="form-select"
                    v-model="form.difficulty"
                >

                    <option value="">Select Difficulty</option>

                    <option>Easy</option>

                    <option>Moderate</option>

                    <option>Hard</option>

                </select>

            </div>

            <!-- Emergency Level -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Emergency Level

                </label>

                <select
                    class="form-select"
                    v-model="form.emergency_level"
                >

                    <option value="">Select Emergency Level</option>

                    <option>Low</option>

                    <option>Medium</option>

                    <option>High</option>

                </select>

            </div>

            <!-- Duration -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Duration (Days)

                </label>

                <input
                    type="number"
                    min="1"
                    class="form-control"
                    placeholder="Duration"
                    v-model="form.duration"
                >

            </div>

            <!-- Price -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Price (₹)

                </label>

                <input
                    type="number"
                    min="0"
                    class="form-control"
                    placeholder="Price"
                    v-model="form.price"
                >

            </div>

            <!-- Capacity -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Capacity

                </label>

                <input
                    type="number"
                    min="1"
                    class="form-control"
                    placeholder="Capacity"
                    v-model="form.capacity"
                >

            </div>

            <!-- Available Slots -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Available Slots

                </label>

                <input
                    type="number"
                    min="0"
                    class="form-control"
                    placeholder="Available Slots"
                    v-model="form.available_slots"
                >

            </div>
        </div>
    </div>
         </section>

        <br><br>

        <!-- Eligibility -->
         <section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-person-check-fill"></i>

            Eligibility

        </h3>

        <p>

            Define who can safely participate in this trek.

        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gy-3 gx-4">

            <!-- Minimum Age -->

            <div class="col-md-6">
                <label class="form-label fw-semibold">

                    Minimum Age

                </label>

                <input
                    type="number"
                    min="5"
                    class="form-control"
                    placeholder="Minimum Age"
                    v-model="form.minimum_age"
                >

            </div>

            <!-- Maximum Age -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Maximum Age

                </label>

                <input
                    type="number"
                    min="5"
                    class="form-control"
                    placeholder="Maximum Age"
                    v-model="form.maximum_age"
                >

            </div>

            <!-- Fitness Requirement -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Fitness Requirement

                </label>

                <select
                    class="form-select"
                    v-model="form.fitness_requirement"
                >

                    <option value="">Select Fitness Level</option>

                    <option>Beginner</option>

                    <option>Intermediate</option>

                    <option>Advanced</option>

                </select>

            </div>

        </div>

    </div>
         </section>
         <br><br>


        <!-- Schedule -->
         <!-- ==========================================
TREK SCHEDULE
========================================== -->

<section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-calendar-event-fill"></i>

            Trek Schedule

        </h3>

        <p>

            Schedule the trek and manage its booking availability.

        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gy-3 gx-4">
            <!-- Start Date -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Start Date

                </label>
                <input
type="date"
v-model="form.start_date"
:min="today"
class="form-control"
>

            </div>

            <!-- End Date -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    End Date

                </label>

                <input
type="date"
v-model="form.end_date"
:min="form.start_date || today"
class="form-control"
>

            </div>

            <!-- REGISTRATION DEADLINE-->
            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Registration Deadline

                </label>
                <input
type="date"
v-model="form.registration_deadline"
:min="today"
class="form-control"
>

            </div>

            <!-- Status -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Status

                </label>

                <select
                    class="form-select"
                    v-model="form.status"
                >

                    <option value="Upcoming">Upcoming</option>
                    <option value="Ongoing">Ongoing</option>
                    <option value="Completed">Completed</option>
                    <option value="Cancelled">Cancelled</option>

                </select>

            </div>
        </div>

    </div>
</section>

<br><br>

        <!-- Gallery -->
         <!-- ==========================================
TREK MEDIA
========================================== -->

<section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-images"></i>

            Trek Media

        </h3>

        <p>

            Upload visual content that showcases your trekking experience.

        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gy-3 gx-4">

            <!-- Cover Image -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Cover Image URL

                </label>
                <br>
                <small class="text-muted">

                    This image will appear on trek cards and listings.

                </small>

                <input
                    type="text"
                    class="form-control"
                    placeholder="https://example.com/cover.jpg"
                    v-model="form.cover_image"
                >

            </div>

            <!-- Live Preview -->

            <div class="col-md-6">

                <label class="form-label fw-semibold">

                    Cover Preview

                </label>

                <div class="cover-preview">

                    <img

                        v-if="form.cover_image"

                        :src="form.cover_image"

                        class="preview-image"

                    >

                    <div
                        v-else
                        class="preview-placeholder"
                    >

                        <i class="bi bi-image"></i>

                        <p>No Image Selected</p>

                    </div>

                </div>

            </div>

            <!-- Gallery -->

            <div class="col-12">

                <label class="form-label fw-semibold">

                    Gallery Images

                </label>
                <br>
                <small class="text-muted">

                    Separate each image using a new line.

                </small>

                <textarea

                    rows="7"

                    class="form-control"

                    placeholder="Paste one image URL per line"

                    v-model="form.gallery_images"

                ></textarea>
                <label class="form-label fw-semibold mt-4">

    Gallery Preview

</label>
<div class="gallery-preview">

    <div
        class="gallery-card"
        v-for="(image,index) in galleryPreview"
        :key="index"
    >

        <img
            :src="image"
            class="gallery-image"
        >

    </div>

</div>

            </div>

        </div>

    </div>

</section>
<br><br>


        <!-- ==========================================
EQUIPMENT & DESCRIPTION
========================================== -->

<section class="glass-card">

    <div class="section-title">

        <h3>

            <i class="bi bi-backpack2-fill"></i>

            Equipment & Description

        </h3>

        <p>

            Help trekkers prepare with essential gear and complete trek information.

        </p>

    </div>

    <hr class="section-divider">

    <div class="section-body">

        <div class="row gy-4 gx-4">

            <!-- Equipment -->

            <div class="col-12">

                <label class="form-label fw-semibold">

                    Equipment Required

                </label>
                <br>
                <small class="text-muted">

                    List the essential items participants should carry.

                </small>

                <textarea

                    rows="4"

                    class="form-control"

                    placeholder="Example: Trekking Shoes, Backpack, Water Bottle, Rain Jacket, Torch, First Aid Kit..."

                    v-model="form.equipment_required"

                ></textarea>

            </div>

            <!-- Description -->

            <div class="col-12">

                <label class="form-label fw-semibold">

                    Trek Description

                </label>
                <br>
                <small class="text-muted">

                    A clear description helps trekkers understand what to expect. Press Enter for a new line, or Enter twice for a paragraph gap.

                </small>

                <textarea

                    rows="7"

                    class="form-control"

                    placeholder="Write a detailed description of the trek, attractions, route, difficulty, experience, and important information..."

                    v-model="form.description"

                ></textarea>

                

            </div>

        </div>

    </div>

</section>

<!-- ==========================================
ACTION BUTTONS
========================================== -->

<div class="action-section">

    <button
        class="reset-btn"
        @click="resetForm"
    >

        <i class="bi bi-arrow-counterclockwise"></i>

        Reset Form

    </button>

    <button
        class="create-btn"
        @click="createTrek"
    >

        <i class="bi bi-check-circle-fill"></i>

        Create Trek

    </button>

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

.admin-create-trek-page{
    min-height:100vh;
    display:flex;
    position:relative;
    overflow:hidden;
}

.page-background{

    position:fixed;

    inset:0;

    background:
        linear-gradient(
            rgba(255,255,255,.72),
            rgba(255,255,255,.78)
        ),
        url("@/assets/images/admin-bg.jpg");

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

    background:#670626;

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
    background:#670626;
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
    background:#c5e4a1;

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

    margin-left:290px;

    padding:35px;

}

/*==================================================
MAIN CONTENT
==================================================*/

.main-content{

    flex:1;

    margin-left:290px;

    padding:35px;

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

    background:rgba(218, 240, 190, 0.65);

    backdrop-filter:blur(16px);

    border:1px solid rgba(255,255,255,.25);

    box-shadow:0 10px 35px rgba(0,0,0,.08);

}

.page-title{

    font-family:"Your Premium Heading Font", serif;

    font-size:3rem;

    color:#670626;

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

.back-btn{

    display:flex;

    align-items:center;

    gap:10px;

    padding:14px 28px;

    border:none;

    border-radius:18px;

    background:#670626;

    color:#fff;

    font-weight:600;

    transition:.3s ease;

    box-shadow:0 10px 25px rgba(103,6,38,.18);

    cursor:pointer;

}

.back-btn:hover{

    transform:translateY(-2px);
    background: white;
    color:#7b0a31;
    border-color: #7b0a31;
}

.back-btn i{

    font-size:1.1rem;

}

.trek-quote{

    font-family:"BrotherSignature", cursive;

    font-size:3.2rem;

    color:#670626;

    font-weight:400;

    line-height:1.3;

    letter-spacing:1.4px;

    opacity:.92;

    margin-top:18px;
    text-align: center;


}

/* ==========================================================
GLASS CARD
========================================================== */
.section-title{
    font-family:"Your Premium Heading Font", serif;
    color:#670626;
    font-size:2.5rem;

    margin:0;

    letter-spacing:1px;
    font-weight: 500;

}


.glass-card{

    background:rgba(255,255,255,0.22);

    backdrop-filter:blur(22px);

    -webkit-backdrop-filter:blur(22px);

    border:1px solid rgba(255,255,255,.35);

    border-top:5px solid #BAD797;

    border-radius:30px;

    padding:28px 40px;

    margin-bottom:40px;

    box-shadow:
        0 20px 45px rgba(0,0,0,.08);

    transition:.35s ease;

}

.glass-card:hover{

    transform:translateY(-4px);

    box-shadow:
        0 28px 60px rgba(0,0,0,.12);

}

.glass-card .col-md-6{
    margin-bottom:20px;
}

/* ==========================================================
SECTION HEADER
========================================================== */

.section-title{

    margin-bottom:15px;

}

.section-title h3{

    display:flex;

    align-items:center;

    gap:12px;

    font-size:2rem;

    color:#670626;

    margin-bottom:8px;

    font-weight:700;

}

.section-title i{

    color:#670626;

    font-size:1.6rem;

}

.section-title p{

    color:#666;

    font-size:1rem;

    margin:0;

}

/* ==========================================================
SECTION DIVIDER
========================================================== */

.section-divider{

    border:none;

    border-top:1px solid rgba(103,6,38,.15);

    margin:18px 0 24px;

}


/* ==========================================================
SECTION BODY
========================================================== */

.section-body{

    width:100%;

}

/* ==========================================================
LABELS
========================================================== */

.form-label{

    color:#670626;

    font-size:17px;

    font-weight:600;

    margin-bottom:10px;
    font-family:"Your Premium Heading Font", serif;
    letter-spacing: 1.2px;

}

/* ==========================================================
INPUTS
========================================================== */

.form-control,
.form-select{

    height:58px;

    border:none;

    border-radius:22px;

    background:rgba(255,255,255,.78);

    padding:0 20px;

    font-size:15px;

    color:#333;

    transition:.3s;

    box-shadow:none;
    width:95%;

}

/* ==========================================================
TEXTAREA
========================================================== */

textarea.form-control{

    height:auto;

    padding:18px;

    resize:none;

}

/* ==========================================================
PLACEHOLDER
========================================================== */

.form-control::placeholder{

    color:#999;

}

/* ==========================================================
FOCUS
========================================================== */

.form-control:focus,
.form-select:focus{

    background:white;

    border:none;

    outline:none;

    box-shadow:

        0 0 0 4px rgba(186,215,151,.35),

        0 8px 25px rgba(0,0,0,.08);

}

/* ==========================================================
SELECT
========================================================== */

.form-select{

    cursor:pointer;

}

/* ==========================================================
ROW SPACING
========================================================== */

.row gy-3 gx-4{

    --bs-gutter-y:1.8rem;

}

/* ==========================================================
INPUT HOVER
========================================================== */

.form-control:hover,
.form-select:hover{

    background:white;

}

/* ==========================================================
RESPONSIVE
========================================================== */

@media(max-width:768px){

    .glass-card{

        padding:25px;

    }

}

.cover-preview{

    width:100%;

    min-height:300px;

    max-height:420px;

    background:#fff;

    border:2px dashed rgba(103,6,38,.18);

    border-radius:22px;

    display:flex;

    justify-content:center;

    align-items:center;

    padding:15px;

    overflow:hidden;

}

.preview-image{

    max-width:100%;

    max-height:380px;

    width:auto;

    height:auto;

    border-radius:16px;

    object-fit:contain;

    transition:.3s;

}

.preview-placeholder{

    display:flex;

    flex-direction:column;

    align-items:center;

    color:#888;

}

.preview-placeholder i{

    font-size:3rem;

    color:#670626;

    margin-bottom:10px;

}

.preview-placeholder p{

    margin:0;

}

.gallery-preview{

    display:flex;

    gap:18px;

    flex-wrap:wrap;

    margin-top:18px;

}

.gallery-card{

    width:180px;

    height:130px;

    border-radius:18px;

    overflow:hidden;

    background:#fff;

    box-shadow:0 10px 25px rgba(0,0,0,.08);

    transition:.3s;

}

.gallery-card:hover{

    transform:translateY(-6px);

}

.gallery-image{

    width:100%;

    height:100%;

    object-fit:cover;

}

/* ==========================================
ACTION BUTTONS
========================================== */

.action-section{

    display:flex;

    justify-content:flex-end;

    gap:18px;

    margin:45px 0;

}

.reset-btn{

    border:none;

    background:#b7d57a;

    color:white;

    padding:14px 34px;

    border-radius:50px;

    font-weight:600;

    box-shadow:0 10px 30px rgba(0,0,0,.08);

    transition:.3s;

}

.reset-btn:hover{

    background:#ececec;
    color:black;

    transform:translateY(-3px);

}

.create-btn{

    border:none;

    background:#670626;

    color:white;

    padding:14px 40px;

    border-radius:50px;

    font-weight:600;

    box-shadow:0 12px 35px rgba(103,6,38,.25);

    transition:.3s;

}

.create-btn:hover{

    background:white;

    color:black;

    transform:translateY(-3px);

}
</style>

<script>

import axios from "axios"
export default {

    name: "AdminCreateTrek",

    data() {

        return {

            form: {

                trek_name: "",
                trek_type: "",
                organizer: "",
                location: "",
                meeting_point: "",
                state: "",

                difficulty: "",
                emergency_level: "",
                duration: "",
                price: "",
                capacity: "",
                available_slots: "",

                minimum_age: "",
                maximum_age: "",
                fitness_requirement: "",
                equipment_required: "",
                description: "",
                cover_image: "",
                gallery_images: "",

                start_date: "",
                end_date: "",
                registration_deadline: "",
                status: "Upcoming",
                today: new Date().toISOString().split("T")[0],

            }

        }

    },

    methods: {

        async createTrek() {
            try {
                const response = await axios.post(
                    "http://127.0.0.1:5000/api/admin/create-trek",
                    this.form
                )
                alert(response.data.message)
                this.$router.push(
                    "/admin-view-trek/" + response.data.trek_id
                )
            }
            catch (error) {
    console.log(error.response)

    if (error.response) {
        console.log(error.response.data)
        alert(error.response.data.message)
    } else {
        alert("Server Error")
    }
}
        },

        resetForm() {
            this.form = {
                trek_name: "",
                trek_type: "",
                organizer: "",
                location: "",
                meeting_point: "",
                state: "",
                difficulty: "",
                emergency_level: "",
                duration: "",
                price: "",
                capacity: "",
                available_slots: "",
                minimum_age: "",
                maximum_age: "",
                fitness_requirement: "",
                equipment_required: "",
                description: "",
                cover_image: "",
                gallery_images: "",
                start_date: "",
                end_date: "",
                status: "Upcoming"
            }
        }

    },

    computed: {
        galleryPreview(){

    if(!this.form.gallery_images){

        return []

    }

    return this.form.gallery_images
        .split("\n")
        .map(img=>img.trim())
        .filter(img=>img!="")

}
    }

}

</script>
