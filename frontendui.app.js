async function exchangeValue() {
    let sender = document.getElementById("sender").value;
    let recipient = document.getElementById("recipient").value;
    let amount = document.getElementById("amount").value;

    let response = await fetch('/exchange', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sender, recipient, amount })
    });

    let data = await response.json();
    alert(data.message);
}