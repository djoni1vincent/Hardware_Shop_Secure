function checkConsent() {
    if (!localStorage.getItem("cookie_consent")) {
        const banner = document.getElementById("cookie-banner");
        if (banner) {
            banner.style.display = "block";
            alert("Du må godta cookies før du kan legge varer i kurven.");
        }
        return false;
    }
    return true;
}

function acceptCookies() {
    localStorage.setItem("cookie_consent", "true");
    document.getElementById("cookie-banner").style.display = "none";
    alert("Takk! Nå kan du handle.");
}

window.onload = function () {
    if (!localStorage.getItem("cookie_consent")) {
        document.getElementById("cookie-banner").style.display = "block";
    }
};

function toggleProducts() {
    const hiddenProducts = document.querySelectorAll('.hidden-product');
    const btn = document.getElementById('show-more-btn');

    hiddenProducts.forEach(product => {
        product.classList.remove('hidden-product');
    });

    btn.style.display = 'none';
}