// DOM Elements

const loginContainer = document.querySelector(".login-container");
const loginForm = document.getElementById("loginForm");
const loginUsername = document.getElementById("loginUsername");

const loginPassword = document.getElementById("loginPassword");

const showPasswordIcon = document.querySelector("i.fa-eye");

showPasswordIcon.addEventListener("click", showPassword);

// *Show Hide Password
function showPassword() {
  //   console.log(loginPassword);
  if (loginPassword.type === "password") {
    loginPassword.type = "text";
    showPasswordIcon.style.color = "red";
  } else {
    loginPassword.type = "password";
    showPasswordIcon.style.color = "#ddd";
  }
}

// console.log(loginForm);

// *Simple Validation

loginForm.addEventListener("submit", submitValidation);

function submitValidation(event) {
  event.preventDefault();
  //   User name validation
  if (loginUsername.value === "" || loginUsername.value.length < 3) {
    // console.log(" empty");
    showError(loginUsername, "User name can not be empty & must be > 3");
  } else {
    // console.log("not empty");
    showSuccess(loginUsername);
  }
  //   Password validation

  if (loginPassword.value === "" || loginPassword.value.length < 6) {
    // console.log(" empty");
    showError(loginPassword, "Password can not be empty or less then 6");
  } else {
    // console.log("not empty");
    showSuccess(loginPassword);
  }
}

// Show error Message
function showError(input, message) {
  const formField = input.parentElement;
  //   console.log(formField.className);
  formField.className = "form-field error";
  if ((formField.className = "form-field error")) {
    const alert_message = formField.querySelector(".alert-message");
    alert_message.style.visibility = "visible";
    alert_message.style.color = "red";
    alert_message.innerText = message;
  }
}
function showSuccess(input) {
  const formField = input.parentElement;
  formField.className = "form-field success";
  if ((formField.className = "form-field success")) {
    const alert_message = formField.querySelector(".alert-message");
    alert_message.style.visibility = "hidden";
  }
}
// Request Form

const requestForm = document.querySelector(".form-request");

requestForm.style.display = "none";

const showRequestForm = document.querySelector(".reset-password");

showRequestForm.addEventListener("click", function (e) {
  e.preventDefault();
  if (requestForm.style.display !== "block") {
    loginContainer.style.minHeight = "650px";
    requestForm.style.display = "block";
  } else {
    requestForm.style.display = "none";
    loginContainer.style.minHeight = "initial";
  }
});
requestForm.addEventListener("submit", request);

function request(e) {
  e.preventDefault();

  //   console.log(requestEmail);
  if (requestForm.style.display === "block") {
    const requestEmail = document.getElementById("requestEmail");
    if (requestEmail.value === "") {
      showError(requestEmail, "Email can not be empty");
    } else {
      showSuccess(requestEmail);
    }
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-input");
  const clearBtn = document.getElementById("Clear-btn");

  // Show or hide the "X" icon based on input
  searchInput.addEventListener("input", function () {
    if (searchInput.value.length > 0) {
      clearBtn.style.display = "block"; // Show the "X" icon
    } else {
      clearBtn.style.display = "none"; // Hide the "X" icon
    }
  });

  // Clear the input when the "X" icon is clicked
  clearBtn.addEventListener("click", function () {
    searchInput.value = ""; // Clear the input value
    clearBtn.style.display = "none"; // Hide the "X" icon
    searchInput.focus(); // Optionally refocus the input
  });
});
