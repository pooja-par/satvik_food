// JavaScript to add some interactivity to the booking form
document.addEventListener("DOMContentLoaded", function () {
    const guestCountInput = document.querySelector("#guest_count");
    const guestCountWarning = document.createElement("p");
    guestCountWarning.style.color = "red";
    guestCountWarning.style.fontSize = "14px";
    guestCountInput.insertAdjacentElement("afterend", guestCountWarning);

    guestCountInput.addEventListener("input", function () {
        const guestCount = parseInt(guestCountInput.value, 10);
        if (guestCount > 10) {
            guestCountWarning.textContent = "Sorry, we cannot accommodate more than 10 guests per table.";
        } else {
            guestCountWarning.textContent = "";
        }
    });
});
