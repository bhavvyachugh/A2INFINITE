"use strict";

const alertContainer = document.querySelector(".alert");
const alertCross = document.querySelector(".alert__cross");

if (alertContainer) {
  alertCross.addEventListener("click", () => {
    alertContainer.style.display = "none";
  });
}
