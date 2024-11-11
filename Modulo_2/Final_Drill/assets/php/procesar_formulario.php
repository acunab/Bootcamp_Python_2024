<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
require 'vendor/autoload.php'; // Incluir autoload de Composer

header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $phone = htmlspecialchars($_POST['phone']);
    $website = htmlspecialchars($_POST['website']);
    $services = [];
    if (isset($_POST['seo'])) {
        $services[] = 'SEO';
    }
    if (isset($_POST['web'])) {
        $services[] = 'WEB';
    }
    $budget = htmlspecialchars($_POST['budget']);
    $message = htmlspecialchars($_POST['message']);
    $recaptchaResponse = $_POST['g-recaptcha-response'];

    // Verificar reCAPTCHA
    $secretKey = 'TU_CLAVE_SECRETA_RECAPTCHA';
    $verifyResponse = file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret=$secretKey&response=$recaptchaResponse");
    $responseData = json_decode($verifyResponse);

    if (!$responseData->success) {
        echo json_encode(["success" => false, "message" => "Captcha no verificado."]);
        exit;
    }

    // Configurar PHPMailer
    $mail = new PHPMailer(true);
    try {
        // Configuración del servidor SMTP
        $mail->isSMTP();
        $mail->Host = 'smtp.tu_servidor.com'; // Ajusta esto a tu servidor SMTP
        $mail->SMTPAuth = true;
        $mail->Username = 'tu_correo@tu_dominio.com'; // Tu correo SMTP
        $mail->Password = 'tu_contraseña'; // Tu contraseña SMTP
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = 587;

        // Destinatarios
        $mail->setFrom('tu_correo@tu_dominio.com', 'Formulario de Contacto');
        $mail->addAddress('destino@dominio.com', 'Destinatario'); // Ajusta esto a tu dirección de correo de destino

        // Contenido del correo
        $mail->isHTML(true);
        $mail->Subject = 'Nuevo mensaje del formulario de contacto';
        $mailContent = "
            <h1>Nuevo mensaje del formulario de contacto</h1>
            <p><b>Nombre:</b> $name</p>
            <p><b>Email:</b> $email</p>
            <p><b>Teléfono:</b> $phone</p>
            <p><b>Sitio web:</b> $website</p>
            <p><b>Servicios:</b> " . implode(", ", $services) . "</p>
            <p><b>Presupuesto:</b> $budget</p>
            <p><b>Mensaje:</b> $message</p>
        ";
        $mail->Body = $mailContent;

        $mail->send();
        echo json_encode(["success" => true]);
    } catch (Exception $e) {
        echo json_encode(["success" => false, "message" => "No se pudo enviar el correo. Error: {$mail->ErrorInfo}"]);
    }
} else {
    echo json_encode(["success" => false, "message" => "Método de solicitud no permitido."]);
}
?>
