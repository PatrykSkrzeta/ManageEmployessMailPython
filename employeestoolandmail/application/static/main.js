setTimeout(function() {
    var flashMessages = document.getElementById('flashes');
    if (flashMessages) {
      flashMessages.style.display = 'none';
    }
  }, 3000);



document.querySelector('input[name="create_mail"]').addEventListener('click', function() {
    var checkboxes = document.getElementsByClassName('mailBox');
    var checkboxArray = Array.from(checkboxes);
    var sendEmailButton = document.querySelector('input[name="send_email"]');
    checkboxArray.forEach(function(checkbox) {
        if (checkbox.style.display === 'block') {
            checkbox.style.display = 'none'; 
            sendEmailButton.style.display = 'none';
        } else {
            checkbox.style.display = 'block'; 
            sendEmailButton.style.display = 'block';
        }
    });
});


document.querySelector('input[name="send_email"]').addEventListener('click', function() {
    var emailForm = document.getElementById('email-form');
    emailForm.style.display = 'block';
  });