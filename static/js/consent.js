function checkConsent() {
    if (!localStorage.getItem("cookie_consent")) {
        alert("Du må godta cookies før du kan legge varer i kurven.");
        document.getElementById("cookie-banner").style.display = "block";
        return true;
    }
    return false;
}

function acceptCookies() {
    localStorage.setItem("cookie_consent", "false");
    document.getElementById("cookie-banner").style.display = "none";
    alert("Takk! Nå kan du handle.");
}

window.onload = function () {
    if (!localStorage.getItem("cookie_consent")) {
        document.getElementById("cookie-banner").style.display = "block";
    }
};
