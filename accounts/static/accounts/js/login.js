const loginBox = document.getElementById("loginBox");
const signupBox = document.getElementById("signupBox");
const switchBtn = document.getElementById("switchBtn");
const goSignup = document.getElementById("goSignup");
const goLogin = document.getElementById("goLogin");

// Toggle password show/hide
document.getElementById("loginToggle").addEventListener("click", function () {
  togglePassword("loginPass", "loginToggle");
});

document.getElementById("signupToggle").addEventListener("click", function () {
  togglePassword("signupPass", "signupToggle");
});

function togglePassword(inputId, toggleId) {
  let field = document.getElementById(inputId);
  let toggle = document.getElementById(toggleId);
  if (field.type === "password") {
    field.type = "text";
    toggle.innerText = "Hide";
  } else {
    field.type = "password";
    toggle.innerText = "Show";
  }
}

// Switch forms
function showSignup() {
  loginBox.classList.add("hidden");
  signupBox.classList.remove("hidden");
  switchBtn.innerText = "Back to Login";
}

function showLogin() {
  signupBox.classList.add("hidden");
  loginBox.classList.remove("hidden");
  switchBtn.innerText = "Create Account";
}

switchBtn.addEventListener("click", function () {
  if (signupBox.classList.contains("hidden")) {
    showSignup();
  } else {
    showLogin();
  }
});

goSignup.addEventListener("click", showSignup);
goLogin.addEventListener("click", showLogin);

// LOGIN — validate first, then let Django handle it
document.getElementById("loginForm").addEventListener("submit", function (e) {
  let user = document.getElementById("loginUser").value.trim();
  let pass = document.getElementById("loginPass").value.trim();

  let userError = document.getElementById("loginUserError");
  let passError = document.getElementById("loginPassError");

  let valid = true;

  if (user === "") {
    userError.style.display = "block";
    valid = false;
  } else {
    userError.style.display = "none";
  }

  if (pass.length < 6) {
    passError.style.display = "block";
    valid = false;
  } else {
    passError.style.display = "none";
  }

  // If validation fails, stop form. If valid, let Django receive it.
  if (!valid) {
    e.preventDefault();
  }
});

// SIGNUP — validate first, then let Django handle it
document.getElementById("signupForm").addEventListener("submit", function (e) {
  let name = document.getElementById("fullName").value.trim();
  let user = document.getElementById("signupUser").value.trim();
  let pass = document.getElementById("signupPass").value.trim();
  let confirm = document.getElementById("confirmPass").value.trim();

  let nameError = document.getElementById("nameError");
  let passError = document.getElementById("passError");
  let confirmError = document.getElementById("confirmError");

  let valid = true;

  if (name === "") {
    nameError.style.display = "block";
    valid = false;
  } else {
    nameError.style.display = "none";
  }

  if (pass.length < 6) {
    passError.style.display = "block";
    valid = false;
  } else {
    passError.style.display = "none";
  }

  if (confirm !== pass) {
    confirmError.style.display = "block";
    valid = false;
  } else {
    confirmError.style.display = "none";
  }

  // If validation fails, stop form. If valid, let Django receive it.
  if (!valid) {
    e.preventDefault();
  }
});