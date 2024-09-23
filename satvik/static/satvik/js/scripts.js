/* satvik/static/satvik/js/scripts.js */

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("reservation-form");

    form.addEventListener("submit", function (event) {
        // Simple validation
        const guestCount = document.getElementById("id_guest_count").value;
        if (guestCount <= 0) {
            alert("Guest count must be greater than 0.");
            event.preventDefault();
            return;
        }

        // Add a loading state
        const submitButton = document.querySelector(".fancy-submit-btn");
        submitButton.textContent = "Booking...";
        submitButton.style.backgroundColor = "#2980b9";
        submitButton.disabled = true;
    });

    // Live input validation for guest count
    const guestCountInput = document.getElementById("id_guest_count");
    guestCountInput.addEventListener("input", function () {
        if (guestCountInput.value < 1) {
            guestCountInput.style.borderColor = "#e74c3c";
        } else {
            guestCountInput.style.borderColor = "#2ecc71";
        }
    });
});
