<?php
$url = 'https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_2/hls_fr2/index.m3u8';
$options  = array('https' => array('user_agent' => 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'));
$context  = stream_context_create($options);
$response = file_get_contents($url, false, $context);

header('Connection: keep-alive');
header('Content-Type: application/x-mpegURL');
header('Location: '.$response);
exit();
?>