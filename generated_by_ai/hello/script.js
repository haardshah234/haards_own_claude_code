// script.js - Handles form submission and greets the user
// Ensure the DOM is fully loaded before attaching event listeners

document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  const nameInput = document.querySelector('input[name="username"]');

  if (!form || !nameInput) {
    // If the expected elements are missing, do nothing.
    return;
  }

  form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the default form submission behavior
    const name = nameInput.value.trim();

    if (name === '') {
      alert('Please enter your name.');
    } else {
      alert(`Hello, ${name}!`);
    }
  });
});
