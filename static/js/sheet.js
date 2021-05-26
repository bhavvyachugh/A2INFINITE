/* ------------------------ elements ----------------------- */

const viewBwBtn = document.getElementById("viewBwBtn");
const viewColoredBtn = document.getElementById("viewColoredBtn");

const bwSheet = document.querySelector(".img-container__img--black");
const coloredSheet = document.querySelector(".img-container__img--colored");

const printBwBtn = document.getElementById("printBwBtn");
const printColoredBtn = document.getElementById("printColoredBtn");

const loginWarning = document.querySelector(".login-heading");

/* -------------------------------- functions ------------------------------- */

const viewBwSheet = () => {
  bwSheet.style.display = "block";
  coloredSheet.style.display = "none";
  bwSheet.classList.add("ani");
  console.log(coloredSheet.style.display);
  console.log(bwSheet.style.display);
};

const viewColoredSheet = () => {
  coloredSheet.style.display = "block";
  bwSheet.style.display = "none";
  coloredSheet.classList.add("ani");
};

const printBwSheet = () => {
  //NOTE: setting display to none for both sheet so that problem caused by animation will not be there
  bwSheet.style.display = "none";
  coloredSheet.style.display = "none";
  if (bwSheet.style.display === "none") {
    bwSheet.style.display = "block";
    coloredSheet.style.display = "none";
  }
  window.print();
};

const printColoredSheet = () => {
  coloredSheet.style.display = "none";
  bwSheet.style.display = "none";
  if (coloredSheet.style.display == "none") {
    coloredSheet.style.display = "block";
    bwSheet.style.display = "none";
  }
  window.print();
};

/* --------------------------------- events --------------------------------- */

if (!loginWarning) {
  viewBwBtn.addEventListener("click", viewBwSheet);
  viewColoredBtn.addEventListener("click", viewColoredSheet);
  printBwBtn.addEventListener("click", printBwSheet);
  printColoredBtn.addEventListener("click", printColoredSheet);
}
