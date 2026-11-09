<?php
// Obdelava kontaktnega obrazca – ZigZag Marketing
// Povpraševanja z vseh strani (Meta oglasi, spletne strani, ghostwriting) pridejo na $to.

$to   = 'info@zigzagmarketing.net';
$from = 'info@zigzagmarketing.net'; // mora biti obstoječ nabiralnik na vaši domeni

date_default_timezone_set('Europe/Ljubljana');
header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false]);
    exit;
}

// Past za robote: človek tega polja ne vidi
if (!empty($_POST['website_hp'])) {
    echo json_encode(['ok' => true]);
    exit;
}

function clean($key, $max = 500) {
    $v = isset($_POST[$key]) ? trim((string) $_POST[$key]) : '';
    $v = str_replace(["\r", "\n"], ' ', $v);
    return mb_substr($v, 0, $max);
}

$storitve = [
    'meta'  => 'Meta oglasi',
    'web'   => 'Spletna stran',
    'ghost' => 'Ghostwriting',
    'other' => 'Še ne ve',
];

$ime       = clean('ime', 120);
$email     = clean('email', 160);
$telefon   = clean('telefon', 40);
$podjetje  = clean('podjetje', 200);
$storitev  = clean('storitev', 20);
$proracun  = clean('proracun', 60);
$stran     = clean('stran', 80);
$sporocilo = isset($_POST['sporocilo']) ? mb_substr(trim((string) $_POST['sporocilo']), 0, 3000) : '';
$soglasje  = !empty($_POST['soglasje']);
$jezik     = clean('jezik', 5) === 'EN' ? 'EN' : 'SL';

// Starejše strani brez izbire storitve so bile vse o Meta oglasih
if ($storitev === '') {
    $storitev = 'meta';
}
$storitevIme = isset($storitve[$storitev]) ? $storitve[$storitev] : null;

if ($ime === '' || $podjetje === '' || $storitevIme === null || !$soglasje || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(['ok' => false]);
    exit;
}

$subject = '[' . $jezik . '] ' . $storitevIme . ' – novo povpraševanje: ' . $ime . ' (' . $podjetje . ')';
$body = "Novo povpraševanje s spletne strani\n\n"
      . "Storitev: $storitevIme\n"
      . "Ime: $ime\n"
      . "E-pošta: $email\n"
      . "Telefon: " . ($telefon !== '' ? $telefon : '-') . "\n"
      . "Podjetje / spletna stran: $podjetje\n"
      . ($proracun !== '' ? "Mesečni proračun za Meta oglase: $proracun\n" : '')
      . "\nSporočilo:\n" . ($sporocilo !== '' ? $sporocilo : '-') . "\n\n"
      . "Poslano s strani: " . ($stran !== '' ? $stran : '-') . " ($jezik)\n"
      . "Soglasje za kontakt: da\n"
      . "Čas: " . date('Y-m-d H:i') . "\n";

$headers = "From: ZigZag Marketing <$from>\r\n"
         . "Reply-To: $email\r\n"
         . "Content-Type: text/plain; charset=UTF-8\r\n";

$sent = mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers, '-f' . $from);

if (!$sent) {
    http_response_code(500);
}
echo json_encode(['ok' => (bool) $sent]);
