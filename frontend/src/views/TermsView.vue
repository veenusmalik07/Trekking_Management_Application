<template>
    
    <div class="terms-page">
        
        <!--NAVBAR-->
        <nav class="navbar navbar-expand-lg fixed-top custom-navbar">
            <center>
            <div class="container">
                <p> Welcome to TrekMate </p>
            </div>
            </center>
        </nav>

        <div class="terms-card fixed-top">
            <p class="heading">
                Terms and Conditions
            </p>

            <h5>1. Account Responsibility</h5>
            <p>
                Users are responsible for maintaining the confidentiality of their login credentials and account information. 
                Any activity performed through your account will be considered your responsibility. 
                Please ensure that your password remains secure and is not shared with others. 
                TrekMate reserves the right to suspend accounts involved in suspicious or unauthorized activities.
            </p>
            <br><br>

            <h5>2. Trek Bookings</h5> 
            <p>
                All trek bookings are subject to availability and confirmation by the respective trek organizer. 
                Booking requests may be accepted or declined depending on trek capacity, weather conditions, 
                and safety guidelines. Users are advised to review trek details carefully before confirming a reservation. 
                Once a booking is confirmed, the applicable cancellation policy will apply.
            </p>
            <br><br>

            <h5>3. Health Declaration</h5>
            <p>
                Users must ensure they satisfy the fitness level, age requirements, and any medical conditions 
                specified for a trek before making a booking. TrekMate is not responsible for injuries or 
                health issues arising from participation without proper preparation. 
                Participants should consult a medical professional if they have any health concerns. 
                Safety instructions provided by trek organizers must always be followed.
            </p>
            <br><br>

            <h5>4. Payments</h5>
            <p>
                Payments made through TrekMate are processed using secure third-party payment gateways. 
                Users must ensure that payment information is accurate before completing a transaction. 
                TrekMate is not responsible for delays, failures, or technical issues caused by external payment providers. 
                Refunds, where applicable, will be processed according to the organizer's cancellation policy.
            </p>
            <br><br>

            <h5>5. Cancellation Policy</h5>
            <p>
                Cancellation requests are governed by the individual policies of each trek organizer. 
                Depending on the cancellation period, users may receive a full refund, partial refund, or no refund. 
                TrekMate only facilitates the booking process and does not determine refund eligibility. 
                Users should carefully review the cancellation terms before confirming a booking.
            </p>
            <br><br>

            <h5>6. User Conduct</h5>
            <p>
                Users are expected to behave respectfully toward trek organizers, staff members, and fellow participants. 
                Any abusive language, fraudulent activity, harassment, or 
                misuse of the platform may result in immediate suspension of the account. 
                TrekMate reserves the right to remove users who violate community guidelines. 
                Serious violations may also be reported to the appropriate authorities when required.
            </p>
            <br><br>

            <h5>7. Privacy</h5>
            <p>
                TrekMate collects only the information necessary to manage accounts, bookings, and trek participation. 
                Personal information is handled securely and is not shared with third parties 
                except where required for booking services or by law. 
                Users are encouraged to keep their account information updated for smooth communication. 
                By using TrekMate, you agree to our data handling and privacy practices.
            </p>
            <br><br><br>

            <center>
                <router-link to="/login"
                    class="btn btn-primary mt-4"
                >
                    Back to Login
                </router-link>
            </center>
        </div>
    </div>
</template>









<style scoped>

/* HIDE SCROLLER */
body{
    overscroll-behavior: none;
}

html{
    scroll-behavior : smooth;
    scroll-padding-top: 100px;
}

/* NAVBAR */
.custom-navbar{
    background:#ffffff;
    height: 62px;
    backdrop-filter:blur(12px);
    padding: 0;
    margin: 0px;
    transition:.4s;
}

/* Container */
.custom-navbar .container{
    max-width:100%;
    padding:0 45px;
}

/* Welcome Text */
.custom-navbar p{
    margin-left:500px;
    font-size:2.9rem;
    font-weight:700;
    color:#1E293B;
    letter-spacing:.5px;
    font-family:"Poppins",sans-serif;
    margin-top:20px;
}

.terms-page {
    margin-top: 30px;  /* ← Space for fixed navbar */
    background: url("@/assets/images/terms-bg.jpg") center/cover fixed no-repeat;
    background-size: cover;
    display: block;
    position: relative;
    overflow-y: auto;
    min-height: 250vh;
}

.terms-card {
    position: relative;
    width: min(1000px, 92%);
    min-height: calc(100vh - 120px);
    background: rgba(255, 255, 255, 0.08);
    color: white;
    backdrop-filter: blur(15px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, .15);
    margin: 0 auto;
    z-index: 2;
    padding: 20px;
    padding-top:90px;
}

.terms-card .heading{
    align-items: center;
    text-align: center;
    font-weight:700;
    font-size:2rem;
}

.terms-card h5{
    color:#037936;
    font-size:1.4rem;
    font-weight:700;
}

.terms-card p{
    color:black;
    line-height:1.9;
    font-size:18px;
}

.btn-primary{
    border-radius:40px;
    padding:12px 35px;
    font-weight:200;
    text-align: center;
    align-items: center;
    background:rgb(102, 163, 188);
}

.btn-primary:hover{
    background:rgb(135, 218, 235);
}

</style>