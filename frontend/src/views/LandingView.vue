<template>
    <div class="lanidng-page">
        <nav class="navbar navbar-expand-lg navbar-dark fixed-top custom-navbar">
  <div class="container">

    <router-link class="navbar-brand brand" to="/">
      <i class="bi bi-signpost-split-fill me-2"></i>
      TrekMate
    </router-link>

    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarContent"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div
      class="collapse navbar-collapse"
      id="navbarContent"
    >

      <ul class="navbar-nav mx-auto">

        <li class="nav-item">
          <a class="nav-link active" href="#">Home</a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="#about">
            About
          </a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="#features">
            Features
          </a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="#gallery">
            Gallery
          </a>
        </li>


      </ul>

      <div class="d-flex">

        <router-link
          to="/login"
          class="btn btn-outline-light me-2 px-4"
        >
          Login
        </router-link>

        <router-link
          to="/register"
          class="btn btn-success px-4"
        >
          Create Account
        </router-link>

      </div>

    </div>

  </div>
</nav>


<!-- ================= HERO SECTION ================= -->

<section class="hero-section">

    <div class="hero-overlay"></div>

    <div class="container hero-content">

        <div class="row align-items-center min-vh-100">

            <!-- Left Content -->

            <div class="col-lg-7">

                <span class="hero-badge">
                    🏔 India's Trusted Trekking Platform
                </span>

                <h1 class="hero-title mt-4">

                    Every Trail Leads To
                    <span>A New Story.</span>

                </h1>

                <p class="hero-text">

                    Discover breathtaking Himalayan adventures,
                    scenic forest trails, peaceful valleys and unforgettable
                    camping experiences with TrekMate.

                </p>

                <div class="mt-5">

                    <a href="#gallery"
                       class="btn btn-outline-light btn-lg ms-3 hero-btn">

                        View Gallery

                    </a>

                </div>

            </div>

            <!-- Right Glass Card -->

            <div class="col-lg-5 d-none d-lg-flex justify-content-end">

                <div class="hero-card">

                    <h5 class="mb-4">

                        Adventure Statistics

                    </h5>

                    <div class="hero-stat">

                        <h3>50+</h3>

                        <p>Available Treks</p>

                    </div>

                    <div class="hero-stat">

                        <h3>10,000+</h3>

                        <p>Happy Trekkers</p>

                    </div>

                    <div class="hero-stat">

                        <h3>100+</h3>

                        <p>Expert Trek Leaders</p>

                    </div>

                    <div class="hero-stat">

                        <h3>4.9 ★</h3>

                        <p>Average Rating</p>

                    </div>

                </div>

            </div>

        </div>

    </div>

    <div class="scroll-down">

        <span>Scroll Down</span>

        <div class="mouse"></div>

    </div>

</section>

<!-- ================= WHY CHOOSE TREKMATE ================= -->

<section id="about" class="why-section">

    <div class="container">

        <div class="text-center mb-5">

            <span class="section-badge">
                WHY CHOOSE US
            </span>

            <h2 class="section-heading mt-3">
                More Than Just Trek Booking
            </h2>

            <p class="section-subtitle">
                TrekMate is your trusted adventure companion, making every journey
                safer, smoother, and more memorable from booking to the summit.
            </p>

        </div>

        <div class="row g-4">

            <!-- Card 1 -->
            <div class="col-lg-3 col-md-6">
                <div class="why-card">
                    <div class="why-icon">
                        🛡️
                    </div>
                    <h4>Verified Organizers</h4>
                    <p>
                        Every trek is managed by verified organizers with proven
                        experience to ensure safety and reliability.
                    </p>
                </div>
            </div>

            <!-- Card 2 -->
            <div class="col-lg-3 col-md-6">
                <div class="why-card">
                    <div class="why-icon">
                        🏔️
                    </div>
                    <h4>Handpicked Treks</h4>
                    <p>
                        Discover carefully selected adventures ranging from
                        beginner-friendly trails to high-altitude expeditions.
                    </p>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="col-lg-3 col-md-6">
                <div class="why-card">
                    <div class="why-icon">
                        👨‍🏕️
                    </div>
                    <h4>Expert Trek Leaders</h4>
                    <p>
                        Experienced trek leaders guide every journey with safety,
                        navigation, and local knowledge.
                    </p>
                </div>
            </div>

            <!-- Card 4 -->
            <div class="col-lg-3 col-md-6">
                <div class="why-card">
                    <div class="why-icon">
                        ❤️
                    </div>
                    <h4>Adventure Community</h4>
                    <p>
                        Meet fellow explorers, share experiences, and build
                        unforgettable memories together.
                    </p>
                </div>
            </div>
        </div>

    </div>

</section>

<!-- ================= FEATURES ================= -->

<section id="features" class="features-section">

    <div class="container">

        <div class="text-center mb-5">

            <span class="section-badge">
                OUR FEATURES
            </span>

            <h2 class="section-heading mt-3">
                Everything You Need For
                Your Next Adventure
            </h2>

            <p class="section-subtitle">

                TrekMate simplifies every step of your trekking journey—from
                discovering amazing destinations to booking safely and creating
                unforgettable memories.

            </p>

        </div>

        <div class="row g-4">

            <!-- Feature -->

            <div class="col-lg-4 col-md-6">

                <div class="feature-card">

                    <div class="feature-icon">

                        <i class="bi bi-compass"></i>

                    </div>

                    <h4>Explore Treks</h4>

                    <p>

                        Discover breathtaking trekking destinations across India
                        with detailed information and stunning visuals.

                    </p>

                </div>

            </div>

            <!-- Feature -->

            <div class="col-lg-4 col-md-6">

                <div class="feature-card">

                    <div class="feature-icon">

                        <i class="bi bi-calendar-check"></i>

                    </div>

                    <h4>Easy Booking</h4>

                    <p>

                        Reserve your seat in minutes with a smooth and secure
                        booking experience.

                    </p>

                </div>

            </div>

            <!-- Feature -->

            <div class="col-lg-4 col-md-6">

                <div class="feature-card">

                    <div class="feature-icon">

                        <i class="bi bi-people-fill"></i>

                    </div>

                    <h4>Expert Guides</h4>

                    <p>

                        Every adventure is led by experienced and knowledgeable
                        trekking professionals.

                    </p>

                </div>

            </div>

            <!-- Feature -->

            <div class="col-lg-4 col-md-6">

                <div class="feature-card">

                    <div class="feature-icon">

                        <i class="bi bi-shield-check"></i>

                    </div>

                    <h4>Safety First</h4>

                    <p>

                        Verified organizers, emergency support and carefully
                        planned trekking experiences.

                    </p>

                </div>

            </div>

            <!-- Feature -->

            <div class="col-lg-4 col-md-6">

                <div class="feature-card">

                    <div class="feature-icon">

                        <i class="bi bi-camera-fill"></i>

                    </div>

                    <h4>Adventure Gallery</h4>

                    <p>

                        Relive incredible journeys through beautiful photographs
                        captured by our trekking community.

                    </p>

                </div>

            </div>

            <!-- Feature -->

            <div class="col-lg-4 col-md-6">

                <div class="feature-card">

                    <div class="feature-icon">

                        <i class="bi bi-stars"></i>

                    </div>

                    <h4>Top Rated Experience</h4>

                    <p>

                        Join thousands of happy trekkers who trust TrekMate for
                        unforgettable outdoor adventures.

                    </p>

                </div>

            </div>

        </div>

    </div>

</section>

<section>
    <div class="gallery-grid">

    <div class="gallery-item">
        <img src="@/assets/images/gallery1.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Hampta Pass</h5>
            <p>Himachal Pradesh</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery2.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Kedarkantha</h5>
            <p>Uttarakhand</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery3.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Valley of Flowers</h5>
            <p>Uttarakhand</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery4.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Triund</h5>
            <p>Himachal Pradesh</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery5.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Sandakphu</h5>
            <p>West Bengal</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery6.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Kasol</h5>
            <p>Himachal Pradesh</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery7.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Kuari Pass</h5>
            <p>Uttarakhand</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery8.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Brahmatal</h5>
            <p>Uttarakhand</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery9.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Tarsar Marsar</h5>
            <p>Kashmir</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery10.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Goechala</h5>
            <p>Sikkim</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery11.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Rupin Pass</h5>
            <p>Himachal Pradesh</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery12.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Nag Tibba</h5>
            <p>Uttarakhand</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery13.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Pin Parvati</h5>
            <p>Himachal Pradesh</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery14.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Har Ki Dun</h5>
            <p>Uttarakhand</p>
        </div>
    </div>

    <div class="gallery-item">
        <img src="@/assets/images/gallery15.jpg" alt="">
        <div class="gallery-overlay">
            <h5>Dzongri</h5>
            <p>Sikkim</p>
        </div>
    </div>

</div>
</section>

<!-- ================= HOW IT WORKS ================= -->

<section class="how-section">

    <div class="container">

        <div class="text-center mb-5">

            <span class="section-badge">
                HOW IT WORKS
            </span>

            <h2 class="section-heading mt-3">
                Start Your Adventure In 4 Easy Steps
            </h2>

            <p class="section-subtitle">
                From discovering your dream trek to reaching the summit,
                TrekMate makes every step simple and hassle-free.
            </p>

        </div>

        <div class="steps">

            <div class="step">

                <div class="step-circle">
                    <i class="bi bi-search"></i>
                </div>

                <h5>Explore Treks</h5>

                <p>
                    Browse a variety of breathtaking trekking destinations across India.
                </p>

            </div>

            <div class="line"></div>

            <div class="step">

                <div class="step-circle">
                    <i class="bi bi-calendar-check"></i>
                </div>

                <h5>Book Your Trek</h5>

                <p>
                    Choose your preferred dates and reserve your seat securely.
                </p>

            </div>

            <div class="line"></div>

            <div class="step">

                <div class="step-circle">
                    <i class="bi bi-backpack2-fill"></i>
                </div>

                <h5>Meet Your Team</h5>

                <p>
                    Connect with trek leaders and fellow adventurers before departure.
                </p>

            </div>

            <div class="line"></div>

            <div class="step">

                <div class="step-circle">
                    <i class="bi bi-geo-alt-fill"></i>
                </div>

                <h5>Enjoy The Journey</h5>

                <p>
                    Experience unforgettable landscapes and create lifelong memories.
                </p>

            </div>

        </div>

    </div>

</section>

<!-- ================= POPULAR TREKS ================= -->

<section class="popular-section">

    <div class="container">

        <div class="text-center mb-5">

            <span class="section-badge">
                POPULAR TREKS
            </span>

            <h2 class="section-heading mt-3">
                Explore Our Most Loved Adventures
            </h2>

            <p class="section-subtitle">
                Handpicked destinations loved by thousands of trekkers for their breathtaking views and unforgettable experiences.
            </p>

        </div>

        <div class="row g-4">

            <!-- Trek 1 -->

            <div class="col-lg-4">

                <div class="trek-card">

                    <img src="@/assets/images/gallery16.jpg" class="trek-image">

                    <div class="trek-content">

                        <span class="difficulty easy">
                            Easy
                        </span>

                        <h4>Valley of Flowers</h4>

                        <p class="location">
                            <i class="bi bi-geo-alt-fill"></i>
                            Uttarakhand
                        </p>

                        <div class="trek-info">

                            <div>
                                <i class="bi bi-clock"></i>
                                5 Days
                            </div>

                            <div>
                                ⭐ 4.9
                            </div>

                        </div>

                    </div>

                </div>

            </div>

            <!-- Trek 2 -->

            <div class="col-lg-4">

                <div class="trek-card">

                    <img src="@/assets/images/gallery17.jpg" class="trek-image">

                    <div class="trek-content">

                        <span class="difficulty moderate">
                            Moderate
                        </span>

                        <h4>Hampta Pass</h4>

                        <p class="location">
                            <i class="bi bi-geo-alt-fill"></i>
                            Himachal Pradesh
                        </p>

                        <div class="trek-info">

                            <div>
                                <i class="bi bi-clock"></i>
                                6 Days
                            </div>

                            <div>
                                ⭐ 4.8
                            </div>

                        </div>

                    </div>

                </div>

            </div>

            <!-- Trek 3 -->

            <div class="col-lg-4">

                <div class="trek-card">

                    <img src="@/assets/images/gallery18.jpg" class="trek-image">

                    <div class="trek-content">

                        <span class="difficulty difficult">
                            Difficult
                        </span>

                        <h4>Kedarkantha</h4>

                        <p class="location">
                            <i class="bi bi-geo-alt-fill"></i>
                            Uttarakhand
                        </p>

                        <div class="trek-info">

                            <div>
                                <i class="bi bi-clock"></i>
                                7 Days
                            </div>

                            <div>
                                ⭐ 5.0
                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>

<!-- ================= TESTIMONIALS ================= -->

<section class="testimonial-section">

    <div class="container">

        <div class="text-center mb-5">

            <span class="section-badge">
                TESTIMONIALS
            </span>

            <h2 class="section-heading mt-3">
                What Our Trekkers Say
            </h2>

            <p class="section-subtitle">
                Thousands of adventure lovers have trusted TrekMate for unforgettable trekking experiences.
            </p>

        </div>

        <div class="row g-4">

            <!-- Testimonial 1 -->

            <div class="col-lg-4">

                <div class="testimonial-card">

                    <div class="stars">
                        ★★★★★
                    </div>

                    <p class="review">

                        "The Hampta Pass trek was beautifully organized. Everything from registration to reaching the summit was seamless. I can't wait for my next adventure."

                    </p>

                    <div class="user">

                        <img src="@/assets/images/user1.jpg">

                        <div>

                            <h5>Priya Sharma</h5>

                            <span>Delhi</span>

                        </div>

                    </div>

                </div>

            </div>

            <!-- Testimonial 2 -->

            <div class="col-lg-4">

                <div class="testimonial-card">

                    <div class="stars">
                        ★★★★★
                    </div>

                    <p class="review">

                        "Professional trek leaders, breathtaking views, and excellent safety arrangements. TrekMate made my first Himalayan trek unforgettable."

                    </p>

                    <div class="user">

                        <img src="@/assets/images/user2.jpg">

                        <div>

                            <h5>Rahul Verma</h5>

                            <span>Chandigarh</span>

                        </div>

                    </div>

                </div>

            </div>

            <!-- Testimonial 3 -->

            <div class="col-lg-4">

                <div class="testimonial-card">

                    <div class="stars">
                        ★★★★★
                    </div>

                    <p class="review">

                        "The booking process was simple, the campsite was amazing, and the entire journey exceeded my expectations. Highly recommended!"

                    </p>

                    <div class="user">

                        <img src="@/assets/images/user3.jpg">

                        <div>

                            <h5>Ananya Patel</h5>

                            <span>Ahmedabad</span>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>


<!-- ================= CTA ================= -->

<section class="cta-section">

    <div class="container">

        <div class="cta-box">

            <span class="cta-badge">
                START YOUR JOURNEY
            </span>

            <h2>
                Adventure Awaits Beyond Every Trail
            </h2>

            <p>
                Create your TrekMate account today and become part of a community
                of passionate explorers. Discover breathtaking trails, connect
                with fellow adventurers, and make unforgettable memories.
            </p>

            <router-link
                to="/register"
                class="btn btn-light btn-lg cta-btn"
            >
                Create Your Account
                <i class="bi bi-arrow-right ms-2"></i>
            </router-link>

        </div>

    </div>

</section>
    </div>
</template>

<style scoped>
.custom-navbar{
    padding:16px 0;
    background:rgba(20,20,20,.18);
    backdrop-filter:blur(18px);
    transition:.35s ease;
}

.brand{
    font-size:1.8rem;
    font-weight:700;
    color:#fff !important;
    letter-spacing:.5px;
}

.navbar-nav .nav-item{
    margin:0 12px;
}

.nav-link{
    color:white !important;
    font-weight:500;
    position:relative;
    transition:.3s;
}

.nav-link::after{
    content:"";
    position:absolute;
    left:0;
    bottom:-4px;
    width:0;
    height:2px;
    background:#6CC24A;
    transition:.3s;
}

.nav-link:hover::after{
    width:100%;
}

.nav-link:hover{
    color:#8be96b !important;
}

.btn-success{
    background:#2E7D32;
    border:none;
    border-radius:50px;
    font-weight:600;
}

.btn-success:hover{
    background:#256428;
}

.btn-outline-light{
    border-radius:50px;
    font-weight:600;
}

.navbar-toggler{
    border:none;
}

.navbar-toggler:focus{
    box-shadow:none;
}

/* HERO */

.hero-section{

    position:relative;

    min-height:100vh;

    background:url("@/assets/images/hero.jpg") center center/cover no-repeat;

    overflow:hidden;

}

.hero-overlay{

    position:absolute;

    inset:0;

    background:linear-gradient(
        rgba(0,0,0,.60),
        rgba(0,0,0,.55)
    );

}

.hero-content{

    position:relative;

    z-index:2;

    color:white;

}

.hero-badge{

    display:inline-block;

    padding:10px 20px;

    border-radius:50px;

    background:rgba(255,255,255,.12);

    backdrop-filter:blur(12px);

    border:1px solid rgba(255,255,255,.2);

    font-weight:600;

}

.hero-title{

    font-size:4.5rem;

    font-weight:800;

    line-height:1.15;

}

.hero-title span{

    color:#77dd77;

}

.hero-text{

    margin-top:25px;

    font-size:1.2rem;

    color:#ececec;

    max-width:650px;

    line-height:1.8;

}

.hero-btn{

    border-radius:50px;

    padding:14px 34px;

    font-weight:600;

}

.hero-card{

    width:330px;

    padding:35px;

    border-radius:25px;

    background:rgba(255,255,255,.12);

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,.25);

    box-shadow:0 25px 60px rgba(0,0,0,.35);

}

.hero-stat{

    margin-bottom:25px;

}

.hero-stat h3{

    color:#7CFC00;

    font-size:2rem;

    font-weight:700;

    margin-bottom:5px;

}

.hero-stat p{

    margin:0;

    color:white;

}

.scroll-down{

    position:absolute;

    bottom:30px;

    left:50%;

    transform:translateX(-50%);

    text-align:center;

    color:white;

    z-index:2;

}

.mouse{

    width:28px;

    height:48px;

    border:2px solid white;

    border-radius:20px;

    margin:10px auto;

    position:relative;

}

.mouse::before{

    content:"";

    position:absolute;

    top:8px;

    left:50%;

    transform:translateX(-50%);

    width:5px;

    height:10px;

    background:white;

    border-radius:50px;

    animation:scroll 1.8s infinite;

}

@keyframes scroll{

    0%{

        opacity:1;

        transform:translate(-50%,0);

    }

    100%{

        opacity:0;

        transform:translate(-50%,18px);

    }

}

@media(max-width:992px){

    .hero-title{

        font-size:3rem;

    }

    .hero-text{

        font-size:1rem;

    }

}

/* ================= WHY CHOOSE ================= */

.why-section{

    padding:120px 0;

    background:#f8faf8;

}

.section-badge{

    display:inline-block;

    background:#E8F5E9;

    color:#2E7D32;

    padding:8px 22px;

    border-radius:40px;

    font-weight:600;

    letter-spacing:1px;

    font-size:.9rem;

}

.section-heading{

    font-size:2.8rem;

    font-weight:700;

    color:#1E293B;

}

.section-subtitle{

    max-width:700px;

    margin:auto;

    color:#6B7280;

    font-size:1.1rem;

    line-height:1.8;

}

.why-card{

    background:white;

    padding:40px 30px;

    border-radius:22px;

    text-align:center;

    height:100%;

    transition:.35s ease;

    box-shadow:0 15px 40px rgba(0,0,0,.06);

    border:1px solid #edf2f7;

}

.why-card:hover{

    transform:translateY(-12px);

    box-shadow:0 30px 60px rgba(46,125,50,.15);

}

.why-icon{

    width:80px;

    height:80px;

    margin:auto;

    margin-bottom:25px;

    border-radius:50%;

    background:#E8F5E9;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:2rem;

}

.why-card h4{

    font-weight:700;

    margin-bottom:18px;

    color:#1F2937;

}

.why-card p{

    color:#6B7280;

    line-height:1.8;

    margin:0;

}

/*================ FEATURES ================*/

.features-section{

    padding:120px 0;

    background:white;

}

.feature-card{

    background:#fff;

    border-radius:24px;

    padding:40px 30px;

    height:100%;

    text-align:center;

    transition:.35s ease;

    border:1px solid #edf2f7;

    box-shadow:0 12px 35px rgba(0,0,0,.05);

}

.feature-card:hover{

    transform:translateY(-12px);

    box-shadow:0 25px 60px rgba(46,125,50,.15);

}

.feature-icon{

    width:85px;

    height:85px;

    border-radius:50%;

    margin:auto;

    margin-bottom:25px;

    background:linear-gradient(135deg,#2E7D32,#66BB6A);

    display:flex;

    justify-content:center;

    align-items:center;

    color:white;

    font-size:34px;

}

.feature-card h4{

    font-weight:700;

    margin-bottom:18px;

    color:#1F2937;

}

.feature-card p{

    color:#6B7280;

    line-height:1.8;

    margin:0;

}

/*================ GALLERY ================*/

.gallery-section{

    padding:120px 0;

    background:#f8faf8;

}

.gallery-grid{

    display:grid;

    grid-template-columns:repeat(3,1fr);

    gap:25px;

}

.gallery-item{

    position:relative;

    overflow:hidden;

    border-radius:22px;

    height:300px;

    cursor:pointer;

    box-shadow:0 12px 35px rgba(0,0,0,.12);

}

.gallery-item img{

    width:100%;

    height:100%;

    object-fit:cover;

    transition:.5s ease;

}

.gallery-item:hover img{

    transform:scale(1.1);

}

.gallery-overlay{

    position:absolute;

    inset:0;

    background:linear-gradient(

        transparent 35%,

        rgba(0,0,0,.78)

    );

    display:flex;

    flex-direction:column;

    justify-content:flex-end;

    padding:20px;

    color:white;

}

.gallery-overlay h5{

    margin:0;

    font-weight:700;

}

.gallery-overlay p{

    margin:0;

    opacity:.9;

}

@media(max-width:992px){

.gallery-grid{

grid-template-columns:repeat(2,1fr);

}

}

@media(max-width:768px){

.gallery-grid{

grid-template-columns:1fr;

}

.gallery-item{

height:250px;

}

}

/*================ HOW IT WORKS ================*/

.how-section{

    padding:120px 0;

    background:white;

}

.steps{

    display:flex;

    justify-content:space-between;

    align-items:flex-start;

    margin-top:70px;

    flex-wrap:wrap;

}

.step{

    width:220px;

    text-align:center;

}

.step-circle{

    width:90px;

    height:90px;

    margin:auto;

    border-radius:50%;

    background:linear-gradient(135deg,#2E7D32,#66BB6A);

    display:flex;

    justify-content:center;

    align-items:center;

    color:white;

    font-size:34px;

    box-shadow:0 15px 35px rgba(46,125,50,.25);

    margin-bottom:25px;

    transition:.35s;

}

.step:hover .step-circle{

    transform:translateY(-8px) scale(1.05);

}

.step h5{

    font-weight:700;

    margin-bottom:15px;

}

.step p{

    color:#6b7280;

    line-height:1.7;

}

.line{

    flex:1;

    height:4px;

    background:#d8e8da;

    margin:42px 15px 0;

    border-radius:20px;

}

@media(max-width:992px){

.steps{

flex-direction:column;

align-items:center;

}

.line{

width:4px;

height:70px;

margin:15px 0;

}

.step{

width:100%;

max-width:300px;

}

}

/*================ POPULAR TREKS ================*/

.popular-section{

    padding:120px 0;

    background:#F8FAF8;

}

.trek-card{

    background:white;

    border-radius:24px;

    overflow:hidden;

    box-shadow:0 15px 40px rgba(0,0,0,.08);

    transition:.35s;

}

.trek-card:hover{

    transform:translateY(-10px);

    box-shadow:0 25px 60px rgba(46,125,50,.18);

}

.trek-image{

    width:100%;

    height:270px;

    object-fit:cover;

}

.trek-content{

    padding:25px;

}

.difficulty{

    display:inline-block;

    padding:6px 14px;

    border-radius:30px;

    font-size:.85rem;

    font-weight:600;

    margin-bottom:15px;

}

.easy{

    background:#E8F5E9;

    color:#2E7D32;

}

.moderate{

    background:#FFF8E1;

    color:#F9A825;

}

.difficult{

    background:#FFEBEE;

    color:#C62828;

}

.trek-content h4{

    font-weight:700;

    margin-bottom:12px;

}

.location{

    color:#6B7280;

    margin-bottom:20px;

}

.trek-info{

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding-top:15px;

    border-top:1px solid #ECECEC;

    color:#374151;

    font-weight:500;

}

/*================ TESTIMONIALS ================*/

.testimonial-section{

    padding:120px 0;

    background:white;

}

.testimonial-card{

    background:#fff;

    border-radius:24px;

    padding:35px;

    height:100%;

    border:1px solid #edf2f7;

    box-shadow:0 12px 35px rgba(0,0,0,.06);

    transition:.35s;

}

.testimonial-card:hover{

    transform:translateY(-10px);

    box-shadow:0 25px 60px rgba(46,125,50,.15);

}

.stars{

    color:#FFC107;

    font-size:22px;

    margin-bottom:20px;

    letter-spacing:2px;

}

.review{

    color:#6B7280;

    line-height:1.8;

    font-style:italic;

    min-height:150px;

}

.user{

    display:flex;

    align-items:center;

    gap:15px;

    margin-top:25px;

}

.user img{

    width:60px;

    height:60px;

    border-radius:50%;

    object-fit:cover;

}

.user h5{

    margin:0;

    font-weight:700;

}

.user span{

    color:#6B7280;

    font-size:.9rem;

}

/*================ CTA =================*/

.cta-section{

    padding:120px 0;

    background:#F8FAF8;

}

.cta-box{

    background:linear-gradient(135deg,#1B4332,#2D6A4F);

    border-radius:30px;

    padding:80px 60px;

    text-align:center;

    color:white;

    box-shadow:0 25px 60px rgba(27,67,50,.25);

}

.cta-badge{

    display:inline-block;

    padding:8px 22px;

    background:rgba(255,255,255,.15);

    border:1px solid rgba(255,255,255,.25);

    border-radius:50px;

    font-size:.9rem;

    letter-spacing:1px;

    margin-bottom:20px;

}

.cta-box h2{

    font-size:3rem;

    font-weight:700;

    margin-bottom:20px;

}

.cta-box p{

    max-width:720px;

    margin:0 auto 40px;

    font-size:1.1rem;

    line-height:1.8;

    color:#E9F5EC;

}

.cta-buttons .btn{

    border-radius:50px;

    font-weight:600;

    padding:14px 35px;

}

.cta-buttons .btn-success{

    background:#52B788;

    border:none;

}

.cta-buttons .btn-success:hover{

    background:#40916C;

}

@media(max-width:768px){

.cta-box{

padding:50px 25px;

}

.cta-box h2{

font-size:2.2rem;

}

.cta-buttons{

display:flex;

flex-direction:column;

gap:15px;

}

.cta-buttons .btn{

width:100%;

margin:0 !important;

}

}

/*================ CTA SECTION ================*/

.cta-section{

    padding:120px 0;

    background:#F8FAF8;

}

.cta-box{

    background:linear-gradient(135deg,#1B4332,#2D6A4F);

    border-radius:30px;

    padding:80px 60px;

    text-align:center;

    color:white;

    box-shadow:0 20px 60px rgba(0,0,0,.15);

}

.cta-badge{

    display:inline-block;

    padding:8px 22px;

    background:rgba(255,255,255,.15);

    border:1px solid rgba(255,255,255,.25);

    border-radius:50px;

    font-size:.85rem;

    font-weight:600;

    letter-spacing:1px;

    margin-bottom:20px;

}

.cta-box h2{

    font-size:3rem;

    font-weight:700;

    margin-bottom:20px;

}

.cta-box p{

    max-width:700px;

    margin:0 auto 40px;

    color:#EAF4EC;

    font-size:1.1rem;

    line-height:1.8;

}

.cta-btn{

    border-radius:50px;

    padding:15px 40px;

    font-weight:600;

    transition:.3s;

}

.cta-btn:hover{

    transform:translateY(-3px);

    box-shadow:0 12px 30px rgba(255,255,255,.2);

}

@media(max-width:768px){

.cta-box{

padding:50px 25px;

}

.cta-box h2{

font-size:2rem;

}

.cta-box p{

font-size:1rem;

}

.cta-btn{

width:100%;

}

}
</style>