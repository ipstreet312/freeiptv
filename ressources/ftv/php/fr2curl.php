<?php
$url = 'https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_2/hls_fr2/index.m3u8';

$content = file_get_contents($url);

header('Connection: keep-alive');
header('Content-Type: application/x-mpegURL');
header('Location: '.$content);
exit();
?>