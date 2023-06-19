import React from 'react'

const LandingPage = () => {
  const gradientCustom = {
    background: "linear-gradient(109.6deg, rgb(187, 0, 212) 11.2%, rgb(32, 38, 238) 91.1%)"
  }
  return (
    <section class="h-100 w-100 gradient-form" style={{backgroundColor: "#eee"}}>
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-xl-10">
            <div class="card rounded-3 text-black">
              <div class="row g-0">
                <div class="col-lg-6">
                  <div class="card-body p-md-5 mx-md-4">

                    <div class="text-center">
                      <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/lotus.webp"
                        style={{width: "185px"}} alt="logo" />
                      <h4 class="mt-1 mb-5 pb-1">Hyper Wasabi</h4>
                    </div>

                    <form>
                      {/* <h6 class="mb-4">Please login to your account</h6> */}

                      <div class="form-outline mb-4">
                        <label class="form-label mx-1" htmlFor="form2Example11">Username</label>
                        <input type="email" id="form2Example11" class="form-control"
                          placeholder="Username or Email Address" />
                      </div>

                      <div class="form-outline mb-4">
                        <label class="form-label mx-1" htmlFor="form2Example22">Password</label>
                        <input type="password" id="form2Example22" class="form-control" />
                      </div>

                      <div class="d-flex flex-column text-center pt-1 mb-5 pb-1">
                        <button class="btn btn-primary btn-block fa-lg mb-3 border-0" style={ gradientCustom } type="button">Log in</button>
                        <a class="text-muted" href="#!">Forgot password?</a>
                      </div>

                      <div class="d-flex align-items-center justify-content-center pb-4">
                        <p class="mb-0 me-2">Don't have an account?</p>
                        <button type="button" class="btn btn-outline-danger">Create new</button>
                      </div>

                    </form>

                  </div>
                </div>
                <div class="col-lg-6 d-flex align-items-center" style={ gradientCustom }>
                  <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                    <h4 class="mb-4">We are more than just a company</h4>
                    <p class="small mb-0">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                      exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default LandingPage

/* .bg-image-vertical {
position: relative;
overflow: hidden;
background-repeat: no-repeat;
background-position: right center;
background-size: auto 100%;
} */