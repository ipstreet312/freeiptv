<?php
// Token request URL
$token_api_url = "https://token.easybroadcast.io/all?url=https://cdn.live.easybroadcast.io/abr_corp/73_tamazight_tccybxt/corp/73_tamazight_tccybxt_480p/chunks_dvr.m3u8";

// Fetch the token as plain text
$response = file_get_contents($token_api_url);

if ($response === false) {
    http_response_code(500);
    echo "Error: Could not retrieve token.";
    exit;
}

// Parse the response like a query string
parse_str($response, $data);

// Validate required fields
if (!isset($data['token'], $data['token_path'], $data['expires'])) {
    http_response_code(500);
    echo "Error: Invalid token response format.";
    exit;
}

// Extract values
$token = $data['token'];
$token_path = $data['token_path'];
$expires = $data['expires'];

// Base stream URL
$base_url = "https://cdn.live.easybroadcast.io/abr_corp/73_tamazight_tccybxt/corp/73_tamazight_tccybxt_480p/chunks_dvr.m3u8";

// Append token parameters
$content = $base_url . "?token=" . urlencode($token) . "&token_path=" . urlencode($token_path) . "&expires=" . urlencode($expires);

// Send headers and redirect
header('Connection: keep-alive');
header('Content-Type: application/x-mpegURL');
header('Location: ' . $content);
exit;
?>
