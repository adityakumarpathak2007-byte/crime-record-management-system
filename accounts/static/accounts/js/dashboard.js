// Show current date in navbar
const d = new Date();
const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
document.getElementById('currentDate').innerText = d.toLocaleDateString('en-IN', options);