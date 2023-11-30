<?php

$url = "https://securevideotoken.tmgrup.com.tr/webtv/secure?000000&url=https%3A%2F%2Ftrkvz.daioncdn.net%2Fatv%2Fatv.m3u8%3Fce%3D3%26app%3Dd1ce2d40-5256-4550-b02e-e73c185a314e";
$headers = [
    'Origin: https://www.atv.com.tr',
    'Referer: https://www.atv.com.tr/',
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
];

$curl = curl_init($url);

curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($curl);

// Check for errors
if (curl_errno($curl)) {
    echo 'Curl error: ' . curl_error($curl);
} else {
    // Handle the response as needed
    echo $response;
}

// Close curl session
curl_close($curl);
?>
