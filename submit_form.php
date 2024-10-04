<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form inputs and sanitize them to prevent security issues like XSS attacks
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Server-side validation (optional but recommended)
    if (!empty($name) && !empty($email) && !empty($message)) {
        // Validate email
        if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
            // Here you can process the form data
            // For example, send an email or save the data to a database
            
            // Example: Send an email
            $to = "tuberculens@gmail.com"; // Replace with your email address
            $subject = "New Contact Form Submission";
            $body = "Name: $name\nEmail: $email\nMessage: $message";
            $headers = "From: $email";
            
            if (mail($to, $subject, $body, $headers)) {
                echo "Message sent successfully!";
            } else {
                echo "Failed to send the message!";
            }
        } else {
            echo "Invalid email address!";
        }
    } else {
        echo "All fields are required!";
    }
} else {
    echo "Form was not submitted correctly!";
}
?>
