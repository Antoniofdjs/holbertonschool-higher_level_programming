addEventListener("DOMContentLoaded", function () {
  // 1) Function to change the color of the header element
  function changeColor() {
    document.querySelector("header").style.color = "#FF0000";
  }

  // 2) Get the div element to which we will apply the event listener
  const divRedHeader = document.querySelector("#red_header");

  // 3) Add the click event listener to the div element
  divRedHeader.addEventListener("click", changeColor);
});
