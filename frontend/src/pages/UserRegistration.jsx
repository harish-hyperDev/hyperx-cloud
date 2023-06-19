import { useState, useEffect } from "react";

const UserRegistration = () => {

  const [name, setName] = useState('')

  const gradientCustom = {
    background: "linear-gradient(109.6deg, rgb(187, 0, 212) 11.2%, rgb(32, 38, 238) 91.1%)"
  }

  const handleStateChange = () => {

  }
  return (
    <section class="vh-100 w-100 bg-image"
      // style={{backgroundImage: "url('https://mdbcdn.b-cdn.net/img/Photos/new-templates/search-box/img4.webp')"}}>
      style={gradientCustom}>
      <div class="mask d-flex align-items-center h-100 gradient-custom-3">
        <div class="container h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-9 col-lg-7 col-xl-6">
              <div class="card" style={{borderRadius: "15px"}}>
                <div class="card-body p-5">
                  <h4 class="text-center mb-5">Create Hyper Cloud Account</h4>

                  <form>

                    <div class="form-outline mb-2">
                      <label class="form-label" htmlFor="form3Example1cg">Your Name</label>
                      <input type="text" id="form3Example1cg" class="form-control" />
                    </div>

                    <div class="form-outline mb-2">
                      <label class="form-label" htmlFor="form3Example3cg">Your Email</label>
                      <input type="email" id="form3Example3cg" class="form-control" />
                    </div>

                    <div class="form-outline mb-2">
                      <label class="form-label" htmlFor="form3Example4cg">Password</label>
                      <input type="password" id="form3Example4cg" class="form-control" />
                    </div>

                    <div class="form-outline mb-4">
                      <label class="form-label" htmlFor="form3Example4cdg">Repeat your password</label>
                      <input type="password" id="form3Example4cdg" class="form-control" />
                    </div>

                    <div class="form-check d-flex justify-content-center mb-4">
                      <input class="form-check-input me-2" type="checkbox" value="" id="form2Example3cg" />
                      <label class="form-check-label" htmlFor="form2Example3g">
                        I agree all statements in <a href="#!" class="text-body"><u>Terms of service</u></a>
                      </label>
                    </div>

                    <div class="d-flex justify-content-center">
                      <button type="button"
                        class="btn btn-success btn-block btn-lg text-white px-5 border-0" style={gradientCustom}>Register</button>
                    </div>

                    <p class="text-center text-muted mt-4 mb-0">Already have an account? <a href="/"
                      class="fw-bold text-body"><u>Login here</u></a></p>

                  </form>

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default UserRegistration