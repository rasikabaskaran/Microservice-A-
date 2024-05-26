document
  .getElementById("lightModeButton")
  .addEventListener("click", function () {
    updateColors("light");
  });

document
  .getElementById("darkModeButton")
  .addEventListener("click", function () {
    updateColors("dark");
  });

function updateColors(mode) {
  fetch(`http://localhost:5000/get_contrast_colors?mode=${mode}`)
    .then((response) => response.json())
    .then((data) => {
      console.log("Received data:", data); // Log to confirm data is received
      document.body.style.color = data.text_color;
      document.body.style.backgroundColor = data.background_color;
    })
    .catch((error) => {
      console.error("Error fetching colors:", error); // Log errors
    });
}
