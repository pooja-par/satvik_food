/* satvik/static/satvik/js/scripts.js */

// JavaScript to add interactivity to the reservation form
document.addEventListener("DOMContentLoaded", function () {
    const guestCountInput = document.querySelector("#id_guest_count");
    if (guestCountInput) {
        const guestCountWarning = document.createElement("p");
        guestCountWarning.style.color = "red";
        guestCountWarning.style.fontSize = "14px";
        guestCountInput.insertAdjacentElement("afterend", guestCountWarning);

        guestCountInput.addEventListener("input", function () {
            const guestCount = parseInt(guestCountInput.value, 10);
            if (guestCount > 10) {
                guestCountWarning.textContent = "Sorry, we cannot accommodate more than 10 guests per table.";
            } else if (guestCount < 1) {
                guestCountWarning.textContent = "Number of guests must be at least 1.";
            } else {
                guestCountWarning.textContent = "";
            }
        });
    }

    // Confirmation before canceling a reservation
    const cancelForms = document.querySelectorAll("form[action^='{% url 'cancel_reservation' %}']");
    cancelForms.forEach(form => {
        form.addEventListener("submit", function (e) {
            const confirmation = confirm("Are you sure you want to cancel this reservation?");
            if (!confirmation) {
                e.preventDefault();
            }
        });
    });
});
