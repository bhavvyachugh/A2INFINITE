/* ------------------------ elements ----------------------- */

const viewBwBtn = document.getElementById("viewBwBtn");
const viewColoredBtn = document.getElementById("viewColoredBtn");

const bwSheet = document.querySelector(".img-container__img--black");
const coloredSheet = document.querySelector(".img-container__img--colored");

const printBwBtn = document.getElementById("printBwBtn");
const printColoredBtn = document.getElementById("printColoredBtn");

const loginWarning = document.querySelector(".login-heading");

/* -------------------------------- otg tags -------------------------------- */

const imageColored = document.querySelector(".img-container__img--colored").src;
const imageBw = document.querySelector(".img-container__img--black").src;

let urlOtg = document.createElement("meta");
urlOtg.setAttribute("property", "og:url");
urlOtg.content = document.location;
document.getElementsByTagName("head")[0].appendChild(urlOtg);

let imgOtg = document.createElement("meta");
imgOtg.setAttribute("property", "og:image");
imgOtg.content = imageColored;
document.getElementsByTagName("head")[0].appendChild(imgOtg);

/* -------------------------------- functions ------------------------------- */

const viewBwSheet = () => {
  bwSheet.style.display = "block";
  coloredSheet.style.display = "none";
  bwSheet.classList.add("ani");
  imgOtg.content = imageBw;
};

const viewColoredSheet = () => {
  coloredSheet.style.display = "block";
  bwSheet.style.display = "none";
  coloredSheet.classList.add("ani");
  imgOtg.content = imageColored;
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
