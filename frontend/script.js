const form = document.querySelector('form');
const greeting = document.querySelector('#greeting');

form.addEventListener('submit', (event) => {
	event.preventDefault();
	const name = document.querySelector('#name').value;
	greeting.textContent = `Hello, ${name}!`;
});

const counter = document.querySelector(".counter-number");

async function updateCounter() {
    try {
        const response = await fetch(
            "https://d5d4i5cmpicqsn2ubdtm5sskem0zbxsu.lambda-url.ap-south-1.on.aws/"
        );
        if (!response.ok) {
            throw new Error(`Request failed: ${response.status}`);
        }
        const data = await response.json();
        counter.textContent = `Views: ${data}`;
    } catch (error) {
        console.error("Could not update the view counter:", error);
        counter.textContent = "Views: unavailable";
    }
}

updateCounter();
