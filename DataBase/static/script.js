let checkDB = document.getElementById('check-database')
let addDB = document.getElementById('add-to-database')

function redirectToDB() {

    window.location.href = '/problems'
}




function redirectToForm() {

    window.location.href = '/submit'
}

checkDB.addEventListener('click', redirectToDB)
addDB.addEventListener('click', redirectToForm)



const messageContainer = document.getElementById('message-container');

// Define the message content
const message = 'Welcome to my website!';

// Function to animate the message
function animateMessage() {
  let index = 0;
  const intervalId = setInterval(() => {
    // Add one letter to the message
    messageContainer.textContent = message.slice(0, index);

    // Increase the index
    index++;

    // Check if the animation is complete
    if (index > message.length) {
      // Stop the interval and fade in the complete message
      clearInterval(intervalId);
      messageContainer.style.opacity = 1;
    }
  }, 100); // Delay between each letter (in milliseconds)
}

// Call the animateMessage function after the page loads
window.addEventListener('load', animateMessage);