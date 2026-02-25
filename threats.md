| Trussel (Hva kan skje?)            | Risiko  | Tiltak (Hvordan vi beskytter systemet) |
|------------------------------------|---------|----------------------------------------|
| XSS (Cross-Site Scripting)         | Høy     | Flask/Jinja2 auto-escaper alle data. Brukeren kan ikke injisere ondsinnet skript i produktnavn eller handlekurv. |
| Manipulering av data               | Middels | Vi bruker `app.secret_key` for å signere cookies. Brukeren kan ikke endre innholdet i handlekurven sin manuelt uten å bryte signaturen. |
| Manglende samtykke                 | Lav     | Vi har implementert en "Cookie Banner". Ingen data lagres i sesjonen før brukeren har fått informasjon og akseptert vilkårene. |
| Ugyldig input (Injection)          | Middels | Vi bruker sterke typer i URL-ruten (`<int:prod_id>`). Dette sikrer at kun tall blir behandlet og hindrer uventet kode i systemet. |